#!/usr/bin/env python3
"""Generate the 1080x1440 Xiaohongshu carousel cards.

Usage: python3 tools/make_xhs.py
Writes: docs/xhs/01..04.png   (gitignored; these are for posting, not the repo)
"""

import re
from html import escape
from pathlib import Path

import cairosvg

W, H = 1080, 1440
M = 84                      # side margin
COL = W - M * 2

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

SANS = "Noto Sans CJK SC"
SERIF = "Noto Serif CJK SC"


def t(x, y, s, *, font=SANS, size=34, fill=BODY, weight="normal",
      style="normal", anchor="start"):
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" '
            f'fill="{fill}" font-weight="{weight}" font-style="{style}" '
            f'text-anchor="{anchor}">{escape(s)}</text>')


def mixed(x, y, segs, *, font=SERIF, size=34, base=BODY, mark=RED):
    parts = []
    for s, m in segs:
        parts.append(f'<tspan fill="{mark}">{escape(s)}</tspan>' if m
                     else escape(s))
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" '
            f'fill="{base}" xml:space="preserve">' + "".join(parts) + '</text>')


def bubble(x, y, w, lines, *, size=32):
    h = 34 + 44 * len(lines)
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" '
           f'fill="{QUOTE_BG}"/>']
    for i, ln in enumerate(lines):
        out.append(t(x + 26, y + 58 + i * 44, ln, size=size, fill=MUTED,
                     style="italic"))
    return "".join(out), h


def chip(x, y, label, size=26):
    w = 34 + len(label) * 27
    return ("".join([
        f'<rect x="{x}" y="{y}" width="{w}" height="46" rx="10" '
        f'fill="{CHIP_BG}" stroke="{CHIP_LINE}" stroke-width="2"/>',
        t(x + w / 2, y + 32, label, size=size, fill=MUTED, anchor="middle"),
    ]), w + 16)


def frame(body, accent=None):
    head = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}">',
            f'<rect width="{W}" height="{H}" fill="{PAPER}"/>']
    if accent:
        head.append(f'<rect x="0" y="0" width="{W}" height="10" '
                    f'fill="{accent}"/>')
    return "".join(head) + "".join(body) + "</svg>"


def render(name, svg):
    out = Path(__file__).resolve().parent.parent / "docs" / "xhs"
    out.mkdir(parents=True, exist_ok=True)
    cairosvg.svg2png(bytestring=svg.encode(), write_to=str(out / f"{name}.png"))
    print("wrote", out / f"{name}.png")


# ---------------------------------------------------------------- card 1
def card1():
    b = [t(M, 168, "科研工具 / 开源", size=28, fill=MUTED)]
    b.append(f'<path d="M {M} 196 H {W-M}" stroke="{RULE}" stroke-width="2"/>')
    for i, ln in enumerate(["AI 解释一个", "你不懂的领域时", "总是默认你", "已经懂了一半"]):
        b.append(t(M, 336 + i * 108, ln, font=SERIF, size=82, fill=INK,
                   weight="bold"))
    b.append(f'<rect x="{M}" y="820" width="{COL}" height="248" rx="16" '
             f'fill="{CARD}" stroke="{RULE}" stroke-width="2"/>')
    b.append(f'<path d="M {M+2} 838 v 212" stroke="{RED}" stroke-width="8" '
             f'stroke-linecap="round"/>')
    para = [
        [("拓扑光子学在", 0), ("光子能带", 1), ("中构造", 0), ("贝里曲率", 1), ("，", 0)],
        [("使", 0), ("边缘态", 1), ("继承体态的", 0), ("拓扑不变量", 1), ("。在", 0),
         ("陈绝缘体", 1), ("中，", 0)],
        [("用", 0), ("旋磁响应", 1), ("破坏", 0), ("时间反演对称性", 1), ("……", 0)],
    ]
    for i, ln in enumerate(para):
        b.append(mixed(M + 40, 900 + i * 52, ln, size=32))
    b.append(t(M, 1132, "技术上正确，完全没用。", size=36, fill=RED, weight="bold"))
    b.append(t(M, 1188, "问题不在它懂不懂，在它没问你懂什么。", size=34, fill=BODY))
    b.append(f'<path d="M {M} 1276 H {W-M}" stroke="{RULE}" stroke-width="2"/>')
    b.append(t(M, 1332, "一个开源 skill，让它先问再讲", size=32, fill=MUTED))
    return frame(b, RED)


