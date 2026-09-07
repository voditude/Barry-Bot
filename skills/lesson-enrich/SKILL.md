---
name: lesson-enrich
description: Use when generating an enriched study lesson from lecture material (transcript/notes, slides, and an optional problem set) for a specific university course — produces an additive companion document (intuition, worked derivations, practice questions, diagrams) layered on top of the original content, published as an interactive HTML artifact.
---

# lesson-enrich

## Overview

Turns raw lecture material for one lecture into an enriched companion document. The
document is **additive**: every definition, proposition, proof, and example from the
source is kept in full. Enrichment (intuition, step-by-step derivations, worked examples,
diagrams, woven practice questions) is layered alongside the original content, never in
place of it. Only the opening topic summary is a genuine condensation.

This skill covers structure, tone, and workflow that hold across every subject. Subject-specific
mechanics (which markup libraries to load, how diagrams get generated, what course content
looks like) live in `subjects/<subject>/PACK.md` — read the relevant one before generating
content. `subjects/math/` and `subjects/stochastic-modelling/` are full packs (see
`subjects/LIGHT-PACK-PROCESS.md` for the distinction); `subjects/economics-finance/`,
`subjects/law/`, `subjects/engineering/`, `subjects/computer-science/`, and
`subjects/marketing-management/` are light packs — read `LIGHT-PACK-PROCESS.md` once to
understand what that tier means before using one.

**Reference material** (read before first use, and whenever a rule is unclear):
- `reference/invariants.md` — the rules that never change, regardless of subject or user preference
- `reference/tone-guide.md` — the writing style rule and its forbidden-phrase list
- `reference/onboarding-survey.md` — the first-launch-per-course calibration questions
- `reference/quality-bar-sample.html` — the finished, approved reference artifact (open it in a
  browser to see the actual bar, not just read about it)
- `../transcript-slide-extract/SKILL.md` — the required sub-skill for cross-checking a dropped
  transcript against the slides (see step 4 below); only relevant when a transcript file is
  present for the lecture being enriched

## Workflow

1. **App-level onboarding (first run, once ever).** Check for `.barry-profile.md` at the repo
   root (not inside any `courses/<id>/` folder). If absent, run
   `reference/app-onboarding.md`'s conversation in full before doing anything else, then write
   the result there. If present, load it and continue — do not re-run this for a new course;
   it's app-level, not per-course (that's the existing onboarding survey in step 2 below).
2. **Onboarding (first time for a given course only).** Check for a preferences file at
   `<course-folder>/.enrich-preferences.md`. If absent, run the calibration questions in
   `reference/onboarding-survey.md`, then write the answers to that file. If present, load it
   and skip straight to step 3. See `reference/onboarding-survey.md` for exactly what may and
   may not change based on the answers — the invariants in `reference/invariants.md` never do.
   `reference/onboarding-survey.md`'s question 5 reads `.barry-profile.md`'s "Explanation
   style" line as the app-level default this course can optionally override.
3. **Identify the subject pack.** Determine the course's subject area and read
   `subjects/<subject>/PACK.md`. If no pack exists yet for that subject, say so explicitly to
   the user rather than improvising subject-specific conventions.
4. **Ingest.** If the material hasn't been placed under a `courses/<course-id>/` folder yet
   (the user handed you files directly, e.g. a slide deck and a transcript, without setting
   up any folder themselves), create that structure yourself before anything else in this
   step: infer a `<course-id>` slug from what the user has told you about the course, or ask
   directly if it's genuinely ambiguous ("what should I call this course as a folder name?"),
   then create `courses/<course-id>/source/lectures/` (and `source/problem-sets/` too, if a
   problem set was also given) per the layout in `design-enrichment.md` §3b, and copy the
   dropped files there. The user is never required to build this structure by hand first.
   Check for `<course-folder>/course-notes.md` first and follow anything it says
   about the source material's shape (e.g. a cumulative problem-set document rather than one
   file per lecture — see `practice-weave/SKILL.md` step 1 for why this matters). Pull the
   lecture's transcript/notes, slides (if present), and matching problem set for this lecture,
   per the course's manifest/naming convention (inferred per-course, not fixed — see
   `design-enrichment.md` at the project root for the resolved decision on this). Extract the
   slide section structure (section titles/headers, in order) as part of this step — it's
   needed for drafting either way, and it's also what step 4a hands to `transcript-slide-extract`
   below rather than that skill re-reading the slides itself.
   - **4a. Transcript cross-check (only if a transcript file is present for this lecture).**
     **REQUIRED SUB-SKILL:** Use `transcript-slide-extract`, passing it the slide section
     structure just extracted and the transcript file's path. It returns a manifest at
     `<course-folder>/manifests/<lecture-id>-transcript-gaps.md`. If no transcript file exists
     for this lecture, skip this sub-step entirely and proceed exactly as before — a missing
     transcript is never an error.
