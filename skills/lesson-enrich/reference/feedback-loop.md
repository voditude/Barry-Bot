# Feedback loop (runs after every lesson-enrich / assignment-solver publish)

## Light-pack promotion offer (once per course, light-pack subjects only)

After the second real `lesson-enrich` run for a course whose subject pack is light-tier (per
`../subjects/LIGHT-PACK-PROCESS.md`), and before this run's regular feedback CTA, add: "This
is the second lesson I've built for this subject with a starter pack, not a fully-tuned one —
want me to formalize what's worked so far into a proper pack, the way the math one was built?"
Mention this at most once per course — record that it was offered (regardless of answer) in
`.enrich-preferences.md` so it never repeats.

## The prompt

Immediately after publishing an artifact, in chat (never as an in-artifact control — see
`lesson-enrich/SKILL.md` step 7's existing rule against that):

> "One more thing — how did this land? If anything felt off, tell me and I'll adjust for next
> time."

If the user doesn't respond or moves on, that's the end of it — never chase a non-response.

## Step 1: try to map the response to an existing axis

| What the user says (examples, not exhaustive) | Axis | File |
|---|---|---|
| "too long", "repetitive", "convoluted", "says the same thing twice" | Explanation depth → shorter | `.enrich-preferences.md` |
| "too simple", "I already know this", "go deeper" | Background level → ahead of course's assumed level | `.enrich-preferences.md` |
| "too advanced", "explain more from scratch" | Background level → behind course's assumed level | `.enrich-preferences.md` |
| "want more diagrams", "more visual" | Diagram density → more | `.enrich-preferences.md` |
| "too many diagrams", "just the words are fine" | Diagram density → fewer | `.enrich-preferences.md` |
| "show the full numeric answer, not just the method" | Practice-answer depth → fully worked | `.enrich-preferences.md` |
| "too formal/dry", "want more analogy", "too flowery", "too wordy" | Explanation style override (this course) | `.enrich-preferences.md` |
| Same as above, but framed as general ("you always...", "not just this course") | Explanation style (general) | `.barry-profile.md` |

If the response clearly matches one row, apply it, mention it in passing (e.g. "Noted — I'll
keep explanations tighter for this course from now on"), and log it (see "Logging" below). Do
not ask for confirmation before writing — the preference file is human-editable and visible
either way.

## Step 2: if it doesn't map cleanly, ask exactly one follow-up

Example:

> User: "this is vague"
> Barry: "Got it — can you point at roughly where? E.g. was a specific section repeating
> itself, or is it long throughout? That tells me whether to tighten depth generally or fix a
> specific pattern."

Take whatever comes back and map it per Step 1, even if it's still not perfectly specific — a
best-effort mapping beats a second follow-up round. Never ask more than one clarifying
question per piece of feedback.

## Step 3: the fundamentals path (rare — check this before defaulting to Step 1/2)

Route here instead of Step 1/2 only when the feedback explicitly asks to change something
`invariants.md` or `tone-guide.md` actually states as a fixed rule (not merely sounds
strongly worded) — e.g. "stop always giving a fresh analogy for every bijection," "you don't
need to keep every example in full," "stop disclaiming generated answers." A vague-but-strong
complaint ("this is way too formulaic") still goes through Step 1/2 first; it only reaches
here if the clarified answer turns out to name an actual fixed rule.

1. Identify the specific line in `invariants.md`/`tone-guide.md` the feedback is actually
   asking to change.
2. Tell the user plainly: "That's not a per-user setting — it's one of Barry's core rules
   [name it], the same for every course and every install by default. I can change it for
   *this* local install specifically, but that means editing Barry's own instructions, not
   just your preferences. Here's exactly what I'd change:" — then show the literal before/after
   wording diff.
3. Wait for explicit yes. Do not proceed on an ambiguous or non-committal reply.
4. If confirmed, edit the file with the smallest change that satisfies the request — never a
   wholesale rewrite of the surrounding rule.
5. Append an entry to `.barry-local-overrides.md` at the repo root (create it if absent):

```
## <date> — <file>:<line or section>
Feedback: "<verbatim or near-verbatim user feedback>"
Changed: <one-line summary of the before/after>
```

## Logging (Step 1/2 outcomes — separate from Step 3's overrides log)

Append to `<course-folder>/.feedback-log.md` (create if absent):

```
## <date>
Said: "<verbatim or near-verbatim feedback>"
Mapped to: <axis name> (<file>)
Changed: <old value> -> <new value>
```
