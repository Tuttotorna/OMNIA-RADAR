# OMNIA-RADAR v7 — Structure vs Persistence Map

## Overview

This experiment maps RADAR behavior across two axes:

```text
X = structural intensity
Y = structural persistence

RADAR remains in pure mode:

no semantic interpretation

no quality judgment

no coherence classification

no OMNIA proxy



---

Objective

Previous tests showed that RADAR can detect structural intensity.

This test asks a deeper question:

Does maximum structure also mean maximum persistence?


---

Method

Three regimes were tested:

NOISE

HUMAN-like structure

OPTIMIZED structure


Each sample was progressively degraded.

For each sample:

initial_score = RADAR score before degradation
final_score   = RADAR score after degradation
relative_drop = (initial_score - final_score) / initial_score
persistence   = 1 - relative_drop


---

Results

NOISE
structure (X):   1.7910
persistence (Y): 1.0293

HUMAN
structure (X):   1.8417
persistence (Y): 1.0565

OPTIMIZED
structure (X):   5.7595
persistence (Y): 0.7678


---

Interpretation

Noise

low structure
high apparent persistence

Noise does not collapse because it has little organized structure to lose.

This is a flat baseline, not meaningful robustness.


---

Human-like structure

medium structure
high persistence

Human-like structure is not maximal, but it is distributed.

It degrades gradually rather than collapsing sharply.


---

Optimized structure

very high structure
low persistence

Optimized structure begins with extreme regularity, but loses structure quickly under perturbation.

This confirms:

maximum structure is fragile


---

Key Finding

maximum structural intensity != maximum structural persistence

RADAR now separates:

how much structure exists

from:

how long that structure survives under perturbation


---

Structural Map

PERSISTENCE
                       ↑

 high persistence       human-like / distributed structure
                       noise plateau

 low persistence        optimized / brittle structure

                       └──────────────→ STRUCTURAL INTENSITY


---

Regime Interpretation

Regime	Structure	Persistence	Interpretation

Noise	low	high/flat	no structure to lose
Human-like	medium	high	distributed resilient structure
Optimized	very high	low	brittle over-structured regime



---

Conceptual Result

RADAR is no longer only a static detector.

It can be used as a dynamic structural probe:

structure field = intensity × persistence

This enables separation between:

strong but brittle structure

and:

moderate but persistent structure


---

Relation to Previous Tests

This result is consistent with:

v5 adversarial structure test

v6 temporal degradation test

v4 cross-domain structure scan


Together, they show:

RADAR detects structure,
tracks degradation,
and separates intensity from persistence.


---

Boundary Statement

OMNIA-RADAR does not determine:

truth

meaning

usefulness

semantic coherence

final validity


It determines:

where structure is present
how strong it is
how it behaves under perturbation


---

Conclusion

OMNIA-RADAR v7 demonstrates a two-axis structural map:

structure intensity
+
structure persistence

Main result:

maximum structure is not maximum robustness

This supports the central RADAR hypothesis:

regions that appear meaningful, meaningless, optimized, noisy, or post-limit
can be scanned as structural fields without semantic interpretation.


---

Next Step

Possible next extension:

RADAR v8 — boundary leak scan

Goal:

scan near an OMNIA-LIMIT boundary and detect residual structures that persist beyond the expected stop point.