# ---------------------------------------------------------------- card 2
def card2():
    b = [t(M, 140, "现在的样子", font=SERIF, size=58, fill=INK, weight="bold")]
    b.append(f'<path d="M {M} 176 H {W-M}" stroke="{RED}" stroke-width="4"/>')
    bub, h = bubble(M, 216, COL, ["讲讲拓扑光子学。"])
    b.append(bub)
    y = 216 + h + 56
    para = [
        [("拓扑光子学在", 0), ("光子能带", 1), ("中构造", 0), ("贝里曲率", 1), ("，", 0)],
        [("使", 0), ("边缘态", 1), ("继承体态的", 0), ("拓扑不变量", 1), ("。", 0)],
        [("在", 0), ("陈绝缘体", 1), ("中，用", 0), ("旋磁响应", 1), ("破坏", 0)],
        [("时间反演对称性", 1), ("，在", 0), ("狄拉克点", 1), ("处打开能隙，", 0)],
        [("由此得到的", 0), ("手性边缘模", 1), ("不受", 0), ("背散射", 1), ("影响。", 0)],
    ]
    for i, ln in enumerate(para):
        b.append(mixed(M, y + i * 54, ln, size=34))
    y += len(para) * 54 + 30
    bub, h = bubble(M, y, COL, ["等一下，这里面哪些是我本来就该会的？"])
    b.append(bub)
    y += h + 56
    para2 = [
        [("贝里曲率是", 0), ("贝里联络", 1), ("在", 0), ("布里渊区", 1), ("上的旋度，", 0)],
        [("也就是一条", 0), ("布洛赫能带", 1), ("的", 0), ("几何相位密度", 1), ("。", 0)],
    ]
    for i, ln in enumerate(para2):
        b.append(mixed(M, y + i * 54, ln, size=34))
    y += len(para2) * 54 + 30
    bub, h = bubble(M, y, COL, ["那贝里联络又是什么？"])
    b.append(bub)
    y += h + 56
    para3 = [
        [("它是", 0), ("波函数", 1), ("在", 0), ("参数空间", 1), ("中的", 0),
         ("规范势", 1), ("，", 0)],
        [("依赖", 0), ("规范选择", 1), ("，本身不是可观测量……", 0)],
    ]
    for i, ln in enumerate(para3):
        b.append(mixed(M, y + i * 54, ln, size=34))
    b.append(f'<path d="M {M} 1230 H {W-M}" stroke="{RULE}" stroke-width="2"/>')
    b.append(t(M, 1296, "十二个术语。", size=40, fill=RED, weight="bold"))
    b.append(t(M, 1352, "再问一次，只会得到更多术语。", size=36, fill=RED))
    return frame(b, RED)


# ---------------------------------------------------------------- card 3
def card3():
    b = [t(M, 140, "它应该先做的事", font=SERIF, size=58, fill=INK, weight="bold")]
    b.append(f'<path d="M {M} 176 H {W-M}" stroke="{BLUE}" stroke-width="4"/>')
    bub, h = bubble(M, 216, COL, ["讲讲拓扑光子学。"])
    b.append(bub)
    y = 216 + h + 60
    b.append(t(M, y, "先找出从你已有的知识到这里的最短路径。", size=34, fill=BODY))
    b.append(t(M, y + 48, "请给下面几项各标一个：", size=34, fill=BODY))
    y += 116
    rows = [
        ("布洛赫模式与能带结构", "把光描述成动量空间里的能带"),
        ("贝里相位与贝里曲率", "拓扑不变量就是从这里来的"),
        ("紧束缚与耦合模理论", "描述谐振腔阵列的简洁模型"),
        ("对称性与对称性破缺", "决定哪些拓扑相能不能存在"),
    ]
    for name, gloss in rows:
        b.append(t(M, y, name, size=36, fill=INK, weight="bold"))
        b.append(t(M, y + 44, gloss, size=28, fill=MUTED))
        cx = M
        for c in ["用过", "学过", "没接触"]:
            s, adv = chip(cx, y + 66, c)
            b.append(s)
            cx += adv
        y += 186
    b.append(f'<path d="M {M} 1236 H {W-M}" stroke="{RULE}" stroke-width="2"/>')
    b.append(t(M, 1300, "一轮问完。", size=40, fill=BLUE, weight="bold"))
    b.append(t(M, 1356, "之后每轮讲一级，锚在你标的那几项上。", size=36, fill=BLUE))
    return frame(b, BLUE)


# ---------------------------------------------------------------- card 4
def card4():
    b = [t(M, 140, "三条规则", font=SERIF, size=58, fill=INK, weight="bold")]
    b.append(f'<path d="M {M} 176 H {W-M}" stroke="{RULE}" stroke-width="4"/>')
    items = [
        ("先问再讲", ["由它自己列出这个话题的 3-5 个前置概念，",
                  "你只需要勾选，而不是回答“你什么背景”。"]),
        ("一次只讲一级", ["动机 → 词汇 → 框架 → 方法 → 前沿。",
                    "每级一轮，讲完出一道诊断题再往上走。"]),
        ("不许编文献", ["每篇要么当场查过并给出 DOI，",
                   "要么明确标注“凭记忆，未核实”。"]),
        ("该闭嘴时闭嘴", ["窄问题就直接回答，不摆问卷。",
                    "这条是实测里发现漏掉的，后来补上的。"]),
    ]
    y = 280
    for i, (head, lines) in enumerate(items):
        b.append(t(M, y, head, font=SERIF, size=46, fill=INK, weight="bold"))
        for j, ln in enumerate(lines):
            b.append(t(M, y + 62 + j * 48, ln, size=32, fill=BODY))
        y += 232
    b.append(f'<path d="M {M} 1216 H {W-M}" stroke="{RULE}" stroke-width="2"/>')
    b.append(t(M, 1280, "MIT 开源，ChatGPT / Codex / Claude 都能装", size=32,
               fill=MUTED))
    b.append(t(M, 1340, "GitHub 搜 research-field-onboarding", size=36,
               fill=BLUE, weight="bold"))
    return frame(b)


if __name__ == "__main__":
    for i, fn in enumerate([card1, card2, card3, card4], start=1):
        render(f"{i:02d}", fn())
