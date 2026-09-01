# Diagram conventions (math)

## When a diagram earns its place

Generate one when at least one of these is true:
- The source lecture already contains a figure or plot for this concept. Regenerate it
  (matching axes/labels/behavior) rather than describing it in prose — this is preserving
  original content, not inventing enrichment. Add at most one small annotation if it
  clarifies something the source leaves implicit (see the birthday-probability plot in the
  reference sample: the source has no marker for the 50% crossover; the regenerated version
  adds one).
- A relationship is genuinely easier to verify visually than algebraically — e.g. a plotted
  function, a region defined by inequalities, a graph-theory structure.

Skip a diagram when the concept is fully specified by a short set-builder or algebraic
expression that a reader can hold in their head — a two-set Venn diagram for `A ∩ B` and
`A ∪ B` was cut from the reference sample for exactly this reason.

## How

- matplotlib, via `../assets/scripts/diagram_style.py` for consistent colors/typography.
- Save as PNG, embed as a base64 `data:` URI in the final page (never a relative path or an
  external image link — the Artifact CSP blocks non-CDN image fetches at view time, and a
  relative path won't resolve at all once published).
- One figure per concept, captioned, explaining what (if anything) was added versus the
  source.
