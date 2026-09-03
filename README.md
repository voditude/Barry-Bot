# barry-the-bot

Claude Code skills for turning raw university lecture material into enriched,
interactive study documents — additive explanations, worked derivations,
diagrams, and practice questions layered on top of your own course content.

## Skills

- **`lesson-enrich`** — turns a lecture's transcript/notes, slides, and
  (optionally) problem set into one additive companion document per lecture:
  intuition, step-by-step derivations, worked examples, and diagrams, published
  as an interactive HTML artifact. Every definition, proposition, proof, and
  example from the source is kept in full — enrichment is layered on top, never
  a replacement.
- **`practice-weave`** — called by `lesson-enrich` to weave practice questions
  into a lesson from the course's real problem set: matches real questions to
  lesson sections via a concept-tag manifest, generates new questions in the
  same style where a section would otherwise have no practice, and verifies
  every generated answer by running real code before it's written down.
- **`i-dont-get-it`** — a companion skill for when one specific topic from an
  already-enriched lecture isn't landing. Produces a focused, first-principles,
  example-led standalone explainer for just that topic.
- **`transcript-slide-extract`** — called by `lesson-enrich` at ingest time when
  a lecture transcript is present. Cross-checks it against the slides and
  surfaces spoken content (asides, clarifications, extra examples) the slides
  don't contain, so `lesson-enrich` can fold it into the enriched document.
- **`assignment-solver`** — takes a dropped problem set or assignment for a
  course already ingested by `lesson-enrich`/`practice-weave` and produces a
  full worked-solution document, using only content that course actually
  taught, verified and cited back to the exact week/lecture.

See each skill's `SKILL.md` for full details, and `skills/*/reference/` for
design/quality-bar references. `samples/` has a hand-built worked example
(`week1-enriched-sample.md` / `.html`) showing what `lesson-enrich` +
`practice-weave` output looks like together, built against an invented course
so it's fully self-contained.

## Using these skills

Drop a skill folder into `~/.claude/skills/<name>/` (personal, all projects)
or `.claude/skills/<name>/` inside a project (project-scoped), then invoke it
by name in Claude Code. `lesson-enrich` and `i-dont-get-it` expect your own
course material to live under a `courses/<course-id>/` folder — see
`skills/i-dont-get-it/SKILL.md` and `skills/lesson-enrich/SKILL.md` for the
expected layout.

## License

MIT — see `LICENSE`.
