# OMNIA-RADAR  
Structural opportunity detector (SEI-high / IRI-low growth zones)

This repository is part of the **MB-X.01 / OMNIA** ecosystem.

**Author:** Massimiliano Brighindi  
**Signature:** MB-X.01 / Omniabase±  

OMNIA-RADAR is **architecture-agnostic**, **model-agnostic**, and **strictly non-decisional**.  
It performs **measurement only**.

---

## Overview

**OMNIA-RADAR** is a **post-hoc structural opportunity detector**.

It uses OMNIA-derived measurements to identify zones where:

- **SEI is high** → structure is still extractable (not saturated)
- **IRI is low** → no irreversible collapse (no lock-in)
- **drift is controlled** → growth regime, not fragmentation

RADAR does **not** optimize, decide, recommend, or predict outcomes.

It measures **where growth is still structurally possible beyond OMNIA-LIMIT**.

---

## Core Idea

**OMNIA-LIMIT** marks structural saturation.

**OMNIA-RADAR** maps the remaining feasible space:

- **LIMIT → excluded**
- **Residual → opportunity**

RADAR acts as a **strict structural gate**:  
it outputs a non-zero value **only if the system is neither saturated nor collapsed**.

There is no soft scoring.  
There is no heuristic optimization.  
Only structural admissibility.

---

## Structural Chain

OMNIA measures invariance and instability.  
OMNIA-LIMIT marks saturation (STOP).  
OMNIA-RADAR maps the residual space where opportunity is still measurable.

OMNIA → OMNIA-LIMIT → OMNIA-RADAR

---

## Inputs

RADAR expects, per candidate trajectory or domain, the minimal OMNIA signals:

- **Ω / Ω̂** — coherence / Omega-set residue
- **SEI** — saturation / extractability index
- **IRI** — irreversibility risk
- **drift** — controlled vs unstable drift

Inputs can be imported from an OMNIA run or assembled from a compatible report.

All values are assumed normalized in **[0, 1]**.

---

## Output

For each candidate, RADAR returns:

- `radar_score` — structural opportunity gate ∈ [0,1]
- `sei_norm`
- `iri_norm`
- `drift_gate`
- `gate_collapsed` — boolean hard collapse indicator
- optional metadata (domain, window, etc.)

RADAR outputs **measurements**, not actions.

---

## Formal Definition (minimal)

### 1) Drift Gate

`drift_gate ∈ [0,1]` collapses opportunity when drift becomes unstable.

Minimal definition:

- define `drift ∈ [0,1]` where:
  - `0 = fully stable`
  - `1 = fully unstable`

Then:

drift_gate = 1 - drift

Hard-collapse variant (optional):

- if `drift > drift_max` ⇒ `drift_gate = 0`

---

### 2) Opportunity Score (standard)

Strict multiplicative gate:

radar_score = clip01( sei_norm * (1 - iri_norm) * drift_gate )

Where:

- `sei_norm ∈ [0,1]`
- `iri_norm ∈ [0,1]`
- `drift_gate ∈ [0,1]`

---

### Collapsing Rule (non-negotiable)

RADAR **must collapse to zero** under any boundary condition:

- if `sei_norm = 0` ⇒ `radar_score = 0`
- if `iri_norm = 1` ⇒ `radar_score = 0`
- if `drift_gate = 0` ⇒ `radar_score = 0`

This is a **measurement gate**, not a soft heuristic.

---

## Minimal Executable Example

A deterministic minimal demo is provided:

examples/minimal_radar_demo.py

Run:

```bash
python examples/minimal_radar_demo.py

The script evaluates synthetic inputs and outputs a JSON structure containing:

radar_score

sei_norm

iri_norm

drift_gate

gate_collapsed


This file constitutes the reference executable artifact of the repository.


---

Minimal Integration Contract (suggested)

Input (Python)

from dataclasses import dataclass
from typing import Optional, Dict, Any

@dataclass(frozen=True)
class RadarInput:
    sei_norm: float            # [0,1]
    iri_norm: float            # [0,1]
    drift_gate: float          # [0,1]
    meta: Optional[Dict[str, Any]] = None


---

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


Any decision, optimization, or policy layer must remain external.

RADAR measures structural opportunity only.


---

License / Usage

OMNIA-RADAR is a measurement layer.

It exists to expose where opportunity is still structurally admissible
after saturation has been declared by OMNIA-LIMIT.

RADAR never decides.
It only detects.

