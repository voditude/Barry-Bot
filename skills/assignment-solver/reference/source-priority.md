# Source priority and skill dependencies

Assignment Solver sits downstream of `lesson-enrich` and `practice-weave` — it consumes their
output rather than re-deriving course content from scratch. For a given week/topic, gather
content in this order, falling back only when the higher-priority source is missing or
doesn't cover the needed technique:

1. **`courses/<course-id>/artifacts/week<N>-enriched.html`** — LessonEnrich's finished,
   curated artifact. Read this first: it's more concise than raw lecture material and already
   contains the intuition/derivation layer, so matching a problem to its taught technique is
   faster and more reliable here than starting from source.
2. **`courses/<course-id>/manifests/week<N>-question-manifest.md`** — PracticeWeave's
   concept-tag manifest. Use it to cross-check which section/technique a problem type maps
   to, and to catch a technique the artifact covers under a heading you weren't expecting. Its
   "Lecture section" column is an index into the *enriched artifact's* own section numbers —
   not citation-ready theorem/section numbering itself (see
   `reference/scope-and-citation.md` for what to actually cite).
3. **`courses/<course-id>/source/lectures/*`** — raw lecture material. Fall back here only
   when neither of the above exists yet for that week, or neither actually covers the specific
   technique the problem needs. This is the same PDF-ingestion path PracticeWeave already
   relies on: native Read-tool text + page-image extraction, cross-referenced by hand, since
   math-mode PDF text extracts garbled (e.g. `P(\Ti j=0 Aj)` for what's actually
   $\bigcap_{j=0}^i A_j$) — no OCR/math-parsing tool exists in this repo, and none is needed;
   the rendered page image is the ground truth when the extracted text is ambiguous.

## Precondition: a course needs *some* ingested material to begin with

If a course folder has no ingested material at all — no `artifacts/`, no `source/lectures/`
content — that's not a fallback case, it's a precondition failure. Stop and tell the user to
run `lesson-enrich` for that course first, rather than trying to solve problems from outside
knowledge because nothing course-scoped exists yet. A missing artifact/manifest for *one*
week within an otherwise-populated course is normal (step 3 above handles it); an entirely
empty course is a different situation and shouldn't be papered over.

## Reused, not duplicated

Assignment Solver has no subject-pack system of its own. Diagrams reuse the course's existing
subject pack directly — `skills/lesson-enrich/subjects/<subject>/assets/scripts/
diagram_style.py` and the pre-built `katex.inline.css` under the same `assets/` folder — keyed
off whatever subject the course's own `lesson-enrich` pack already established. Don't create a
second copy of any of this under `assignment-solver/`.
