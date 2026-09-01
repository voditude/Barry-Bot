# Verifying generated answers

A generated question's answer is never written down on assertion — it's computed, then
checked by an independent method, and only written down once both agree. This is what caught
a real arithmetic slip during the week1 v1 pass (536,824 by hand vs. 436,800 from verified
code).

## Lane 1 — computational (proven, default)

For any question with a closed-form numeric/symbolic answer:

1. Compute the closed form (sympy for symbolic work: `binomial`, `factorial`, `simplify`).
2. Independently brute-force count/enumerate a *small* analogue of the same question
   (`itertools.product`/`combinations`/`permutations` over a reduced size or alphabet).
3. Assert the two agree. Only write the answer down after the assertion passes.

Worked pattern (7 questions verified this way):
`samples/practice-weave-verify-week1.py`.

## Lane 2 — proof-based (structured self-check + small-n spot-check; not yet exercised against real content)

For a question whose answer is a proof or argument rather than a number, brute-force
enumeration doesn't directly apply. Proposed approach, flagged as unproven:

- **Structured self-check**: write the proof as an explicit numbered step list, checking each
  step doesn't assume the conclusion or silently skip a case.
- **Small-n spot-check**: where the proof claims a property for general `n`, verify it holds
  by direct computation/enumeration for a few small concrete values of `n`.

This lane is expected to matter starting with posets (weeks 2+ of MAST30012, per
`handoff.md`). Treat it as provisional until it's been run against a real proof-based
question and shown to catch a real error the way Lane 1 did — don't present it with the same
confidence as Lane 1 until then.
