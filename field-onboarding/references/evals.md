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

---

## Positive cases: the skill must do its job

### P1 — bare field name, no request to be taught

> I keep seeing "chiral phonons" in talks.

- **Passes if** it names 3-5 prerequisites and asks the user to mark each.
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

### P3 — an interactive control is used when one exists

Same as P1, in an interface with a checklist or multi-select control.

- **Passes if** the prerequisites are rendered with the control.
- **Fails if** they are printed as a static table the user has to type answers
  to.
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
