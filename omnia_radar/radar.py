from __future__ import annotations

from typing import List, Dict

from .types import RadarInput, RadarOutput


def _clip01(x: float) -> float:
    return max(0.0, min(1.0, float(x)))


def compute_drift_gate(drift: float, drift_max: float = 0.85) -> float:
    """
    Minimal drift gate.

    drift ∈ [0,1]
      0 = stable regime
      1 = unstable fragmentation

    Hard collapse:
      if drift > drift_max -> gate = 0
    """
    d = _clip01(drift)
    if d > drift_max:
        return 0.0
    return 1.0 - d


def radar_score(x: RadarInput, drift_max: float = 0.85) -> RadarOutput:
    """
    OMNIA-RADAR minimal multiplicative opportunity detector.

    Non-negotiable collapse:
      SEI=0 or IRI=1 or drift_gate=0 -> score=0
    """
    flags: List[str] = []

    omega = _clip01(x.omega_coherence)
    sei = _clip01(x.sei)
    iri = _clip01(x.iri)

    gate = compute_drift_gate(x.drift, drift_max=drift_max)

    if sei <= 0.0:
        flags.append("SATURATED")
    if iri >= 1.0:
        flags.append("IRREVERSIBLE")
    if gate <= 0.0:
        flags.append("DRIFT_UNSTABLE")

    raw = sei * (1.0 - iri) * gate * omega
    score = _clip01(raw)

    # Hard collapse enforcement
    if ("SATURATED" in flags) or ("IRREVERSIBLE" in flags) or ("DRIFT_UNSTABLE" in flags):
        score = 0.0

    breakdown: Dict[str, float] = {
        "omega_coherence": omega,
        "sei": sei,
        "iri_complement": (1.0 - iri),
        "drift_gate": gate,
        "raw": raw,
    }

    return RadarOutput(
        radar_score=score,
        drift_gate=gate,
        flags=flags,
        breakdown=breakdown,
    )