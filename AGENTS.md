# AGENTS.md

## Purpose

This repository contains **Field Onboarding**, a reusable instruction set for guiding researchers into unfamiliar fields and decoding dense scientific literature.

This file provides repository-level instructions for Codex and other coding or research agents. The behavioral specification itself lives in `field-onboarding/SKILL.md`.

## Agent entrypoint

When a request involves onboarding a researcher into an unfamiliar field or decoding dense scientific material:

1. Read `field-onboarding/SKILL.md` first.
2. **Check applicability before starting.** The skill has an explicit "When not to use this skill" section. Narrow factual questions, specialist questions inside the user's own field, explicit requests for a short answer, and non-comprehension tasks such as translation, editing, search, or debugging are answered directly. Do not open the calibration intake in front of a question that one turn would have answered.
3. Follow its calibration, onboarding-ladder, checkpoint, and Decode-mode rules.
4. Read `field-onboarding/references/examples.md` only when an example is useful for resolving how to apply the rules.
5. Preserve the user's language unless they request another language.
6. When external research is needed and the agent has web/search access, prefer primary literature, official documentation, and authoritative reviews.
7. **Apply the "Naming literature" rule without exception.** Every named paper, review, book, or package is either verified in this session with a checkable identifier, or explicitly labelled "from memory, unverified". Never attach a DOI or arXiv ID that was not actually retrieved. If the agent has no web/search capability, state that limitation once, mark everything unverified, and prefer executable search pointers over citations.

## Cross-agent compatibility

The core workflow is intentionally tool-agnostic. Agents should map capabilities as follows:

- **Web/search available:** verify recent papers, methods, software, datasets, and frontier claims before presenting them as current.
- **File access available:** read supplied papers or excerpts directly and distinguish source claims from background, inference, and critique.
- **No external tools:** perform conceptual onboarding from the provided context, flag anything that would require verification, and give search pointers (venue, group, query) instead of citations that cannot be checked.
- **Interactive agent:** use one rung per turn by default and checkpoint before advancing.
- **Batch/non-interactive agent:** if interaction is unavailable, provide a compact calibration assumption, then a clearly sectioned multi-rung answer while labeling those assumptions. This is not licence to run the ladder on a request that did not warrant it; the applicability check still applies first.

## Repository conventions

- Keep the canonical reusable instructions in `field-onboarding/SKILL.md`.
- Keep examples in `field-onboarding/references/examples.md`; do not bloat the entrypoint with long demonstrations.
- Keep ChatGPT-specific UI metadata in `field-onboarding/agents/openai.yaml`.
- Keep general agent instructions in this `AGENTS.md`.
- Do not add vendor-specific behavior to the core workflow unless it is isolated and optional.
- Preserve YAML frontmatter in `SKILL.md` with only `name` and `description`.
- Keep the skill name lowercase and hyphenated.
- Keep the `description` under 1024 characters, and keep both the positive triggers and the "Do not use for ..." clause in it. Trigger scope is set in the frontmatter; the body cannot recover a trigger the description lost.
- Any change that widens what the skill fires on must add a matching negative case to `references/examples.md`.

## Validation

After modifying the skill, validate/package it with the Skill tooling available in the environment. A valid distributable archive should contain one skill with `SKILL.md` at its skill root.

## Maintainers

Primary contributors:

- LI Junxiang
- Ziyan Zhou (Anna)
