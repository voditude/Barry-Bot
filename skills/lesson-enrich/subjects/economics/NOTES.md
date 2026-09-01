# Economics subject pack — not yet built

Stub. Follow the same process used for `subjects/math/`: pick a real economics course and
real lecture material, build a worked sample lesson from it, iterate on quality with the
user, then extract the resolved decisions into a `PACK.md` alongside subject-specific
reference/assets (analogous to `subjects/math/reference/` and `subjects/math/assets/`).

The invariants in `../../reference/invariants.md` and the tone rule in
`../../reference/tone-guide.md` already apply here unchanged — they don't get re-decided per
subject. What's still open for economics specifically:

- Whether/how LaTeX applies (economics uses less dense notation than pure math, but still
  has real formulas — utility functions, elasticities, optimization conditions).
- What "diagram" means here — likely supply/demand curves, indifference-curve diagrams,
  production-possibility frontiers, generated the same way the math pack generates plots
  (matplotlib), rather than the math pack's geometric/set-theoretic diagrams.
- What counts as a "worked example" or "practice weave" source in an economics course
  (problem sets look different from a pure-math problem set — may include short-answer or
  graph-reading questions, not just closed-form answers).
