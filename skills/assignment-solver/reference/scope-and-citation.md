# Scope, provenance, and citation rules

## The hard boundary

Course-taught content is the ceiling for how a problem gets solved — never reach past it
except in the two narrow cases below. "Course-taught" means: covered in the LessonEnrich
artifact for the relevant week, covered in the linked section of a PracticeWeave manifest, or
found directly in the raw lecture source under `source/lectures/` (see
`reference/source-priority.md` for which of these to check, and in what order).

## When outside content is allowed

1. **It matches lecture material specifically.** Look again before concluding a technique
   isn't covered — a differently-named or differently-notated version of the same idea still
   counts as covered. This is a re-check, not an excuse to broaden scope.
2. **It's foundational/expected prerequisite knowledge for the course's own level.** A
   formulaic, well-known technique the lecturer assumes without re-teaching — e.g. a
   closed-form summation identity assumed at 3rd-year level. This case is never flagged:
   flagging it would wrongly suggest to the student that it's off-limits to cite, when the
   opposite is true.

Anything else that isn't covered still gets solved — never refuse a problem — but flagged
inline, directly before the content it applies to, using this exact lead-in:

```
**Not covered in the lectures — general knowledge:** <the technique/explanation>
```

This is a judgment call, not a fixed rule, and the two cases above are genuinely ambiguous at
the edges. Default toward *not* flagging prerequisite-level material a student at this course
level is expected to already have; *do* flag anything that reads like a technique from a
different or later course, or a specialized trick the lecture material never gestures toward.

## Multiple taught methods for the same problem type

If the course material itself teaches more than one method for the same kind of problem (e.g.
two different lectures show two approaches), use judgment and write up the single most
efficient, best-practice one. Don't present both — the goal is a clean model solution, not a
survey of options. Expected to be rare in practice.

## Citation format

Cite inline, parenthetically, immediately after the technique is used — sourced from
whichever source material was actually read (the LessonEnrich artifact's own numbering, or
the raw lecture's numbering), never invented and never copied from a PracticeWeave manifest's
section labels (those are the manifest's own index, not citation-ready numbering):

- `(Week 3, Theorem 3.1.2)` — when the source has a numbered result to point to
- `(Week 4, §4.3)` — when there's no numbered result, just a section

## Full worked solutions, never withheld

Every problem gets a complete, step-by-step worked solution with the final answer included —
this is a model answer key, not a Socratic scaffold. Don't hold back a final answer or a key
step "for the student to figure out."
