from __future__ import annotations

from omnia_radar.types import RadarInput
from omnia_radar.radar import radar_score


def _print_case(name: str, x: RadarInput) -> None:
    out = radar_score(x)
    print(f"\n== {name} ==")
    print(f"radar_score: {out.radar_score:.6f}")
    print(f"drift_gate:   {out.drift_gate:.6f}")
    print(f"flags:        {out.flags}")
    for k, v in out.breakdown.items():
        print(f"{k:>14}: {v:.6f}")


def main() -> None:
    # Case A: valid opportunity (SEI high, IRI low, drift stable, omega good)
    case_opportunity = RadarInput(
        omega_coherence=0.90,
        sei=0.80,
        iri=0.10,
        drift=0.20,
        meta={"case": "opportunity"},
    )

    # Case B: saturated (SEI = 0 -> hard collapse)
    case_saturated = RadarInput(
        omega_coherence=0.95,
        sei=0.0,
        iri=0.10,
        drift=0.10,
        meta={"case": "saturated"},
    )

    # Case C: irreversible (IRI = 1 -> hard collapse)
    case_irreversible = RadarInput(
        omega_coherence=0.95,
        sei=0.70,
        iri=1.0,
        drift=0.10,
        meta={"case": "irreversible"},
    )

    _print_case("A) OPPORTUNITY", case_opportunity)
    _print_case("B) SATURATED", case_saturated)
    _print_case("C) IRREVERSIBLE", case_irreversible)


if __name__ == "__main__":
    main()