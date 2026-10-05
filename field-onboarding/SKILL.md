---
name: field-onboarding
description: Guide a researcher step by step into an unfamiliar research field, or decode a paper, abstract, figure caption, or referee comment they cannot parse. Builds understanding in rungs (motivation, vocabulary, core framework, methods, frontier), anchored to what the user already knows, with a checkpoint before each advance. Use when the user says they are new to a field, asks what a research area or method is, says an explanation was too technical, asks to be walked through something step by step, asks for a reading path, or supplies dense research text. Trigger even when the user only names an unfamiliar field or pastes an abstract without asking to be taught. Do not trigger for a one-line summary, a short overview request, or a direct factual answer; do not use it for translation, editing, search, debugging, or specialist questions inside the user's own field. Also trigger in other languages, including Chinese such as 入门, 一步一步讲, 看不懂, 这篇论文讲什么, 帮我理解这个领域.
---

# Field Onboarding

Get someone productively oriented in an unfamiliar research field, fast, without
losing them.

The failure this skill exists to prevent: answering a beginner's question at the
level of a specialist, so the answer is technically correct and completely
useless.

## When not to use this skill

This is a teaching mode, not a default. Running the full ladder on someone who
wanted one sentence is its own failure, and a more irritating one than pitching
too high. Do not run Step 0 or the ladder when:

- **The question is narrow and factual.** "What does PL stand for?" "What
  wavelength do people usually pump at?" Answer it. Do not calibrate.
- **The user is already a specialist in this exact area** and is asking a
  specific technical question inside it.
- **The user asked for it short.** "quickly", "one line", "just tell me",
  "TL;DR", "简单说", "赶时间", "Give me a two-sentence overview of X", or
  "summarize the field in a paragraph". These are not onboarding requests
  unless the user explicitly says they want to be taught step by step.
- **The task is not understanding.** Translation, proofreading, formatting,
  debugging, writing, or a literature search with a known target.
- **The user is mid-task and blocked.** Someone whose fit is failing at 2am
  needs the fix, not motivation and vocabulary.
- **The user already declined the ladder this session.** Offer once. Never
  twice.

**The one-turn test.** Before starting Step 0, ask whether the question can be
answered well in a single turn. If it can, answer it, then offer the ladder in
one line: "that is the short answer; if you want to actually work in this area,
I can walk you up from the motivation." Offer once, drop it if unclaimed.

When in doubt, answer first and offer second. A good answer followed by an offer
costs the user nothing. An intake questionnaire in front of a one-line question
costs them a turn and their patience.

## Core rules

1. **One step per turn.** One rung, or one path node, per turn. Never deliver
   the whole ladder at once. Stop, check, advance. If the user asks for the whole ladder, a compact overview, or a
   specific rung, honor that immediately.
2. **No unexplained jargon.** Every term gets defined on first use, in one
   clause, inline. If a sentence needs three undefined terms, it is the wrong
   sentence.
3. **Anchor to what they know.** Explain the new field in terms of the user's
   existing expertise. Map new concept onto familiar concept, then immediately
   say where the mapping breaks.
4. **Plain is not shallow.** Default to a capable researcher who is new to this
   field. Define field-specific language, but preserve the real mechanism,
   assumptions, scales, and equations. Never turn “simple” into childish or
   remove the formal content that makes the explanation true.
5. **Be explicit about confidence.** Mark what is settled, what is contested,
   and what you are unsure of. Do not flatten real disagreement in the
   literature, and do not dress a strong consensus up as an open question.
   "Some argue X, others Y" with no indication of where the weight of evidence
   sits is not balance, it is abdication.
6. **Search before teaching.** If the field is fast-moving, or the user names a
   specific paper, method, material, dataset, or software package, search
   first. Do not teach a five-year-old snapshot as current.
7. **State your conventions.** Where a field uses competing sign, phase, unit,
   or normalization conventions, say which one you are using and name the
   alternative the literature also uses. A reader who cannot map your equation
   onto the paper's equation has not been onboarded. This costs one clause and
   prevents the single most common silent failure in physical-science reading.
8. **Never invent a reference.** Every named work is either verified in this
   session or explicitly marked unverified. See "Naming literature".
9. **Retrieve the field's structure, do not invent it.** Label it verified or
   unverified.
10. **Name what you left out.** Every map node you did not teach, and what it
   is for.
11. **Match the user's language.** Reply in whatever language they wrote in.
12. **Preserve the source when decoding.** Keep what the source claims separate
   from background, inference, and your own critique.

## Step 0 — Locate them (one short turn)

Do not start teaching until this is done. Answering before you know what they
already have is the failure this skill exists to prevent.

**First, search once.** One search answers three things before you write the
intake: how settled the field is, its structure (the map below), and what that
structure assumes a reader already knows. If you cannot search, say so, reason
from memory out loud, and call the result provisional.

- **Settled.** Textbooks and review articles exist, the vocabulary is standard,
  the core framework is not in dispute. Teach normally.
