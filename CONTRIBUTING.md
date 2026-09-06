# Contributing

Thank you for improving Field Onboarding.

## Maintainers

Primary contributors and maintainers:

- **LI Junxiang**
- **Ziyan Zhou (Anna)**

## What to contribute

Useful contributions include:

- clearer trigger conditions;
- stronger calibration and checkpoint logic;
- examples from additional scientific disciplines;
- multilingual examples;
- improvements to source-fidelity rules;
- compatibility improvements for ChatGPT, Codex, and other instruction-following agents.

## Workflow

1. Fork the repository.
2. Create a branch for one focused change.
3. Edit the relevant file. Keep core behavior in `field-onboarding/SKILL.md` and longer examples in `field-onboarding/references/examples.md`.
4. Check that the instructions remain tool-agnostic unless a tool-specific section is explicitly required.
5. Validate the skill with the available Skill validator/packager.
6. Test at least one representative prompt affected by the change.
7. Open a pull request explaining the problem, the change, and the test prompt/result.

Please avoid adding long background tutorials to `SKILL.md`; the entrypoint should remain a compact control plane.
