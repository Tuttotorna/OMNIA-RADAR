"""
OMNIA-RADAR — minimal demo (deterministic).

Run:
  python examples/minimal_radar_demo.py

RADAR score (standard):
  radar_score = sei_norm * (1 - iri_norm) * drift_gate

Interpretation:
- sei_norm    ∈ [0,1]  higher = more extractable structure
- iri_norm    ∈ [0,1]  higher = more irreversible risk
- drift_gate  ∈ [0,1]  1 = controlled drift, 0 = fragmentation

Hard gate: if any axis collapses, opportunity collapses.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, asdict


def _clamp01(x: float) -> float:
    if x < 0.0:
        return 0.0
    if x > 1.0:
        return 1.0
    return x


@dataclass(frozen=True)
class RadarInput:
    sei_norm: float
    iri_norm: float
    drift_gate: float
    # Optional metadata (keep minimal)
    domain: str = "demo"
    window: str = "N/A"


@dataclass(frozen=True)
class RadarOutput:
    radar_score: float
    sei_norm: float
    iri_norm: float
    drift_gate: float
    domain: str
    window: str
    gate_collapsed: bool


def radar_score(sei_norm: float, iri_norm: float, drift_gate: float) -> float:
    sei = _clamp01(sei_norm)
    iri = _clamp01(iri_norm)
    drift = _clamp01(drift_gate)
    return sei * (1.0 - iri) * drift


def evaluate(inp: RadarInput) -> RadarOutput:
    sei = _clamp01(inp.sei_norm)
    iri = _clamp01(inp.iri_norm)
    drift = _clamp01(inp.drift_gate)

    score = radar_score(sei, iri, drift)
    gate_collapsed = (sei <= 0.0) or (drift <= 0.0) or (iri >= 1.0)

    return RadarOutput(
        radar_score=score,
        sei_norm=sei,
        iri_norm=iri,
        drift_gate=drift,
        domain=inp.domain,
        window=inp.window,
        gate_collapsed=gate_collapsed,
    )


def main() -> None:
    # Example inputs (edit these to test regimes)
    samples = [
        RadarInput(sei_norm=0.82, iri_norm=0.12, drift_gate=0.90, domain="toy", window="t0"),
        RadarInput(sei_norm=0.55, iri_norm=0.75, drift_gate=0.80, domain="toy", window="t1"),
        RadarInput(sei_norm=0.10, iri_norm=0.10, drift_gate=0.90, domain="toy", window="t2"),
        RadarInput(sei_norm=0.85, iri_norm=0.20, drift_gate=0.00, domain="toy", window="t3"),
    ]

    outputs = [asdict(evaluate(s)) for s in samples]
    print(json.dumps({"radar_outputs": outputs}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()