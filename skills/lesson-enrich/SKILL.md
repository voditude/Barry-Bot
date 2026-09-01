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
content. Only `subjects/math/PACK.md` is built; `subjects/economics/` and
`subjects/finance/` are stubs (see their `NOTES.md`) until scoped the same way math was.

**Reference material** (read before first use, and whenever a rule is unclear):
- `reference/invariants.md` — the rules that never change, regardless of subject or user preference
- `reference/tone-guide.md` — the writing style rule and its forbidden-phrase list
- `reference/onboarding-survey.md` — the first-launch-per-course calibration questions
- `reference/quality-bar-sample.html` — the finished, approved reference artifact (open it in a
  browser to see the actual bar, not just read about it)

## Workflow

1. **Onboarding (first time for a given course only).** Check for a preferences file at
   `<course-folder>/.enrich-preferences.md`. If absent, run the calibration questions in
   `reference/onboarding-survey.md`, then write the answers to that file. If present, load it
   and skip straight to step 2. See `reference/onboarding-survey.md` for exactly what may and
   may not change based on the answers — the invariants in `reference/invariants.md` never do.
2. **Identify the subject pack.** Determine the course's subject area and read
   `subjects/<subject>/PACK.md`. If no pack exists yet for that subject, say so explicitly to
   the user rather than improvising subject-specific conventions.
3. **Ingest.** Check for `<course-folder>/course-notes.md` first and follow anything it says
   about the source material's shape (e.g. a cumulative problem-set document rather than one
   file per lecture — see `practice-weave/SKILL.md` step 1 for why this matters). Pull the
   lecture's transcript/notes, slides (if present), and matching problem set for this lecture,
   per the course's manifest/naming convention (inferred per-course, not fixed — see
   `design-enrichment.md` at the project root for the resolved decision on this).
4. **Draft content section by section**, following the source's own structure. For each
   section: reproduce the original content in full, then add an intuition/derivation block
   per `reference/tone-guide.md`. Do not condense or skip a section because it seems
   "obvious" or "already clear" — the one narrow exception is when the enrichment layer has
   nothing to add and says so explicitly (see the quality-bar sample, Section 4/"unchanged from
   source" pattern) — that is a judgment call about the *enrichment*, never license to shorten
   the *original* content.
5. **Diagrams and subject-specific tooling** — follow `subjects/<subject>/PACK.md` exactly
   for what tool to call and when a diagram earns its place (default bar: skip trivial
   concepts; prefer regenerating a diagram already in the source over inventing a new one).
6. **Weave practice questions.** **REQUIRED SUB-SKILL:** Use `practice-weave` to build the
   concept-tag manifest, decide what's woven vs. generated-only vs. skipped, and verify every
   generated answer by running real code. Embed the questions it returns inline at the point
   where their technique is introduced, each with a collapsible, disclaimered generated answer
   (inline flag per answer, not a banner) — `practice-weave` doesn't touch the document's HTML
   itself.
7. **Assemble, verify, and publish** as an HTML Artifact: topic summary + linked index at
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
   symptom.

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
