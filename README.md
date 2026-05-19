# OMNIA-RADAR

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19829096.svg)](https://doi.org/10.5281/zenodo.19829096)

**OMNIA-RADAR** is the structural detection, drift surfacing, signal persistence, and residual-structure scanning layer of the OMNIA ecosystem.

It detects measurable structure.

It does not decide what the structure means.

It does not certify truth.

It does not replace OMNIA.

Core boundary:

```text
measurement != inference != decision
```

OMNIA-RADAR is not a truth oracle.

OMNIA-RADAR is not a semantic judge.

OMNIA-RADAR is not a decision engine.

Decision remains external.

---

## What OMNIA-RADAR is

OMNIA-RADAR is a post-hoc structural detection layer.

It scans sequences, outputs, traces, texts, logs, code, numeric patterns, or symbolic systems and measures:

```text
detectable structure
structural intensity
structural persistence
structural anomalies
residual structure
drift under perturbation
instability signals
```

It asks:

```text
Is there measurable structure here?
How strong is it?
How persistent is it?
How does it behave under perturbation?
```

---

## What OMNIA-RADAR is not

OMNIA-RADAR is not:

- a truth detector
- a meaning detector
- a semantic evaluator
- a coherence validator
- a quality evaluator
- a reasoning system
- a decision engine
- an optimization layer
- a policy layer

It does not recommend action.

It does not decide.

It detects and surfaces structural signal.

---

## Core distinction

OMNIA-RADAR separates structure from meaning.

```text
structure != meaning
structure != truth
structure != coherence
structure != quality
```

A system can contain structure without human meaning.

A system can contain strong structure and still be degenerate.

A system can contain moderate structure and be more persistent than a maximally regular system.

---

## Main empirical claim

Across the validation path, OMNIA-RADAR repeatedly shows:

```text
maximum structural intensity != maximum structural persistence
```

More directly:

```text
the strongest structures are often the most fragile under perturbation
```

This separates two axes:

- structural intensity: how much structure is detectable
- structural persistence: how long structure survives under perturbation

---

## Structural map

OMNIA-RADAR maps sequences into a structural field:

```text
X = structural intensity
Y = structural persistence
```

Typical regimes:

```text
low intensity  + flat persistence  -> noise baseline
medium intensity + high persistence -> distributed / resilient structure
high intensity + low persistence   -> brittle / over-structured regime
```

This is the central RADAR reading.

---

## Position in the ecosystem

OMNIA-RADAR is a bounded layer inside the MB-X.01 / OMNIA ecosystem.

```text
OMNIABASE       = representation / multi-base observation
OMNIA           = structural measurement core
OMNIA-RADAR     = structural detection / drift surfacing
OMNIA-LIMIT     = terminal boundary / stop condition
OMNIA-VALIDATION = evidence / reproducibility
Decision         = external layer
```

Functional separation:

```text
RADAR -> detects structure
OMNIA -> measures structural coherence / fragility
LIMIT -> identifies terminal structural boundary
```

RADAR is therefore not OMNIA.

RADAR detects the presence, intensity, persistence, and residual behavior of structure.

OMNIA measures structural coherence under transformation.

LIMIT identifies where continuation no longer produces admissible structure.

---

## Current validation path

The repository documents a progressive validation path:

```text
v1-v2 -> emergence detection
v3B   -> pure structure scan
v3C   -> external real-data scan
v3D   -> natural outlier scan
v4    -> cross-domain structure scan
v5    -> adversarial structure test
v6    -> temporal degradation test
v7    -> structure vs persistence map
```

Recommended entry path:

- [`docs/RADAR_ONE_PAGER.md`](docs/RADAR_ONE_PAGER.md)
- [`docs/RADAR_ENTRY_POINT.md`](docs/RADAR_ENTRY_POINT.md)
- [`docs/RADAR_CLAIM.md`](docs/RADAR_CLAIM.md)
- [`docs/RADAR_STRUCTURE_PERSISTENCE_MAP_V7.md`](docs/RADAR_STRUCTURE_PERSISTENCE_MAP_V7.md)

---

## What RADAR measures

RADAR uses structural indicators such as:

- compression ratio
- token entropy
- character entropy
- n-gram entropy
- repetition ratio
- repeated n-gram excess
- autocorrelation
- temporal score decay under perturbation

These are structural signals.

They are not semantic metrics.

---

## Repository structure

```text
omnia_radar/      package code
examples/         runnable demos
tests/            smoke and collapse tests
docs/             experimental notes and result writeups
results/          result artifacts
candidates/       candidate input traces
RADAR_SCHEMA.md   schema reference
radar_scan.py     scan entry script
```

---

## Quickstart

```bash
git clone https://github.com/Tuttotorna/OMNIA-RADAR.git
cd OMNIA-RADAR
python -m pip install -e .
python -m pytest -q
```

Minimal demo examples:

```bash
python examples/minimal_radar_demo.py
python examples/radar_minimal.py
python examples/radar_demo.py
```

---

## Public entrypoints

- [`docs/RADAR_SCOPE.md`](docs/RADAR_SCOPE.md)
- [`docs/RESULTS_INDEX.md`](docs/RESULTS_INDEX.md)
- [`docs/REPOSITORY_STATUS.md`](docs/REPOSITORY_STATUS.md)
- [`docs/RADAR_ONE_PAGER.md`](docs/RADAR_ONE_PAGER.md)
- [`docs/RADAR_ENTRY_POINT.md`](docs/RADAR_ENTRY_POINT.md)
- [`RADAR_SCHEMA.md`](RADAR_SCHEMA.md)

---

## Related repositories

- lon-mirror: https://github.com/Tuttotorna/lon-mirror
- OMNIABASE: https://github.com/Tuttotorna/OMNIABASE
- OMNIA: https://github.com/Tuttotorna/OMNIA
- OMNIA-INVARIANCE: https://github.com/Tuttotorna/OMNIA-INVARIANCE
- OMNIA-VALIDATION: https://github.com/Tuttotorna/OMNIA-VALIDATION
- omnia-limit: https://github.com/Tuttotorna/omnia-limit

---

## Public position

OMNIA-RADAR public positioning is documented here:

- [`docs/OMNIA_RADAR_PUBLIC_POSITION.md`](docs/OMNIA_RADAR_PUBLIC_POSITION.md)

Core thesis:

```text
detection != judgment
RADAR signal != final decision
```

Core boundary:

```text
detection != decision
measurement != inference != decision
```

Core role:

```text
OMNIA-RADAR scans for structural warning signals before semantic evaluation or final decision.
```

OMNIA-RADAR does not decide truth.

It does not certify safety.

It does not approve deployment.

It detects structural risk signals that may require measurement, validation, retry, escalation, or external review.
---

## Citation

If you reference this repository, use the archived Zenodo record:

```text
DOI: 10.5281/zenodo.19829096
https://doi.org/10.5281/zenodo.19829096
```

Citation metadata is available in:

- [`CITATION.cff`](CITATION.cff)

---

## Summary

OMNIA-RADAR detects and surfaces structure.

It does not judge truth or meaning.

It separates structural intensity from structural persistence.

Its central boundary is:

```text
measurement != inference != decision
structure != meaning
structure != truth
```
