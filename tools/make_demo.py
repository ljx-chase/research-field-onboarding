#!/usr/bin/env python3
"""Generate the before/after comparison graphic for the README.

Usage:  python3 tools/make_demo.py
Writes: docs/before-after.svg      (English, embedded in README)
        docs/before-after-zh.svg   (Chinese, for social posts)
"""

from html import escape
from pathlib import Path

W, H = 1240, 764
MARGIN = 44
GAP = 36
PANEL_W = (W - MARGIN * 2 - GAP) // 2
PANEL_X1 = MARGIN
PANEL_X2 = MARGIN + PANEL_W + GAP
PANEL_Y = 112
PANEL_H = 600
PAD = 26

PAPER = "#FCFBF9"
CARD = "#FFFFFF"
INK = "#191C20"
BODY = "#2C3238"
MUTED = "#71767C"
RULE = "#E5E2DC"
CHIP_BG = "#F3F1ED"
CHIP_LINE = "#E2DFD8"
QUOTE_BG = "#F5F3EF"
RED = "#B23A2B"
BLUE = "#1F4E9C"

SERIF = ("Charter,&apos;Bitstream Charter&apos;,&apos;Iowan Old Style&apos;,"
         "Georgia,&apos;Times New Roman&apos;,serif")
SANS = ("-apple-system,BlinkMacSystemFont,&apos;Segoe UI&apos;,Roboto,"
        "Helvetica,Arial,sans-serif")
CJK = ("&apos;PingFang SC&apos;,&apos;Hiragino Sans GB&apos;,"
       "&apos;Microsoft YaHei&apos;,&apos;Noto Sans CJK SC&apos;,"
       "&apos;Source Han Sans SC&apos;," + SANS)


def txt(x, y, s, *, font, size, fill=BODY, weight="normal", style="normal",
        anchor="start", spacing="0"):
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" '
            f'fill="{fill}" font-weight="{weight}" font-style="{style}" '
            f'text-anchor="{anchor}" letter-spacing="{spacing}">'
            f'{escape(s)}</text>')


def mixed(x, y, segments, *, font, size, base=BODY, mark=RED, cjk=False):
    """One line built from (text, is_marked) pairs, flowed inline."""
    parts = []
    for s, marked in segments:
        if marked:
            parts.append(f'<tspan fill="{mark}">{escape(s)}</tspan>')
        else:
            parts.append(escape(s))
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" '
            f'fill="{base}" xml:space="preserve">' + "".join(parts) + '</text>')


def chip(x, y, label, *, font, size=11.5, cjk=False):
    w = 16 + len(label) * (10.5 if cjk else 6.3)
    h = 22
    r = (f'<rect x="{x}" y="{y}" width="{w:.0f}" height="{h}" rx="5" '
         f'fill="{CHIP_BG}" stroke="{CHIP_LINE}"/>')
    t = txt(x + w / 2, y + 15, label, font=font, size=size, fill=MUTED,
            anchor="middle")
    return r + t, w + 8


def quote(x, y, w, lines, *, font, size=14):
    h = 26 + 22 * len(lines)
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" '
           f'fill="{QUOTE_BG}"/>']
    for i, line in enumerate(lines):
        out.append(txt(x + 14, y + 24 + i * 21, line, font=font, size=size,
                       fill=MUTED, style="italic"))
    return "".join(out)


