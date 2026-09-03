---
name: transcript-slide-extract
description: Use when a lecture transcript (a dropped text file — e.g. a Canvas Studio auto-generated transcript) is present alongside slides for a lecture lesson-enrich is about to enrich. Cross-checks the transcript against the lecture's already-extracted slide section structure and surfaces spoken content (asides, clarifications, extra examples) the slides don't contain. Triggered automatically by lesson-enrich's ingest step whenever a transcript file is present for that lecture — never run standalone, and never touches the final document's HTML.
---

# transcript-slide-extract

## Overview

Takes a lecture's slide section structure (already extracted by `lesson-enrich`) and its
matching transcript file, and finds spoken content the slides don't contain — an aside, a
clarification, or a full extra example the lecturer gave live. It's the sub-skill
`lesson-enrich` calls at ingest time when a transcript is present (see `lesson-enrich/SKILL.md`
step 3), the same way `practice-weave` is called for practice questions. It does not own the
document's HTML — it hands a manifest back, and `lesson-enrich` decides everything about
placement and wording.

**Slides are the source of truth.** This skill only looks for transcript content that adds to
the slides. The reverse — slide content the lecturer never verbally addressed — is out of
scope; it's a different, lower-value signal (often just "ran out of time," not missing
pedagogical content) and is not designed here.

**Text transcripts only.** No audio/video/frame processing. If a course only has a
video/audio recording and no transcript file, this skill does not run — ask the user to drop a
transcript (Canvas Studio's own auto-generated transcripts are downloadable) rather than
attempting any transcription.

**Reference material:**
- `reference/transcript-gap-manifest.md` — the manifest template and the pointer-style rule

## Precondition

Two things are handed in by `lesson-enrich`, never re-derived here:
1. The slide section structure `lesson-enrich` already extracted for this lecture (section
   titles/headers, in the order they appear).
2. The path to the transcript file for this lecture, located under
   `<course-folder>/source/lectures/` per the course's own file-naming convention (the same
   convention `lesson-enrich` already infers per course — no new naming convention here).

If `lesson-enrich` finds no transcript file for a lecture, it does not call this skill at all.
This is never a hard dependency — `lesson-enrich` must produce a complete document with no
transcript present, exactly as it does today.

## Workflow

1. **First-run notice, once per course.** Check `<course-folder>/.enrich-preferences.md` for a
   line reading `transcript-slide-extract: sequential-alignment-notice-shown`. If absent, tell
   the user once, in one sentence, that matching assumes the transcript follows the slides in
   roughly sequential order (not a full reordered topic search), then append that line to
   `.enrich-preferences.md`. If present, skip straight to step 2 — do not repeat the notice on
   later lectures for the same course.
2. **One sequential pass over the transcript.** Walk the transcript from top to bottom in
   parallel with the slide section list, in order. For each slide section, read forward through
   the transcript until the content stops matching that section's keywords/topic and starts
   matching the next section's — that boundary is the section's transcript range. Do this in a
   single linear walk. Do not dispatch parallel subagents, and do not run a full cross-product
   keyword search (every section against every transcript segment) — this is a light
   single-pass cross-check layer over the slides, not an exhaustive matching problem, and the
   token cost of an exhaustive approach is exactly what this design avoids.
3. **Detect order jumps.** If a stretch of transcript doesn't match the section it's currently
   walking but clearly matches a different section (the lecturer backtracked or previewed later
   material), record the jump in the manifest's "Order jumps" list and resume alignment from the
   matched section, rather than forcing a bad match or silently dropping the stretch.
4. **Classify anything beyond plain restatement, case by case:**
   - **Inline fold** — a short aside, clarifying remark, or "why this matters" comment on a
     concept the slides already cover. One or two sentences, not a full worked unit.
   - **Add-on box** — a full add-on unit: either a genuinely new topic with no slide
     counterpart, or a complete worked example (even one illustrating an already-covered
     concept). Judge by size and shape, not just topic overlap — a full example a lecturer gave
     to illustrate a covered concept is still a box, the same shape `lesson-enrich`'s invariants
     already require for the "fresh, non-lecture analogy" on bijections; this skill is just
     surfacing one the lecturer already gave.
   - This is a case-by-case judgment call, not a mechanical rule — expected to sharpen with real
     usage feedback over time, not something to over-formalize now.
   - A stretch that simply restates what's already on the slides is not a gap — do not record it
     as a fold or a box.
5. **Capture timestamps when present.** If the transcript file carries timestamps (Canvas
   Studio's format does), record the approximate timestamp range for each matched section and
   each gap found, so the reader can jump back to that point in the recording. If the transcript
   has no timestamps (e.g. manually typed notes), omit this — it is never a blocking
   requirement, just an automatic addition when the source supports it.
6. **Write the manifest.** Following `reference/transcript-gap-manifest.md`'s template exactly,
   write `<course-folder>/manifests/<lecture-id>-transcript-gaps.md`. Log every slide section's
   outcome — matched with no gap, inline fold, add-on box, or deliberately not surfaced — not
   just the sections where something was found. Every row is pointer-style: a transcript
   line/timestamp range and a one-line paraphrase, never a quoted transcript passage of any
   length. `lesson-enrich` re-reads the raw transcript file at the given range to get exact
   wording when it drafts — the manifest is an index, not a second copy of the transcript.
7. **Hand the manifest path back to `lesson-enrich`.** This skill's job ends here. It never
   writes to, or reasons about, the document's HTML — `lesson-enrich` reads the manifest during
   its own section-by-section drafting pass (step 4 of its workflow) and decides exact wording
   and placement, the same boundary `practice-weave` already holds for practice questions.

## Common mistakes

| Mistake | Fix |
|---|---|
| Re-deriving the slide section structure independently | Reuse what `lesson-enrich` already extracted — it's handed in, not re-read from the slides a second time. |
| Parallel/exhaustive matching (every section against every transcript segment, or subagent fan-out) | One sequential pass only — this is a light cross-check layer, not a search problem. Token cost was the explicit reason this design was chosen. |
| Quoting transcript passages into the manifest | Pointer-style only: line/timestamp range + one-line paraphrase. `lesson-enrich` re-reads the raw transcript for exact wording at drafting time. |
| Treating slide-only gaps (slide content the lecturer skipped) as in scope | Out of scope for v1 — this skill only surfaces transcript-to-slide gaps, never the reverse. |
| Boxing every clarifying remark, or folding every full example | Judge by size/shape: short asides fold inline; full add-on units (including full examples for already-covered concepts) get their own box. |
| Logging only the sections where a gap was found | Log every section's outcome, including "matched, no gap" and "deliberately not surfaced" — an unevaluated gap and a considered skip must stay distinguishable later. |
| Repeating the sequential-alignment notice every lecture | Check `.enrich-preferences.md` first; show it once per course, then record that it was shown. |
| Forcing a bad match when the lecturer jumps out of slide order | Detect the jump, record it in the manifest's "Order jumps" list, and resume alignment from the correct section. |
