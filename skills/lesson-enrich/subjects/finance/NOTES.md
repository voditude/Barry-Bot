# Finance subject pack — not yet built

Stub. Same process as `subjects/economics/NOTES.md` describes — build from a real course's
real material first, resolve quality-bar questions with the user, then extract a `PACK.md`.

What's likely different here from both math and economics, to scope when this gets built:

- Heavier use of time-series/financial charts (price paths, cash-flow diagrams, amortization
  schedules) rather than pure functions or economic curves — may need a different matplotlib
  convention set than `subjects/math/assets/scripts/diagram_style.py`, or a shared one if the
  palette/style transfers directly.
- Formula density is closer to math (NPV, IRR, options pricing) — the math pack's KaTeX
  wiring (`subjects/math/assets/scripts/build_katex_css.py` and the embedded-font CSS
  pattern) likely transfers as-is; confirm rather than re-deriving it.
- Whether finance courses commonly supply spreadsheets/models alongside transcripts and
  slides, which would need its own ingest handling not yet designed anywhere in this project.
