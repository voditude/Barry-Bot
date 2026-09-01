# Concept-tag manifest

Built once per lecture, at ingest time, before any weaving decision is made. Maps every
problem-set question to the lecture's own section structure — the taxonomy is the lecture's,
never invented. Written to `<course-folder>/manifests/<lecture-id>-question-manifest.md`.

## Template

```
# <Lecture ID> concept-tag manifest — <Problem set name>

| Q | Technique tested | Lecture section |
|---|---|---|
| Q1 | ... | Section N |
...

## Woven

<which section -> which real question(s), plus what was paired with a generated question>

## Deliberately unwoven (not a gap)

<section or question -> reason, using the decision rule in SKILL.md>
```

Worked example, built against real course content (from the author's own private course
folder, not included in this repo): a `courses/<course-id>/manifests/week1-question-manifest.md`
following this same shape.

## Why "deliberately unwoven" is its own section, not just an absence

The manifest gets re-read later — including a direct question like "is this section's missing
coverage deliberate, or just an unfinished pass?" Without an explicit unwoven list with
reasons, a genuine gap and a considered skip look identical from the outside. Recording the
reason at decision time is what lets that question get answered without re-deriving the
decision from scratch.
