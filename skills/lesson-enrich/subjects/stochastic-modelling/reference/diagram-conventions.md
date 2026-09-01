# Diagram conventions (stochastic modelling)

## When a Markov transition/state diagram earns its place

Generate one when at least one of these is true:
- The source lecture already draws one for this concept (e.g. the general
  `j → k₁..k₄` transition-diagram convention, or a specific worked chain's
  diagram) — regenerate it rather than describing it in prose, matching axes/
  arrows/labels. This is preserving original content, not inventing enrichment.
- A classification-of-states argument (accessibility, communicating classes,
  essential/non-essential, periodicity) is being worked through for a specific
  chain — the class structure is genuinely easier to verify visually on a graph
  than to trace through a transition matrix's entries.

Skip a diagram when the transition structure is fully specified by a short
matrix a reader can scan directly (e.g. a 2-state chain, or a chain whose
structure is stated purely symbolically without concrete transition values).

## When an ordinary plot earns its place

Same bar as the math pack: the source already has one, or a relationship (e.g.
a probability as a function of a parameter) is genuinely easier to verify
visually than algebraically.

## How

- Markov diagrams: `../assets/scripts/state_diagram.py`'s `draw_state_diagram`.
- Ordinary plots: `../assets/scripts/diagram_style.py`, same as the math pack.
- Save as PNG, embed as a base64 `data:` URI in the final page (never a relative
  path or external image link — the Artifact CSP blocks non-CDN image fetches at
  view time).
- One figure per concept, captioned, explaining what (if anything) was added
  versus the source (e.g. probability labels added to a diagram the source left
  unlabelled, or a communicating-class colour/grouping added to make essential
  vs. non-essential visually obvious where the source only states it in prose).
