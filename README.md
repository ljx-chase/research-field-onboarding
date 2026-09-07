# Field Onboarding

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v1.0.0-blue.svg)](#)
[![ChatGPT Skill](https://img.shields.io/badge/ChatGPT-Skill-10a37f.svg)](field-onboarding/SKILL.md)
[![Codex Compatible](https://img.shields.io/badge/Codex-compatible-111827.svg)](AGENTS.md)
[![Agent Friendly](https://img.shields.io/badge/agents-cross--agent-6f42c1.svg)](AGENTS.md)

A reusable research-onboarding skill for **ChatGPT, Codex, and other instruction-following agents**. It guides researchers into unfamiliar scientific fields step by step and decodes dense papers, abstracts, talks, figure captions, and referee comments without assuming specialist knowledge too early.

**Primary contributors:** LI Junxiang and Ziyan Zhou (Anna)

## Quick start — try it in under a minute

**ChatGPT:** install the packaged `skill.zip` from the latest release, then try:

```text
I understand nonlinear optics but not topological photonics. Guide me into the field step by step.
```

**Codex or another repository-aware agent:** clone/open this repository so the agent can read `AGENTS.md`, then try:

```text
Use the Field Onboarding workflow to teach me chiral phonons. My background is experimental optics.
```

**No installation / manual adaptation:** give your agent `field-onboarding/SKILL.md` as its instruction file and ask one of the example prompts below.

A good first response should calibrate your prerequisites and learning target instead of immediately dumping a full expert-level explanation.

## Core workflow

The agent follows a progressive research-learning loop:

1. **Calibrate** — identify 3–5 load-bearing prerequisites and the user's target.
2. **Why the field exists** — explain the problem and what capability the field adds.
3. **Vocabulary map** — define the small set of terms that unlock the literature.
4. **Core framework** — introduce the central model/equation with a worked example.
5. **Practice** — explain how experiments, calculations, datasets, or analysis are actually done.
6. **Frontier** — identify unresolved questions and a verified reading path.
7. **Checkpoint and branch** — test understanding, then advance, re-explain, or skip ahead.

For supplied scientific text, the skill switches to **Decode mode** and separates **source claim**, **background**, **inference**, and **critique**.

## Repository structure

```text
field-onboarding-public/
├── README.md
├── AGENTS.md
├── CONTRIBUTING.md
├── LICENSE
├── .gitignore
└── field-onboarding/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    └── references/
        └── examples.md
```

## Step-by-step: use with ChatGPT Skills

1. Download or clone this repository.
2. Use the `field-onboarding/` directory as the skill root.
3. Keep `SKILL.md` at that root and preserve `agents/openai.yaml`.
4. Package the skill directory with the Skill packaging tool available in your ChatGPT environment, or upload the validated `skill.zip` release artifact.
5. Start a conversation with a prompt such as: `I understand nonlinear optics but not topological photonics. Guide me into the field step by step.`
6. The skill should first calibrate prerequisites and target rather than dumping a complete specialist explanation.

## Step-by-step: use with Codex

The repository includes a root-level `AGENTS.md`, which tells Codex how to discover and apply the canonical workflow.

1. Clone the repository into a workspace visible to Codex.
2. Open the repository as the working project.
3. Keep `AGENTS.md` at the repository root.
4. Keep the canonical behavior in `field-onboarding/SKILL.md`; `AGENTS.md` directs Codex to read it when the task matches.
5. Ask Codex a research-onboarding task, for example: `Use the Field Onboarding workflow to teach me chiral phonons. My background is experimental optics.`
6. If Codex has web/search capability, it should verify freshness-sensitive claims. If it does not, it should flag that limitation rather than invent current references.

## Step-by-step: adapt to other agents

The skill is deliberately tool-agnostic. For another agent framework:

1. Use `field-onboarding/SKILL.md` as the canonical instruction document.
2. Configure the framework to load it when the user's task matches the frontmatter description.
3. If the framework supports repository instructions, also load or adapt `AGENTS.md`.
4. Map the agent's capabilities to the compatibility rules in `AGENTS.md` (web, files, interactive vs. batch).
5. Keep vendor-specific metadata separate from the canonical workflow.
6. Test the agent with the sample prompts in `field-onboarding/references/examples.md` and compare behavior against the stated good-response patterns.

## Example prompts

- `I am new to exciton-polaritons. Walk me through the field step by step.`
- `I understand nonlinear optics but not topological photonics. Help me get oriented.`
- `I cannot parse this abstract. Explain what it is actually saying.`
- `Give me a reading path into chiral phonons.`
- `一步一步带我入门拓扑光子学。`

## Design principles

- One conceptual rung per turn by default.
- Define jargon on first use.
- Anchor new concepts to the user's existing expertise.
- Separate source claims, background knowledge, inference, and critique.
- Verify freshness-sensitive information when tools permit.
- Use diagnostic checkpoints instead of generic comprehension questions.
- Degrade gracefully when an agent lacks browsing, file access, or interactivity.

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT License. Copyright (c) 2026 LI Junxiang and Ziyan Zhou (Anna).
