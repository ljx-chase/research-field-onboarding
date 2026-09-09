#!/usr/bin/env python3
"""Generate the project logo.

Usage: python3 tools/make_logo.py
Writes: logo.png              banner, English, for the README header
        docs/logo-zh.png      banner, Chinese
        docs/logo-icon.png    square mark, for avatars and social previews
        docs/logo.svg         vector source of the English banner

The mark is a doorway, taking the Chinese name 入门 literally. The open leaf
is solid because it is the field the reader already has; the opening is pale
because the new field has been entered but not filled in.
"""

from html import escape
import math
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


TINT = "#E7EDF6"


def stairs(cx, cy, scale=1.0, compact=False):
    """Side view. A wall seen edge on, its door swung open toward the viewer,
    steps rising away behind it, and the new field at the top.

    The leaf is solid because it is the field the reader already has.
    Everything past the threshold is outline only: entered, not filled in."""
    e = []
    G = 160.0
    tw, lw = 7.5, 9.0
    jamb_w, jamb_top = 15.0, 6.0
    ld, flare = 60.0, 0.0

    sw, sh, n = 52.0, 34.0, 3
    ext = 82.0
    sx = jamb_w
    top_x = sx + n * sw + ext
    top_y = G - n * sh
    ar = 42.0

    if compact:
        xmin, xmax = -ld - 20, jamb_w + 52
        ymin, ymax = jamb_top - 8, G + 8
    else:
        xmin, xmax = -ld - 20, top_x + 20
        ymin, ymax = top_y - 2 * ar * 0.72 - 22, G + 8

    # steps rising away behind the wall, and the ground they end on
    if not compact:
        d = [f'M {sx} {G}']
        for i in range(n):
            d.append(f'V {G - (i + 1) * sh:.1f}')
            d.append(f'H {sx + (i + 1) * sw + (ext if i == n - 1 else 0):.1f}')
        e.append(f'<path d="{" ".join(d)}" fill="none" stroke="{BLUE_SOFT}" '
                 f'stroke-width="{tw}" stroke-linecap="round" '
                 f'stroke-linejoin="round"/>')

        # the new field, waiting at the top: an atom, drawn open
        acx = top_x - ext / 2
        tilt = math.radians(32)
        half_v = math.hypot(ar * math.sin(tilt), ar * 0.42 * math.cos(tilt))
        acy = top_y - half_v - 10
        for ang in (-32, 32):
            e.append(f'<ellipse cx="{acx:.1f}" cy="{acy:.1f}" rx="{ar:.1f}" '
                     f'ry="{ar * 0.42:.1f}" fill="none" stroke="{BLUE_SOFT}" '
                     f'stroke-width="{tw}" transform="rotate({ang} {acx:.1f} '
                     f'{acy:.1f})"/>')
        e.append(f'<circle cx="{acx:.1f}" cy="{acy:.1f}" r="{ar * 0.27:.1f}" '
                 f'fill="{BLUE}"/>')

    # the door, swung open toward the viewer
    e.append(f'<path d="M {jamb_w:.1f} {jamb_top:.1f} L {-ld:.1f} '
             f'{jamb_top - flare:.1f} V {G} H {jamb_w:.1f} Z" fill="{BLUE}" '
             f'stroke="{INK}" stroke-width="3.5" stroke-linejoin="round"/>')
    e.append(f'<circle cx="{-ld + 17:.1f}" cy="{(jamb_top + G) / 2:.1f}" '
             f'r="7.5" fill="{PAPER}"/>')

    # the wall itself, seen edge on, drawn over the hinge side of the leaf
    e.append(f'<rect x="0" y="{jamb_top - 10:.1f}" width="{jamb_w}" '
             f'height="{G - jamb_top + 10:.1f}" rx="{jamb_w / 2:.1f}" '
             f'fill="{INK}"/>')

    # the ground, running the full width of the climb
    ground_r = (xmax - 10) if compact else (sx + sw * 1.5)
    e.append(f'<path d="M {xmin + 10:.1f} {G} H {ground_r:.1f}" '
             f'stroke="{INK}" stroke-width="{lw}" stroke-linecap="round"/>')

    mx, my = (xmin + xmax) / 2, (ymin + ymax) / 2
    return (f'<g transform="translate({cx - scale*mx:.1f},{cy - scale*my:.1f}) '
            f'scale({scale})">' + "".join(e) + '</g>')


def banner(lang="en"):
    W, H = 1600, 470
    if lang == "en":
        w1, w2 = "Field", "Onboarding"
        tag = "Find the door into a field you do not know yet. Then step through it."
        size, tsize = 104, 32
    else:
        w1, w2 = "领域", "入门"
        tag = "先问你已经会什么，再带你进门，一次一级。"
        size, tsize = 132, 36

    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}">',
         f'<rect width="{W}" height="{H}" fill="{PAPER}"/>',
         stairs(246, 224, 0.95)]

    tx = 470
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
         stairs(256, 256, 1.95, compact=True),
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