- **Emerging or contested.** No textbook, terminology still shifting, or the
  central claims are actively argued over. Switch to grounded mode below.
- **You do not actually know.** You recognize the words but cannot say what the
  field currently contains. Say that plainly and do not teach. See "When you
  cannot onboard them" below.

Say which of the three you are in, in one line, naming what you checked.

**Second, name the prerequisites from that structure.** Take the three upstream
frameworks its opening chapters or sections assume (four if the target is
already known) and list them explicitly. Do not ask a vague "what's your
background" — the user cannot answer that usefully, and it puts the work of
scoping on the person who by definition does not know the scope yet.

Then ask them to mark each one:

- **used it** — has applied it in their own work
- **learned it** — saw it in a course, could follow a derivation, has not used it
- **new** — no real contact

Present this as a short checklist, one line per prerequisite, with a one-clause
gloss so they can tell what each item means.

**Third, the target**: read one paper / follow a talk / start an experiment /
judge whether a method fits their own work / pass an exam. This sets the depth.
If they already said it, state your reading of it instead of asking.

- **Target artifact**, when they name one. If they arrived with a specific
  paper, abstract, talk, or apparatus, keep it. Say at the start which steps
  stand between them and it, point out along the way when a step has just
  unlocked part of it, and return to it at the end. A reader who came in saying
  "I want to read X" should finish being told whether they can now read X.

**Ask in one control.** If a structured user-input, checklist, quiz, or
elicitation tool is actually callable, call it once, with the prerequisites and
the target together; never chain controls, and never print options while saying
a control would be nice. Do not infer that a control is callable just because
the app is graphical. Otherwise use a numbered fallback that accepts `1 used, 2
learned, 3 new, target a`; never require a prose background essay.

**Ask nothing else.** Explanation style defaults to physical picture first, and
the map is not shown; if they already stated a style, use it. Load
[references/explanation-styles.md](references/explanation-styles.md) before
Rung 1. End Rung 1 with one line saying they can ask for "derivation first",
"balanced" or "show the map" at any time, and switch the moment they do.

That is the whole intake. One turn, then start teaching.

**Then use the answers.** They are not decoration:

- Anything marked *used it* becomes an anchor. Explain new material by mapping
  onto it, and skip its own explanation entirely. It licenses **only what was
  listed**, at the breadth you listed it. "Lasers in practice" does not mean
  femtosecond pulses, mode-locking, or dispersion management; "programming" does
  not mean their specific framework. When a rung needs a narrower sub-skill
  inside a marked anchor, name that sub-skill and give it one line, or ask. Do
  not silently widen an anchor to cover a neighbour.
- Anything marked *learned it* gets a two-line refresher at the moment it is
  first needed, not up front.
- Anything marked *new* gets built up before the rung that depends on it, or, if
  it is too large to build, gets a stated black box: "you can take this as
  given; here is the one property of it that matters downstream."

If a prerequisite marked *new* is genuinely load-bearing for the whole field,
say so at the start and propose covering it first, rather than teaching on top
of a gap.

**If the user ignores the checklist** and just says "go ahead", do not re-ask.
Assume *learned it* across the board, say in one line that you are assuming it,
and start. Correct downward the first time an anchor fails to land.

### Paper-first exception

If the user supplies a paper, abstract, paragraph, figure caption, or referee
comment and mainly wants to understand that passage, use **Decode mode** below
instead of forcing the intake. Derive the prerequisites from the passage itself
and ask about depth only if the depth they want is ambiguous.

### Keep state without burdening the user

For a multi-turn ladder, when Python and temporary file access are available,
load [references/state-runtime.md](references/state-runtime.md) after Step 0 and
use the bundled state helper invisibly. Never ask the user to run commands,
manage JSON, or choose storage. If the helper is unavailable, continue with
conversation state.

## When the field is not settled

If Step 0 found the field emerging, contested, or beyond you, load
[references/unsettled-fields.md](references/unsettled-fields.md) before Rung 1
and follow it for the rest of the session. When you cannot form a picture at
all, hand over a search instead of teaching.

## Map and path

The structure from Step 0 is the map: what the field contains, at chapter level.
Do not invent one, and do not search again only for it. Label it **verified** or
**from memory, unverified**, and label **inferred** any dependency you work out
rather than read off a source. Build a map only for an onboarding request, never
because a question looked large.

Plan the path from it: the three to six nodes this session walks, in dependency
order. Mark every node `new`, `taught`, `checked`, `shaky` or `skipped`, with a
reason for each skip. Show the map only when asked; once shown, never reprint
it, and after each node turn print only the nodes whose state changed.

On a pasted map, continue from its node states; do not re-run Step 0 for
`taught` or `checked` nodes. Load
[references/field-map.md](references/field-map.md) before planning the path.

## The ladder

Rungs 1 and 2 run once, for the whole field. Then the path: one turn per path
node, each carrying Rungs 3 and 4 for that node. Rung 5 runs once, at the end.
Announce which rung or node you are on and what comes next.

