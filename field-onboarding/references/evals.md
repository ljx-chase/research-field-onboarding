# Evals

A regression set for the skill itself. Run it after any change to `SKILL.md` or
to a reference file. It is not part of using the skill.

## How to run

Start a **fresh session** with the skill installed and no other context, one
prompt per session. A prompt run in a session that already discussed the skill
proves nothing, because the model has been primed.

Read the response against the checks. Each check is pass or fail, not a
judgement call. If a check needs interpretation, it is written badly: rewrite
the check.

Record results as a table in your PR. Five negatives and five positives is the
minimum bar for merging a change to trigger scope or to a core rule.

```
| id  | pass | note                                  |
|-----|------|---------------------------------------|
| N1  | ✓    |                                       |
| N2  | ✗    | opened the intake on a 3-word question |
```

A failing check is not always a bug in the model. It is at least as often a rule
that reads clearly to you and ambiguously to a cold reader. Fix the rule first.

---

## Negative cases: the skill must stay out of the way

These exist because v1.0.0 had broad positive triggers and no negative ones, and
over-fired on every one of them.

### N1 — narrow factual question

> Quick question: in this field, what does MRO stand for?

- **Passes if** the answer is direct and short.
- **Fails if** a prerequisite checklist, a rung, or a calibration question
  appears before the answer.
- An offer of the ladder is allowed, once, at the end, in one line.

### N2 — specialist inside their own field

> I run RA-Raman on layered antiferromagnets. For a C2h crystal, which tensor
> elements survive at oblique incidence?

- **Passes if** it answers the technical question.
- **Fails if** it offers to teach Raman spectroscopy, or asks what the user
  already knows about tensors.

### N3 — explicit request for brevity

> One line only: what's the difference between SHG and SFG?

- **Passes if** the answer is one or two lines.
- **Fails if** the ladder, the intake, or a multi-paragraph explanation appears.

### N4 — not a comprehension task

> Translate this abstract into Chinese, keep the terminology as is.

- **Passes if** it translates.
- **Fails if** it explains the field, decodes the abstract, or offers to.

### N5 — blocked mid-task

> My Lorentzian fit keeps diverging on this Raman peak and I need it working
> tonight. Here's the code.

- **Passes if** it goes at the problem.
- **Fails if** it offers an onboarding ladder into peak fitting.

### N6 — already declined

Run N1, and when the ladder is offered, reply "no thanks, just the answer".
Then ask a second question in the same field.

- **Passes if** the ladder is not offered again.
- **Fails if** it re-offers.

### N7 — one-turn answers do not start state machinery

Run N1 in an environment where the bundled state helper is available.

- **Passes if** it answers directly without creating onboarding state.
- **Fails if** it initializes a session merely because the helper exists.

### N8 — Decode mode does not expose or require the runtime

> Decode this abstract for me: [supply a short abstract].

- **Passes if** it enters Decode mode directly.
- **Fails if** it asks the user to initialize state, run a command, or manage a
  file before receiving the explanation.

### N9 — one-turn answers do not open a style intake

Run N1 in an interface with structured choice controls.

- **Passes if** it answers directly without asking for an explanation style.
- **Fails if** the existence of a choice tool causes an unnecessary style or
  prerequisite questionnaire.

### N10 — one question does not get a map

> In single-cell RNA sequencing, what is a UMI?

- **Passes if** the question is answered and no map or skeleton appears.
- **Fails if** a field structure is retrieved or printed.

### N11 — Decode mode does not get a map

> What is this abstract saying? [supply a dense abstract]

- **Passes if** Decode mode runs normally with no map.
- **Fails if** a skeleton is retrieved or printed first.

### N12 — a short answer stays short

> TL;DR: what is reinforcement learning?

- **Passes if** the answer is short and no map appears.
- **Fails if** a map is printed anyway.

### N13 — a declined ladder stays declined

Run N1, decline the offered ladder, then ask a follow-up in the same field.

- **Passes if** no map appears.
- **Fails if** the map becomes a second way of starting the ladder.

---

## Positive cases: the skill must do its job

### P1 — bare field name, no request to be taught

> I keep seeing "chiral phonons" in talks.

- **Passes if** it names three prerequisites (four if the target is already
  known), asks the user to mark each, and asks the target in the same turn.
- **Fails if** it opens with a definition paragraph, or asks "what's your
  background?" instead of naming the prerequisites itself.
- Also fails if it teaches Rung 1 in the same turn as the intake.

### P2 — the marks are actually used

Answer P1's checklist with one prerequisite marked *used it* and one marked
*new*.

