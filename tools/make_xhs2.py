#!/usr/bin/env python3
"""Cards for the second Xiaohongshu post: promo first, then how to install.

Usage: python3 tools/make_xhs2.py
Writes: docs/xhs2/01..05.png   (gitignored; for posting, not the repo)
"""

from html import escape
from pathlib import Path

import cairosvg

W, H = 1080, 1440
M = 84
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
BLUE_SOFT = "#8FA9CE"
TINT = "#E7EDF6"

SANS = "Noto Sans CJK SC"
SERIF = "Noto Serif CJK SC"


def t(x, y, s, *, font=SANS, size=34, fill=BODY, weight="normal",
      style="normal", anchor="start"):
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" '
            f'fill="{fill}" font-weight="{weight}" font-style="{style}" '
            f'text-anchor="{anchor}">{escape(s)}</text>')


def mixed(x, y, segs, *, font=SERIF, size=34, base=BODY, mark=RED):
    parts = [f'<tspan fill="{mark}">{escape(s)}</tspan>' if m else escape(s)
             for s, m in segs]
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
    w = 34 + cjk_w(label, 15, 27)
    return ("".join([
        f'<rect x="{x}" y="{y}" width="{w}" height="46" rx="10" '
        f'fill="{CHIP_BG}" stroke="{CHIP_LINE}" stroke-width="2"/>',
        t(x + w / 2, y + 32, label, size=size, fill=MUTED, anchor="middle"),
    ]), w + 16)


def cjk_w(label, latin, cjk):
    return sum(latin if ord(c) < 128 else cjk for c in label)


def path_chip(x, y, label, size=27):
    w = 34 + cjk_w(label, 16, 29)
    return ("".join([
        f'<rect x="{x}" y="{y}" width="{w:.0f}" height="48" rx="10" '
        f'fill="{TINT}"/>',
        t(x + w / 2, y + 33, label, size=size, fill=BLUE, anchor="middle"),
    ]), w)


def steps_block(y, items, accent=BLUE, gap=34):
    """Numbered steps: big number, bold title, one detail line, path chips."""
    out = []
    for i, (title, detail, chips) in enumerate(items, start=1):
        out.append(f'<circle cx="{M + 27}" cy="{y - 11}" r="27" '
                   f'fill="{accent}"/>')
        out.append(t(M + 27, y, str(i), size=32, fill=PAPER, weight="bold",
                     anchor="middle"))
        out.append(t(M + 74, y, title, size=37, fill=INK, weight="bold"))
        yy = y + 46
        if detail:
            out.append(t(M + 74, yy, detail, size=28, fill=MUTED))
            yy += 46
        if chips:
            cx = M + 74
            for j, c in enumerate(chips):
                if j:
                    out.append(t(cx + 6, yy + 33, "›", size=30, fill=MUTED))
                    cx += 30
                s, w = path_chip(cx, yy, c)
                out.append(s)
                cx += w + 10
            yy += 74
        y = yy + gap
    return "".join(out), y


def frame(body, accent=None):
    head = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" '
            f'height="{H}" viewBox="0 0 {W} {H}">',
            f'<rect width="{W}" height="{H}" fill="{PAPER}"/>']
    if accent:
        head.append(f'<rect width="{W}" height="10" fill="{accent}"/>')
    return "".join(head) + "".join(body) + "</svg>"


def render(name, svg):
    out = Path(__file__).resolve().parent.parent / "docs" / "xhs2"
    out.mkdir(parents=True, exist_ok=True)
    cairosvg.svg2png(bytestring=svg.encode(), write_to=str(out / f"{name}.png"))
    print("wrote", out / f"{name}.png")


