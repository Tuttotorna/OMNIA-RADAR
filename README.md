# OMNIA-RADAR

**Structural signal detection layer.**

OMNIA-RADAR is the pre-measurement detection layer of the MB-X.01 / OMNIA ecosystem.

Its role is narrow:

    candidate trace -> signal scan -> anomaly / persistence / drift -> measurement candidate

It asks one question:

    is there a structural signal worth sending into full OMNIA measurement?

OMNIA-RADAR is not the ecosystem landing page.

It is not the validation showroom.

It is not the OMNIA core measurement engine.

It is not a security scanner.

It is the layer that detects structural signal candidates before full measurement.

Canonical boundary:

    measurement != inference != decision

---

## Start here

From a clean environment:

    git clone https://github.com/Tuttotorna/OMNIA-RADAR.git
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

## Related repositories

| Repository | Role |
|---|---|
| [lon-mirror](https://github.com/Tuttotorna/lon-mirror) | Canonical ecosystem entry point |
| [OMNIA-VALIDATION](https://github.com/Tuttotorna/OMNIA-VALIDATION) | Public validation showroom |
| [OMNIA](https://github.com/Tuttotorna/OMNIA) | Core structural measurement engine |
| [OMNIABASE](https://github.com/Tuttotorna/OMNIABASE) | Representation invariance foundation |
| [omnia-limit](https://github.com/Tuttotorna/omnia-limit) | Stop / continue boundary layer |
| [OMNIA-INVARIANCE](https://github.com/Tuttotorna/OMNIA-INVARIANCE) | Transformation and invariance layer |
| [OMNIA-CONSTANT](https://github.com/Tuttotorna/OMNIA-CONSTANT) | Stable-region falsification layer |

---

## Ecosystem entry point

For the full ecosystem map, start here:

    https://github.com/Tuttotorna/lon-mirror

For public validation artifacts, start here:

    https://github.com/Tuttotorna/OMNIA-VALIDATION

For core structural measurement, start here:

    https://github.com/Tuttotorna/OMNIA

---


## Smoke-test required terms

    not a truth oracle
    not a semantic judge
    Decision remains external
    structure != meaning

## License

MIT.

