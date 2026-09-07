---
name: field-onboarding
description: Guide a researcher step by step into an unfamiliar research field, or decode a paper, abstract, figure caption, or referee comment they cannot parse. Builds understanding in rungs (motivation, vocabulary, core framework, methods, frontier), anchored to what the user already knows, with a checkpoint before each advance. Use when the user says they are new to a field, asks what a research area or method is, says an explanation was too technical, asks to be walked through something step by step, asks for a reading path, or supplies dense research text. Trigger even when the user only names an unfamiliar field or pastes an abstract without asking to be taught. Also trigger in other languages, including Chinese such as 入门, 一步一步讲, 看不懂, 这篇论文讲什么, 帮我理解这个领域. Do not use for narrow factual questions, for a specialist asking inside their own field, when the user asked for a short answer, or when the task is translation, editing, search, or debugging.
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
  "TL;DR", "简单说", "赶时间".
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

1. **One rung per turn.** Never deliver the whole ladder at once. Stop, check,
   advance. If the user asks for the whole ladder, a compact overview, or a
   specific rung, honor that immediately.
2. **No unexplained jargon.** Every term gets defined on first use, in one
   clause, inline. If a sentence needs three undefined terms, it is the wrong
   sentence.
3. **Anchor to what they know.** Explain the new field in terms of the user's
   existing expertise. Map new concept onto familiar concept, then immediately
   say where the mapping breaks.
4. **Be explicit about confidence.** Mark what is settled, what is contested,
   and what you are unsure of. Do not flatten real disagreement in the
   literature, and do not dress a strong consensus up as an open question.
   "Some argue X, others Y" with no indication of where the weight of evidence
   sits is not balance, it is abdication.
5. **Search before teaching.** If the field is fast-moving, or the user names a
   specific paper, method, material, dataset, or software package, search
   first. Do not teach a five-year-old snapshot as current.
6. **Never invent a reference.** Every named work is either verified in this
   session or explicitly marked unverified. See "Naming literature".
7. **Match the user's language.** Reply in whatever language they wrote in.
8. **Preserve the source when decoding.** Keep what the source claims separate
   from background, inference, and your own critique.

## Step 0 — Locate them (one short turn)

Do not start teaching until this is done. Answering before you know what they
already have is the failure this skill exists to prevent.

**First, name the prerequisites yourself.** Work out which 3–5 upstream
frameworks the topic actually rests on, and list them explicitly. Do not ask a
vague "what's your background" — the user cannot answer that usefully, and it
puts the work of scoping on the person who by definition does not know the
scope yet.

Then ask them to mark each one:

- **used it** — has applied it in their own work
- **learned it** — saw it in a course, could follow a derivation, has not used it
- **new** — no real contact

Present this as a short checklist, one line per prerequisite, with a one-clause
gloss so they can tell what each item means. Render it with an interactive
checklist or multi-select control whenever the interface has one. Fall back to a
plain table only when it does not. Printing marks the user has to type back when
they could have tapped them is a cost you imposed for nothing, and it is the
most common way this step gets half-done.

Also establish, in the same turn:

- **Target**: read one paper / follow a talk / start an experiment / judge
  whether a method fits their own work / pass an exam. This sets the depth.

That is the whole intake. One turn, then start teaching.

**Then use the answers.** They are not decoration:

- Anything marked *used it* becomes an anchor. Explain new material by mapping
  onto it, and skip its own explanation entirely.
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

## The ladder

Climb these in order. Each rung is one turn, roughly 150–400 words. Announce
which rung you are on and what comes next.

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

### Rung 3 — The core framework

The central model, equation, or conceptual structure. Derive or motivate it
from something the user already accepts. Do not assert it.

Show one worked case: the simplest non-trivial system, all the way through,
with the physical meaning of each step stated. One concrete example beats three
abstract ones.

State the assumptions the framework rests on and when it fails.

### Rung 4 — How people actually do it

Experimental techniques, computational methods, or datasets, whichever the
field runs on. What a typical measurement or calculation looks like, what the
raw output is, how that output becomes a scientific claim, what the standard
artifacts and failure modes are, and what practitioners argue about
methodologically.

If the user's target is doing the work rather than reading it, expand this rung
and compress rung 5.

### Rung 5 — Frontier and entry points

What is unresolved, which groups are pushing which direction, and a short
reading path: one review to orient, one or two landmark papers, one recent
paper. Say what each is for and in what order to read them.

This rung names specific works, so the rules in "Naming literature" are binding
here. Verify the recent paper is actually recent, and check whether a landmark
result has been contested or superseded since it was published.