- **Passes if** the *used it* item is treated as an anchor and never explained,
  and the *new* item is either built up before the rung that needs it or
  declared a black box with the one property that matters.
- **Fails if** it explains the anchor anyway, or teaches on top of the gap
  without acknowledging it.

### P3 — a prerequisite control is called when available

Same as P1, in an environment exposing a callable structured user-input,
checklist, or elicitation tool.

- **Passes if** the agent calls the control once, with the prerequisite marks
  and the target together.
- **Fails if** every prerequisite is printed as a static table the user has to
  type back despite the tool being callable, or if it chains several controls.
- This one failed in live testing when the rule was phrased as a conditional
  clause, which is why it is here.

### P4 — the checkpoint is scoped to the rung

Complete one rung and reach the checkpoint.

- **Passes if** the answer to the checkpoint question appears in the rung just
  delivered. Point at the sentence.
- **Fails if** answering needs a scaling law, a formula, or a sub-skill the rung
  never stated.
- Also fails if the question assumes a narrower skill than the user marked, for
  example reading "used lasers" as "familiar with femtosecond pulses".

### P5 — the target reshapes the climb

Run P1 twice, once with the target "read one paper", once with "build the
apparatus".

- **Passes if** the two sessions differ in more than length: notation and
  formalism weighted in the first, Rung 4 expanded into procedure in the second,
  Rung 1 visibly shorter in the second.
- **Fails if** the two are the same content at different word counts.

### P6 — no unverified citation goes out unlabelled

Reach Rung 5, or ask directly for a reading path.

- **Passes if** every named work carries either a checkable identifier or the
  words "from memory, unverified".
- **Fails if** any title, author list, or year appears with no label, or if a
  DOI or arXiv ID appears that was not retrieved in the session.
- With no search tool available, passes if it says so once and labels everything
  unverified.

### P7 — unsettled fields are declared as such

> Guide me into <a field with no textbook and heavy recent churn>.

- **Passes if** it states, before Rung 1, that the field is emerging or
  contested, and afterwards attributes central claims, flags terminology that is
  not yet standard, and says how old its picture is.
- **Fails if** it teaches a frontier area in the same confident register as a
  settled one.

### P8 — it refuses when it should

> Guide me into <a real but very narrow, very recent area>, and do not search.

- **Passes if** it says plainly that it cannot form a reliable picture and hands
  over a way to find a review, rather than teaching.
- **Fails if** it produces a fluent five-rung account anyway.
- This is the check most likely to fail, and the most important one.

### P9 — conventions are stated

Reach a rung containing an equation or a sign-dependent quantity.

- **Passes if** it says which convention it is using and names the competing one
  where the literature disagrees.
- **Fails if** the equation appears bare.

### P10 — the target artifact closes the loop

Open with "I want to read this paper" and a title or abstract.

- **Passes if** it says at the start which rungs stand between the reader and
  that paper, and at the end whether they can now read it and what is still
  likely to block them.
- **Fails if** the paper is collected and never mentioned again.

### P11 — state support is invisible

Run P1 in an environment with Python, temporary file access, and the bundled
state helper, then continue for at least two concepts.

- **Passes if** state is maintained without asking the user to run commands,
  prepare JSON, choose a file path, or understand the implementation.
- **Fails if** runtime mechanics appear in the lesson or become user homework.

### P12 — state support degrades gracefully

Run P1 in an environment without Python or writable files.

- **Passes if** the ordinary prompt workflow continues with no loss of the
  calibration, pacing, or checkpoint behavior.
- **Fails if** onboarding stops or the user is asked to repair the environment.

### P13 — style and map are defaults, not intake questions

Run P1 in an environment with a structured user-input or elicitation tool.

- **Passes if** the intake asks neither for an explanation style nor about the
  map.
- **Fails if** either appears in the intake, as a question or as a control.

### P14 — the default is intuitive without becoming shallow

Run P1, do not choose a style, and reply “go ahead” after calibration.

- **Passes if** Rung 1 or the first formal rung starts from a physical picture
  and later retains the relevant equation, assumptions, and limitations.
- **Fails if** it opens with unexplained specialist notation, or removes the
  formal content and substitutes a childish analogy.

### P15 — level corrections change one axis

After a technical explanation, reply: “Too professional; keep the equations,
but give me the physical picture and do not talk down to me.”

- **Passes if** the agent preserves the claim and equation, fills only the
  smallest missing prerequisite, and changes the explanation order or
  representation.
- **Fails if** it restarts the whole ladder, deletes the mathematics, or merely
  repeats the same explanation with simpler adjectives.

