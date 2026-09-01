# Invariants

These rules hold for every subject and every user, regardless of the onboarding calibration
in `onboarding-survey.md`. If a user's stated preference conflicts with one of these, the
invariant wins — say so explicitly rather than silently complying with the preference.

## Content

- **Additive, not condensed.** Every definition, proposition, proof, and worked example from
  the source lecture material is reproduced in full in its own section. The only permitted
  condensation is the topic summary at the top of the document.
- **Original vs. added content is visually distinguishable throughout** — not just true in
  principle, but legible at a glance (the quality-bar sample uses two box styles/colors with
  a legend; a different visual system is fine as long as the distinction is as clear).
- **Undergrad-level calibration**: assume the course's own baseline level by default (see the
  onboarding survey for how a user can shift this). For any concept flagged as newly
  introduced in the lecture being enriched, build up from first principles rather than
  assuming prior exposure, regardless of the calibrated baseline.
- **Practice questions are woven inline** at the point in the document where their technique
  is introduced, never appended in a block at the end.
- **Generated answers to practice questions are disclaimered inline**, per answer (a
  collapsible flag directly on that answer — "may be incorrect, verify against course
  materials"), not as one banner covering a whole section.
- **Diagrams earn their place.** Skip a diagram for a concept simple enough not to need one.
  Prefer regenerating a diagram/plot that already exists in the source over inventing a new
  visual. Diagrams are always produced by an actual tool call (the subject pack specifies
  which), never described in prose as a stand-in for a real image.

- **Small-case enumeration for every introduced bijection.** Alongside the general
  definition/proof, show the complete correspondence for one small, concrete case — every
  element on both sides, generated and checked by real code, not 2-3 illustrative examples.
  This is what lets the reader verify the argument instead of taking it on faith (confirmed
  in live tutoring use: a full table of, say, all 10 length-5 binary words with two zeros
  next to their matching subsets is what made a bijection concrete rather than asserted).
- **A fresh, non-lecture analogy for every introduced bijection.** After reproducing the
  lecture's own example in full (never cut it), add at least one further worked instance in
  a different, relatable real-world setting the lecture didn't use (coin flips, light
  switches, card games, distributing items among people, and so on) — chosen to differ from
  the lecture's own numbers/objects, so the reader has to re-apply the pattern rather than
  pattern-match on surface details.
- **End a newly-introduced technique's box with a self-check, not a summary.** One short
  "try this yourself" variant — different numbers or objects, same technique — rather than a
  restated conclusion. It gives the reader something to actually do, and something concrete
  to bring to the `i-dont-get-it` skill if it doesn't land.

## Writing

- Follow `tone-guide.md` exactly: direct, logical, step-by-step. No filler, no rhetorical
  flourish, no pleasantries.
- Math renders as real typeset notation (LaTeX via KaTeX for subjects where that applies —
  see the relevant subject pack), never unicode-approximated symbols.

## Follow-up when a concept doesn't land

Lessons no longer carry an in-artifact Q&A control ("Ask about this section" was retired —
see `design-enrichment.md` at the project root, §6). When a specific concept isn't landing for the reader, use the
separate `i-dont-get-it` skill instead: it reads this artifact plus the raw lecture source
and builds a dedicated, first-principles rebuild of just that topic. Do not reintroduce a
`sample()`-capability control into a lesson-enrich document.
