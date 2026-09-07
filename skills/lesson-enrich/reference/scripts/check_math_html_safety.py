"""
Verifies a finished lesson-enrich artifact won't silently mis-render its math. Run this on
every generated HTML artifact before publishing it — see SKILL.md step 7. Exits non-zero if
any check fails, so it can gate a publish step directly.

Why this exists: two real bugs shipped across 8 published artifacts (discrete maths weeks
1-4 + assignment 1, stochastic modelling weeks 1-3) before this check did, both silent —
KaTeX gave no console error, the page just rendered wrong:

1. Raw `<`/`>` inside a `$...$`/`$$...$$` formula (e.g. `a<b`, `P(X>t)`). The formula text
   sits directly in page HTML, not inside a `<script>`/`<style>` block, so the browser's
   HTML parser reads it before KaTeX ever runs. A literal `<` followed by a letter opens
   what the parser treats as a real, unclosed tag, silently swallowing every character up
   to the next stray `>` it finds — often several formulas and paragraphs later. This is
   the more severe bug: it corrupts visible document structure, not just one formula, and
   was worst wherever strict-inequality notation is idiomatic (poset relations in discrete
   maths, tail-probability/hitting-time bounds in stochastic modelling — 29-32 formulas hit
   per file in the worst cases).
2. A math-alphabet command (`\\mathcal`, `\\mathfrak`, `\\mathscr`, ...) used in the content
   without its KaTeX webfont embedded in the page's inlined `<style>` block. KaTeX still
   parses and renders these fine — it just falls back to the browser's default font for
   that character, which looks like a formatting glitch, not a broken formula, and is easy
   to read past on a screenshot.

Both were missed on the first two passes of manually fixing this exact problem before this
script existed, because both checks require simulating something neither a LaTeX-syntax
check nor a plain grep does on its own: #1 requires knowing how an HTML parser (not a LaTeX
parser) treats the character, and #2 requires cross-referencing every math-alphabet command
used against which fonts are actually embedded, not just whether the formula parses.

Usage:
    python check_math_html_safety.py path/to/artifact.html [more.html ...]
"""

import re
import sys

MATH_FONT_COMMANDS = {
    "mathcal": "KaTeX_Caligraphic",
    "mathfrak": "KaTeX_Fraktur",
    "mathscr": "KaTeX_Script",
    "mathbb": "KaTeX_AMS",
    "mathsf": "KaTeX_SansSerif",
    "mathtt": "KaTeX_Typewriter",
}


def protect_raw_blocks(html: str) -> str:
    """Blank out <script>/<style> content (same length) so it can't match as math/text,
    while keeping every other character's offset unchanged for readable context slices."""
    def blank(m: "re.Match") -> str:
        return re.sub(r"[^\n]", " ", m.group(0))

    html = re.sub(r"<script[\s\S]*?</script>", blank, html)
    html = re.sub(r"<style[\s\S]*?</style>", blank, html)
    return html


def find_math_regions(html: str):
    """Yields (tex, start_index) for every $$...$$ then every remaining $...$ span."""
    protected = protect_raw_blocks(html)
    regions = []
    for m in re.finditer(r"\$\$([\s\S]+?)\$\$", protected):
        regions.append((m.group(1), m.start()))
    protected_no_display = re.sub(r"\$\$[\s\S]+?\$\$", lambda m: " " * len(m.group(0)), protected)
    for m in re.finditer(r"\$([^$\n]+?)\$", protected_no_display):
        regions.append((m.group(1), m.start()))
    return regions


def check_angle_brackets(html: str):
    violations = []
    for tex, idx in find_math_regions(html):
        if "<" in tex or ">" in tex:
            line = html.count("\n", 0, idx) + 1
            violations.append((line, tex.strip()[:100]))
    return violations


def check_missing_fonts(html: str):
    protected = protect_raw_blocks(html)
    violations = []
    for cmd, font_family in MATH_FONT_COMMANDS.items():
        if re.search(r"\\" + cmd + r"\b", protected) is None:
            continue
        # A real embedded @font-face has this family name followed eventually by a
        # data: URI src within the same rule, not just a `.mathcal{font-family:...}`
        # class-mapping rule (which has no src at all).
        pattern = re.compile(
            r"@font-face\{[^}]*font-family:\"?" + re.escape(font_family) + r"\"?[^}]*\}"
        )
        found_with_data = any("src:url(data:" in m.group(0) for m in pattern.finditer(html))
        if not found_with_data:
            count = len(re.findall(r"\\" + cmd + r"\b", protected))
            violations.append((cmd, font_family, count))
    return violations


def check_file(path: str) -> bool:
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    ok = True
    bracket_violations = check_angle_brackets(html)
    if bracket_violations:
        ok = False
        print(f"FAIL {path}: {len(bracket_violations)} formula(s) with raw < or >")
        for line, snippet in bracket_violations[:10]:
            print(f"    line {line}: {snippet}")
        if len(bracket_violations) > 10:
            print(f"    ... and {len(bracket_violations) - 10} more")

    font_violations = check_missing_fonts(html)
    if font_violations:
        ok = False
        print(f"FAIL {path}: math-alphabet command(s) used without embedded font")
        for cmd, font_family, count in font_violations:
            print(f"    \\{cmd} used {count}x but {font_family} has no embedded @font-face. "
                  f"Fix: run the subject's assets/scripts/build_katex_css.py "
                  f"--add-font {font_family}-Regular, then re-run this check.")

    if ok:
        n = len(find_math_regions(html))
        print(f"PASS {path}: {n} formulas, no raw <>, all used fonts embedded")

    return ok


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_math_html_safety.py path/to/artifact.html [more.html ...]")
        sys.exit(2)

    all_ok = True
    for path in sys.argv[1:]:
        if not check_file(path):
            all_ok = False

    sys.exit(0 if all_ok else 1)
