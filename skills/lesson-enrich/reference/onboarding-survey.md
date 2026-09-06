# Onboarding survey (first launch per course)

Run once per course, the first time `lesson-enrich` is used for it — not once per lecture.
Store the answers at `<course-folder>/.enrich-preferences.md` and load them on every
subsequent run for that course instead of re-asking. If the user later says their level or
preferences changed, re-run this and overwrite the file.

## What this calibrates

Only presentation and depth. It never changes anything in `invariants.md` — always LaTeX for
math notation, always the full source content kept in full, always inline practice weave,
always disclaimered answers. Say this to the user before asking, so they understand what is
and isn't being tailored.

## Questions to ask (via AskUserQuestion or equivalent)

1. **Background level for this course**, relative to the course's own assumed level (not an
   absolute scale — "3rd-year" means nothing without knowing the course is 3rd-year):
   - At the course's own assumed level
   - Behind the course's assumed level — explain more from first principles even for things
     the course itself doesn't flag as new
   - Ahead of the course's assumed level — keep explanations tighter, spend less space on
     material the user says they already have solid

2. **Explanation depth preference** for the added intuition/derivation boxes:
   - Full derivations every time (default — matches the invariant bar)
   - Full derivations, but shorter — key steps only, skip restating what's already obvious
     from the previous step
   (Do not offer a "no derivation, just the intuition" option — that would violate the
   always-show-the-mechanism rule in `tone-guide.md`. If the user asks for that anyway, say
   explicitly that it conflicts with the invariant and confirm they want to override it
   knowingly before doing so.)

3. **Diagram density**, where the subject pack supports diagrams:
   - Default bar (only where source has one, or where a concept genuinely needs a visual)
   - More diagrams — lower the bar for what counts as "needing" one
   - Fewer diagrams — text/derivation only unless something is genuinely hard to describe in
     words

4. **Practice question depth**: whether generated answers to woven practice questions should
   include just the final method/formula (as in the quality-bar sample) or a fully worked
   numeric solution where the source problem allows one.

5. **Explanation style for this course specifically**, versus your general default (loaded
   from `.barry-profile.md`: "<the recorded style line>"):
   - Use my general default
   - Different for this course — describe how (e.g. "more formal/terse than my usual style"
     or "more analogy-driven than my usual style")

   This exists because a style pick made against everyday examples (Google, time zones) may
   not be the pick you'd make for every course — a humanities elective and a STEM major might
   reasonably want different registers even from the same person.

## Storing the result

Write `<course-folder>/.enrich-preferences.md` with the five answers in plain prose (not
JSON — this file is meant to be human-readable and hand-editable by the user directly if
their preference changes). Example:

```markdown
# Enrichment preferences — <course-id>

- Background: at the course's own assumed level
- Explanation depth: full derivations every time
- Diagrams: default bar
- Practice answers: method/formula only, not fully worked numerically
- Explanation style for this course: use general default
```
