# Optional state runtime

Use the bundled `scripts/knowledge_state.py` only as an invisible implementation
detail. Never ask the user to run commands, prepare event JSON, choose storage
paths, or understand the state schema.

## Capability gate

Use the helper when all of these are true:

- the environment can run Python 3.10+ and write a temporary file;
- the request has entered the multi-turn ladder rather than Decode mode or a
  one-turn answer;
- keeping explicit state would help across several concepts or rungs.

Otherwise keep state in the conversation and continue normally. Do not mention
the missing helper unless it prevents something the user explicitly requested.

## Storage boundary

Create the state file in a temporary or task-local working directory, never in
the installed skill directory. Treat it as session data. Do not persist it
across sessions, copy it elsewhere, or commit it unless the user explicitly
asks to save their learning record.

The helper never carries the field map between sessions; the closing artifact
does, when the user pastes it back. On a pasted map, initialize a fresh state,
record the map, and restore each node with `mark`.

## Agent workflow

After Step 0:

1. Initialize a session with the target, target artifact, language, selected
   explanation style, and technical register.
2. Set the field status.
3. Add the 3-5 calibrated prerequisites in dependency order. Use stable,
   lowercase concept IDs.
4. Record the field map: `set-map` with its source and label, `add --on-map`
   for each node with its dependencies, then `mark --as skipped --reason` for
   every node off the path. Map nodes take no self-report; skip one the user
   already has. Beyond the map, add concepts only when they become relevant;
   do not attempt to build a universal ontology.
5. Ask the helper for `next`, choose one ready concept on the path, and
   activate it.
6. Teach and checkpoint as required by the main skill.
7. Judge the scientific answer yourself, then record `pass`, `partial`, or
   `fail`. Code routes the result; it does not judge scientific correctness.
   If the user skipped the checkpoint, `mark --as taught` instead.
8. Ask for `next` again. At the end, read `summary` to prepare the closing
   artifact; its `map_states` gives every node's state.

Invoke the helper with the environment's Python executable:

```text
python <skill-root>/scripts/knowledge_state.py <command> <state-file> ...
```

Available commands are `init`, `validate`, `add`, `set-field-status`,
`set-preferences`, `set-map`, `next`, `activate`, `checkpoint`, `mark`, and
`summary`. Run `--help` for exact arguments.

Use `--operation-id` with a stable value when retrying a mutating command. The
same operation ID is applied at most once.

## State semantics

Keep these dimensions distinct:

- `preferences`: explanation style and technical register selected at intake;
- `self_report`: `used`, `learned`, or `new` from calibration;
- `evidence`: `untested`, `pass`, `partial`, or `fail` from checkpoints;
- `progress`: `queued`, `active`, `covered`, or `skipped` for workflow routing.

An item marked `used` starts covered for routing but remains untested. A later
partial or failed checkpoint overrides that shortcut and blocks dependents.

A skipped node carries its reason and never blocks dependents; when a path node
leans on one, state it as a black box. `summary` derives each map node's state
from the dimensions above: `skipped`, else `checked` on a pass, else `taught`
once activated or covered, else `new`. `mark --as checked` exists only to
restore a pasted map; in-session, a passed checkpoint records it.

Keep the runtime invisible in the response. The user should experience only a
well-paced lesson that remembers what happened.
