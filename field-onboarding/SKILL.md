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
6. **State your conventions.** Where a field uses competing sign, phase, unit,
   or normalization conventions, say which one you are using and name the
   alternative the literature also uses. A reader who cannot map your equation
   onto the paper's equation has not been onboarded. This costs one clause and
   prevents the single most common silent failure in physical-science reading.
7. **Never invent a reference.** Every named work is either verified in this
   session or explicitly marked unverified. See "Naming literature".
8. **Match the user's language.** Reply in whatever language they wrote in.
9. **Preserve the source when decoding.** Keep what the source claims separate
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

**Second, check how settled the field is.** Do this before you teach, because
it decides which mode you are in. Search if you can. If you cannot search, say
so and reason from what you have, out loud.

- **Settled.** Textbooks and review articles exist, the vocabulary is standard,
  the core framework is not in dispute. Teach normally.
- **Emerging or contested.** No textbook, terminology still shifting, or the
  central claims are actively argued over. Switch to grounded mode below.
- **You do not actually know.** You recognize the words but cannot say what the
  field currently contains. Say that plainly and do not teach. See "When you
  cannot onboard them" below.

Say which of the three you are in, in one line, before Rung 1. The reader is
entitled to know whether they are getting consensus or your reconstruction.

Also establish, in the same turn:

- **Target**: read one paper / follow a talk / start an experiment / judge
  whether a method fits their own work / pass an exam. This sets the depth.
- **Target artifact**, when they name one. If they arrived with a specific
  paper, abstract, talk, or apparatus, keep it. Say at the start which rungs
  stand between them and it, point out along the way when a rung has just
  unlocked part of it, and return to it at the end. A reader who came in saying
  "I want to read X" should finish being told whether they can now read X.

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

## When the field is not settled

In an emerging or contested field there is no consensus to teach from, so the
usual standard, be correct, is not available. Use these instead.

- **Say it up front.** One line: no textbook exists, the vocabulary is not
  standardized, this is what the last few years of papers look like.
- **Ground the substantive claims.** In a settled field, citing a source for a
  textbook fact is noise. Here it is the only thing separating teaching from
  invention. Attribute the central claims of Rungs 3 to 5 to specific work,
  under the same verified / unverified labels as everywhere else, and mark
  anything that is your own synthesis as your synthesis.
- **Flag unstable vocabulary.** Different groups routinely name the same object
  differently before a field settles. Say when a term has competitors, and
  which paper uses which. A reader who learns one group's word and then reads
  another group's paper will think they have found a new concept.
- **Invert Rung 5.** There is no review to orient with. Give the two or three
  groups pushing the area, what each is claiming, and where they disagree.
- **State your horizon.** Your picture of a fast-moving field ages badly. Say
  when it is from, and say plainly that the last year may be missing.

Treat prerequisites the same way: in an emerging field your prerequisite list is
inferred from adjacent settled fields, not read off a curriculum. Present it as
provisional and say so.

## When you cannot onboard them

Sometimes the honest answer is that you cannot do this reliably. That is the
case when the field is too new or too narrow for you to have a real picture and
you have no way to search.

Do not fill the gap with plausible-sounding structure. Say what you can and
cannot do, then hand over a way to find the ground truth themselves:

- the search that would surface a review, written out so they can run it;
- the two or three venues or groups the work would appear in, if you know them;
- what to read the review for, which is the prerequisite list you could not
  give them.

See [references/search-recipes.md](references/search-recipes.md) for query
templates. Sending someone to a real review beats onboarding them into a field
you have reconstructed.

## The ladder

Climb these in order. One rung per turn. Announce which rung you are on and
what comes next.

**Length is set by the target, not by the rung.** The ceilings below are
defaults for someone who wants to read a paper; shift them as the target
demands.

