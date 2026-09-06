# Light subject packs — process and confidence tier

Every subject pack in this project is one of two tiers:

- **Full** (currently: `math/`, `stochastic-modelling/`) — built by generating a real worked
  sample against a real course's real material, iterating on quality with the user, then
  extracting the resolved decisions into `PACK.md`. Every convention in a full pack has been
  checked against actual output.
- **Light** (this file's process — `economics-finance/`, `law/`, `engineering/`,
  `computer-science/`, `marketing-management/`) — drafted directly from general subject
  knowledge, with no real course material and no iteration. Every light pack states this
  plainly at its own top. Treat its conventions as a reasonable starting point, not a
  verified quality bar — expect some to need correcting once real material is actually run
  through them.

## Promotion: light → full

After a light-pack subject's course has had two real `lesson-enrich` runs, the feedback loop
(`../feedback-loop.md`) offers to formalize what's worked into a full pack, the same way math
was built — extracting the actually-used conventions from those two real runs rather than
redrafting from scratch. This is an offer, never automatic — the user decides whether it's
worth doing.

## Drafting a light pack on demand (for a subject not already covered)

When a user names a subject with no existing pack (via the app-level onboarding's
subject-coverage check, or any other point this comes up), draft one using this same process:
say explicitly that no pack exists yet, offer to draft a light one now, and if agreed, produce
a `PACK.md` covering at minimum: notation conventions (does the field use real math notation,
a different symbolic system, or none), diagram/tooling conventions (and an honest note if
nothing in this project's existing tooling actually fits), what a "worked example" looks like
in this field (a solved problem, an applied framework, a legal analysis, a traced algorithm —
fields differ substantially here), and rigor/citation conventions (how a named result, test,
framework, or algorithm gets attributed rather than re-derived from scratch every time it
recurs — the same pattern `tone-guide.md` already uses for proof skeletons, generalized).

## Resolving a diagram-tooling gap (install-with-confirmation)

Several light packs below flag a real diagram need with no tested tool in this project yet
(a flowchart, a circuit schematic, a tree/graph diagram, a framework matrix). When
`lesson-enrich` actually hits one of these in real use, resolve it like this rather than
leaving it stuck or inventing an untested pattern silently:

1. **Barry picks the specific tool** — this is a technical judgment call, not a preference to
   ask the user about (the same reasoning `App Onboarding Plan.md` used to keep style
   preference out of open self-report: most users can't usefully choose between `graphviz`
   and `networkx` for a state diagram, but Barry can reason about which fits).
2. **Get a one-time confirmation before installing anything new** — e.g. "This needs a circuit
   diagram; I'd install `schemdraw` to draw it. OK to proceed?" Installing a new dependency is
   a real environment change (network access, potential conflicts, a permanent addition to the
   machine) — a different risk tier from calling already-installed matplotlib, closer to the
   feedback loop's core-file-edit confirmation tier than to a normal content decision.
3. **Remember the answer.** Record the approved tool in the course's `.enrich-preferences.md`
   (e.g. `diagram tool for schematics: schemdraw, approved <date>`) so this never re-prompts
   for the same tool on the same machine.
