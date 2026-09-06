# Engineering subject pack (light tier — see ../LIGHT-PACK-PROCESS.md)

Drafted from general subject knowledge, not iterated against a real course. Written broad
enough for a general engineering course (mechanics, circuits, systems) rather than one
specific discipline — expect a specific course to need discipline-specific refinement when
this gets promoted to full tier.

## Notation

Real LaTeX via KaTeX, same wiring as `../math/PACK.md`. Density and style is close to math
(differential equations, vectors, transforms) with one addition math doesn't need: **every
physical quantity always carries its unit**, in every step of a derivation, not just the
final answer — dropping units mid-derivation is a common, specifically-engineering error
worth guarding against explicitly.

## Tooling

Matplotlib (reusing `../math/assets/scripts/diagram_style.py`) covers quantitative plots
cleanly: stress-strain curves, Bode plots, step/frequency responses, time-series signals. It
does **not** cleanly cover schematic diagrams (circuit diagrams, free-body diagrams) — those
need a different tool this project hasn't built or tested. Flag that gap honestly rather than
attempting a schematic in matplotlib and presenting it as a solved pattern.

## Worked example shape

A solved numeric problem in the classic given/find/solve/check format — reproduce the
source's own problem and solution in full, then expand any skipped algebra step, carrying
units through every line and sanity-checking the final magnitude explicitly (a real
engineering habit worth reproducing, not just deriving the number).

## Rigor / citation

Name the physical law or principle being applied the first time it's used (Newton's second
law, Kirchhoff's voltage law, conservation of energy) rather than re-deriving it from scratch
each time it recurs.
