# Field map

Loaded after Step 0 of an onboarding request, before planning the path; at the
close; and when the user pastes a map back. Never build a map for a one-turn
answer, in Decode mode, after a declined ladder, or because a question looked
large.

## Map and path

The **map** is what the field contains and which parts depend on which, taken
from the structure Step 0 retrieved. It does not change during the session. The **path** is the three to six nodes this session walks, one turn
each, in dependency order, chosen by the target (`pacing.md`) and the Step 0
marks.

## The skeleton

Step 0's one search finds it. Take the first you can get: the standard graduate
textbook's table of contents, a recent review's section headings, or a
published course syllabus. Where a field has no textbook, as in much of the
humanities and many interdisciplinary fields, use a handbook's or companion
volume's contents, or a scholarly encyclopedia entry's sections.

Label it **verified** or **from memory, unverified**, as `citations.md` says.
Without search, also give one concrete action that checks it: the book and
edition whose contents page to compare, or the exact listing and query to run
(`search-recipes.md`). "Check a textbook" is not a check.

Never number a from-memory skeleton as a book's chapters, or give a chapter
count you did not retrieve: a fabricated contents page is worse than none,
because it looks checked.

A contents page gives order, not dependencies. Label every dependency you infer
**inferred**; only a source that states it makes it verified.

Keep the map at chapter level, six to twelve nodes. If the source has more,
merge neighbours and say so.

## Node states

- `new`: on the path, not yet reached;
- `taught`: covered in its node turn, not yet checked;
- `checked`: the user answered its checkpoint correctly;
- `shaky`: taught, but the answer was wrong or partial; re-teach it from a
  different angle before its dependents;
- `skipped`: deliberately left out, with the reason in one clause.

Every node has exactly one. Nodes off the path start `skipped`, sharing a
clause when they share a reason; a node the user already has is skipped as
"already yours".

## Showing it

Do not ask about it in Step 0. Plan from it silently, and end Rung 1 with one
line saying the user can ask to see it.

When asked, show it once: the path one line per node with a one-clause gloss,
then the skipped nodes on a single line, a count and names only, grouped by
reason. Never reprint it; after each node turn, print only the nodes whose
state changed.

## Closing check and omissions

The session's last checkpoint tests structure, not recall: ask which node
depends on which, or why one node had to come before another. Do not ask for a
definition you already gave. The scoping rule in `checkpoints.md` still holds.

At the end, name every node you did not teach and what each one is needed for.
Do not present the path as though it were the whole field.

## Where the map lives

Within a session: the state helper when `state-runtime.md` allows it,
otherwise the conversation. Across sessions: only the closing artifact, which
the user saves and pastes back. Never imply that anything carries over on its
own.

When a map is pasted back, continue from its node states. Do not re-run the
Step 0 intake for nodes marked `taught` or `checked`. Keep the target and style
it records, re-teach `shaky` nodes first, and fold a one-line check on a
`taught` node the next turn needs into that turn's opening.

## Example

Single-cell RNA sequencing, for one paper on a new cell type. The closing
artifact, after the user stopped mid-path:

```text
Field map: single-cell RNA sequencing. [review] headings, verified, [DOI]
Target: one paper on a new cell type. Style: physical picture first

checked  count matrix
shaky    quality control: doublet removal still unclear
taught   normalization
new      dimensionality reduction: needed to judge what the UMAP shows
new      clustering and annotation: needed for the paper's central claim
skipped  differential expression (no conditions): needed to compare
         conditions
skipped  trajectory inference (no time order): needed for differentiation

Depends (inferred): counts -> QC -> normalization -> reduction ->
         clustering -> DE; reduction -> trajectory

Paste this into a new session to continue.
```