def panel(x, accent, label, prompt, body_svg, note_lines, note_color, font_sans):
    out = [
        f'<rect x="{x}" y="{PANEL_Y}" width="{PANEL_W}" height="{PANEL_H}" '
        f'rx="8" fill="{CARD}" stroke="{RULE}"/>',
        f'<path d="M {x+0.5} {PANEL_Y+8} v {PANEL_H-16}" stroke="{accent}" '
        f'stroke-width="3" stroke-linecap="round"/>',
        txt(x + PAD, PANEL_Y + 36, label, font=font_sans, size=14,
            fill=accent, weight="600"),
        f'<path d="M {x+PAD} {PANEL_Y+52} H {x+PANEL_W-PAD}" stroke="{RULE}"/>',
        f'<rect x="{x+PAD}" y="{PANEL_Y+70}" width="{PANEL_W-PAD*2}" '
        f'height="42" rx="6" fill="{QUOTE_BG}"/>',
        txt(x + PAD + 14, PANEL_Y + 96, prompt, font=font_sans, size=14,
            fill=MUTED, style="italic"),
    ]
    out.extend(body_svg)
    out.append(f'<path d="M {x+PAD} {PANEL_Y+512} H {x+PANEL_W-PAD}" '
               f'stroke="{RULE}"/>')
    ny = PANEL_Y + 534
    for i, line in enumerate(note_lines):
        out.append(txt(x + PAD, ny + i * 22, line, font=font_sans, size=13.5,
                       fill=note_color, weight="600" if i == 0 else "normal"))
    return "".join(out)