### P16 — a skeleton is retrieved and labelled before any rung

Run P1 with search available, answer the checklist, and after Rung 1 say
"show the map".

- **Passes if** the map is labelled verified with a named source, and any
  dependency it shows is labelled inferred unless the source states it.
- **Fails if** there is no skeleton, a chapter list appears with no label, or
  an inferred dependency is presented as verified.

### P17 — without search, the label and the check survive

Same as P16, search unavailable.

- **Passes if** the skeleton is labelled from memory and unverified, and the
  user is given one concrete action that checks it: a specific book and
  edition, or a specific arXiv listing and query.
- **Fails if** the skeleton is unlabelled, is numbered as a named book's
  chapters, or the suggested check is vague ("look it up in a textbook").

### P18 — omissions are named at the end

Run an onboarding session to its close, or say "I have to stop here" after
Rung 2.

- **Passes if** every untaught node is named with what it is needed for, and a
  dependency line, if present, is labelled inferred unless a source states it.
- **Fails if** the session ends as though the path were the whole field.

### P19 — a pasted map resumes

In a fresh session, paste a closing-artifact map with some nodes marked
`taught` or `checked`, and say "continue".

- **Passes if** it continues from those states and does not re-run the intake
  for them.
- **Fails if** it starts over, re-asks about covered nodes, or ignores the
  states.

### P20 — the closing check tests structure

Reach the last rung of a session.

- **Passes if** the final check asks which node depends on which, or why one
  node came before another.
- **Fails if** it asks for a definition that was already given.

### P21 — style and map change on request

After Rung 1, say "show the map", and in the next turn "derivation first".

- **Passes if** the map appears once, with its label and node states, and the
  following turn switches to derivation first without restarting.
- **Fails if** either request re-runs the intake or is ignored.

### P22 — Rung 1 announces the defaults

Answer P1's checklist, or reply "go ahead".

- **Passes if** Rung 1 starts with no map printed and ends with one line saying
  the user can ask for "derivation first", "balanced" or "show the map".
- **Fails if** a map is printed unasked, or the line is missing.

### P23 — the intake is built on a search

Run P1 with search available.

- **Passes if** a search runs before the intake is written, and the intake says
  what it checked.
- **Fails if** the prerequisites appear with no search although search was
  available.

### P24 — one path node per turn

Answer P1's checklist and continue past Rung 2.

- **Passes if** the next turn teaches one path node, names it, and ends with a
  checkpoint on it.
- **Fails if** one turn covers several path nodes.

### P25 — a wrong answer leaves the node shaky

Answer a node turn's checkpoint wrongly.

- **Passes if** the node is re-taught from a different angle, and wherever its
  state is reported it is `shaky`.
- **Fails if** it advances to a node that depends on it, or reports the node as
  `taught` or `checked`.

### P26 — a humanities field

> I'm a cognitive scientist. Guide me into phenomenology step by step.

- **Passes if** the intake says what kind of source its structure came from
  (textbook, review, syllabus, handbook, companion or encyclopedia entry) with
  a verification label, and names prerequisites from it.
- **Fails if** it claims a standard textbook it did not find, or numbers
  chapters it did not retrieve.

### P27 — an interdisciplinary field

> I'm a statistician and want to get into environmental history. Walk me
> through it.

- Same bar as P26.

---

## Multilingual spot check

### M1

> 一步一步带我入门拓扑光子学。

- **Passes if** the whole response, including the prerequisite checklist and the
  three marking labels, is in Chinese.
- **Fails if** it replies in English, or mixes in English section headers.

### M2

> 这个缩写在这个领域是什么意思？

- Negative case in Chinese. Same bar as N1.

---

## Known-weak checks

Written down so the next person does not mistake them for solid.

- **P5** depends on judging whether two responses "differ in more than length",
  which is the softest check here. If you can make it binary, do.
- **P7 and P8** need a field you personally know is unsettled. Pick one from
  your own area rather than trusting the model's judgement about which fields
  are settled, since that judgement is exactly what is under test.
- Nothing here tests session length. The skill claims one rung per turn, but a
  ten-turn session is expensive to run and nobody has done it yet.
- **P1** is borderline by nature: a bare field name sits between the one-turn
  test and the "trigger even when the user only names a field" clause. Before
  v1.9 the same prompt got the intake in one of three fresh runs, and in three
  of three on v1.8.1. Run it three times and record the count, not one result.
- **P18 and P20** need a session that reaches its end. A transcript prefix that
  ends on the user leaving, or on the last rung, is a cheaper stand-in, but it
  primes the model with the earlier turns, so record which you used.
