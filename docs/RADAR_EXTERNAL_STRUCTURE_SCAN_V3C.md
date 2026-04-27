# OMNIA-RADAR · External Structure Scan v3C

## Status

PASS

---

## Objective

Test OMNIA-RADAR on external real data.

This test evaluates only:

```text
detectable structural intensity

It does NOT evaluate:

meaning

truth

quality

semantic coherence

usefulness



---

Core Principle

structure != meaning
structure != quality
structure != coherence

OMNIA-RADAR asks only:

is there measurable structure here?


---

Data Sources

External public-domain text was fetched from Project Gutenberg:

Alice in Wonderland

Sherlock Holmes

Frankenstein


From these sources, four groups were produced:


---

Dataset

A — External Random Noise

Random token sequences used as a noise control.

Expected:

lowest structural intensity


---

B — External Corrupted-Like Text

Real text with:

block shuffling

random token injection

surface corruption


Expected:

more structure than pure noise
less structure than intact real text


---

C — External Real Text

Unmodified real public-domain text chunks.

Expected:

natural structural intensity


---

D — External Degraded-Like Text

Real text with:

repeated words

repeated fragments

mechanical degeneration

loop-like reinforcement


Expected:

highest structural intensity

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

external_random_noise     mean: 1.282760
external_corrupted_like   mean: 1.828570
external_real_text        mean: 1.985936
external_degraded_like    mean: 2.763189

Observed ordering:

external_random_noise
<
external_corrupted_like
<
external_real_text
<
external_degraded_like

Pairwise separation:

external_corrupted_like - external_random_noise: 0.545810
external_real_text - external_corrupted_like:     0.157366
external_degraded_like - external_real_text:      0.777253
external_degraded_like - external_random_noise:   1.480429


---

Interpretation

OMNIA-RADAR produced a graded structural field on external data:

noise → corrupted text → real text → degraded / loop-reinforced text

This confirms that the signal observed in earlier synthetic tests was not limited to toy data.

The system detects structural intensity across:

pure random noise

damaged real text

intact real text

mechanically reinforced degraded text



---

Key Finding

Degraded-like text scored highest:

external_degraded_like > external_real_text

This is expected under a pure RADAR lens.

Repetition loops and mechanical degeneration increase:

redundancy

compressibility

repeated n-gram excess

detectable regularity


Therefore, they generate a stronger RADAR signal.

This does NOT mean degraded text is better.

It means degraded text is more structurally rigid.


---

Boundary Statement

OMNIA-RADAR should not be described as:

a truth detector
a meaning detector
a quality detector
a coherence validator

It should be described as:

a structural scanner for residual, emergent, weak, strong, or pathological structure


---

Relation to OMNIA-LIMIT

OMNIA-LIMIT identifies a boundary where known coherence or useful continuation appears to stop.

OMNIA-RADAR scans near, inside, or beyond that boundary for measurable residual structure.

The correct question is not:

does this have human meaning?

The correct RADAR question is:

does this preserve measurable structure?


---

Main Result

external_random_noise < external_corrupted_like < external_real_text < external_degraded_like

This supports the hypothesis:

regions that appear meaningless, corrupted, degraded, or post-limit may still contain measurable structure


---

Limitation

This test still includes derived variants:

corrupted-like text was generated from real text

degraded-like text was generated from real text

random noise was synthetically generated


Therefore, this is not yet a fully natural-world dataset.

It is an external-real-data scan with controlled perturbation layers.


---

Conclusion

OMNIA-RADAR v3C demonstrates that RADAR can detect a structural gradient on external real text sources.

It confirms the core RADAR trajectory:

detect structure
do not interpret it
do not judge it
do not classify it as good or bad


---

Next Step

Proposed next test:

RADAR v3D — natural outlier scan

Goal:

scan unmodified external sources only
and identify structural outliers without synthetic perturbation