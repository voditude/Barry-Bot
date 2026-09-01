# Math subject pack

Subject-specific rules and tooling for `lesson-enrich` when the course is a math subject
(proven out on MAST30012 Discrete Mathematics; should generalize to other proof/formula-heavy
math courses).

## Rules specific to math

- **Math notation is always real LaTeX**, rendered with KaTeX — never unicode approximations
  (`n^m`, not `nᵐ`; `\sum`, not `Σ`). This is on top of, not instead of, the general
  invariants in `../../reference/invariants.md`.
- **Diagrams**: generate with matplotlib (see `assets/scripts/diagram_style.py` for the
  palette/style module that keeps generated figures visually consistent with the document).
  Default bar from the invariants applies: skip trivial concepts (a union/intersection Venn
  diagram was cut from the reference sample as unnecessary), prefer regenerating a plot
  already in the source over inventing a new one.
- **Proofs**: reproduce the source's proof in full in the source-content box. In the
  added-derivation box, if the source proof is terse, expand the steps it skips — this is
  the primary way "additive" cashes out for a math lecture.

## Tool calling

### KaTeX with embedded fonts (required for every generated lesson)

Artifacts' CSP blocks a `<link>` to KaTeX's CSS from any CDN, and blocks a runtime `fetch()`
of it too — only `<script>` tags are allowed from cdnjs. The fix, already built and tested:
inline KaTeX's CSS directly in the page, with its needed webfonts embedded as base64 `data:`
URIs inside the `@font-face` rules.

1. Run `assets/scripts/build_katex_css.py` (re-run it if the KaTeX version needs bumping, or
   if a lesson needs a font subset this hasn't fetched yet — the default now covers
   `\mathcal`/`\mathfrak`/`\mathscr`/`\mathsf`/`\mathtt` too, so this is rare; very large
   delimiters would need `KaTeX_Size3`/`KaTeX_Size4` added). It downloads `katex.min.css` plus
   the font subset from cdnjs and writes `assets/katex/katex.inline.css`.
2. Splice `assets/katex/katex.inline.css` into a `<style>` tag in the generated page — do
   this splice via a script/file operation, not by reading the ~180KB CSS text into your own
   context.
3. Load `katex.min.js` and the `contrib/auto-render.min.js` extension from cdnjs as
   `<script>` tags (these are fine as CDN scripts, unlike the CSS):
   ```html
   <script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.18.4/katex.min.js"></script>
   <script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.18.4/contrib/auto-render.min.js"></script>
   ```
4. Write formulas as `$...$` (inline) / `$$...$$` (display) directly in the HTML content, and
   call `renderMathInElement(document.body, {delimiters: [...], throwOnError: false})` on
   `DOMContentLoaded`. Copy the exact call from `../../reference/quality-bar-sample.html`.
5. **HTML-escape `<` and `>` inside every formula** — write `a \le c &lt; b`, never
   `a \le c < b`. The formula text sits directly in the page's HTML, not inside a `<script>`
   or `<style>` block, so it's parsed as markup before KaTeX ever sees it: a literal `<`
   followed by a letter (`<b`, `<n`, `<k`, ...) opens what the browser treats as a real,
   unclosed tag, silently swallowing everything up to the next stray `>` it finds — often
   several formulas and paragraphs later, corrupting whatever is between the two. This bit
   discrete-math content hard: strict order relations (`a<b`, `c<b`) are common there,
   `\le`/`\ge` mask the same risk for `\leq`/`\geq` but the bare `<`/`>` forms don't.
   `\lt`/`\gt` also render correctly in KaTeX and sidestep the issue entirely if simpler to
   default to. Check any generated page for this before publishing: no `$...$`/`$$...$$`
   span should contain a raw `<` or `>` — only `&lt;`/`&gt;`, `\lt`/`\gt`, or `\le`/`\ge`.

The default font subset in `build_katex_css.py` (Main-Regular/Bold/Italic, Math-Italic,
AMS-Regular, Size1, Size2, plus Caligraphic/Fraktur/Script/SansSerif/Typewriter — about
190KB raw) covers standard algebra/set-theory/probability notation including `\mathcal`
(power sets, sigma-algebras), `\mathfrak`, and `\mathscr`. Only very large delimiters
(`\big\big\big(` and bigger) fall outside it — add `KaTeX_Size3-Regular`/`KaTeX_Size4-Regular`
to `KEEP` and re-run the script if a lesson needs those.

### Diagrams

Use `assets/scripts/diagram_style.py` — import it in any one-off plotting script for a
specific lesson (see `assets/scripts/example_plot.py` for a full worked example: the
birthday-probability plot from the reference sample) so generated figures share the
document's palette (`--source`, `--add`, `--accent` colors) instead of matplotlib defaults.
Save each figure as a PNG, then embed it as a base64 `data:` URI in the page the same way
the KaTeX CSS is spliced in — never leave a relative file path in the published artifact.

## Reference

- `reference/diagram-conventions.md` — expanded guidance on when a diagram earns its place
- `../../reference/quality-bar-sample.html` — the finished example built from real MAST30012
  Week 1 content; the KaTeX wiring and the diagram in that file are the literal pattern to
  copy, not just an illustration
