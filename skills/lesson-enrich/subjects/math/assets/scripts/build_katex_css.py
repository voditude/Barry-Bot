"""
Fetches KaTeX's CSS and a chosen subset of its webfonts from cdnjs, then rewrites the CSS
so each @font-face's src is a base64 data: URI instead of a relative fonts/*.woff2 path.

Why: the Artifact CSP only allows external <script> tags from cdnjs (not stylesheets or
font fetches), so KaTeX's own katex.min.css cannot be <link>'d or fetched at runtime. This
script produces a self-contained CSS block that can be spliced straight into a <style> tag.

Usage:
    python build_katex_css.py [--version 0.18.4] [--out katex.inline.css]

Re-run this when: bumping the KaTeX version, or when a lesson needs a font not in KEEP
(rare now — KEEP already covers \\mathcal/\\mathfrak/\\mathscr; e.g. a lesson using very large
delimiters would need "KaTeX_Size3-Regular"/"KaTeX_Size4-Regular" added).
"""

import argparse
import base64
import os
import re
import urllib.request

# Default font subset: covers standard algebra / set theory / probability notation, plus the
# alphabet fonts (Caligraphic, Fraktur, Script) that discrete-math and probability content
# reach for constantly (\mathcal for sigma-algebras and power sets, \mathfrak for algebras,
# \mathscr for sigma-fields) -- omitting these silently drops to the browser's default font
# for any symbol using them instead of erroring, so they belong in the default rather than
# behind a "re-run if needed" step someone has to remember.
# Add entries here (matching the *-Style.woff2 filenames KaTeX ships) for other notation.
KEEP = {
    "KaTeX_Main-Regular",
    "KaTeX_Main-Bold",
    "KaTeX_Main-Italic",
    "KaTeX_Math-Italic",
    "KaTeX_AMS-Regular",
    "KaTeX_Size1-Regular",
    "KaTeX_Size2-Regular",
    "KaTeX_Caligraphic-Regular",
    "KaTeX_Fraktur-Regular",
    "KaTeX_Script-Regular",
    "KaTeX_SansSerif-Regular",
    "KaTeX_Typewriter-Regular",
}

FONT_FACE_RE = re.compile(r"@font-face\{[^}]*\}")


def fetch(url: str) -> bytes:
    with urllib.request.urlopen(url) as resp:
        return resp.read()


def build(version: str, keep: set, out_path: str) -> None:
    base_url = f"https://cdnjs.cloudflare.com/ajax/libs/KaTeX/{version}"
    css = fetch(f"{base_url}/katex.min.css").decode("utf-8")

    font_cache = {}

    def process_block(m: re.Match) -> str:
        block = m.group(0)
        name_match = re.search(r"fonts/([A-Za-z0-9_-]+)\.woff2", block)
        if not name_match:
            return ""
        name = name_match.group(1)
        if name not in keep:
            return ""
        if name not in font_cache:
            font_cache[name] = fetch(f"{base_url}/fonts/{name}.woff2")
        b64 = base64.b64encode(font_cache[name]).decode("ascii")
        data_uri = f"data:font/woff2;base64,{b64}"
        new_src = f"src:url({data_uri}) format('woff2')"
        return re.sub(r"src:[^}]+(?=\})", new_src, block, count=1)

    new_css = FONT_FACE_RE.sub(process_block, css)

    missing = keep - set(font_cache)
    if missing:
        raise SystemExit(f"Font names in KEEP not found in katex.min.css: {missing}")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(new_css)

    print(f"KaTeX {version}: wrote {out_path} ({len(new_css)} chars, {len(font_cache)} fonts embedded)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", default="0.18.4")
    parser.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "katex", "katex.inline.css"))
    parser.add_argument("--add-font", action="append", default=[], help="Extra font family filename (without .woff2) to include")
    args = parser.parse_args()

    keep = set(KEEP) | set(args.add_font)
    build(args.version, keep, args.out)
