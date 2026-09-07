# Field Onboarding

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v1.2.0-blue.svg)](#changelog)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-skill-d97757.svg)](field-onboarding/SKILL.md)
[![ChatGPT Skill](https://img.shields.io/badge/ChatGPT-Skill-10a37f.svg)](field-onboarding/SKILL.md)
[![Codex Compatible](https://img.shields.io/badge/Codex-compatible-111827.svg)](AGENTS.md)
[![Agent Friendly](https://img.shields.io/badge/agents-cross--agent-6f42c1.svg)](AGENTS.md)

<p align="center">
  <img src="docs/before-after.svg" alt="Left: a general assistant answers a beginner's question about topological photonics with twelve unexplained terms, and answers the follow-up with three more. Right: Field Onboarding first asks the reader to mark four prerequisites as used it, learned it, or new." width="960">
</p>

**Ask an assistant about a field you do not know, and it will answer at the level
of someone who already does.** The answer is correct. You cannot use it, and you
cannot tell which of its twelve terms you were supposed to already know. Ask
again and you get more terms.

The problem is not that the model knows too little. It is that nobody asked you
what you know before choosing where to start.

Field Onboarding is a skill for **Claude Code, ChatGPT, Codex, and other
instruction-following agents**. It makes the agent locate you first, then teach
upward from there, one step at a time.

## Quick start

**Claude Code** — one command:

```bash
npx skills add ljx-chase/research-field-onboarding -g
```

Or copy `field-onboarding/` into `~/.claude/skills/`. Drop `-g`, or use
`.claude/skills/`, to scope it to a single project instead.

**Claude apps (claude.ai, Desktop, Cowork)** — desktop and cloud sessions do not
read `~/.claude/skills/`. Enable the skill on your account instead, via Customize
in the Desktop sidebar or the skill settings on claude.ai.

**ChatGPT Skills** — use `field-onboarding/` as the skill root, keep `SKILL.md`
at that root and `agents/openai.yaml` alongside it, and package it with the skill
packaging tool in your environment.

**Codex or another repository-aware agent** — clone this repository into the
workspace and keep `AGENTS.md` at the root. It tells the agent when to load the
workflow.

**Anything else** — hand the agent `field-onboarding/SKILL.md` as its
instruction file.

Then try:

```text
I understand nonlinear optics but not topological photonics. Guide me into the field step by step.
```

A good first response names the prerequisites and asks which ones you already
have. It does not open with a paragraph of definitions.

## What it does differently

**1. It names your gaps for you.** Not "what's your background?" — you cannot
audit a gap you cannot see. The agent works out the three to five upstream
frameworks the topic actually rests on, lists them with a one-clause gloss, and
asks you to mark each as *used it*, *learned it*, or *new*. Then it uses the
marks: anchors are never re-taught, black boxes are declared as black boxes, and
a load-bearing gap gets built before anything stands on it.

**2. It teaches one rung at a time.** Motivation, vocabulary, core framework,
methods, frontier. Each rung is one turn and ends with a real diagnostic — a
prediction, a restatement, a forced choice — not "does that make sense?", which
always gets a yes. Wrong answers get a different explanation, not a louder one.

**3. It will not invent a reference.** Reading paths are where models fabricate,
and a plausible title with a plausible year costs you an afternoon. Every named
work is either verified in-session with a DOI or arXiv ID, or explicitly labelled
`from memory, unverified`. There is no third option, and an identifier that was
not retrieved is never attached.

**4. It knows when to stay out of the way.** Ask a narrow factual question and
you get a narrow factual answer. The ladder is offered once, in one line, and
dropped if you do not take it.

## Scope: when it fires, and when it does not

**It should run** when you are new to a field, cannot parse a paper or abstract,
ask for a step-by-step walkthrough or a reading path, or say an explanation was
too technical. It fires even if you only name an unfamiliar field without asking
to be taught.

**It should not run** when the question is narrow and factual, when you are a
specialist asking inside your own field, when you asked for it short, when the
task is translation, editing, formatting, debugging or a search with a known
target, when you are blocked mid-experiment and need the fix, or when you already
declined the ladder earlier in the session.

The governing heuristic is the **one-turn test**: if a single turn answers the
question well, the agent answers it and then offers the ladder once. Answer
first, offer second.

## The ladder

| Rung | What it delivers |
| --- | --- |
| 0. Calibrate | Prerequisites named and marked, plus your target |
| 1. Why the field exists | The problem it was invented for, and what was inadequate before |
| 2. Vocabulary map | The 5–10 terms that unlock the literature, with symbols, home-field analogues, and false friends |
| 3. Core framework | The central model, motivated rather than asserted, with one worked case and its failure regime |
| 4. How people actually do it | Measurements or calculations, raw output, how output becomes a claim, standard artifacts |
| 5. Frontier and entry points | What is unresolved, and a labelled reading path |

Your **target** routes the whole ladder, not just its length. Reading a paper
weights notation and formalism; judging whether a method fits your work leads
with phenomena and worked numbers and expands Rung 4; doing it hands-on turns
Rung 4 into a procedure. At the end the agent produces a takeaway you keep: the
glossary, the reading path, the field's open questions, and the prerequisites you
still have not covered.

For supplied text it switches to **Decode mode** instead, separating **source
claim**, **background**, **inference**, and **critique** so you can see which is
which.

## Reference discipline

- **Verified** — looked up in this session, with DOI, arXiv ID, or
  journal/volume/page.
- **From memory, unverified** — believed to exist, not checked, and labelled in
  those words.

Bare unlabelled citations are not permitted. Where verification is impossible,
the skill gives an executable search pointer — venue, group, query — instead of a
citation, and prefers three verified items to seven unverified ones.

It also states its conventions. Where a field uses competing sign, phase, unit or
normalization conventions, the agent says which one it is using and names the
alternative, because a reader who cannot map the equation onto the paper's
equation has not been onboarded.

## Example prompts

- `I am new to exciton-polaritons. Walk me through the field step by step.`
- `I understand nonlinear optics but not topological photonics. Help me get oriented.`
- `I cannot parse this abstract. Explain what it is actually saying.`
- `Give me a reading path into chiral phonons.`
- `一步一步带我入门拓扑光子学。`

And one it should **not** take over:

- `Quick one: what does MRO stand for in this field?` — expect a direct answer
  plus a one-line offer, not a prerequisite checklist.

## Repository structure

```
research-field-onboarding/
├── README.md
├── AGENTS.md                   # entrypoint for repository-aware agents
├── CONTRIBUTING.md
├── LICENSE
├── .gitignore
├── docs/
│   ├── before-after.svg        # README graphic (English)
│   └── before-after-zh.svg     # Chinese variant
├── tools/
│   └── make_demo.py            # regenerates the SVGs, and PNGs on demand
└── field-onboarding/
    ├── SKILL.md                # the canonical instruction document
    ├── agents/
    │   └── openai.yaml
    └── references/
        └── examples.md         # positive and negative behavioral examples
```

`SKILL.md` is the single source of truth. Everything else is packaging.

## Design principles

- Answer first, offer the ladder second. Never put an intake questionnaire in
  front of a one-line question.
- One conceptual rung per turn by default.
- Define jargon on first use, and state which convention you are using.
- Anchor new concepts to the user's existing expertise, then say where the
  analogy breaks. An analogy the user over-trusts is worse than no analogy.
- Separate source claims, background knowledge, inference, and critique.
- Never invent a reference. Verified or labelled unverified, with no third
  option.
- Use diagnostic checkpoints instead of generic comprehension questions.
- Close with something the user keeps.
- Degrade gracefully when an agent lacks browsing, file access, or
  interactivity.

## Changelog

### v1.2.0

- **Conventions rule.** The agent must state which sign, phase, unit or
  normalization convention it is using, and name the competing one. Mismatched
  conventions are a common silent failure when moving between an explanation and
  a paper.
- **The target now routes the whole ladder**, not just which rung gets expanded.
  Reading a paper, judging a method's fit, hands-on work and following a talk
  each get a different shape.
- **Closing artifact.** Sessions end with a takeaway the user keeps: glossary,
  labelled reading path, the field's open questions, and uncovered prerequisites.
- **Word budget raised** to roughly 200–500 words per rung and up to 700 for
  Rung 3, which could not fit a motivated framework plus a worked example plus
  its limits in the old ceiling.

### v1.1.2

- Removed the committed PNG rasters. They were derived artifacts duplicating the
  SVGs, and as the only binary files in the repository they were the ones that
  failed on a constrained `git clone`. `tools/make_demo.py --png` regenerates
  them when a raster is needed.

### v1.1.1

- Step 0 now requires an **interactive** checklist wherever the interface has
  one, with a plain table as the explicit fallback. The previous wording (`Use a
  checklist or multi-select control if the interface offers one`) was a
  conditional clause, and in live testing it was skipped: the prerequisite list
  was printed as a static table and the user had to type their marks back. Same
  hardening applied to the checkpoint quiz.
- Added a matching anti-pattern.

### v1.1.0

- Added a **When not to use this skill** section and the one-turn test, plus a
  matching `Do not use for ...` clause in the frontmatter description. The skill
  previously had broad positive triggers and no negative ones, so it over-fired
  on narrow questions.
- Added a **Naming literature** section making the verified /
  `from memory, unverified` label mandatory for every named work, and forbidding
  unretrieved identifiers.
- Restored the imperative register of the instruction text throughout. Normative
  prose was replaced with direct rules, which agents follow more reliably.
- Added handling for the two most common real-session behaviors: the user
  ignoring the prerequisite checklist, and the user skipping the checkpoint with
  "continue".
- Added `references/examples.md` cases for a negative trigger and for a labelled
  reading path.

### v1.0.0

- Initial public release.

## Contributing

Contributions are welcome, particularly behavioral examples from disciplines
other than the physical sciences, and negative cases where the skill fires when
it should not. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT License. Copyright (c) 2026 LI Junxiang and Ziyan Zhou (Anna).