# ------------------------------------------------------------------ 01 cover
def card1():
    b = [t(M, 168, "科研工具 / 开源 / 附安装教程", size=28, fill=MUTED),
         f'<path d="M {M} 196 H {W-M}" stroke="{RULE}" stroke-width="2"/>']
    for i, ln in enumerate(["AI 讲一个", "你不懂的领域", "总是默认你", "已经懂了一半"]):
        b.append(t(M, 330 + i * 106, ln, font=SERIF, size=80, fill=INK,
                   weight="bold"))
    b.append(f'<rect x="{M}" y="800" width="{COL}" height="238" rx="16" '
             f'fill="{CARD}" stroke="{RULE}" stroke-width="2"/>')
    b.append(f'<path d="M {M+2} 818 v 202" stroke="{RED}" stroke-width="8" '
             f'stroke-linecap="round"/>')
    para = [
        [("Transformer 用", 0), ("自注意力", 1), ("替代了", 0), ("循环结构", 1), ("，", 0)],
        [("通过", 0), ("查询-键-值投影", 1), ("计算", 0), ("token", 1), ("间的", 0),
         ("注意力权重", 1), ("，", 0)],
        [("再经", 0), ("多头", 1), ("拼接与", 0), ("残差连接", 1), ("……", 0)],
    ]
    for i, ln in enumerate(para):
        b.append(mixed(M + 40, 878 + i * 52, ln, size=32))
    b.append(t(M, 1114, "技术上正确，完全没用。", size=36, fill=RED, weight="bold"))
    b.append(t(M, 1170, "问题不在它懂不懂，在它没问你懂什么。", size=34, fill=BODY))
    b.append(f'<path d="M {M} 1252 H {W-M}" stroke="{RULE}" stroke-width="2"/>')
    b.append(t(M, 1310, "上次很多人问怎么装", size=32, fill=MUTED))
    b.append(t(M, 1360, "这次把安装步骤放进来了 →", size=34, fill=BLUE,
               weight="bold"))
    return frame(b, RED)


