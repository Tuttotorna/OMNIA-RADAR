from __future__ import annotations

import json
from pathlib import Path

from omnia.omega import OmegaEstimator


EPS = 1e-6


def load_jsonl(path: Path):
    out = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                out.append(json.loads(line))
    return out


def encode_record(r: dict) -> str:
    # Generic encoding: stable structural token string
    return "|".join(f"{k}:{v}" for k, v in sorted(r.items()))


def opportunity_score(sei: float, iri: float) -> float:
    return sei / (iri + EPS)


def scan(path: Path):
    est = OmegaEstimator()
    data = load_jsonl(path)

    omegas = []
    seis = []
    iris = []

    for r in data:
        text = encode_record(r)
        res = est.estimate(text)

        omegas.append(res.omega)
        seis.append(res.sei)
        iris.append(res.iri)

    omega_m = sum(omegas) / len(omegas)
    sei_m = sum(seis) / len(seis)
    iri_m = sum(iris) / len(iris)

    score = opportunity_score(sei_m, iri_m)

    return {
        "file": path.name,
        "omega_mean": round(omega_m, 6),
        "sei_mean": round(sei_m, 6),
        "iri_mean": round(iri_m, 6),
        "opportunity": round(score, 6),
    }


def main():
    candidates = list(Path("candidates").glob("*.jsonl"))
    if not candidates:
        print("No candidates found in /candidates/")
        return

    print("\n=== OMNIA-RADAR SCAN ===\n")

    results = []
    for c in candidates:
        r = scan(c)
        results.append(r)

    # Sort by opportunity descending
    results.sort(key=lambda x: x["opportunity"], reverse=True)

    for r in results:
        print(
            f"{r['file']} | "
            f"Ω={r['omega_mean']:.4f} | "
            f"SEI={r['sei_mean']:.4f} | "
            f"IRI={r['iri_mean']:.4f} | "
            f"OPP={r['opportunity']:.4f}"
        )

    print("\n=== TOP OPPORTUNITY ZONE ===")
    print(results[0])
    print("===========================\n")


if __name__ == "__main__":
    main()