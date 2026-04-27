# OMNIA-RADAR · Natural Outlier Scan v3D

## Status

PASS

---

## Objective

Test OMNIA-RADAR on unmodified external real text.

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

Dataset

Unmodified public-domain texts from Project Gutenberg:

Alice in Wonderland

Sherlock Holmes

Frankenstein

Moby Dick

Dracula


No synthetic manipulation was applied.

No degradation, no corruption, no injected noise.


---

Method

Each text was:

1. cleaned (basic normalization)


2. split into fixed-size chunks


3. analyzed independently



Total:

150 chunks


---

Metrics

RADAR score combines:

compression ratio

token entropy

character entropy

n-gram entropy

repetition ratio

repeated n-gram excess

autocorrelation


Interpretation:

higher score = stronger detectable structure / regularity
lower score = weaker / more variable structure


---

Global Results

chunks: 150

mean:   2.022667
median: 2.022254
std:    0.079124

min:    1.819585
max:    2.359450


---

Source-Level Summary

ALICE
mean: 2.084566

DRACULA
mean: 2.053855

FRANKENSTEIN
mean: 2.005491

SHERLOCK
mean: 2.005770

MOBY_DICK
mean: 1.963651

Observation:

different authors / styles produce measurable structural shifts


---

Top Structural Outliers

Examples:

1. Dracula — front matter / metadata block

START OF THE PROJECT GUTENBERG EBOOK...
Copyright...
Publisher...

Properties:

strong repetition patterns

rigid formatting

list-like structure



---

2. Moby Dick — index / chapter listing

CHAPTER 1...
CHAPTER 2...
CONTENTS...

Properties:

enumerations

repetitive syntax

highly regular structure



---

3. Alice — dialogue loops

repeated conversational patterns
question/answer cycles

Properties:

moderate repetition

structured interaction patterns



---

Bottom Structural Outliers

Examples:

Moby Dick / Frankenstein narrative passages

long descriptive prose
variable sentence length
low repetition density

Properties:

high variability

lower redundancy

less rigid structure



---

Key Finding

RADAR automatically identified:

- front matter blocks
- indices
- enumerations
- rigid formatting
- conversational loops

without:

labels
categories
supervision
semantic understanding


---

Interpretation

OMNIA-RADAR behaves as a structural sensor:

it highlights regions with abnormal structural regularity

It does not detect:

meaning
truth
quality
narrative value

It detects:

pattern density
redundancy
structural rigidity


---

Important Observation

Highest scores are not “best text”.

They are:

most structurally constrained regions

Examples:

headers

copyright sections

lists

repetitive dialogue



---

Boundary Statement

OMNIA-RADAR is NOT:

a semantic analyzer
a quality evaluator
a truth verifier
a coherence checker

OMNIA-RADAR IS:

a detector of structural intensity and structural anomalies


---

Main Result

Without any prior knowledge, RADAR successfully produced:

a ranked field of structural outliers

From purely real-world text.


---

Significance

This is the first test where:

no synthetic manipulation was used

and still:

meaningful structural distinctions emerged


---

Relation to OMNIA-LIMIT

OMNIA-LIMIT identifies where meaningful continuation may stop.

OMNIA-RADAR scans:

inside
at the boundary
beyond the boundary

to detect residual or hidden structure.

Correct question:

does structure exist here?

Not:

does this make sense?


---

Conclusion

OMNIA-RADAR v3D demonstrates:

structure can be detected blindly
in real data
without labels
without semantics

This confirms the core hypothesis:

structure persists even when meaning is not evaluated


---

Next Step

RADAR v4 — cross-domain structure scan

Goal:

test RADAR across different data types
(text, logs, code, numeric sequences)