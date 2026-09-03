# Transcript-gap manifest

Built once per lecture, at ingest time, before `lesson-enrich` starts drafting. Maps every
slide section to the matching stretch of the transcript and records what (if anything) the
transcript adds beyond the slides. Written to
`<course-folder>/manifests/<lecture-id>-transcript-gaps.md`.

Every row is a **pointer**, never a quote: a transcript line range (or timestamp range, when
the transcript has timestamps) and a one-line paraphrase. The manifest is an index back into
the real transcript file, not a second copy of it — `lesson-enrich` re-reads the raw transcript
at the given range to get exact wording when it drafts. This is the same pattern
`practice-weave`'s `concept-tag-manifest.md` uses for problem-set questions (tag rows pointing
at the real file, never the full question text), applied here to keep the manifest small
regardless of how long or verbose the transcript is.

## Template

```
# <Lecture ID> transcript-gap manifest — <transcript file name>

| Section | Transcript ref | Outcome |
|---|---|---|
| Section 1 | lines 1-40 (~0:00-3:10) | Matched, no gap |
| Section 2 | lines 41-95 (~3:10-7:40) | Inline fold — see below |
| Section 3 | lines 96-110 (~7:40-9:05) | Add-on box — see below |
...

## Inline folds

| Section | Transcript ref | Paraphrase |
|---|---|---|
| Section 2 | lines 60-63 (~4:50-5:20) | ... |

## Add-on boxes

| Section | Transcript ref | Paraphrase |
|---|---|---|
| Section 3 | lines 96-110 (~7:40-9:05) | ... |

## Order jumps

<Transcript ref -> what happened -> which section it actually matched -> where alignment
resumed. Empty if the transcript followed slide order throughout.>

## Deliberately not surfaced

<Section or transcript stretch -> reason. E.g. "restates slide content near-verbatim, no
independent value" or "off-topic aside (housekeeping, Q&A logistics), not lecture content.">
```

Worked example: not yet built — the first course this skill runs against should have its
manifest kept as the reference worked example here, the same way
`practice-weave`'s `week1-question-manifest.md` became its own worked-example pointer.

## Why every section is logged, not just the gaps

The manifest gets re-read later, including a direct question like "was this section's missing
transcript coverage a real gap, or just never checked?" Without an explicit "matched, no gap"
row for every section, a genuine gap and an unevaluated section look identical from the
outside. This mirrors `practice-weave`'s own reasoning for its "Deliberately unwoven" section:
a gap never evaluated is a bug, a gap evaluated and judged not worth surfacing is a design
decision — only a fully logged manifest tells them apart.
