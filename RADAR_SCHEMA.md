Step 1: congelare il perimetro in RADAR_SCHEMA.md (solo definizioni + output), senza codice.

Incollare questo file nel repo:

# OMNIA-RADAR — Schema (Frozen v0.1)

This repository is part of the MB-X.01 / OMNIA ecosystem.

OMNIA-RADAR is a **structural opportunity detector**:
it measures **where growth is still possible** beyond OMNIA-LIMIT, without optimizing or deciding.

Author: Massimiliano Brighindi  
Signature: MB-X.01 / Omniabase±

---

## 1) Inputs (abstract)

RADAR operates on **candidate trajectories/domains** already representable as OMNIA-style objects:
- representations (variants) under independent transformations
- optional time ordering (t0..tn)

No semantic interpretation is assumed.

---

## 2) Core quantities (measured)

RADAR consumes (or reuses) the following OMNIA measurements:

- **Ω̂ (Omega-set):** invariance of a representation under transformations
- **SEI:** saturation / remaining extractable structure (high = still extractable)
- **IRI:** irreversibility risk (low = no collapse / no irreversible loss)
- **drift:** controlled change vs fragmentation (implementation-defined)

RADAR does not redefine these metrics; it only composes them.

---

## 3) Boundary gating (non-negotiable)

RADAR must not score inside OMNIA-LIMIT.

If OMNIA-LIMIT is triggered for a candidate:
- `radar_state = "excluded_limit"`
- no opportunity score is produced (or score is forced to 0)

---

## 4) Residual Opportunity Region (concept)

A candidate is in the *residual opportunity region* when:
- SEI is sufficiently high
- IRI is sufficiently low
- drift is controlled (growth regime)

This region is “what remains” after LIMIT exclusion.

---

## 5) RADAR score (placeholder definitions)

RADAR score is a monotone combination of:
- increasing in SEI
- decreasing in IRI
- penalized by uncontrolled drift
- optionally modulated by Ω̂-residual stability

Two equivalent placeholder families are acceptable:

### A) Multiplicative (simple)
radar_score = sei_norm * (1 - iri_norm) * drift_gate

### B) Additive with penalties (more stable)
radar_score = w1*sei_norm + w2*(1 - iri_norm) - w3*drift_penalty
clamped to [0, 1]

Where:
- `sei_norm, iri_norm ∈ [0,1]`
- `drift_gate ∈ [0,1]` (1 = controlled, 0 = fragmentation)
- weights `w1,w2,w3 ≥ 0` and `w1+w2+w3 = 1`

This document is the contract; implementation must match monotonicity.

---

## 6) Output schema (JSON)

Minimum output for each candidate:

```json
{
  "candidate_id": "string",
  "radar_state": "ok | excluded_limit | insufficient_data",
  "omega_residual": 0.0,
  "sei": 0.0,
  "sei_gradient": 0.0,
  "iri": 0.0,
  "iri_risk": 0.0,
  "drift": 0.0,
  "radar_score": 0.0
}

Notes:

omega_residual is optional if Ω̂ not computed; then set to null and state may be insufficient_data.

sei_gradient is optional unless time ordering exists.



---

7) Non-goals (explicit)

RADAR:

does not recommend actions

does not optimize outcomes

does not interpret meaning

does not learn

does not override OMNIA-LIMIT


It only measures where structural growth remains possible.

