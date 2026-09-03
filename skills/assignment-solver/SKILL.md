---
name: assignment-solver
description: Use when the user drops a problem set or assignment (PDF, occasionally an image) for a course whose lecture material has already been at least partly ingested — matches each problem to the technique actually taught in that course, works through a full step-by-step worked solution using only course-scoped content (flagging the rare exception inline), verifies every computed answer, cites back to the exact week/lecture, and publishes the finished solutions as an HTML artifact. If the drop looks like an assignment/problem set but wasn't paired with an explicit request to solve it, confirm with the user before running rather than triggering silently.
---

# assignment-solver

## Overview

Takes a problem set or assignment for one course and produces a full worked-solution
document — a model answer key, not a scaffold that withholds steps. The defining constraint
is scope: every solution uses only what the course itself taught (or expects as prerequisite
knowledge), never a different valid method the course didn't cover, and never outside content
without saying so.

This skill sits downstream of `lesson-enrich` and `practice-weave` — it reads their output
rather than re-deriving course content from scratch, and it never invokes either of them to
generate anything on the fly (see `reference/source-priority.md` for what happens when their
output is missing for a given week). It shares `lesson-enrich`'s document conventions (KaTeX
rendering, box styles, build pipeline) rather than maintaining a second copy of any of it.

**Reference material** (read before first use, and whenever a rule is unclear):
- `reference/source-priority.md` — which source to check first for a given week's content,
  and the fallback chain when the preferred source is missing
- `reference/scope-and-citation.md` — the hard boundary on what content is allowed, the
  general-knowledge judgment call, the multiple-taught-methods rule, and the exact citation
  format
- `../practice-weave/reference/verification.md` — the two verification lanes (computational,
  proof-based) to reuse directly; don't fork a separate copy
- `../lesson-enrich/reference/scripts/check_math_html_safety.py` — the mandatory pre-publish
  gate (see step 9)
- `../lesson-enrich/subjects/<subject>/` — the course's existing subject pack: diagram
  tooling and pre-built KaTeX CSS, reused as-is

## Workflow

