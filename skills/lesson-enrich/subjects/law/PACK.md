# Law subject pack (light tier — see ../LIGHT-PACK-PROCESS.md)

Drafted from general subject knowledge, not iterated against a real course. Law's shape
differs from every other pack more than any two of the others differ from each other — no
math notation by default, no matplotlib diagrams by default, a completely different unit of
"worked example."

## Notation

No math/LaTeX notation by default (occasional statistics in a law-and-economics elective is
the exception, not the norm — treat that as economics-finance content when it appears). The
real notation convention here is **legal citation** — case names, statute references. Citation
style (AGLC, Bluebook, OSCOLA, etc.) is genuinely jurisdiction- and institution-specific:
confirm which one the course actually uses rather than defaulting to one, and record the
answer in the course's `.enrich-preferences.md` once confirmed rather than re-asking.

## Tooling

Diagrams are rare and, when used, are flowcharts/decision trees (e.g. "does this fact pattern
satisfy element X of the test") rather than data plots — this doesn't fit the matplotlib
line/bar-chart pipeline the way economics-finance's diagrams do. No tested tooling exists for
this yet; flag that honestly rather than forcing a matplotlib flowchart that wasn't designed
for it. Resolving this is real scope for whoever promotes this pack to full tier.

## Worked example shape

Not a numeric problem — an IRAC-style analysis (Issue, Rule, Application, Conclusion) applied
to a hypothetical fact pattern. State the legal test's elements once, in full, the first time
it's introduced (the direct analogue of `tone-guide.md`'s proof-skeleton pattern), then apply
each element explicitly to the hypothetical rather than asserting the conclusion.

## Rigor / citation

Every stated rule or test must trace to its source case or statute — cite it. This is the
field's version of "additive, not condensed": the source case's actual holding stays
reproduced in full, enrichment builds the application around it.

## Tone exception, stated explicitly

Legal writing conventionally hedges ("it is arguable that," "on balance, a court would likely
find...") where the hedge reflects genuine doctrinal uncertainty, not filler. This looks like
exactly what `tone-guide.md` forbids ("hedges used for rhythm rather than meaning") but isn't
the same thing — a hedge that names a real, substantive uncertainty about how a rule applies
is content, not rhythm. Treat `tone-guide.md`'s hedge rule as still binding for hedges that
add nothing; this is a narrow, named exception for hedges that state a genuine open question.
