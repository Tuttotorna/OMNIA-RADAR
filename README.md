<!-- MB-X.01 LON RELEASE:START -->

## MB-X.01 / L.O.N. release state

Repository: Tuttotorna/OMNIA-RADAR
Release tag: v2026.05.21
Release commit: f0c14e8
Release DOI: 10.5281/zenodo.20322686

Boundary:

measurement != validation
validation != orchestration
orchestration != decision
decision != measurement

<!-- MB-X.01 LON RELEASE:END -->

# OMNIA-RADAR

<!-- ZENODO DOI:START -->

## DOI

[![DOI](https://zenodo.org/badge/DOI/10.5281%2Fzenodo.20322686.svg)](https://doi.org/10.5281/zenodo.20322686)

Zenodo DOI badge for this repository.

Repository: Tuttotorna/OMNIA-RADAR
GitHub repository id: 1143359510
Release tag: v2026.05.21
Latest release DOI: 10.5281/zenodo.20322686

<!-- ZENODO DOI:END -->


## DOI

[![DOI](https://zenodo.org/badge/1143359510.svg)](https://zenodo.org/badge/latestdoi/1143359510)

Release DOI: [10.5281/zenodo.19829096](https://doi.org/10.5281/zenodo.19829096)

GitHub release: [OMNIA-RADAR v1.0.0 release](https://github.com/Tuttotorna/OMNIA-RADAR/releases/tag/v1.0.0)

## Start here

From a clean environment:

    git clone [OMNIA-RADAR.git](https://github.com/Tuttotorna/OMNIA-RADAR.git)
    cd OMNIA-RADAR
    python -m pip install -e .
    pytest

If example scripts are available, run the smallest demonstration after tests pass.

The goal is to see the radar path:

    candidate trace
      -> signal scan
      -> anomaly / persistence / drift
      -> measurement candidate
      -> external validation

---

## What OMNIA-RADAR does

OMNIA-RADAR scans candidate traces, outputs, representations, or sequences for structural signals.

It can help detect:

- anomaly;
- persistence;
- drift;
- weak structural signal;
- candidate instability;
- candidate patterns worth measuring later.

Public compression:

    RADAR detects.
    OMNIA measures.
    VALIDATION tests artifacts.

---

## What OMNIA-RADAR does not do

OMNIA-RADAR does not:

- infer semantic truth;
- decide correctness;
- replace OMNIA measurement;
- replace OMNIA-VALIDATION;
- perform security scanning;
- perform cryptographic attacks;
- recover keys;
- prove physical truth;
- convert detection into final decision.

The final decision remains external.

---

## Public mental model

    Not every trace deserves full measurement.
    OMNIA-RADAR detects structural candidates.
    OMNIA decides nothing; RADAR decides even less.

RADAR is an early-warning layer, not a verdict layer.

---

## Radar contract

Every serious OMNIA-RADAR result should make clear:

| Component | Meaning |
|---|---|
| candidate | The trace, output, representation, or sequence being scanned |
| scan mode | What kind of signal scan is applied |
| anomaly | Whether unexpected structure appears |
| persistence | Whether signal survives basic variation |
| drift | Whether signal moves across observations |
| candidate signal | What should be sent to full measurement |
| limitation | What the detection does not prove |
| external validation | How the result should be validated later |

---

## Result vocabulary

Recommended result vocabulary:

    no_signal
    candidate
    anomaly
    persistent
    drifting
    inconclusive

Meaning:

- no_signal: no relevant structural signal detected under the declared scan;
- candidate: a possible signal exists and should be measured;
- anomaly: unexpected structure appears;
- persistent: signal remains visible across declared checks;
- drifting: signal moves across observations;
- inconclusive: the scan is insufficient or ambiguous.

---

## Recommended reading order

1. [docs/QUICKSTART_RADAR.md](docs/QUICKSTART_RADAR.md)
2. [docs/RADAR_OVERVIEW.md](docs/RADAR_OVERVIEW.md)
3. [docs/SIGNAL_CONTRACT.md](docs/SIGNAL_CONTRACT.md)
4. [docs/ANOMALY_PERSISTENCE_DRIFT.md](docs/ANOMALY_PERSISTENCE_DRIFT.md)
5. [docs/DETECTION_BOUNDARY.md](docs/DETECTION_BOUNDARY.md)
6. [docs/RADAR_MANIFEST.json](docs/RADAR_MANIFEST.json)

---

## Ecosystem entry point

For the full ecosystem map, start here:

[lon-mirror](https://github.com/Tuttotorna/lon-mirror)

For public validation artifacts, start here:

[OMNIA-VALIDATION](https://github.com/Tuttotorna/OMNIA-VALIDATION)

For core structural measurement, start here:

[OMNIA](https://github.com/Tuttotorna/OMNIA)

---


## Smoke-test required terms

    not a truth oracle
    not a semantic judge
    Decision remains external
    structure != meaning

## Related repositories

| Repository | Role |
|---|---|
| [lon-mirror](https://github.com/Tuttotorna/lon-mirror) | Canonical public entry point |
| [OMNIA-VALIDATION](https://github.com/Tuttotorna/OMNIA-VALIDATION) | Public validation showroom |
| [OMNIA](https://github.com/Tuttotorna/OMNIA) | Core structural measurement engine |
| [OMNIABASE](https://github.com/Tuttotorna/OMNIABASE) | Representation invariance foundation |
| [omnia-limit](https://github.com/Tuttotorna/omnia-limit) | Stop / continue boundary layer |
| [OMNIA-RADAR](https://github.com/Tuttotorna/OMNIA-RADAR) | Structural signal detection layer |
| [OMNIA-INVARIANCE](https://github.com/Tuttotorna/OMNIA-INVARIANCE) | Structural invariance layer |
| [OMNIA-CONSTANT](https://github.com/Tuttotorna/OMNIA-CONSTANT) | Structural constant candidate layer |
| [OMNIAMIND](https://github.com/Tuttotorna/OMNIAMIND) | Structural cognition orchestration layer |
| [OMNIA-THREE-BODY](https://github.com/Tuttotorna/OMNIA-THREE-BODY) | Dynamic divergence stress test |
| [OMNIA-SECURITY](https://github.com/Tuttotorna/OMNIA-SECURITY) | Bounded structural security diagnostics |
| [OMNIA-CRYPTO](https://github.com/Tuttotorna/OMNIA-CRYPTO) | Bounded structural crypto diagnostics |

---

## Boundary and smoke-test required terms

    measurement != inference != decision

---

## License

MIT.

<!-- OMNIA_ECOSYSTEM_BOUNDARY_V1 -->

## Ecosystem Boundary

```text
measurement != inference != decision
```

This repository is part of the MB-X.01 / OMNIA ecosystem. Its outputs must be read as structural measurement, validation, detection, orchestration or adapter artifacts according to the repository role. They are not autonomous semantic truth claims and they do not make external decisions.
