"""
OMNIA-RADAR minimal example.

RADAR score (standard, multiplicative gate):
  radar_score = sei_norm * (1 - iri_norm) * drift_gate

All inputs are normalized in [0, 1].
"""

from __future__ import annotations


def radar_score(sei_norm: float, iri_norm: float, drift_gate: float) -> float:
    for name, x in (("sei_norm", sei_norm), ("iri_norm", iri_norm), ("drift_gate", drift_gate)):
        if not (0.0 <= x <= 1.0):
            raise ValueError(f"{name} must be in [0,1], got {x}")
    return sei_norm * (1.0 - iri_norm) * drift_gate


def main() -> None:
    # Example values (normalized)
    sei_norm = 0.82       # high extractable structure
    iri_norm = 0.18       # low irreversible risk
    drift_gate = 0.90     # controlled drift (not fragmentation)

    score = radar_score(sei_norm, iri_norm, drift_gate)

    print("OMNIA-RADAR minimal example")
    print(f"SEI_norm   : {sei_norm:.3f}")
    print(f"IRI_norm   : {iri_norm:.3f}")
    print(f"drift_gate : {drift_gate:.3f}")
    print(f"RADAR score: {score:.6f}")


if __name__ == "__main__":
    main()