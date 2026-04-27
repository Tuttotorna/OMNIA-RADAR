# OMNIA-RADAR · Pure Structure Scan v3B

## Status

PASS

---

## Objective

Test OMNIA-RADAR as a pure structural scanner.

This test does NOT evaluate:

- meaning
- truth
- quality
- semantic coherence
- usefulness

It evaluates only:

```text
detectable structural intensity


---

Core Principle

structure != meaning
structure != quality
structure != coherence

OMNIA-RADAR asks only:

is there measurable structure here?


---

Dataset

Four categories were generated:

A — Random Noise

Random token sequences.

Expected:

lowest structure


---

B — Corrupted-Like Text

Human-like text with:

shuffled blocks

random token corruption

partial surface damage


Expected:

more structure than pure noise
less structure than intact text


---

C — Human-Like Text

Coherent real-like sentences sampled from a controlled pool.

Expected:

moderate natural structure


---

D — Degraded-Like Text

Human-like text with:

repetition loops

repeated fragments

mechanical pattern reinforcement


Expected:

high structural intensity

Important:

high structure does NOT mean high quality


---

Metrics

RADAR score combines structural indicators:

compression ratio

token entropy

character entropy

n-gram entropy

repetition ratio

repeated n-gram excess

autocorrelation


Interpretation:

higher score = stronger detectable structure / regularity
lower score = closer to random noise


---

Results

random_noise     mean: 1.537397
corrupted_like   mean: 1.756441
human_like       mean: 2.104670
degraded_like    mean: 2.641043

Observed ordering:

random_noise < corrupted_like < human_like < degraded_like

Pairwise separation:

corrupted_like - random_noise: 0.219044
human_like - corrupted_like:   0.348229
degraded_like - human_like:    0.536373
degraded_like - random_noise:  1.103646


---

Interpretation

OMNIA-RADAR produced a clean structural gradient:

noise → corrupted structure → natural structure → mechanical/degenerate structure

This is the correct RADAR behavior.

It does not decide whether a structure is good or bad.

It detects where structural regularity is present and how strong it is.


---

Key Finding

Degraded-like text scored highest:

degraded_like > human_like

This is not a failure.

It confirms that OMNIA-RADAR measures structural intensity, not human quality.

Repetition loops and mechanical collapse increase:

compression

redundancy

repeated n-gram excess

structural regularity


Therefore they produce a stronger RADAR signal.


---

Boundary Statement

OMNIA-RADAR should not be described as:

a coherence detector
a truth detector
a quality detector
a semantic validator

It should be described as:

a structural scanner for residual, emergent, weak, strong, or pathological structure


---

Relation to OMNIA-LIMIT

OMNIA-LIMIT identifies a boundary where known coherence appears to stop.

OMNIA-RADAR scans near, inside, or beyond that boundary for measurable residual structure.

The correct question is not:

does this have human meaning?

The correct RADAR question is:

does this preserve measurable structure?


---

Conclusion

OMNIA-RADAR v3B demonstrates that the system can detect a graded structural field:

random_noise < corrupted_like < human_like < degraded_like

This supports the core hypothesis:

regions that appear meaningless, corrupted, or post-limit may still contain measurable structure


---

Next Step

Move from controlled real-like data to external real data.

Proposed next test:

RADAR v3C — external real-world structure scan

Goal:

test whether RADAR detects structural gradients in non-generated data