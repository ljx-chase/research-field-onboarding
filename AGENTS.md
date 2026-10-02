# AGENTS.md

## Purpose

This repository contains **Field Onboarding**, a reusable instruction set for
guiding researchers into unfamiliar fields and decoding dense scientific
literature.

This file is the entrypoint for agents. It covers two things: how to install the
skill, and how to behave once it is loaded. The behavioral specification itself
lives in `field-onboarding/SKILL.md`.

## Installation

If a user has asked you to install this skill, do the following. The skill root
is the directory `field-onboarding/`, which contains `SKILL.md` at its top level
plus `agents/`, `references/`, and `scripts/` directories. Keep that structure
intact; `SKILL.md` resolves its optional resources relative to its own location.

Pick the case that matches your environment.

**Claude Code.** Copy `field-onboarding/` into `~/.claude/skills/` for all
projects, or into `.claude/skills/` in the current repository for this project
only. Equivalent one-liner if `npx` is available:

```bash
npx skills add ljx-chase/research-field-onboarding -g
```

**Claude web, Desktop, or Cowork.** These do not read `~/.claude/skills/`. Tell
the user to download `field-onboarding.zip` from the repository's releases and
upload it under Customize, then Skills. The zip must contain a single folder
with `SKILL.md` inside it, not a bare `SKILL.md` and not the whole repository.

**ChatGPT Skills.** Package `field-onboarding/` as the skill root, keeping
`SKILL.md` at that root and `agents/openai.yaml` beside it, then upload through
the Skills tab of the plugin directory.

**Codex or another repository-aware agent.** Clone this repository into the
workspace and keep this `AGENTS.md` at the workspace root. No further
installation is needed; you will load `SKILL.md` when the entrypoint below
applies.

**Cursor, OpenCode, Kimi, Gemini CLI, or any other agent with a skills
directory.** Copy `field-onboarding/` into whatever directory that agent reads
skills from, preserving the folder structure.

**Anything else.** Use `field-onboarding/SKILL.md` directly as the instruction
file. References and scripts are optional; use them when `SKILL.md` points at
them and the environment supports them.

After installing, verify it by asking a question that should trigger it, for
example "guide me into topological photonics step by step". A correct response
names three to five prerequisites, asks the user to mark each one, and offers
the three explanation styles. If it starts explaining the field immediately,
the skill did not load.

## Agent entrypoint

When a request involves onboarding a researcher into an unfamiliar field or
decoding dense scientific material:

1. Read `field-onboarding/SKILL.md` first.
2. **Check applicability before starting.** The skill has an explicit "When not
   to use this skill" section. Narrow factual questions, specialist questions
   inside the user's own field, explicit requests for a short answer, and
   non-comprehension tasks such as translation, editing, search, or debugging
   are answered directly. Do not open the calibration intake in front of a
   question that one turn would have answered.
3. Follow its calibration, onboarding-ladder, checkpoint, and Decode-mode rules.
4. **Map before climbing.** Retrieve the field's existing structure, label it
   verified or unverified, and mark node states. Only for onboarding requests.
5. Load a file from `field-onboarding/references/` when the moment for it
   arrives, not up front. `SKILL.md` carries an index of what to load when.
6. Preserve the user's language unless they request another language.
7. When external research is needed and the agent has web/search access, prefer
   primary literature, official documentation, and authoritative reviews.
8. **Carry the target through.** The target collected at calibration routes the
   shape of every rung, not only which rung is expanded. Do not collect it and
   then ignore it.
9. **Check how settled the field is before teaching**, and say which of the
   three states applies. A field with no textbook is taught in grounded mode:
   central claims attributed, unstable vocabulary flagged, horizon stated. When
   you cannot form a reliable picture and cannot search, say so and hand over a
   search instead of teaching.
10. **State conventions.** Where competing sign, phase, unit or normalization
    conventions exist, name the one in use and the alternative.
11. **Apply the "Naming literature" rule without exception.** Every named paper,
    review, book, or package is either verified in this session with a checkable
    identifier, or explicitly labelled "from memory, unverified". Never attach a
    DOI or arXiv ID that was not actually retrieved. If the agent has no
    web/search capability, state that limitation once, mark everything
    unverified, and prefer executable search pointers over citations.

## Cross-agent compatibility

The core workflow is intentionally tool-agnostic. Agents should map capabilities
as follows:

- **Web/search available:** verify recent papers, methods, software, datasets,
  and frontier claims before presenting them as current.
- **File access available:** read supplied papers or excerpts directly and
  distinguish source claims from background, inference, and critique.
- **Python and temporary file access available:** for a multi-turn ladder, use
  the bundled state helper invisibly. Never make the user operate it. Store
  session state temporarily unless the user explicitly asks to keep it.
- **No external tools:** perform conceptual onboarding from the provided
  context, flag anything that would require verification, and give search
  pointers (venue, group, query) instead of citations that cannot be checked.
- **Structured choice tool callable:** actually call it for explanation style,
  prerequisite calibration, and checkpoint choices within its question limits.
  If no such tool is callable, use compact numbered choices and accept numbers;
  do not require a prose answer.
- **Interactive agent:** one rung per turn by default, checkpoint before
  advancing.
- **Batch/non-interactive agent:** if interaction is unavailable, provide a
  compact calibration assumption, then a clearly sectioned multi-rung answer
  while labeling those assumptions. This is not licence to run the ladder on a
  request that did not warrant it; the applicability check still applies first.

## Repository conventions

- Keep the canonical reusable instructions in `field-onboarding/SKILL.md`, and
  keep it a control plane: triggers, the ladder, and one-line statements of each
  rule. Under roughly 3,000 words. Detail goes in `references/` with a pointer.
- Keep examples in `field-onboarding/references/examples.md`; do not bloat the
  entrypoint with long demonstrations.
- Keep ChatGPT-specific UI metadata in `field-onboarding/agents/openai.yaml`.
- Keep general agent instructions in this `AGENTS.md`.
- Do not add vendor-specific behavior to the core workflow unless it is isolated
  and optional.
- Preserve YAML frontmatter in `SKILL.md` with only `name` and `description`.
- Keep the skill name lowercase and hyphenated.
- Keep the `description` under 1024 characters, and keep both the positive
  triggers and the "Do not use for ..." clause in it. Trigger scope is set in
  the frontmatter; the body cannot recover a trigger the description lost.
- Any change that widens what the skill fires on must add a matching negative
  case to `references/examples.md`.

## Validation

After modifying the skill, run the relevant cases from
`field-onboarding/references/evals.md` in a fresh session. A change to trigger
scope or to a core rule needs at least five negative and five positive cases.

If `field-onboarding/scripts/knowledge_state.py` changes, also run
`python -m unittest tools.test_knowledge_state -v`.

A valid distributable archive contains one skill folder with `SKILL.md` at its
root.

## Maintainers

Primary contributors:

- LI Junxiang
- Ziyan Zhou (Anna)
