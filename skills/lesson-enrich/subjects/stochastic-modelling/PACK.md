# Stochastic modelling subject pack

Subject-specific rules and tooling for `lesson-enrich` when the course is a
probability/stochastic-processes subject (proven out on a real stochastic-modelling
course). A dedicated pack rather than an extension of `subjects/math/PACK.md`
because this subject needs a diagram type — Markov transition/state diagrams —
that the math pack doesn't cover, and its own notation conventions
(recurrence/transience, periodicity, stationary distributions) that don't overlap
with the discrete-math pack's remit. Per-subject-pack architecture (economics/finance
are stubbed the same way math was before this pack existed).

## Rules specific to stochastic modelling

- **Math notation is always real LaTeX**, rendered with KaTeX — never unicode
  approximations. Same requirement as the math pack, reused verbatim (see Tool
  calling below).
- **Diagrams**: two distinct diagram types come up in this subject:
  - **Markov transition/state diagrams** — generate with
    `assets/scripts/state_diagram.py` (see below). Earns its place from the first
    time the course itself draws one (the `j → k₁..k₄` diagram convention,
    introduced when transition matrices are introduced) and repeatedly afterward
    for classification-of-states worked examples, since a communicating-class
    structure is genuinely easier to see as a graph than to infer from a matrix.
  - **Ordinary function/line plots** (e.g. the birthday-problem-style curves that
    show up in the probability-review material) — use
    `assets/scripts/diagram_style.py` directly, same as the math pack.
  - Default bar from the invariants still applies: skip a diagram for a concept
    fully specified by a short formula a reader can hold in their head.
- **Proofs**: reproduce the source's proof in full in the source-content box. Where
  the source is terse (e.g. the "communication classes are either recurrent or
  transient" argument), the added-derivation box expands the skipped algebraic
  steps — same additive philosophy as the math pack's proof handling.
- **State-space notation**: use the lecture's own state labels (numeric or named)
  consistently across prose, transition matrices, and diagrams for a given
  worked example — don't relabel states for tidiness.

## Tool calling

### KaTeX with embedded fonts (required for every generated lesson)

Identical wiring to the math pack — reuse it rather than re-deriving:

1. `assets/katex/katex.inline.css` is already built (synced from the math pack's
   font subset, which now covers algebra/probability notation plus `\mathcal`
   (filtrations, sigma-algebras), `\mathfrak`, and `\mathscr` — those used to be
   missing and rendered in the browser's default font instead of KaTeX's, which is
   why they're in the default now rather than behind a re-run step). Re-run
   `assets/scripts/build_katex_css.py` only if a lesson needs something outside that
   subset, e.g. very large delimiters (`KaTeX_Size3`/`KaTeX_Size4`).
2. Splice `assets/katex/katex.inline.css` into a `<style>` tag via a script/file
   operation — never read the ~180KB CSS text into your own context.
3. Load `katex.min.js` and `contrib/auto-render.min.js` from cdnjs as `<script>`
   tags (same URLs as the math pack, see its `PACK.md`).
4. Write formulas as `$...$` / `$$...$$` and call `renderMathInElement` on
   `DOMContentLoaded` — copy the exact call from
   `../../reference/quality-bar-sample.html`.
5. **HTML-escape `<` and `>` inside every formula** (`P(X &lt; t)`, not `P(X < t)`) — this
   content sits directly in page HTML, so a raw `<n`/`<t`/etc. opens what the browser reads
   as an unclosed tag and silently swallows everything up to the next stray `>`, corrupting
   whatever's between. See the math pack's `PACK.md` for the full explanation (found via a
   real bug: hitting-time and tail-probability bounds like `P(T>n)`, `X_n < k` are exactly
   the pattern that triggers this). `\lt`/`\gt` or `\le`/`\ge` are the easy defaults that
   avoid the issue entirely.

### Markov transition/state diagrams

`assets/scripts/state_diagram.py` — `draw_state_diagram(ax, P, labels=...)` draws
a circular-layout directed graph for a transition matrix `P` (list of lists,
rows summing to 1): filled nodes for states, curved arrows for a reciprocal pair
of transitions, straight arrows otherwise, small self-loops for `p_ii > 0`, and
probability labels (auto-formatted as a simplified fraction where one exists,
else a 2-decimal value). No `networkx` dependency — plain matplotlib
`FancyArrowPatch` on a hand-computed circular layout, since `networkx` isn't
installed in this environment. Save each figure as a PNG via
`plt.savefig(..., facecolor="white", bbox_inches="tight")`, then embed as a
base64 `data:` URI — never a relative path (see `diagram-conventions.md`).

### Ordinary plots

`assets/scripts/diagram_style.py` — same module as the math pack, palette-matched
to this document (`--source`/`--add`/`--accent`).

## Reference

- `reference/diagram-conventions.md` — expanded guidance on when a diagram earns
  its place, specific to state diagrams
- `../../reference/quality-bar-sample.html` — the KaTeX wiring is the literal
  pattern to copy (the diagram in that file is a math-pack one; for a state
  diagram, follow this pack's own conventions instead)

## Known gaps (flagged for extending this pack, not yet needed for weeks 1-3)

- No stationary-distribution / linear-system solver helper yet — week 4+ content
  (deriving `π` from `πP = π` plus `Σπⱼ = 1`) will need a `sympy`-based
  `linsolve` helper in the verify-script toolkit.
- No periodicity/gcd or communicating-class computation helper — fine by hand for
  the 3-4 state matrices seen in weeks 1-3; would be worth adding if a later
  week's tutorial scales up to a general-k argument that needs it computed rather
  than reasoned through.