def build(lang):
    cjk = lang == "zh"
    fs = CJK if cjk else SANS
    fserif = CJK if cjk else SERIF

    if not cjk:
        title = "Same question. The difference is everything before the explanation."
        sub = "A researcher in nonlinear optics asks about a neighbouring field."
        prompt = "Tell me about topological photonics."
        lab_a = "Any assistant"
        lab_b = "With Field Onboarding"
        para = [
            [("Topological photonics engineers ", 0), ("Berry curvature", 1),
             (" in ", 0), ("photonic bands", 1)],
            [("so that ", 0), ("edge states", 1), (" inherit a ", 0),
             ("bulk invariant", 1), (". In ", 0), ("Chern insulators", 1), (",", 0)],
            [("breaking ", 0), ("time-reversal symmetry", 1), (" with a ", 0),
             ("gyromagnetic response", 1)],
            [("opens a gap at the ", 0), ("Dirac point", 1),
             ("; the resulting ", 0), ("chiral edge modes", 1)],
            [("are immune to ", 0), ("backscattering", 1), (". ", 0),
             ("Valley-Hall", 1), (" and ", 0), ("Floquet", 1), (" analogues", 0)],
            [("avoid magnetic bias entirely.", 0)],
        ]
        followup = "Wait, which of those am I supposed to already know?"
        para2 = [
            [("Berry curvature is the curl of the ", 0),
             ("Berry connection", 1), (",", 0)],
            [("i.e. the ", 0), ("geometric phase density", 1),
             (" of a ", 0), ("Bloch band", 1), (".", 0)],
        ]
        note_a = ["Twelve terms you cannot yet audit.",
                  "Asking again just produces more of them."]
        intro = ["Before we start: the shortest bridge from what you",
                 "already know. Mark each one."]
        rows = [
            ("Bloch modes and band structure",
             "the field describes light as bands over momentum space"),
            ("Berry phase and Berry curvature",
             "these are what become the topological invariants"),
            ("Tight-binding and coupled-mode models",
             "compact descriptions of lattices of resonators"),
            ("Symmetry and symmetry breaking",
             "decides which topological phases can exist at all"),
        ]
        chips = ["used it", "learned it", "new"]
        target = ["And your target: read one paper, follow a talk,",
                  "or build something?"]
        note_b = ["One turn of intake.",
                  "Then one rung per turn, anchored to what you marked."]
    else:
        title = "同一个问题，区别在于解释之前发生了什么。"
        sub = "一个做非线性光学的研究者，问起隔壁领域。"
        prompt = "讲讲拓扑光子学。"
        lab_a = "普通助手"
        lab_b = "装上 Field Onboarding"
        para = [
            [("拓扑光子学在", 0), ("光子能带", 1), ("中构造", 0), ("贝里曲率", 1), ("，", 0)],
            [("使", 0), ("边缘态", 1), ("继承体态的", 0), ("拓扑不变量", 1), ("。在", 0),
             ("陈绝缘体", 1), ("中，", 0)],
            [("用", 0), ("旋磁响应", 1), ("破坏", 0), ("时间反演对称性", 1), ("，", 0)],
            [("在", 0), ("狄拉克点", 1), ("处打开能隙，由此得到的", 0), ("手性边缘模", 1)],
            [("不受", 0), ("背散射", 1), ("影响。", 0), ("能谷霍尔", 1), ("与", 0),
             ("Floquet", 1), ("方案", 0)],
            [("则完全不需要磁偏置。", 0)],
        ]
        followup = "等一下，这里面哪些是我本来就该会的？"
        para2 = [
            [("贝里曲率是", 0), ("贝里联络", 1), ("在", 0), ("布里渊区", 1), ("上的旋度，", 0)],
            [("也就是一条", 0), ("布洛赫能带", 1), ("的", 0), ("几何相位密度", 1), ("。", 0)],
        ]
        note_a = ["十二个你还没法判断该不该懂的术语。", "再问一次，只会得到更多术语。"]
        intro = ["开始之前，先找出从你已有的知识到这里的最短路径。", "请给下面几项各标一个："]
        rows = [
            ("布洛赫模式与能带结构", "这个领域把光描述成动量空间里的能带"),
            ("贝里相位与贝里曲率", "拓扑不变量就是从这里来的"),
            ("紧束缚与耦合模理论", "描述谐振腔阵列的简洁模型"),
            ("对称性与对称性破缺", "决定了哪些拓扑相根本能不能存在"),
        ]
        chips = ["用过", "学过", "没接触"]
        target = ["以及你的目标：读懂一篇论文、听懂一个报告，", "还是要动手做？"]
        note_b = ["一轮问完。", "之后每轮讲一级，全程锚在你标的那几项上。"]

    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}" role="img" aria-label="Before and after '
         f'comparison of a research onboarding skill">',
         f'<rect width="{W}" height="{H}" fill="{PAPER}"/>',
         txt(MARGIN, 56, title, font=fserif, size=27, fill=INK),
         txt(MARGIN, 84, sub, font=fs, size=15, fill=MUTED)]

    # left panel body
    lb = []
    y = PANEL_Y + 152
    for i, line in enumerate(para):
        lb.append(mixed(PANEL_X1 + PAD, y + i * 27, line,
                        font=fserif, size=15.5, base=BODY, mark=RED))
    lb.append(quote(PANEL_X1 + PAD, PANEL_Y + 336, PANEL_W - PAD * 2,
                    [followup], font=fs))
    for i, line in enumerate(para2):
        lb.append(mixed(PANEL_X1 + PAD, PANEL_Y + 424 + i * 27, line,
                        font=fserif, size=15.5, base=BODY, mark=RED))
    s.append(panel(PANEL_X1, RED, lab_a, prompt, lb, note_a, RED, fs))

    # right panel body
    rb = []
    y = PANEL_Y + 148
    for i, line in enumerate(intro):
        rb.append(txt(PANEL_X2 + PAD, y + i * 22, line, font=fs, size=14.5,
                      fill=BODY))
    ry = PANEL_Y + 198
    for name, gloss in rows:
        rb.append(txt(PANEL_X2 + PAD, ry, name, font=fs, size=14.5,
                      fill=INK, weight="600"))
        rb.append(txt(PANEL_X2 + PAD, ry + 19, gloss, font=fs, size=12.8,
                      fill=MUTED))
        cx = PANEL_X2 + PAD
        for c in chips:
            svg, adv = chip(cx, ry + 30, c, font=fs, cjk=cjk)
            rb.append(svg)
            cx += adv
        ry += 68
    for i, line in enumerate(target):
        rb.append(txt(PANEL_X2 + PAD, PANEL_Y + 478 + i * 21, line,
                      font=fs, size=13.5, fill=MUTED))
    s.append(panel(PANEL_X2, BLUE, lab_b, prompt, rb, note_b, BLUE, fs))

    s.append('</svg>')
    return "".join(s)


if __name__ == "__main__":
    out = Path(__file__).resolve().parent.parent / "docs"
    out.mkdir(exist_ok=True)
    (out / "before-after.svg").write_text(build("en"), encoding="utf-8")
    (out / "before-after-zh.svg").write_text(build("zh"), encoding="utf-8")
    print("wrote", out / "before-after.svg")
    print("wrote", out / "before-after-zh.svg")
