#!/usr/bin/env python3
"""Generate the project logo.

Usage: python3 tools/make_logo.py
Writes: logo.png              banner, English, for the README header
        docs/logo-zh.png      banner, Chinese
        docs/logo-icon.png    square mark, for avatars and social previews
        docs/logo.svg         vector source of the English banner

The mark is a five-rung ladder in three states: the bottom two rungs solid
(used it), the middle one half (learned it), the top two outlined (new). It
carries both halves of the skill at once, the five teaching rungs and the
three-state calibration.
"""

from html import escape
from pathlib import Path

import cairosvg

PAPER = "#FCFBF9"
INK = "#191C20"
BODY = "#2C3238"
MUTED = "#71767C"
RULE = "#DCD8D1"
BLUE = "#1F4E9C"
BLUE_SOFT = "#8FA9CE"
RED = "#B23A2B"

SERIF = "Noto Serif CJK SC"
SANS = "Noto Sans CJK SC"


def txt(x, y, s, *, font, size, fill=BODY, weight="normal", anchor="start",
        spacing="0"):
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" '
            f'fill="{fill}" font-weight="{weight}" text-anchor="{anchor}" '
            f'letter-spacing="{spacing}">{escape(s)}</text>')


def ladder(cx, cy, scale=1.0):
    """Five-rung ladder, filled bottom-up: 2 solid, 1 half, 2 outlined."""
    w, h = 126 * scale, 26 * scale          # rung size
    gap = 19 * scale
    rail_w = 7 * scale
    n = 5
    total_h = n * h + (n - 1) * gap
    x = cx - w / 2
    y0 = cy - total_h / 2
    out = []

    # rails
    for rx in (x - rail_w - 6 * scale, x + w + 6 * scale):
        out.append(f'<rect x="{rx:.1f}" y="{y0 - 8 * scale:.1f}" '
                   f'width="{rail_w:.1f}" height="{total_h + 16 * scale:.1f}" '
                   f'rx="{rail_w / 2:.1f}" fill="{INK}"/>')

    # rungs, top row first
    states = ["open", "open", "half", "solid", "solid"]
    for i, state in enumerate(states):
        y = y0 + i * (h + gap)
        r = 5 * scale
        if state == "solid":
            out.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" '
                       f'height="{h:.1f}" rx="{r:.1f}" fill="{BLUE}"/>')
        elif state == "half":
            out.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" '
                       f'height="{h:.1f}" rx="{r:.1f}" fill="{PAPER}" '
                       f'stroke="{BLUE}" stroke-width="{3 * scale:.1f}"/>')
            out.append(f'<path d="M {x + r:.1f} {y:.1f} '
                       f'H {x + w / 2:.1f} V {y + h:.1f} '
                       f'H {x + r:.1f} A {r:.1f} {r:.1f} 0 0 1 {x:.1f} '
                       f'{y + h - r:.1f} V {y + r:.1f} '
                       f'A {r:.1f} {r:.1f} 0 0 1 {x + r:.1f} {y:.1f} Z" '
                       f'fill="{BLUE}"/>')
        else:
            out.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" '
                       f'height="{h:.1f}" rx="{r:.1f}" fill="none" '
                       f'stroke="{BLUE_SOFT}" stroke-width="{3.5 * scale:.1f}"/>')
    return "".join(out)


def banner(lang="en"):
    W, H = 1600, 470
    if lang == "en":
        w1, w2 = "Field", "Onboarding"
        tag = "Locate the reader first. Then teach upward, one rung at a time."
        size, tsize = 128, 34
    else:
        w1, w2 = "领域", "入门"
        tag = "先问你已经会什么，再往上讲，一次一级。"
        size, tsize = 132, 36

    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}">',
         f'<rect width="{W}" height="{H}" fill="{PAPER}"/>',
         ladder(210, 238, 1.18)]

    tx = 380
    base = 258
    s.append(txt(tx, base, w1, font=SERIF, size=size, fill=INK, weight="bold"))
    off = len(w1) * (size * 0.60 if lang == "en" else size * 1.02) + size * 0.22
    s.append(txt(tx + off, base, w2, font=SERIF, size=size, fill=BLUE,
                 weight="bold"))

    s.append(f'<path d="M {tx} {base + 68} H {W - 120}" stroke="{RULE}" '
             f'stroke-width="3"/>')
    s.append(txt(tx + 4, base + 126, tag, font=SANS, size=tsize, fill=MUTED))
    s.append('</svg>')
    return "".join(s)


def icon():
    W = 512
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{W}" '
         f'viewBox="0 0 {W} {W}">',
         f'<rect width="{W}" height="{W}" rx="96" fill="{PAPER}"/>',
         f'<rect x="6" y="6" width="{W-12}" height="{W-12}" rx="90" '
         f'fill="none" stroke="{RULE}" stroke-width="4"/>',
         ladder(256, 256, 1.46),
         '</svg>']
    return "".join(s)


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    docs = root / "docs"
    docs.mkdir(exist_ok=True)

    (docs / "logo.svg").write_text(banner("en"), encoding="utf-8")

    cairosvg.svg2png(bytestring=banner("en").encode(),
                     write_to=str(root / "logo.png"), scale=1.5)
    cairosvg.svg2png(bytestring=banner("zh").encode(),
                     write_to=str(docs / "logo-zh.png"), scale=1.5)
    cairosvg.svg2png(bytestring=icon().encode(),
                     write_to=str(docs / "logo-icon.png"), scale=1.0)
    for p in (root / "logo.png", docs / "logo-zh.png", docs / "logo-icon.png",
              docs / "logo.svg"):
        print("wrote", p, p.stat().st_size, "bytes")
