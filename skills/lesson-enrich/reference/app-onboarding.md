# App-level onboarding (first run, once ever per install)

Run once, the first time any of `lesson-enrich`, `assignment-solver`, or `i-dont-get-it` is
invoked and `.barry-profile.md` does not exist at the repo root. Write the result to
`.barry-profile.md` at the repo root (not inside any `courses/<id>/` folder — this applies
across every course). On every subsequent invocation of any of the three skills, load that
file instead of re-asking.

## What this calibrates

Identity (name, field of study, subjects) and one inferred explanation-style default. It
never changes anything in `invariants.md`/`tone-guide.md` — say this to the user before
starting, same framing `onboarding-survey.md` already uses for its own scope.

## Part 1 — facts (plain, open prompts, no menus)

Ask these as direct questions, in one conversational turn:

1. "What's your name?"
2. "What are you studying — your major/degree and year?"
3. "Which subject(s) will you be using Barry for?" (Free text; store as given. This list is
   also what future subject-pack work reads to know which packs matter to this install.)

## Part 1a — subject-pack coverage check

After recording the answer to Question 3, check whether each named subject matches an
existing pack under `subjects/` (math, stochastic-modelling, economics-finance, law,
engineering, computer-science, marketing-management — match loosely: "microeconomics" and
"corporate finance" both match economics-finance, "software engineering" matches
computer-science, etc.). For any named subject with no match, tell the user plainly that no
pack exists yet for it and offer to draft a light one now, following
`../subjects/LIGHT-PACK-PROCESS.md`'s on-demand drafting procedure. This is an offer, not a
blocker — the rest of onboarding (Part 2) proceeds regardless of the answer.

## Part 2 — explanation style (inferred from picking, never self-reported)

Say to the user: "Rather than ask you to describe how you like things explained — that's
genuinely hard to do in the abstract — I'll show you a couple of ways of explaining the same
everyday thing, and you tell me which one feels right."

Present **Concept 1**, then **Concept 2**, one at a time. For each, show all three variants
together and ask which feels most natural, plus the 4th option:

### Concept 1 — "What is Google?"

- **Terse/formal:** "Google is a search engine: software that indexes web pages and returns
  the most relevant ones for a query, ranked by relevance and link structure."
- **Analogy/narrative:** "Think of the internet as an enormous library with no card catalog.
  Google is the librarian who's already read every book and can point you straight to the
  right page the moment you ask a question."
- **Example-first/concrete:** "Type 'weather in Melbourne' into Google and it doesn't just
  find a page mentioning those words — it understands you want today's forecast, checks
  dozens of sources, and puts the answer right at the top. That's Google: matching what you
  actually want to what's actually out there."

### Concept 2 — "Why do we have time zones?"

- **Terse/formal:** "Earth rotates once every 24 hours, so different longitudes face the sun
  at different moments. Time zones divide the globe into roughly hourly bands so a region's
  clock stays roughly aligned with actual daylight, instead of every place on Earth sharing
  one clock that would put 'noon' at midnight somewhere."
- **Analogy/narrative:** "Imagine a giant clock painted around the Earth's equator, and the
  sun as a fixed spotlight. As the Earth spins under that spotlight, whichever number is lit
  up is roughly 'noon' there. Time zones are just agreed chunks of that painted clock, so
  nearby places share a number instead of every town needing its own."
- **Example-first/concrete:** "When it's 3pm in Melbourne, it's about 5am in London the same
  day — because London is still rotating toward the sun while Melbourne has already passed
  under it. Time zones exist so '3pm' still roughly means 'afternoon' no matter where on Earth
  you are."

### 4th option (both concepts)

"None of these — I liked parts of different ones." If picked, ask one short open follow-up:
"Which parts, from which version?" and record the answer as free prose. This is the only
point in this onboarding where an open, self-described answer is used — as a fallback for a
genuine blend, not the default path.

## Interpreting the picks

- Same variant picked for both concepts → record that style directly (e.g. "Prefers
  analogy-driven, narrative explanations").
- Different variants picked per concept → record both, tagging which concept is which:
  Concept 1 (Google) is general-knowledge/humanities-flavored, Concept 2 (time zones) is
  science-flavored. E.g. "Picked the analogy variant for the science-flavored concept (time
  zones) and the formal variant for the general-knowledge concept (Google) — leans analogy
  for science content, formal for general/humanities content." This tagging is what lets a
  later split-pick generalize to an actual course (a science-flavored course likely wants
  the style picked for Concept 2, a humanities-flavored one likely wants Concept 1's).
- 4th option used → record the user's own description of the blend verbatim.

Never collapse a split or blended pick into a single forced label — the split itself is
useful signal for later drafting.

## Writing `.barry-profile.md`

Prose, human-editable, same convention as `.enrich-preferences.md`:

```markdown
# Barry profile — <name>

- Name: <name>
- Field of study: <major/degree, year>
- Subjects using Barry for: <list>
- Explanation style: <the recorded style description from "Interpreting the picks" above>
```
