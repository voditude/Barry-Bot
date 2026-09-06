# Tone guide

Direct, logical, professional. The goal is comprehension, not prose. This applies to every
intuition/derivation box in a generated lesson.

## The rule

State the actual reasoning steps explicitly. Do not skip from a claim to its conclusion
without showing the mechanism that connects them. If a statement can be replaced by "trust
me" without losing information, it is filler — cut it or replace it with the missing step.

## Forbidden

- Filler intensifiers/hedges used for rhythm rather than meaning: "simply", "just",
  "precisely", "clearly", "obviously" (when used to wave past a step rather than as a real
  claim about triviality — see the pigeonhole first-principles pattern below for the
  legitimate use).
- Rhetorical payoff lines that assert a feeling instead of a fact: "feels inevitable rather
  than surprising", "which is exactly what makes this click", "beautifully ties together".
  If the sentence's only content is how the reader should feel about the material, delete it
  or replace it with the fact that should produce that feeling.
- Pleasantries and encouragement: "great question", "let's dive in", "don't worry, this gets
  easier". None of this belongs in study material.
- Restating the conclusion in different words as if it were a new sentence.

## Required

- When a derivation has steps, show them in order, each following from the last. Compare:

  **Bad** (asserts, doesn't derive): "The multiplication principle works because the choices
  are independent, which is precisely why we get $|A||B|$."

  **Good** (derives): "Fix any $a \in A$. Pairing it with each element of $B$ gives $|B|$
  pairs. There are $|A|$ choices for $a$, and the pairs from different values of $a$ are
  distinct (they differ in the first coordinate). So the total is $|A|$ groups of $|B|$
  pairs: $|A| \cdot |B|$."

- For a concept flagged as newly introduced (first-principles treatment, per
  `invariants.md`): give a concrete instance before the general statement, then connect the
  instance to the formal claim explicitly, then give the general argument (e.g. proof by
  contradiction) in full — not "obviously true" as a substitute for the argument.
- Bold is fine for key terms; keep it sparse. Lists are fine when the content is actually a
  list (steps, cases), not as a formatting device for prose.

## Techniques that measurably help (from live tutoring transcript analysis, 2026-08-31)

These were extracted by comparing a real back-and-forth tutoring session against which parts
of the answers actually got the student unstuck, versus which parts they skimmed past or
asked to have re-explained. Apply them inside intuition/derivation boxes, on top of the
"Required" rules above — they are about what to include and how to sequence it, not a
replacement for the direct/no-filler rule.

- **Show it's the same object in two notations, not a coincidence.** When a bijection exists
  because both sides encode identical information (e.g. a subset of $\{1,\ldots,n\}$ and its
  length-$n$ indicator string), say so explicitly — these are the same object, written two
  ways — rather than presenting the correspondence as a clever trick that happens to
  preserve size. This is what makes injectivity/surjectivity feel automatic instead of
  something to take on faith.

  **Bad**: "There is a natural bijection between words with $m$ zeros and $m$-subsets of
  positions."
  **Good**: "A word with $m$ zeros and the set of its zero-positions are the same
  information, written two ways: from either one you can write down the other without any
  choice being made. That's why the map can't collide (different words differ somewhere, so
  their position-sets differ) or miss anything (every $m$-subset came from writing zeros
  there)."

- **Name recurring proof methods once, as a reusable skeleton.** The first time a technique
  like "prove $\Phi$ is a bijection" appears, state it as an explicit, numbered, general
  procedure — state $A,B$ precisely, define the map, check it's well-defined, prove
  injective+surjective (or exhibit an inverse and check both round-trips), conclude
  $|A|=|B|$, compute the known side — once, and reference it by name in later sections
  ("apply the bijection-proof skeleton from Section X") instead of re-deriving the method
  from scratch every time it recurs.

- **Point at the exact step a hypothesis is protecting.** When a proposition's condition
  (e.g. "each part positive," "the map must be both injective and surjective, not just one")
  isn't obviously necessary, show which specific proof step breaks if it's dropped, rather
  than only asserting the condition is required.

- **Chain explicitly to prior results — never silently.** When a formula or count is really
  an earlier result applied to a transformed object (e.g. "distributing $m$ items among $n$
  categories" is the same $\binom{n}{m}$ count as choosing zero-positions, applied to a
  longer string), say so in one sentence, naming the section or week it came from. Do not
  present it as an independent new fact — the reader should be able to see the whole
  document's spine, i.e. which techniques reduce to which.

- **Preempt confusion about reused generic notation.** The first time a placeholder symbol
  that will be redefined per example ($\Phi$ for "the map in this proof," $\Psi$ for its
  inverse) is introduced, say explicitly that it is a conventional label redefined fresh each
  time, not one fixed function carried across sections. This specific confusion was observed
  live in a tutoring session and is prevented by one sentence.

**Write in the document's own voice, not as a narrator describing the document.** A
slide-derived derivation or definition should read as direct explanatory prose. Never use
"[the/this] source/notes/lecture says/states/labels/mentions" as a lead-in for content the
reader can already see is sourced from context (the box style, the label) — reserve
lecturer-voice attribution only for genuine transcript quotes, per `invariants.md`.

## Quick check before publishing a box

Read the box and ask: if I removed every sentence that doesn't add a fact, definition, or
derivation step, would the box get shorter? If yes, it had filler — remove it. Also ask: does
this sentence narrate the source's *act of saying* something, rather than stating the thing
itself? If yes, rewrite it as direct prose.

## Whole-document redundancy pass

After drafting every section, do one dedicated re-read pass across the **entire document**
hunting for: (a) two boxes making the same point about the same concept in different words,
even in different sections; (b) a self-check that restates a box's conclusion instead of
giving a genuinely new instance; (c) the topic summary re-explaining, in full, something the
first section is about to explain again immediately. Apply the existing "would removing this
sentence make the box shorter without losing a fact?" question literally, sentence-by-sentence,
not impressionistically — cut every sentence that fails it.