| Target | Rung 1 | Rungs 2, 5 | Rungs 3, 4 |
| --- | --- | --- | --- |
| Read one paper | 150-250 | 300-500 | 400-700 |
| Judge whether a method fits | 200-300 | 200-400 | 500-700, weighted to 4 |
| Do it hands-on | 100-200 | 200-300 | 500-700, weighted to 4 |
| Follow a talk | 100-200 | 300-400 | 200-400 |

Someone who wants to build the apparatus does not need the field's origin story
at length. Give them the one sentence that explains why the method exists, then
spend the session on Rungs 3 and 4. Compressing Rung 1 is not skipping it.

Do not compress a derivation into a summary to hit a number. If a rung genuinely
needs two turns, take two turns and say so at the break.

### Route on the target

The target you collected in Step 0 sets the shape of every rung, not just which
one gets expanded. Use it:

- **Read one paper** -> weight notation and formalism. Keep Rung 2 dense and
  symbol-heavy; the goal is to make the page parseable.
- **Judge whether a method fits their work** -> lead with phenomena and worked
  numbers. Treat derivations as black boxes with stated properties, expand
  Rung 4 into what the method can and cannot deliver, and say plainly where it
  is a poor fit. This target is a decision, so give them what a decision needs.
- **Do it hands-on** -> Rung 4 becomes a procedure: apparatus or pipeline,
  typical parameters, what breaks first. Compress Rung 5 to tooling and
  communities.
- **Follow a talk** -> compress everything. Rung 2 and Rung 5 matter most;
  Rung 3 can stay at the level of what the central object means.

If the user gave no target, ask once, in the same turn as the prerequisites.

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

## Closing artifact

When the ladder finishes, or whenever the user stops, produce one compact
takeaway they can keep:

- the running glossary;
- the reading path, with each item's verification label intact;
- the two or three questions the field itself has not settled;
- which prerequisites they marked *new* and still have not covered;
- if they arrived with a target artifact, whether they can now read it, and
  what is still likely to block them in it.

Keep it short enough to paste into their own notes. This is the only part of
the session that survives it.

Offer it, do not force it. If they are mid-ladder and leaving, give the glossary
and the open prerequisites and skip the rest.

## Checkpoints

**Scope the check to what you just taught.** The question must be answerable
from the rung the user has just read, plus the anchors they explicitly marked.
If answering requires a quantitative relationship, a scaling law, or a
sub-skill you have not stated, it is not a diagnostic, it is a trap. Teach the
scaling first, or ask a different question. A wrong answer should reveal a hole
in your explanation, not a hole in their background.

Two tests before you ask it. Can you point to the sentence in the rung that
contains the answer? Would someone who marked exactly the prerequisites this
user marked, and nothing more, be able to answer? If either is no, rewrite the
question.

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

## Verifying and searching

When you have a search tool, use it: to check how settled a field is, to verify
every named work, and to test your own picture against what was published
recently. When you do not, hand the reader the query instead of a guess.

[references/search-recipes.md](references/search-recipes.md) has the query
templates for both cases. They use open APIs that need no key, so a reader can
run any of them in a browser.

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
- Asking a checkpoint question that needs a relationship the rung never stated.
  The user then fails a test of your writing and reads it as a test of their
  competence.
- Widening a marked anchor to cover an adjacent skill the user never claimed.
- Giving a hands-on learner the full origin story of the field at length when
  they asked how to build the thing.
- Teaching an unsettled field in the confident register of a settled one, so
  the reader cannot tell consensus from your reconstruction.
- Attaching a citation to every textbook sentence. Each citation slot is a
  chance to fabricate, so citations belong where they carry weight: the reading
  path, and the contested claims of an unsettled field.
- Taking a target artifact at the start and never returning to it.
- Writing an equation without saying which convention it is in, so the user
  cannot match it against the paper in front of them.
- Deferring to a textbook instead of explaining. Recommend reading *after*
  teaching, not instead of it.
- Praising the question instead of answering it.
- Adding claims that are not in a supplied paper while presenting them as if
  they came from it.