1. **Identify the course and confirm.** Auto-detect which `courses/<course-id>/` folder the
   dropped file belongs to, by matching its filename and content against existing course
   folders. State the guess and wait for the user to confirm before proceeding — never solve
   against a guessed course without confirmation. If nothing matches, or the drop wasn't
   accompanied by an explicit request, ask directly rather than assuming ("This looks like an
   assignment for `<course-id>` — want me to run Assignment Solver on it?").
2. **Check for onboarding calibration.** Look for `<course-folder>/.enrich-preferences.md`
   (written by `lesson-enrich`'s onboarding). If present, read it and match its tone/depth
   calibration in the write-up — the student is moving between lecture notes and solutions in
   one course, and a jarring voice shift between them is worse than reusing the existing
   calibration. If absent, proceed with a plain, direct default voice; don't run onboarding
   yourself, that's `lesson-enrich`'s job.
3. **Check the precondition, then ingest the problem set/assignment.** Confirm the course
   folder has *some* ingested material already (`reference/source-priority.md`'s precondition
   check) — if not, stop and tell the user to run `lesson-enrich` first. Otherwise, read the
   *entire* content of the dropped file(s) in full — never infer scope from the filename alone,
   the same rule `practice-weave` follows for problem-set files. Use the Read tool's native PDF
   support (text extraction + rendered page images) for PDFs; for math-heavy problems, cross-
   reference the extracted text against the rendered page image by hand, since PDF math-mode
   text extracts with layout artifacts (e.g. `P(\Ti j=0 Aj)` for $\bigcap_{j=0}^i A_j$) and no
   OCR/math-parsing tool exists in this repo. Derive a short slug for this assignment from its
   own name/number (lowercase, no spaces — e.g. `assignment1`, `tute4`), used for every file
   this skill creates.
4. **Gather source content per problem, in priority order.** Follow
   `reference/source-priority.md` exactly: the relevant week's LessonEnrich artifact first,
   then its PracticeWeave manifest for cross-checking, then raw lecture source only as a
   fallback for that week. Don't skip straight to raw source when an enriched artifact exists
   for that week — it's both more concise and already vetted.
5. **Match each problem to its taught technique(s).** Using the gathered content, identify
   which course-taught method applies. Apply `reference/scope-and-citation.md` in full: the
   hard boundary, the two narrow exceptions (matches lecture material after a closer look, or
   is expected prerequisite knowledge), the inline flag for anything else, and the
   single-most-efficient-method rule when the course itself teaches more than one approach to
   the same problem type.
6. **Draft the full worked solution per problem.** Follow the box/layout conventions already
   established in this project's math documents: `.source-box` quoting the problem as set
   verbatim, `.add-box` units for each stage of the solution (labeled by role — setup,
   derivation, etc.), inline `.step`/`.step-label` for individual steps, `.result` for the
   final answer, `.pitfall` for a common-mistake call-out where one is worth flagging. Cite
   using the exact format in `reference/scope-and-citation.md` immediately after each
   technique is used. Never withhold the final answer or a key step.
7. **Verify every computed answer before writing it down.** Reuse
   `practice-weave/reference/verification.md`'s two lanes directly — computational
   (closed-form vs. independent brute-force/enumeration check) and proof-based (structured
   self-check + small-n spot-check). Keep verification lightweight: prefer a known identity or
   analytical cross-check over brute force wherever one exists; when brute-force spot-checking
   is the only option, bound it small (roughly n≤4–6, matching the bounds already used in this
   project's own verify scripts) and never scale it up "to be thorough" — that just burns
   tokens without adding confidence past what a small case already gives you. Write the
   verification as a real, run script at
   `courses/<course-id>/assignments/<assignment-slug>-verify.py`, following the existing
   `assignmentN-verify.py` pattern in this repo (sympy for symbolic work, an
   `ok = lambda label, a, b: print(PASS/FAIL, a == b)`-style helper, one check per computed
   result). Run it and confirm every check passes before drafting the answer into the document.
8. **Diagrams, only where one earns its place.** If a solution benefits from a diagram, reuse
   the course's existing subject pack's `diagram_style.py` (under
   `skills/lesson-enrich/subjects/<subject>/assets/scripts/`) rather than styling one from
   scratch. Save generated images to `courses/<course-id>/assets/<assignment-slug>/`, and
   reference them in the body fragment with an `{{IMG:relative/path.png}}` placeholder — real
   tool calls only, never a described visual.
9. **Assemble, verify, and publish.** If `courses/<course-id>/build_artifact.py` doesn't
   exist yet, find any other course folder under `courses/` that already has one and copy it
   in verbatim — it's a generic, per-course copy of the same assembly script, not something to
   rewrite from scratch, and not tied to any particular course. If no course folder anywhere
   in the project has one yet, that's a project-level gap to flag to the user rather than
   something to invent from scratch. Write the
   solutions as a body-only HTML fragment (no `<head>`/`<html>` wrapper), then run it with
   `BARRY_HEAD`/`BARRY_TAIL` set explicitly to the project-root `.build/head.html`/
   `.build/tail.html` — **don't rely on the script's own default path computation, which
   climbs 4 directory levels from a `courses/<course-id>/` script and overshoots the actual
   project root by 2**:
   ```
   BARRY_HEAD=.build/head.html BARRY_TAIL=.build/tail.html \
     python courses/<course-id>/build_artifact.py <title> <body_fragment_path> \
     courses/<course-id>/artifacts/<assignment-slug>.html
   ```
   (run from the project root, or adjust the two paths to be absolute/correctly relative if
   not). This splices in the KaTeX wiring and replaces every `{{IMG:...}}` placeholder with a
   base64 `data:` URI. **Before
   treating the file as finished, run
   `python skills/lesson-enrich/reference/scripts/check_math_html_safety.py <the-generated-file>.html`
   and treat a non-zero exit as a blocker, not a warning** — it catches raw `<`/`>` inside a
   formula and an unembedded math-alphabet font, neither of which shows up as a KaTeX parse
   error (see `lesson-enrich/SKILL.md` step 7 for the full incident history). Once it passes,
   the file at `courses/<course-id>/artifacts/<assignment-slug>.html` is the persisted
   deliverable — also publish it as a live Claude Artifact in the same turn, so the student
   gets working KaTeX rendering immediately without opening a local file.

## Common mistakes

| Mistake | Fix |
|---|---|
| Presenting a valid method the course happens to support, instead of the one it actually taught | Match to the taught technique specifically — see `reference/scope-and-citation.md`. A mathematically valid alternative the course didn't cover is still out of scope. |
| Flagging a foundational/prerequisite technique as "general knowledge" | Don't — see the two exceptions in `reference/scope-and-citation.md`. Flagging expected prerequisite knowledge misleads the student about what's fair game to cite. |
| Presenting every course-taught method when more than one exists | Pick the single most efficient, best-practice one and write that up — not a survey of options. |
| Withholding the final answer or a key step "for the student to work out" | This is a model answer key, not a Socratic scaffold — every step and the final answer are always included. |
| Reading raw lecture source first, when an enriched artifact already exists for that week | Check `courses/<course-id>/artifacts/week<N>-enriched.html` first — it's more concise and already vetted. Raw source is a fallback, not the default. |
| Blocking the whole assignment because one week's manifest/artifact is missing | Fall back to raw source for that week only — a missing manifest is a shortcut lost, not a hard dependency (see `reference/source-priority.md`). |
| Treating an entirely empty, un-ingested course folder the same as a missing week | That's a precondition failure — tell the user to run `lesson-enrich` first rather than solving from outside knowledge. |
| Verifying with a large brute-force search "to be extra sure" | Keep verification bounded (n≤4–6 style) and prefer known identities. A larger brute force doesn't add confidence past what the small case already proves, and burns the user's tokens. |
| Solving against a guessed course without the user confirming it | Always state the auto-detected course and wait for confirmation before drafting anything. |
| Rebuilding a per-section "Ask about this section" control into the output | That control was retired project-wide (see `design-enrichment.md` §6) — the current `.build/head.html`/`.build/tail.html` no longer carry its wiring. Don't hand-roll a replacement; point the student at the separate `i-dont-get-it` skill instead if a concept doesn't land. |
| Asserting a computed answer without running the verification script | Every computed answer is verified by an independently-run check before it's written into the document — see step 7. |
