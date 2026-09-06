---
name: practice-weave
description: Use when weaving practice questions into an enriched lesson document from a course's real problem set — matching real questions to lesson sections via a concept-tag manifest, deciding where a section needs generated-only coverage, or verifying a generated answer by running real code before it's written down. Triggered by lesson-enrich's practice-weave step, or standalone when a problem set needs interleaving into existing lesson content.
---

# practice-weave

## Overview

Takes a lecture's own section structure plus its matching problem set and decides, section
by section, what practice belongs where — a real question reused with its official solution,
a new question generated to match real style and difficulty, or nothing woven at all when a
section is pure definition or the lecture itself defers the technique to later. It's the
sub-skill `lesson-enrich` calls out to for its "weave practice questions" step (see
`lesson-enrich/SKILL.md` step 7) rather than something folded into it. It does not own the
document's HTML/collapsible-answer rendering — that stays with `lesson-enrich`'s invariants.

**Reference material:**
- `reference/concept-tag-manifest.md` — the manifest template and a worked example pointer
- `reference/verification.md` — the two verification lanes for generated answers

## Workflow

1. **Find every real question for this lecture before concluding none exist.** Check for
   `<course-folder>/course-notes.md` first and follow anything it says about the problem set's
   shape. Then read the *entire* content of every file under `<course-folder>/source/
   problem-sets/` — never infer a file's scope from its name or date. A course may keep one
   cumulative problem-set document covering the whole semester (updated/reprinted as new
   practice classes are added) rather than one file per lecture; a file that covered only
   earlier weeks the last time it was read may have grown since. "No file dated/named for this
   week" is never sufficient grounds for "no problem set exists" — only having read every
   current file in full is. Build the concept-tag manifest from what that full read turns up:
   for every real question found, read it against the lecture's own section headers — not an
   invented taxonomy — and record which section/technique it tests. Write the manifest to
   `<course-folder>/manifests/<lecture-id>-question-manifest.md` following
   `reference/concept-tag-manifest.md`'s template.
2. **Decide weave / generate-only / skip per section**, using the decision rule below. Record
   every decision in the manifest, including skips. A gap never evaluated is a bug; a gap
   evaluated and skipped is a design decision — the manifest is what tells them apart later.
3. **Default mix**: 1 real + 1 generated question per woven concept point, bumped toward more
   generated coverage for concepts the lecture itself flags as newly introduced or heavy.
4. **Generate additional questions** in the same style/difficulty as the real ones — a new
   scenario, not a reworded version of an existing question — for both the real+generated
   pairing case and the generated-only case.
5. **Verify every generated answer by running real code before writing it down** — never
   assert one. See `reference/verification.md` for the two lanes and the worked pattern.
6. **Apply the provenance rule exactly** (below) when writing up each question + answer.
7. **Hand the finished pairs back to `lesson-enrich`** for inline embedding at the tagged
   section, using its existing collapsible-disclaimer pattern. `practice-weave` never touches
   the document's HTML itself.

## Decision rule — weave, generate-only, or skip

| Situation | Action |
|---|---|
| Real question matches a section that has no practice yet | Weave the real question (official solution if the problem set has one) + one generated pairing question |
| Section is conceptually heavy or newly introduced, no real question covers it | Weave a generated-only question anyway — a heavy/new concept with zero practice is exactly the case generation exists for |
| Section is pure definition/notation, nothing to apply yet | Skip; log as deliberately unwoven |
| A real question's technique is stated at one section and first applied at a later one | Weave at the point of application, not the bare statement |
| Real question or section uses a technique the lecture explicitly defers to a later week | Skip for this lecture; log as a future-pass candidate |

## Provenance rule

| Question | Official solution in problem set? | Write-up |
|---|---|---|
| Real | Yes | Reproduce the official solution. No disclaimer. |
| Real | No | Generate the answer, verify it, disclaim it — being a real question does not exempt a generated answer from disclaiming. |
| Generated | n/a | Generate the answer, verify it, disclaim it. |

## Common mistakes

| Mistake | Fix |
|---|---|
| Inventing a concept taxonomy instead of using the lecture's own section numbering | Manifest tags map to the lecture's actual headers — see `reference/concept-tag-manifest.md` |
| Weaving only where real questions exist and leaving thin sections bare | Newly-introduced/heavy concepts get generated-only coverage — that's the point of generation, not a fallback |
| Weaving a real question where its principle is first *stated*, not where it's first *applied* | Match to the section where the lecture itself uses the technique |
| Asserting a generated answer without running it | Verify by real code first — `reference/verification.md`; a genuine arithmetic slip was caught exactly this way in the v1 pass |
| Skipping a disclaimer because the question itself is real | Provenance is per-answer, not per-question — a real question with no official key still gets a disclaimered generated answer |
| Silently dropping a section instead of recording why | Log every skip as "deliberately unwoven" with a reason in the manifest |
| Concluding "no problem set for this lecture" because no per-week file exists | Read every file under `source/problem-sets/` in full first — a course may keep one cumulative, growing document instead of one file per week (see `course-notes.md` if present) |