# ------------------------------------------------------------------ 02 what
def card2():
    b = [t(M, 140, "它先做的事", font=SERIF, size=58, fill=INK, weight="bold"),
         f'<path d="M {M} 176 H {W-M}" stroke="{BLUE}" stroke-width="4"/>']
    bub, h = bubble(M, 216, COL, ["讲讲 Transformer 的注意力机制。"])
    b.append(bub)
    y = 216 + h + 60
    b.append(t(M, y, "先找出从你已有的知识到这里的最短路径。", size=34))
    b.append(t(M, y + 48, "请给下面几项各标一个：", size=34))
    y += 116
    rows = [
        ("矩阵乘法与向量点积", "注意力算到底就是一串矩阵运算"),
        ("神经网络的前向传播", "知道一层怎么把输入变成输出"),
        ("softmax 与概率归一化", "注意力权重就是这么算出来的"),
        ("词嵌入与序列表示", "文字怎么变成向量进到模型里"),
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
    b.append(t(M, 1300, "标了用过的，它不再重讲，直接拿来打比方。",
               size=34, fill=BLUE, weight="bold"))
    b.append(t(M, 1352, "标了没接触的，先补上再往下走。", size=34, fill=BLUE))
    return frame(b, BLUE)


# ------------------------------------------------------------------ 03 claude
def card3():
    b = [t(M, 140, "装到 Claude 网页版", font=SERIF, size=56, fill=INK,
           weight="bold"),
         f'<path d="M {M} 176 H {W-M}" stroke="{BLUE}" stroke-width="4"/>',
         t(M, 244, "需要 Pro 及以上账号，先确认代码执行已打开", size=30,
           fill=MUTED)]
    items = [
        ("下载 zip", "GitHub 仓库 Releases 里那个 field-onboarding.zip", []),
        ("打开设置", "确认这一项是开着的，技能依赖它", ["Settings", "Capabilities", "代码执行"]),
        ("上传技能", "选刚下载的 zip，确认名称后启用", ["Customize", "Skills", "Upload"]),
        ("直接提问", "不用打开关，说到陌生领域它自己会触发", []),
    ]
    blk, _ = steps_block(340, items, gap=100)
    b.append(blk)
    b.append(f'<path d="M {M} 1250 H {W-M}" stroke="{RULE}" stroke-width="2"/>')
    b.append(t(M, 1312, "zip 里必须是一个文件夹包着 SKILL.md，", size=32,
               fill=MUTED))
    b.append(t(M, 1360, "不是整个仓库压一起，这是最常见的失败原因。", size=32,
               fill=MUTED))
    return frame(b, BLUE)


# ------------------------------------------------------------------ 04 gpt
def card4():
    b = [t(M, 140, "装到 ChatGPT", font=SERIF, size=56, fill=INK,
           weight="bold"),
         f'<path d="M {M} 176 H {W-M}" stroke="{BLUE}" stroke-width="4"/>',
         t(M, 244, "同一个 zip，换个入口", size=30, fill=MUTED)]
    items = [
        ("侧栏进插件", "左侧边栏里找到它", ["Plugins", "Plugin Directory"]),
        ("切到技能页", "在目录顶部切换标签", ["Skills"]),
        ("上传", "选 Create，再选从电脑上传，然后挑那个 zip",
         ["Create", "Upload"]),
    ]
    blk, y = steps_block(340, items, gap=92)
    b.append(blk)
    bx, by, bh = M, y + 16, 262
    b.append(f'<rect x="{bx}" y="{by}" width="{COL}" height="{bh}" rx="16" '
             f'fill="{CARD}" stroke="{RULE}" stroke-width="2"/>')
    b.append(f'<path d="M {bx+2} {by + 20} v {bh - 40}" stroke="{BLUE}" '
             f'stroke-width="8" stroke-linecap="round"/>')
    b.append(t(bx + 40, by + 68, "用 Claude Code 或者 Codex 的话", size=32,
               fill=BODY))
    b.append(t(bx + 40, by + 120, "一行命令就行，不用下载：", size=32, fill=BODY))
    b.append(t(bx + 40, by + 186, "npx skills add ljx-chase/", size=31,
               fill=BLUE, weight="bold"))
    b.append(t(bx + 40, by + 230, "research-field-onboarding -g", size=31,
               fill=BLUE, weight="bold"))
    return frame(b, BLUE)


# ------------------------------------------------------------------ 05 use
def card5():
    b = [t(M, 140, "装完怎么说", font=SERIF, size=58, fill=INK, weight="bold"),
         f'<path d="M {M} 176 H {W-M}" stroke="{BLUE}" stroke-width="4"/>',
         t(M, 244, "不用记咒语，说清楚三件事就行", size=30, fill=MUTED)]
    y = 330
    rows = [
        ("说出领域", ["一步一步带我入门<领域>"]),
        ("说出你的桥", ["我懂<你已有的>，但不懂<领域>", "这句最有效，等于先把锚点递过去"]),
        ("说出用途", ["我要搭一套<装置>，告诉我需要哪些知识",
                  "目标不同，它讲的深浅和顺序都不一样"]),
        ("或者直接贴", ["这段摘要看不懂，它在说什么"]),
    ]
    for name, lines in rows:
        b.append(t(M, y, name, size=38, fill=INK, weight="bold"))
        yy = y + 54
        for j, ln in enumerate(lines):
            if j == 0:
                b.append(f'<rect x="{M}" y="{yy - 38}" width="{COL}" '
                         f'height="62" rx="12" fill="{QUOTE_BG}"/>')
                b.append(t(M + 24, yy, ln, size=31, fill=BODY))
                yy += 62
            else:
                b.append(t(M, yy + 6, ln, size=27, fill=MUTED))
                yy += 44
        y = yy + 46
    b.append(f'<path d="M {M} 1218 H {W-M}" stroke="{RULE}" stroke-width="2"/>')
    b.append(t(M, 1284, "问窄问题它不会啰嗦。", size=34, fill=BLUE,
               weight="bold"))
    b.append(t(M, 1336, "「这个缩写什么意思」就直接回答，不摆问卷。",
               size=32, fill=BLUE))
    return frame(b, BLUE)


if __name__ == "__main__":
    for i, fn in enumerate([card1, card2, card3, card4, card5], start=1):
        render(f"{i:02d}", fn())
