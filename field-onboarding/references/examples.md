# Examples

Use these examples as behavioral targets, not scripts to copy verbatim. Preserve the workflow while adapting terminology, depth, and language to the user's field.

## Example 1 — Field-level onboarding from an adjacent specialty

**User**

> I work on nonlinear optics but know almost nothing about topological photonics. Can you guide me into the field step by step?

**Good first response**

Start with Step 0 rather than immediately teaching topology. Name a small set of load-bearing prerequisites and exploit the user's optics background as an anchor.

> Before we start, I want to locate the shortest bridge from nonlinear optics to topological photonics. Please mark each item as **used it / learned it / new**:
>
> | Prerequisite | Why it matters |
> | --- | --- |
> | Bloch modes and band structures | Topological photonics usually describes photonic modes as bands over momentum space. |
> | Berry phase / Berry curvature | These encode geometric properties of bands and lead to topological invariants. |
> | Coupled-mode or tight-binding models | They provide compact models for lattices of coupled resonators or waveguides. |
> | Symmetry and symmetry breaking | Time-reversal, inversion, and crystalline symmetries constrain possible topological phases. |
>
> Also tell me your target: **read papers**, **understand experiments**, **design a system**, or **enter the field broadly**.
>
> I will use your nonlinear-optics intuition wherever it genuinely transfers, but I will flag where the analogy stops working.

**Why this is good**

- It calibrates specific prerequisites instead of asking a vague background question.
- It does not reteach optics the user already knows.
- It establishes the user's target before choosing depth.
- It does not dump the five-rung ladder in the first turn.

## Example 2 — Decode a dense abstract

**User**

> I cannot understand this abstract about moire excitons. Please explain it to me.

**Good response pattern**

Do not force the full Step 0 intake. Enter Decode mode.

> **Gist:** The authors are studying excitons whose motion and optical properties are modified by a long-period moire potential created when two atomically thin crystals are stacked with a small twist or lattice mismatch.
>
> **Terms in order**
> - **Exciton:** a bound electron-hole pair that behaves as a composite quasiparticle.
> - **Moiré superlattice:** a long-wavelength periodic pattern produced by two slightly mismatched lattices.
> - **Localization:** confinement of an exciton's center-of-mass motion to particular regions of that moire potential.
>
> **Reconstructed passage:** [Rewrite the supplied abstract faithfully in simpler language, preserving its claims.]
>
> **What you need to evaluate the claim:** (1) how excitons form in the relevant material system and (2) how a moire potential modifies their energy landscape.
>
> **Source fidelity:** I will label statements that are background or my inference separately from claims explicitly made in the abstract.

When the actual abstract is available, preserve its terminology and scientific scope. Do not insert mechanisms, causality, or conclusions that the authors did not state.

## Example 3 — Chinese request about chiral phonons

**User**

> 我是做实验光学的，想入门 chiral phonons。最好一步一步讲，我主要想知道怎么做实验验证。

**Good first response**

Reply in Chinese and calibrate only prerequisites that matter for an experimental target.

> 可以。你的目标是**实验验证 chiral phonons**，所以我会把路线偏向“物理图像 → 可观测量 → 实验方案”，而不是先从完整的群论形式体系开始。
>
> 先请把下面几项标成 **用过 / 学过 / 基本没接触**：
>
> | 前置概念 | 为什么重要 |
> | --- | --- |
> | 晶格振动与声子本征矢 | chiral phonon 的“旋转”首先体现在原子位移的相位关系上。 |
> | Brillouin zone 与 K/K' valley | 很多二维材料中的声子手性与非等价谷有关。 |
> | 圆偏振光与角动量 | 实验选择定则通常需要讨论光与声子的角动量交换。 |
> | Raman / IR selection rules | 决定哪些声子模式能通过具体光谱手段被看到。 |
>
> 你的实验目标我先按“**判断一个材料是否存在可测的 chiral phonon signature，并设计光学验证方案**”理解。如果你实际更偏向 time-resolved pump-probe 或 Raman，可以告诉我，我会调整路线。

**Why this is good**

- It follows the user's language.
- It uses experimental optics as an anchor.
- It adapts the ladder to the stated hands-on target by preparing to expand Rung 4.
- It does not assume that valley physics automatically proves phonon chirality.

## Example 4 — Checkpoint and branching

After teaching a rung about Berry curvature, do not end with only "Does that make sense?"

**Better checkpoint**

> Quick check: suppose the Berry curvature is strongly concentrated near K and has the opposite sign near K'. If both valleys are equally populated, what would you expect for a valley-summed Hall-like response?
>
> A. The two valley contributions tend to cancel.  
> B. They necessarily add.  
> C. Berry curvature becomes zero at each valley.

**Branching behavior**

- If the user chooses **A** and explains the cancellation correctly, advance.
- If the user chooses **C**, explain the difference between *local nonzero Berry curvature* and *cancellation after summing contributions* using a momentum-space picture.
- If the user says this is trivial, skip ahead rather than adding more elementary questions.

## Example 5 — Respect an explicit request for a compact overview

**User**

> I know the basics already. Give me the whole roadmap in one response so I can decide what to study.

**Good behavior**

Honor the request instead of enforcing one rung per turn. Give a compact five-rung roadmap, identify likely prerequisites, and let the user choose where to zoom in. Keep the overview diagnostic rather than turning every rung into a full lecture.

## Example 6 — Distinguish source claim from inference

**User**

> The paper says the mode has circular atomic motion at K. Does that prove it is a chiral phonon and that circularly polarized Raman must detect it?

**Good response pattern**

> **Source claim:** The paper reports circular atomic motion for the mode at K.
>
> **Background:** Circular or elliptical atomic motion can be associated with phonon angular momentum, but terminology and definitions of phonon chirality depend on the symmetry and mode context.
>
> **Inference:** The reported eigenvector may support a chiral-phonon interpretation, but that conclusion requires checking the mode symmetry, degeneracy, valley relation, and the definition used by the authors.
>
> **Not established by that statement alone:** It does not automatically imply that conventional circularly polarized Raman can detect the mode. Raman visibility depends on momentum conservation, Raman tensors or higher-order processes, resonance conditions, and the experimental geometry.

The exact technical content must be adjusted to the supplied source and verified when freshness or source-specific claims matter.
