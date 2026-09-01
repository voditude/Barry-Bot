# Design tiers — what to reuse from the reference sample

`reference/quality-bar-sample.html` (the Totient & Möbius rebuild) is a real,
finished worked example — not a genericized template. Read it for how the
pieces fit together, but only Tier 1 below travels to a new topic unchanged.

## Tier 1 — always reuse

- **Typography pairing**: a serif display face (headings) + matching sans
  (body) + a mono face (labels, data, code) from the same or a deliberately
  paired family. The *pattern* (three roles, one coherent family or a
  considered pairing) is what's reusable — not necessarily IBM Plex
  specifically if another pairing suits the new subject better.
- **Layout**: masthead (eyebrow + title + one-sentence framing) → sticky
  numbered TOC + main content column, `~680px` reading width, numbered
  sections with a hairline rule between them.
- **Components**: `.panel` (tinted-background callout for a derivation
  step), `.check` (inline verification callout), `.tblwrap`/`table.data`
  (worked-value tables, `tabular-nums`), the masthead/TOC/section CSS
  structure itself.
- **Math rendering plumbing**: the MathJax `tex-svg` config block and
  `<script>` tag (avoids KaTeX's blocked-webfont problem in the Artifact
  CSP). If `lesson-enrich`'s inlined-KaTeX-font approach
  (`skills/lesson-enrich/subjects/math/assets/katex/katex.inline.css`)
  already exists for the subject in question, prefer reusing that proven
  asset instead of loading MathJax fresh — don't maintain two math-rendering
  mechanisms if one already works for that subject.
- **Method**: motivate → build from scratch → worked example → generalize →
  tie back (see `SKILL.md` step 4). This is the actual differentiator from
  `lesson-enrich`, and it is subject-agnostic by construction.

## Tier 2 — always re-derive per subject/topic

- **Accent color.** The sample's amber (`#b8721f` light / `#e0a34c` dark) was
  chosen for a sieve/blueprint number-theory feel. A new topic needs its own
  accent, grounded the same way `artifact-design` asks for any artifact —
  pick something specific to *this* subject's own material, not a reused hex
  value.
- **Diagrams.** The sieve grid, Venn diagrams, cube Hasse diagram, and dark
  matrix-inversion panels are number-theory-specific devices. A stochastic
  modelling topic needs its own diagram vocabulary (state-transition
  diagrams, sample-path plots —
  `skills/lesson-enrich/subjects/stochastic-modelling/assets/scripts/state_diagram.py`
  is the existing tool for that), an economics topic needs its own, and so
  on. Never place one subject's diagram type into another subject's rebuild
  just because it rendered well here.
- **The dark "instrument panel" treatment for matrices** is itself a
  number-theory-motivated choice (poset ζ/μ matrices, framed like a
  terminal output). It is not a general "how to show tabular data" rule —
  don't apply it to, say, a probability table with no matrix-inverse framing
  behind it.

If unsure whether something is Tier 1 or Tier 2, ask: "does this fact about
the page exist *because it's a page*, or *because it's about totients and
Möbius functions*?" The first is Tier 1, the second is Tier 2.
