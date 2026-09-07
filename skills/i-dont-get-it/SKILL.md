---
name: i-dont-get-it
description: Use when a specific topic from an already-enriched lecture isn't landing — the user says something like "I don't get X", "still confused about Y", "explain Z differently". Builds a focused, first-principles, example-led standalone explainer for that one topic. Requires a lesson-enrich artifact to already exist for the course; reads it as primary source (cross-checked against raw lecture material for correctness — see workflow step 3), not raw material alone.
---

# i-dont-get-it

## Overview

Companion skill to `lesson-enrich`. Where `lesson-enrich` produces one additive,
provenance-labeled document per lecture, `i-dont-get-it` produces one freeform,
deep-dive document per *topic* — triggered when a specific concept from that
lecture isn't landing for the reader. It replaces the retired "Ask about this
section" in-artifact control: instead of a short streamed chat answer, this
skill builds a complete standalone artifact using the same first-principles
method every time, with correctly-rendered math and diagrams built for that
topic specifically.

This is not a lighter version of `lesson-enrich`. It has a different job:
`lesson-enrich` stays faithful to the lecture's own structure and never
condenses; `i-dont-get-it` is free to reorder, motivate from scratch, and pull
in outside material, because its only goal is getting the concept to click.

## Precondition

A `lesson-enrich` artifact must already exist for the course this topic
belongs to (`courses/<course-id>/artifacts/weekN-enriched.html` or similar).
If none exists yet, say so and suggest running `lesson-enrich` first — do not
improvise this skill directly from raw source material with no enriched
artifact to ground it.

## Workflow

1. **App-level onboarding (first run, once ever).** Check for `.barry-profile.md` at the repo
   root (not inside any `courses/<id>/` folder). If absent, run
   `../lesson-enrich/reference/app-onboarding.md`'s conversation in full before doing anything
   else, then write the result there. If present, load it and continue — this is app-level,
   run at most once per install regardless of which of the three direct-entry skills triggers
   it first.
2. **Locate the topic.** If the user names a course/week, use it directly. If
   not, search `courses/*/artifacts/*.html` for the enriched artifact(s)
   whose content matches the named topic. If more than one course could
   match, ask which one rather than guessing.
3. **Read the source, both layers.**
   - Read the matching section(s) of the enriched artifact — this is the
     primary source for scope, definitions, and notation the student is
     actually being taught.
   - Cross-check every definition, formula, and worked value the rebuild
     will rely on against the original raw lecture material in
     `courses/<course-id>/source/lectures/`. The enriched artifact is a
     downstream copy and can contain mistakes; the raw lecture material is
     the ground truth. If they disagree, trust the raw source, use its
     version, and flag the discrepancy to the user — do not silently repeat
     an error from the enriched artifact.
4. **Search for better pedagogy, not better math.** Use web search to find
   analogies, real-world motivating hooks, or alternate framings of the
   concept (e.g. the rock-paper-scissors example for transitivity, or the
   fractions/RSA motivation for the totient function). Never let a web
   result override the course's own definitions, notation, or conventions —
   those still have to match what the student is being taught. Web search
   is for finding a better way to explain the same thing, not a second
   source of mathematical truth.
5. **Draft using the fixed method, every time:**
   - **Motivate** — why would anyone care about this, before any formula.
   - **Build from scratch** — construct the idea on small, concrete numbers
     the reader can check by hand, before generalizing.
   - **Worked example** — one running example carried through every
     section, not a fresh example per section.
   - **Generalize** — state the general formula/theorem only after the
     concrete case has made it feel inevitable.
   - **Tie back** — end by reconnecting to the course's own notation and the
     enriched artifact's section numbering, so the reader can return to the
     original material.
   No strict source/added provenance labeling is required here (unlike
   `lesson-enrich`) — this is a freeform rebuild, not an additive companion.
   It still has to be factually correct throughout. Prose style follows
   `../lesson-enrich/reference/tone-guide.md` in full — the same forbidden
   fillers and forbidden AI-sounding patterns apply here as in
   `lesson-enrich`'s own output.
6. **Design: two tiers, not one template.** Read
   `reference/quality-bar-sample.html` and `reference/design-tiers.md` before
   writing any HTML.
   - **Tier 1 (always reuse):** the structural scaffolding — masthead,
     sticky numbered TOC, panel/check-block components, section rhythm,
     table styles, the MathJax `tex-svg` setup. Copy these, don't re-derive
     them. Exception: if `lesson-enrich`'s already-proven inlined-KaTeX-font
     asset (`skills/lesson-enrich/subjects/math/assets/katex/katex.inline.css`)
     already exists for the subject in question, prefer reusing that over
     loading MathJax fresh — see `reference/design-tiers.md`.
   - **Tier 2 (always re-derive):** the accent color and every diagram. The
     sample's amber/paper palette and its Venn/sieve/Hasse/matrix diagrams
     are choices made *for number theory* — grounded in that subject's own
     material (sieves, primes, lattices), per the `artifact-design` skill's
     "ground it in the subject" rule. A different subject needs its own
     accent and its own diagram types, chosen the same way, not these ones
     reused. Load `artifact-design` before choosing them.
7. **Verify by hand, carefully.** Every worked value gets derived step by
   step in the document, the way the reference sample does (e.g. checking
   inclusion–exclusion against an actual sieve grid). No mandatory
   code-verification script is required — this is lighter than
   `practice-weave`'s discipline — but a claimed numeric result must be
   shown arriving at that number, not just stated.
8. **Publish and save.** Before publishing, run
   `python skills/lesson-enrich/reference/scripts/check_math_html_safety.py <the-generated-file>.html`
   and treat a non-zero exit as a blocker, not a warning — same rule
   `lesson-enrich/SKILL.md` states, and for the same reason: raw `<`/`>`
   inside a formula silently corrupts the page's HTML before KaTeX/MathJax
   ever runs (see `design-enrichment.md` at the project root, §5). Then
   publish as an HTML Artifact (load `artifact-design` first, as with any
   artifact), and also write the same file to
   `courses/<course-id>/artifacts/<slug>.html` (e.g.
   `week3-4-totient-mobius.html`) so it persists as a real course deliverable
   alongside the week/assignment artifacts, not just a one-off chat output.

## Common mistakes

| Mistake | Fix |
|---|---|
| Treating the enriched artifact as ground truth with no cross-check | Step 3 requires checking against raw lecture source before relying on a definition/value. |
| Using web search to find a different definition or notation than the course uses | Web search is for pedagogy (analogies, motivation), never for overriding the course's own math. |
| Reusing the amber palette or the Venn/sieve/Hasse diagrams for an unrelated subject | Only Tier 1 (structure) is reusable. Tier 2 (palette, diagrams) is re-derived per subject — see `reference/design-tiers.md`. |
| Following lesson-enrich's provenance-labeling/additive rules here | Those are `lesson-enrich` invariants, not this skill's. This is a freeform rebuild — reorder and motivate freely, as long as it stays correct. |
| Running this with no enriched artifact to source from | Check the precondition first; point the user to `lesson-enrich` if none exists. |
| Writing a fresh example per section instead of one running example | Carry a single worked example through the whole document, the way the reference sample uses n = 30 throughout. |
