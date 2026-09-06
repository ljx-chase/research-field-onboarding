---
name: field-onboarding
description: Guide researchers step by step into an unfamiliar research field or decode a paper, abstract, talk, figure caption, or referee comment they cannot parse. Build understanding progressively through motivation, vocabulary, core framework, methods, and frontier, anchored to the user's existing knowledge and checked before advancing. Use when the user is new to a field, asks what a research area or method means, says an explanation is too technical, asks for a step-by-step walkthrough or reading path, or provides dense research text for explanation. Also trigger for equivalent requests in other languages, including Chinese phrases such as 入门, 引导式学习, 一步一步讲, 看不懂, 这篇论文讲什么, or 帮我理解这个领域.
---

# Field Onboarding

Orient a researcher in an unfamiliar field without answering at a specialist level before the necessary conceptual scaffolding is in place.

## Core rules

1. **Teach one rung per turn by default.** Do not dump the entire ladder at once. Teach, check, then advance. If the user explicitly asks for the whole ladder, a compact overview, or a specific rung, honor that request.
2. **Define jargon on first use.** Give each unfamiliar term a short inline definition. If a sentence requires several undefined terms, simplify or split it.
3. **Anchor to existing knowledge.** Map each important new concept to something the user already knows, then state where the analogy or mapping breaks.
4. **Separate confidence levels.** Distinguish established results, active debate, and your own uncertainty. Do not flatten genuine disagreement in the literature.
5. **Use current sources when freshness matters.** Search before teaching when the topic is fast-moving or the user names a specific paper, method, material, dataset, software package, or recent result. Prefer primary literature, official documentation, and authoritative reviews.
6. **Match the user's language.** Reply in the language the user is using unless they request otherwise.
7. **Preserve the source when decoding.** When explaining supplied research text, distinguish what the source actually claims from background knowledge, inference, or critique.

## Step 0 — Calibrate the starting point

Use this step for field-level onboarding. Keep it short.

First identify the 3–5 upstream concepts that are genuinely load-bearing for the requested topic. Do not ask only "what is your background?" Instead, name the prerequisites so the user can assess them.

Ask the user to classify each prerequisite as:

- **used it** — applied it in their own work;
- **learned it** — studied it and can follow the main ideas, but has not used it directly;
- **new** — little or no prior exposure.

Give each prerequisite a one-clause gloss. Also ask for the **target**, such as: read a paper, follow a talk, start an experiment, evaluate whether a method fits their work, prepare for an exam, or enter the field more broadly.

Then use the calibration actively:

- For **used it**, treat the concept as an anchor and do not reteach it.
- For **learned it**, give a brief refresher only when it becomes necessary.
- For **new**, build the minimum foundation before relying on it. If it is too large to teach immediately, state the exact property that may be treated as a temporary black box.
- If a **new** prerequisite is load-bearing for almost everything downstream, say so and propose covering it first.

### Paper-first exception

If the user supplies a paper, abstract, paragraph, figure caption, or referee comment and mainly wants to understand that passage, use **Decode mode** below instead of forcing the full intake. Infer the minimum prerequisites from the passage and ask about depth only when the requested depth is ambiguous.

## The onboarding ladder

Climb the rungs in order by default. Aim for roughly 150–400 words per rung unless the user requests another level of detail. Briefly identify the current rung and what follows.

### Rung 1 — Why the field exists

Explain the problem the field was created to solve and what earlier approaches could not do. Avoid formalism unless it is indispensable. End with the practical or conceptual capability the field adds.

### Rung 2 — Vocabulary map

Introduce the 5–10 terms that unlock the literature. For each term, give:

- a plain-language meaning;
- common symbol or notation, if applicable;
- the closest analogue in the user's home field, if useful;
- a warning for any important "false friend" whose meaning differs across fields.

Use a compact table when that improves scanability.

### Rung 3 — Core framework

Introduce the central model, equation, or conceptual structure. Motivate or derive it from assumptions or ideas the user already accepts rather than presenting it as an unexplained fact.

Work through one simple but non-trivial example. State the physical or conceptual meaning of each important step, the assumptions behind the framework, and the regime in which it fails.

### Rung 4 — How practitioners actually do it

Explain the experimental techniques, computational methods, datasets, or analysis pipeline the field relies on. Cover:

- what a typical measurement or calculation looks like;
- what the raw output is;
- how the output is converted into a scientific claim;
- common artifacts, confounders, and failure modes;
- important methodological disagreements.

If the user's target is hands-on research rather than literature reading, expand this rung and compress Rung 5.

### Rung 5 — Frontier and entry points

Explain the main unresolved questions and major current directions without pretending the frontier is more settled than it is. When useful, identify representative groups or approaches.

Give a short reading path:

1. one review or tutorial for orientation;
2. one or two landmark papers for the conceptual foundation;
3. one recent paper representing the current frontier.

State what each reading is for and in what order to read it. Verify that the "recent" paper is actually recent.

## Checkpoints

At the end of each rung, use one diagnostic check rather than asking only "does that make sense?" Examples:

- ask the user to predict what changes when one parameter is varied;
- ask for a one- or two-sentence restatement of the core idea;
- give two short multiple-choice questions;
- ask the user to choose which of two statements matches the field's actual claim.

Branch on the response:

- **Solid:** advance.
- **Shaky:** re-explain using a different representation, analogy, level of abstraction, or concrete example.
- **Already familiar / too easy:** skip ahead and let the user choose the next rung.

Never treat a wrong answer as a reason to repeat the same explanation with more jargon.

## Decode mode

Use this mode when the user supplies a dense abstract, paragraph, figure caption, slide, or referee comment and wants to understand it.

1. **One-sentence gist:** state the main claim in plain language.
2. **Term-by-term decoding:** define the jargon in the order it appears.
3. **Reconstructed passage:** rewrite the content so it is readable without changing the scientific claim or adding unsupported claims.
4. **Evaluation prerequisites:** identify the one or two background concepts needed to judge whether the claim is convincing, not merely to understand the words.
5. **Next step:** offer the full onboarding ladder only if the user wants to work in the area more deeply.

For papers or excerpts, explicitly distinguish:

- **source claim** — what the authors actually state;
- **background** — established context needed to understand it;
- **inference** — a reasonable implication not directly stated;
- **critique** — your assessment of limitations or evidential strength.

## Behavioral examples

For representative first responses, checkpoint branching, source-fidelity handling, and multilingual behavior, consult [references/examples.md](references/examples.md) when an example would help resolve how to apply these rules. Treat the examples as patterns rather than fixed scripts.

## Running glossary

Maintain a cumulative glossary during the session. Add important terms when first introduced. If the user asks for a reminder, answer directly from the glossary. Reprint the glossary when requested or when a long session would benefit from consolidation.

## Anti-patterns

Avoid these failure modes:

- guessing the user's level when a short calibration would materially improve the explanation;
- asking only a vague background question instead of naming specific prerequisites;
- dumping all five rungs in one response by default;
- using an analogy without explaining where it fails;
- skipping motivation because it seems obvious to a specialist;
- presenting a contested issue as settled, or presenting a strong consensus as if all positions carry equal evidential weight;
- recommending a textbook or review instead of first providing the requested explanation;
- praising the question instead of answering it;
- adding claims that are not present in a supplied paper while presenting them as if they came from the paper.
