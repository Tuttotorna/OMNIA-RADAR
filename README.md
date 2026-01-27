# OMNIA-RADAR  
Structural opportunity detector (SEI-high / IRI-low growth zones)

This repository is part of the **MB-X.01 / OMNIA** ecosystem.

**Author:** Massimiliano Brighindi  
**Signature:** MB-X.01 / Omniabase±  

OMNIA-RADAR is architecture-agnostic and strictly non-decisional: measurement only.

---

## Overview

**OMNIA-RADAR** is a **post-hoc structural opportunity detector**.

It uses OMNIA measurements to identify zones where:

- **SEI is high** → structure is still extractable (not saturated)
- **IRI is low** → no irreversible collapse (no lock-in)
- **drift is controlled** → growth regime, not fragmentation

RADAR does **not** optimize, decide, or recommend actions.

It measures **where growth is still structurally possible beyond OMNIA-LIMIT**.

---

## Core Idea

**OMNIA-LIMIT** marks saturation.

RADAR maps the remaining feasible space:

- **LIMIT → excluded**
- **Residual → opportunity**

RADAR is a strict structural *gate*:  
it outputs non-zero only if the system is neither saturated nor collapsed.

---

## Structural Chain

OMNIA measures invariance and instability.  
OMNIA-LIMIT marks saturation (STOP).  
OMNIA-RADAR maps the residual space where opportunity is still measurable.

**OMNIA → OMNIA-LIMIT → OMNIA-RADAR**

---

## Inputs

RADAR expects, per candidate trajectory or domain, the minimal OMNIA signals:

- **Ω / Ω̂** (coherence / Omega-set residue)
- **SEI** (saturation / extractability gradient)
- **IRI** (irreversibility risk)
- **drift** (controlled vs unstable drift)

These can be imported from an OMNIA run or assembled from a compatible report.

---

## Output

For each candidate, RADAR returns:

- `omega_coherence`
- `sei`
- `iri`
- `drift_gate`
- `radar_score`
- `flags` (e.g., `SATURATED`, `IRREVERSIBLE`, `DRIFT_UNSTABLE`)
- optional breakdown for debugging

---

## Formal Definition (minimal)

### 1) Drift Gate

`drift_gate ∈ [0,1]` collapses opportunity when drift becomes unstable.

Recommended minimal form:

- define `drift ∈ [0,1]` where:

  - `0 = stable`
  - `1 = unstable`

Then:

`drift_gate = 1 - drift`

Hard collapse variant:

- if `drift > drift_max` ⇒ `drift_gate = 0`

---

### 2) Opportunity Score

Default multiplicative gate:

`radar_score = clip01( SEI * (1 - IRI) * drift_gate * omega_coherence )`

Where:

- `SEI ∈ [0,1]`
- `IRI ∈ [0,1]`
- `omega_coherence ∈ [0,1]`

---

### Collapsing Rule (non-negotiable)

RADAR must collapse to zero under any boundary condition:

- if `SEI = 0` ⇒ `radar_score = 0`
- if `IRI = 1` ⇒ `radar_score = 0`
- if `drift_gate = 0` ⇒ `radar_score = 0`

This is a measurement gate, not a soft heuristic.

---

## Minimal Example

A minimal executable scoring example is provided:

examples/radar_minimal.py

Core rule:

RADAR = SEI_norm · (1 − IRI_norm) · drift_gate

---

## Planned Repository Structure (recommended)

omnia_radar/ init.py radar.py            # score + flags types.py            # dataclasses / typed dicts drift.py            # drift_gate implementations

examples/ radar_demo.py       # synthetic trajectories demo

tests/ test_radar_collapse.py

---

## Minimal Integration Contract (suggested)

### Input (Python)

```python
from dataclasses import dataclass
from typing import Optional, Dict, Any

@dataclass(frozen=True)
class RadarInput:
    omega_coherence: float     # [0,1]
    sei: float                # [0,1]
    iri: float                # [0,1]
    drift: float              # [0,1] (0 stable, 1 unstable)
    meta: Optional[Dict[str, Any]] = None


---

Output (Python)

from dataclasses import dataclass
from typing import Dict, List

@dataclass(frozen=True)
class RadarOutput:
    radar_score: float         # [0,1]
    drift_gate: float          # [0,1]
    flags: List[str]
    breakdown: Dict[str, float]


---

License / Usage

RADAR is intended strictly as a measurement layer.

Any decision or optimization layer must remain external.

RADAR never decides. It only detects structural opportunity beyond OMNIA-LIMIT.