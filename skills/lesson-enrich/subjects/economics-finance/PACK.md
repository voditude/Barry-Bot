# Economics & Finance subject pack (light tier — see ../LIGHT-PACK-PROCESS.md)

Drafted from general subject knowledge, not iterated against a real course. Merged because
the two fields share the same notation density and tooling — a corporate-finance course and
a microeconomics course lean on the same LaTeX/optimization/time-series conventions far more
than they differ.

## Notation

Real LaTeX via KaTeX, same wiring as `../math/PACK.md` (reuse `build_katex_css.py` and the
`&lt;`/`&gt;` escaping rule as-is). Density is lower than pure math — mostly applying a named
formula or optimization condition rather than proving a general theorem. Common notation:
utility functions and indifference/budget constraints, elasticities, Lagrangians and
first-order conditions (micro); NPV/IRR/present-value sums, option payoffs, amortization
formulas (finance).

## Tooling

Matplotlib, reusing `../math/assets/scripts/diagram_style.py` for palette consistency.
Diagram types: supply/demand curves, indifference curves, production-possibility frontiers
(economics); price/cash-flow time series, payoff diagrams, amortization schedules (finance).
All are standard matplotlib plot types — no gap here, unlike some fields below.

## Worked example shape

A solved numeric problem: given inputs (cash flows, prices, elasticities), compute the
target quantity step by step, the same additive pattern as math — reproduce the source's
own worked example in full, then expand any step it states without full derivation.

## Rigor / citation

Name the standard result being applied the first time it's used (e.g. "this is the standard
NPV formula," "this applies the Fisher equation") rather than re-deriving from scratch every
time it recurs — the same pattern `tone-guide.md` already establishes for proof skeletons.