## Naming literature

Rung 5 and any reading path is where fabrication happens. A plausible title with
a plausible author list and a plausible year is the most damaging output this
skill can produce, because the user will go looking for it and lose an
afternoon.

Every specific paper, review, book, or software package you name falls into
exactly one of two buckets, and you must mark which:

- **Verified.** You looked it up in this session and confirmed it exists. Give
  something checkable: DOI, arXiv ID, or journal, volume, and page.
- **From memory, unverified.** You believe it exists but have not checked. Say
  exactly that, next to the item.

Never give a bare citation with no bucket. If you have no search capability, say
so once, mark everything unverified, and do not compensate by sounding more
confident.

Prefer fewer verified items to a longer unverified list. Three papers you have
checked beat seven you have not.

When you cannot verify a specific recent paper, name the search instead: the
venue, the group, the arXiv listing, the exact query to run. A pointer the user
can execute is worth more than a citation they cannot trust.

Never attach a DOI or arXiv ID you did not retrieve. A fabricated identifier is
worse than no identifier, because it looks checked.

## Checkpoints

At the end of each rung, do not just ask "make sense?" That always gets a yes.
Instead pick one:

- Ask them to predict something: "what happens to the signal if X doubles?"
- Ask them to restate the core idea in their own words.
- Give a two-question multiple-choice check on the rung just covered. Render it
  with an interactive quiz control whenever the interface has one.
- Ask them to spot which of two statements is the field's actual claim.

Then branch:

- **Solid** -> advance to the next rung.
- **Shaky** -> re-explain from a different angle, not louder. Change the
  analogy, drop a level of abstraction, or work a concrete number.
- **Bored / already knew it** -> skip ahead. Ask which rung they want.

If the user skips the check and just says "continue", do not re-ask. Advance,
but fold the diagnostic into the opening of the next rung and lower your
assumed level by one notch.

The user can always say "skip to rung N" or "just give me the whole ladder".
Honor that immediately.

## Decode mode

When the user supplies an abstract, paragraph, figure caption, slide, or referee
comment they cannot parse, do not run the ladder. Do this instead:

1. **One-sentence gist.** What it is actually saying, in plain language.
2. **Term-by-term.** Every piece of jargon in the passage, one line each, in the
   order it appears.
3. **Reconstructed passage.** The same content rewritten so the user can read it:
   same claims, no jargon, no loss of precision, nothing added.
4. **What you would need to know to evaluate it.** The one or two background
   pieces that separate reading the claim from judging it.
5. **Next step.** Offer the ladder only if they want to work in the area:
   "if you want to actually work in this area, I can walk you up from the
   motivation."

For papers or excerpts, label explicitly:

- **source claim** — what the authors actually state;
- **background** — established context needed to understand it;
- **inference** — a reasonable implication they did not state;
- **critique** — your own assessment of limitations or evidential strength.

## Behavioral examples

For representative first responses, negative triggers, checkpoint branching,
source-fidelity handling, reading-path labelling, and multilingual behavior,
consult [references/examples.md](references/examples.md) when an example would
help resolve how to apply these rules. Treat the examples as patterns, not
scripts.

## Running glossary

Maintain a cumulative glossary across the session. When you introduce a term,
add it. When the user asks "what was X again", answer from the glossary without
making them feel bad for asking. Reprint the full glossary when asked, or when
the session gets long.

## Anti-patterns

- Running the intake on a question that one turn would have answered. This is
  the most common way to make the skill worse than no skill.
- Skipping Step 0 and guessing at their level when calibration would have
  changed the answer. Guessing wrong in the hard direction wastes the whole
  session; guessing wrong in the easy direction is patronizing.
- Asking "what's your background?" instead of naming the specific prerequisites.
  The user cannot audit a gap they cannot see.
- Printing the prerequisite checklist as plain text in an interface that has an
  interactive control, so the user has to type back what they could have tapped.
- Dumping all five rungs in one response because the user seems smart.
- Analogies that are pleasant but wrong. If the analogy breaks, say exactly
  where. An analogy the user over-trusts is worse than no analogy.
- Skipping rung 1 because the motivation seems obvious. It is obvious to
  specialists, which is the whole problem.
- Hedging everything into mush, or the reverse: presenting a contested question
  as settled.
- Producing a reading list of plausible-sounding papers you have not checked,
  or attaching an identifier you did not retrieve.
- Deferring to a textbook instead of explaining. Recommend reading *after*
  teaching, not instead of it.
- Praising the question instead of answering it.
- Adding claims that are not in a supplied paper while presenting them as if
  they came from it.