Length and emphasis are both set by the reader's stated target, not by the
rung. Load [references/pacing.md](references/pacing.md) before Rung 1 for the
per-target word budgets and for how each target reshapes the climb.

### Rung 1 — Why this field exists

The problem it was invented to solve, and what was inadequate before it. No
formalism. If the user cannot state the motivating question in their own words,
nothing above this rung will stick.

End with: what the field lets you do that you could not do otherwise.

### Rung 2 — Vocabulary map

The 5–10 terms that unlock the literature. For each: plain-language meaning,
the symbol or notation used, and, where one exists, the equivalent concept in
the user's home field.

Format as a compact table. This is the rung the user will come back to most, so
make it dense and scannable. It is a reference card, not a lecture.

Include the field's abbreviations and any term that means something different
here than in the user's home field. Those false friends cause the most damage.

In an emerging field, mark which terms are not yet standard and name the
competing usages.

### Rungs 3–4 — One turn per path node

For each node, in path order:

- **Core framework (Rung 3).** The node's central model or equation, derived
  or motivated from something the user already accepts, never asserted. One
  worked case, the simplest non-trivial system all the way through, with the
  physical meaning of each step. Its assumptions, and when it fails.
- **How people actually do it (Rung 4).** The techniques, calculations or
  datasets behind it: a typical measurement or calculation, its raw output, how
  that output becomes a claim, the standard artifacts and failure modes, and
  what practitioners argue about.

Weight the two by the node and the target: a methods node is mostly Rung 4, a
theory node mostly Rung 3, and a hands-on target turns Rung 4 into procedure.
If a node genuinely needs two turns, take two and say so at the break.

### Rung 5 — Frontier and entry points

What is unresolved, which groups are pushing which direction, and a short
reading path: one review to orient, one or two landmark papers, one recent
paper. Say what each is for and in what order to read them.

Its named works follow "Naming literature": check that the recent paper is
recent and that no landmark result has since been superseded.

## Naming literature

Every specific paper, review, book, or package you name is either **verified**
in this session with a checkable identifier, or explicitly labelled **from
memory, unverified**. There is no third option, and an identifier you did not
retrieve is never attached.

Load [references/citations.md](references/citations.md) before producing a
reading path or attributing a claim.

## Closing artifact

When the ladder finishes, or whenever the user stops, produce one compact
takeaway they can keep:

- the map, with its source label, every node's state, and what each untaught
  node is for;
- the running glossary;
- the reading path, with each item's verification label intact;
- the two or three questions the field itself has not settled;
- which prerequisites they marked *new* and still have not covered;
- if they arrived with a target artifact, whether they can now read it, and
  what is still likely to block them in it.

Keep it short enough to paste into their own notes, or into a new session to
resume. This is the only part of the session that survives it.

Offer it, do not force it. If they are mid-ladder and leaving, give the map,
the glossary and the open prerequisites and skip the rest.

## Checkpoints

End each rung and each node turn with a real diagnostic, never "make sense?",
which always gets a yes. Scope it to what you just taught: you must be able to point at the sentence
containing the answer, and a reader who marked exactly these prerequisites must
be able to answer it. A wrong answer should reveal a hole in your explanation,
not in their background. Then mark the node: `checked` on a correct answer,
`shaky` on a wrong or partial one (re-teach it from a different angle before its
dependents), `taught` if they skip the check. The session's last checkpoint
tests structure, not recall: which node depends on which, or why one came first.

Load [references/checkpoints.md](references/checkpoints.md) for the question
types, how to branch on the answer, and what to do when the user skips it.

## Decode mode

When the user supplies text they cannot parse (see "Paper-first exception"), do
not run the ladder or build a map. Load
[references/decode-mode.md](references/decode-mode.md) and follow it, keeping
**source claim**, **background**, **inference**, and **critique** apart.

## References

This file is the control plane. Load a reference when the moment for it arrives,
not up front.

| File | Load it when |
| --- | --- |
| `references/pacing.md` | Before Rung 1, once the target is known |
| `references/field-map.md` | Planning the path, closing a session, or a map was pasted back |
| `references/unsettled-fields.md` | The field is emerging, contested, or beyond you |
| `references/citations.md` | You are about to name a specific work |
| `references/search-recipes.md` | You need to verify something, or to hand over a query |
| `references/checkpoints.md` | Before the first checkpoint |
| `references/decode-mode.md` | The user supplied text instead of a field |
| `references/explanation-styles.md` | Before Rung 1, and when the user switches style |
| `references/state-runtime.md` | A multi-turn ladder can use local Python and temporary files |
| `references/anti-patterns.md` | Reviewing your own output |
| `references/examples.md` | An example would settle how a rule applies |
| `references/evals.md` | You are changing this skill, not using it |

## Running glossary

Maintain a cumulative glossary across the session. When you introduce a term,
add it. When the user asks "what was X again", answer from the glossary without
making them feel bad for asking. Reprint the full glossary when asked, or when
the session gets long.
