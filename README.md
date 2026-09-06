<!--
This README is the public-facing setup guide for people installing Barry from GitHub.
It does not describe the local/maintainer workflow. If you're developing Barry itself,
see SESSION_HANDOFF.md, GitHub To Be Pushed.md, and design-enrichment.md instead — this
file is intentionally generic and says nothing about the master/public-release branch
split, real course content under courses/**, or anything else specific to this machine's
setup.
-->

# Barry the Bot

**Barry doesn't summarize your lectures. He sits down next to you and explains them
properly.**

Claude Code skills that turn your own lecture material into full, worked-through study
documents — every definition kept, nothing skipped, real derivations, diagrams, and practice
questions layered on top.

![License](https://img.shields.io/badge/license-MIT-green) ![Skills](https://img.shields.io/badge/skills-5-blue)

[See it](#see-it) · [Install](#install) · [Skills](#skills) · [Subjects](#subjects) · [License](#license)

---

## See it

Same concept, before and after. The lecture notes state the pigeonhole principle in one
line:

> "if m > n, at least two people get the same object"

Barry adds the buildup right where that line appears, not a rewritten version of it:

> **Why it's obviously true, before the formal statement:** if you have 5 pigeons and 4
> holes, and every pigeon must go in a hole, you cannot possibly give each pigeon its own
> hole — you only have 4. So some hole gets ≥ 2 pigeons. That's the whole idea; the "proof"
> in the notes is just restating this in the language of words over an alphabet.

*(From `samples/week1-enriched-sample.html` — a full worked sample, built the same way
`lesson-enrich` builds a real lesson from your own material.)*

The original line stays in the document, in full, either way — the explanation sits
alongside it, never in place of it. Same for diagrams and practice questions: your own
lecture's content is never condensed or replaced, only built on.

## Install

You'll need [Claude Code](https://docs.claude.com/en/docs/claude-code) already set up — these
are Claude Code skills, not a standalone app. If you don't have it yet, set that up first.

Then:

```bash
git clone https://github.com/voditude/Barry-Bot.git
cp -r Barry-Bot/skills/* ~/.claude/skills/
```

That installs Barry for every project. To scope it to a single project instead, copy into
that project's `.claude/skills/` folder rather than `~/.claude/skills/`.

**First run:** drop your own course material under a `courses/<course-id>/` folder (see
`skills/lesson-enrich/SKILL.md` for the exact expected layout), then ask Claude Code to use
the `lesson-enrich` skill on one lecture's material. The first time you do this for a given
course, Barry asks a handful of calibration questions — background level, how much
explanation you want, diagram density — and remembers your answers for every lecture in that
course after that.

## Skills

| Skill | What it does |
|---|---|
| `lesson-enrich` | Turns a lecture's transcript/notes, slides, and problem set into one additive companion document — intuition, derivations, worked examples, diagrams — published as an interactive HTML artifact. |
| `practice-weave` | Called by `lesson-enrich`. Weaves real problem-set questions into the lesson right where their technique is introduced, generates new ones where the source has none, and verifies every generated answer by running real code before it's written down. |
| `i-dont-get-it` | Stand-alone skill for when one specific topic from an already-enriched lecture still isn't landing — a focused, first-principles, example-led explainer for just that topic. |
| `transcript-slide-extract` | Called by `lesson-enrich` when a lecture transcript is present. Cross-checks it against the slides and surfaces what the lecturer said that the slides don't cover. |
| `assignment-solver` | Takes a dropped assignment for a course Barry has already ingested and produces a full worked-solution document, using only content that course actually taught, cited back to the exact week. |

See each skill's `SKILL.md` for full detail, and `skills/*/reference/` for the design and
quality-bar references behind it.

## Subjects

Barry ships with conventions for Math, Stochastic Modelling, Economics & Finance, Law,
Engineering, Computer Science, and Marketing & Management. Coverage isn't uniform: Math and
Stochastic Modelling are full packs, built and tuned against real course material; the rest
are lighter starting points that improve the more you actually use them. If your subject
isn't listed, tell Barry what you're studying — it can draft a starter pack for it on the
spot.

## License

MIT — see `LICENSE`.
