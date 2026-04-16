# OMNIA-RADAR — Structural Opportunity Detector

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18390735.svg)](https://doi.org/10.5281/zenodo.18390735)

**Author:** Massimiliano Brighindi  
**Contact:** brighissimo@gmail.com  
**Signature:** MB-X.01 / Omniabase±

Canonical ecosystem map:  
**[lon-mirror / ECOSYSTEM.md](https://github.com/Tuttotorna/lon-mirror/blob/main/ECOSYSTEM.md)**

---

## Position in the Ecosystem

This repository is part of the **MB-X.01 / OMNIABASE / OMNIA** ecosystem.

Within that ecosystem:

- **[OMNIABASE](https://github.com/Tuttotorna/OMNIABASE)** = the general multirepresentational framework
- **[OMNIA](https://github.com/Tuttotorna/OMNIA)** = the Diagnostics / Structural Measurement branch
- **[lon-mirror](https://github.com/Tuttotorna/lon-mirror)** = the deep operational and historical core of the diagnostics lineage
- **[omnia-limit](https://github.com/Tuttotorna/omnia-limit)** = the terminal structural boundary layer
- **OMNIA-RADAR** = the structural opportunity detector of the diagnostics lineage

OMNIA-RADAR is **architecture-agnostic**, **model-agnostic**, and **strictly non-decisional**.

It performs **measurement only**.

---

## Overview

**OMNIA-RADAR** is a **post-hoc structural opportunity detector**.

It uses OMNIA-derived measurements to identify zones where:

- **SEI is high** -> structure is still extractable
- **IRI is low** -> no irreversible collapse is present
- **drift is controlled** -> the system is still in a growth regime rather than in fragmentation

RADAR does **not** optimize, decide, recommend, or predict outcomes.

It measures **where structural opportunity is still admissible inside the remaining non-collapsed space**.

---

## Architectural Role

The OMNIA diagnostics lineage does not only need a measurement core.

It also needs a way to distinguish between:

- zones that are already structurally exhausted
- zones that are still structurally open

That is the role of OMNIA-RADAR.

Where:

- **[OMNIA](https://github.com/Tuttotorna/OMNIA)** measures structural behavior
- **[omnia-limit](https://github.com/Tuttotorna/omnia-limit)** certifies structural non-reducibility
- **OMNIA-RADAR** detects whether a candidate region still contains structurally admissible opportunity

RADAR is therefore not a replacement for OMNIA or OMNIA-LIMIT.

It is a downstream structural detector operating on their signal space.

---

## Core Idea

**OMNIA-LIMIT** marks structural saturation.

**OMNIA-RADAR** maps the remaining feasible space before terminal collapse or outside clearly excluded regions.

Shortest formula:

- **LIMIT -> excluded**
- **Residual admissible region -> opportunity**

RADAR acts as a **strict structural gate**.

It outputs a non-zero value **only if the system is neither saturated nor irreversibly collapsed**.

There is no soft narrative scoring.  
There is no semantic interpretation.  
There is no optimization loop.

Only structural admissibility.

---

## Structural Chain

The diagnostics lineage can be read in simplified form as:

```text
OMNIA -> OMNIA-LIMIT -> OMNIA-RADAR

Meaning:

OMNIA measures invariance, fragility, drift, and collapse signals

OMNIA-LIMIT declares the structural stop boundary where admissible diagnostics must end

OMNIA-RADAR maps the remaining measurable opportunity space in non-collapsed regions


This should not be confused with a decision pipeline.

RADAR measures opportunity.
It does not decide whether the opportunity should be pursued.


---

Inputs

RADAR expects, per candidate trajectory or domain, the minimal OMNIA-derived signals:

Ω / Ω̂ — coherence / Omega-set residue

SEI — saturation / extractability index

IRI — irreversibility risk

drift — controlled vs unstable drift


Inputs can be imported from an OMNIA run or assembled from a compatible structural report.

All values are assumed normalized in [0,1].


---

Output

For each candidate, RADAR returns:

radar_score — structural opportunity gate in [0,1]

sei_norm

iri_norm

drift_gate

gate_collapsed — boolean hard collapse indicator

optional metadata such as domain, window, or source


RADAR outputs measurements, not actions.


---

Formal Definition (Minimal)

1) Drift Gate

drift_gate ∈ [0,1] collapses opportunity when drift becomes unstable.

Minimal definition:

define drift ∈ [0,1] where:

0 = fully stable

1 = fully unstable



Then:

drift_gate = 1 - drift

Hard-collapse variant (optional):

if drift > drift_max -> drift_gate = 0



---

2) Opportunity Score (Standard)

Strict multiplicative gate:

radar_score = clip01( sei_norm * (1 - iri_norm) * drift_gate )

Where:

sei_norm ∈ [0,1]

iri_norm ∈ [0,1]

drift_gate ∈ [0,1]



---

Collapsing Rule (Non-Negotiable)

RADAR must collapse to zero under any boundary condition:

if sei_norm = 0 -> radar_score = 0

if iri_norm = 1 -> radar_score = 0

if drift_gate = 0 -> radar_score = 0


This is a measurement gate, not a soft heuristic.


---

Minimal Executable Example

A deterministic minimal demo is provided:

examples/minimal_radar_demo.py


Run:

python examples/minimal_radar_demo.py

The script evaluates synthetic inputs and outputs a JSON structure containing:

radar_score

sei_norm

iri_norm

drift_gate

gate_collapsed


This file constitutes the reference executable artifact of the repository.


---

Minimal Integration Contract

Input (Python)

from dataclasses import dataclass
from typing import Optional, Dict, Any

@dataclass(frozen=True)
class RadarInput:
    sei_norm: float            # [0,1]
    iri_norm: float            # [0,1]
    drift_gate: float          # [0,1]
    meta: Optional[Dict[str, Any]] = None

Output (Python)

from dataclasses import dataclass
from typing import Dict, Any

@dataclass(frozen=True)
class RadarOutput:
    radar_score: float         # [0,1]
    gate_collapsed: bool
    breakdown: Dict[str, float]
    meta: Dict[str, Any]


---

Repository Scope

OMNIA-RADAR is intentionally minimal.

It does not:

learn

predict

rank alternatives

recommend actions

replace OMNIA

replace OMNIA-LIMIT

act as a policy layer


Any decision, optimization, or policy layer must remain external.

RADAR measures structural opportunity only.


---

Why This Repository Matters

Without a structural opportunity detector, the diagnostics lineage would be able to say only:

where collapse is present

where saturation is final

where stop must be declared


But many systems also need to know something narrower:

where structure is still admissibly open without already being fragmented or irreversibly lost

That is the narrow value of OMNIA-RADAR.

It is not a growth optimizer.
It is not a recommender.
It is a detector of structurally admissible opportunity zones.


---

Relationship to the Broader Ecosystem

At a high level:

OMNIABASE -> umbrella framework

OMNIA -> Diagnostics / Structural Measurement branch

lon-mirror -> deep operational and historical core of the diagnostics lineage

omnia-limit -> terminal structural boundary / SNRC issuance

OMNIA-RADAR -> structural opportunity detector

observer-suspension -> epistemic pre-layer

omniabase-coordinate-discovery -> Coordinate Discovery branch

omega-translator -> Cross-Representation Translation branch


This repository should therefore be read not as an isolated scoring utility, but as one bounded layer inside the Diagnostics branch of OMNIABASE.


---

Related Repositories

For the shortest functional path through the broader ecosystem:

OMNIABASE — umbrella framework

OMNIA — Diagnostics / Structural Measurement branch

lon-mirror — deep operational and historical core of the diagnostics lineage

omnia-limit — terminal structural boundary layer

observer-suspension — epistemic pre-layer

omniabase-coordinate-discovery — Coordinate Discovery branch

omega-translator — Cross-Representation Translation branch



---

Final Statement

OMNIA-RADAR exists to detect where structural opportunity is still admissible.

It never decides what should be done with that opportunity.

It measures.
It does not recommend.

That boundary is not a limitation.
It is the architectural condition that keeps RADAR coherent.


---

Summary

OMNIA-RADAR is the structural opportunity detector of the OMNIA diagnostics lineage inside the broader OMNIABASE ecosystem.

It identifies zones where:

extractable structure is still present

irreversible collapse has not yet occurred

drift remains controlled enough for admissible continuation


It is strictly non-decisional.

Its role is simple:

to detect where structural opportunity is still open without collapsing into optimization, policy, or prediction.