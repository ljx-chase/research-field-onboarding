# Contributing

Thank you for improving Field Onboarding.

## Maintainers

Primary contributors and maintainers:

- **LI Junxiang**
- **Ziyan Zhou (Anna)**

## What to contribute

Useful contributions include:

- clearer trigger conditions, positive and negative;
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
6. Run the relevant cases from `field-onboarding/references/evals.md` in a fresh session, and paste the result table into the PR. A change to trigger scope or to a core rule needs at least five negatives and five positives.
7. If the change widens what the skill fires on, add a negative case to `field-onboarding/references/examples.md` showing a prompt it should still decline to take over.
8. If the change touches how literature is named, check it against the **Naming literature** rule in `SKILL.md`: verified with a checkable identifier, or explicitly labelled `from memory, unverified`, with no third option.
9. Open a pull request explaining the problem, the change, and the test prompt/result.

`SKILL.md` is a control plane, not a manual. It carries triggers, the ladder, and one-line statements of each rule; the detail lives in `references/` and is loaded when the moment for it arrives. Keep it under roughly 3,000 words. If a change would push it past that, move a section into `references/` and leave a pointer, rather than trimming the rule until it stops working.

Keep the register imperative. Rules written as normative description ("guessing the user's level when a short calibration would materially improve the explanation") are followed less reliably by agents than rules written as instructions ("Skipping Step 0 and guessing at their level"). Prefer the short, direct form.