5. **Draft content section by section**, following the source's own structure. For each
   section: reproduce the original content in full, then add an intuition/derivation block
   per `reference/tone-guide.md`. If a `<lecture-id>-transcript-gaps.md` manifest exists for
   this lecture (step 4a), check it for this section: weave an inline fold (`.from-transcript`
   span inside the existing source box) or a standalone add-on box (`.transcript-box`) exactly
   where the manifest indicates, re-reading the raw transcript at the manifest's line/timestamp
   range for exact wording — the manifest never carries the wording itself. Do not condense or
   skip a section because it seems "obvious" or "already clear" — the one narrow exception is
   when the enrichment layer has nothing to add and says so explicitly (see the quality-bar
   sample, Section 4/"unchanged from source" pattern) — that is a judgment call about the
   *enrichment*, never license to shorten the *original* content.
6. **Diagrams and subject-specific tooling** — follow `subjects/<subject>/PACK.md` exactly
   for what tool to call and when a diagram earns its place (default bar: skip trivial
   concepts; prefer regenerating a diagram already in the source over inventing a new one).
7. **Weave practice questions.** **REQUIRED SUB-SKILL:** Use `practice-weave` to build the
   concept-tag manifest, decide what's woven vs. generated-only vs. skipped, and verify every
   generated answer by running real code. Embed the questions it returns inline at the point
   where their technique is introduced, each with a collapsible, disclaimered generated answer
   (inline flag per answer, not a banner) — `practice-weave` doesn't touch the document's HTML
   itself.
8. **Assemble, verify, and publish** as an HTML Artifact: topic summary + linked index at
   the top, then every section. If a concept doesn't land for the reader, the follow-up path
   is the separate `i-dont-get-it` skill, run on request — do not add an in-artifact Q&A
   control to the document itself. **Before publishing, run
   `python reference/scripts/check_math_html_safety.py <the-generated-file>.html` and treat
   a non-zero exit as a blocker, not a warning.** It catches two silent-failure modes that
   shipped across 8 published artifacts before this check existed: raw `<`/`>` inside a
   formula (the browser's HTML parser reads it as an unclosed tag and swallows content up to
   the next stray `>`, well before KaTeX ever runs) and a math-alphabet command
   (`\mathcal`/`\mathfrak`/`\mathscr`/...) used without its KaTeX webfont embedded (renders
   in the wrong font with zero error). Neither produces a console error or a KaTeX parse
   failure, so nothing short of this check (or a rendered screenshot) surfaces them — see the
   script's docstring for the full incident writeup if the reason isn't obvious from the
   symptom. **On failure, self-remediate before asking the user anything.** A raw `<`/`>`
   violation: escape it in the source (`\lt`/`\gt`, or `&lt;`/`&gt;`) and re-run the check. A
   missing-font violation: the check's own output names the exact fix (re-run that subject's
   `assets/scripts/build_katex_css.py --add-font <FontName>-Regular`), so run it and re-run
   the check. Only surface this to the user if remediation genuinely isn't possible (e.g. no
   network access to fetch the font from cdnjs) or the file still fails after it. After
   publishing, run `reference/feedback-loop.md`'s prompt and branch logic.

## Common mistakes

| Mistake | Fix |
|---|---|
| Summarizing a section instead of keeping it in full | Only the top-of-document topic summary is condensed. Everything else is additive. |
| Writing intuition as narrative prose with a rhetorical payoff line | Follow `reference/tone-guide.md` — state the actual derivation steps, no flourish. |
| Treating the enrichment layer's own claims as if they were the lecture's | Keep original and added content visually distinguishable throughout — see `reference/invariants.md`. |
| Re-deriving the KaTeX/diagram wiring from scratch each time | Copy the working pattern out of `reference/quality-bar-sample.html` and the subject pack's assets — they are reusable, not one-off. |
| Applying a user's stated preference to something in `reference/invariants.md` | Invariants never change per user or course. Only presentation/depth calibration (see the onboarding survey) does. |
| Writing a strict inequality in a formula as raw `a<b`/`P(X>t)` | Escape it: `a \lt b` / `\gt`, or `a &lt; b` / `&gt;`. Raw `<`/`>` in page HTML (not inside `<script>`/`<style>`) is parsed as a tag by the browser before KaTeX runs, silently eating content up to the next stray `>`. `reference/scripts/check_math_html_safety.py` catches this — run it before publishing. |
| Trusting "KaTeX parses it with no error" as proof a formula will render correctly | A formula can parse fine and still render wrong — e.g. `\mathcal{F}` renders in the browser's default font, not KaTeX's, if that font isn't embedded. Parsing correctness and HTML-delivery correctness are different questions; `check_math_html_safety.py` checks both, a syntax check alone checks neither of the two bugs actually seen in production. |
| Treating a transcript-sourced example/aside as if it were plain source or plain added-enrichment content | It's neither — use `.transcript-box` (add-on unit) or the `.from-transcript` inline marker (short aside), never the plain `.source-box`/`.add-box` styles, so the reader can tell "the lecturer said this" from both "the slides said this" and "the tool added this." |
| Running `transcript-slide-extract` even when no transcript file was dropped | Step 4a is conditional — skip it entirely and draft exactly as before when there's no transcript for this lecture. |
