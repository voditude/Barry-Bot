# Computer Science subject pack (light tier — see ../LIGHT-PACK-PROCESS.md)

Drafted from general subject knowledge, not iterated against a real course.

## Notation

Two notation systems, both real, never approximated: LaTeX via KaTeX (reusing math's wiring)
for formal content — Big-O/complexity notation, recurrence relations, automata/grammar
definitions — and real, syntax-appropriate **code blocks** in whatever language the course
teaches, for algorithm listings. Code blocks are a content type none of the other packs have;
keep them visually distinct from both source-content and added-enrichment boxes, the same way
`invariants.md` already requires for transcript-sourced content, since a code listing is a
third kind of thing (executable, checkable) distinct from prose derivation.

## Tooling

Matplotlib (reusing `diagram_style.py`) covers performance/complexity graphs cleanly. It does
**not** cleanly cover the field's other common diagram need — trees, graphs, automata/state
diagrams — which need a proper graph-drawing tool (e.g. `networkx` plus matplotlib, or
graphviz) this project hasn't built or tested yet. Flag that gap honestly, same as
engineering's schematic gap. Where a generated code example's *output* matters, run the code
for real and show actual output — never assert what a program prints, the same
verify-by-running principle `practice-weave` already applies to generated answers.

## Worked example shape

Trace an algorithm step-by-step on one concrete small input, showing the full intermediate
state at each step — this is the direct CS analogue of `invariants.md`'s existing "small-case
enumeration for every introduced bijection" rule, not a new invention. Where the source gives
pseudocode, a runnable version in the course's actual language, executed for real, is the
"generated, verified" analogue of `practice-weave`'s answer-verification rule.

## Rigor / citation

Name the algorithm, data structure, or theorem being applied the first time it appears (e.g.
"this is Dijkstra's algorithm," "this follows from the master theorem") rather than
re-deriving it from scratch each time it recurs.
