<!-- OMNIA_RADAR_AUDITOR_TOP_START -->

# OMNIA-RADAR

## Concrete entrypoint: OMNIA Radar Auditor

This repository now has a direct operational tool:

    python -m omnia_radar_auditor.cli --input examples/sample_radar_stream.jsonl --out-dir report

It solves a concrete problem:

    given streams of structural observations over time,
    detect normal signal,
    drift,
    anomaly,
    and alert conditions.

In short:

    streams / observations over time -> signal / drift / anomaly / alert report

## What problem does it solve?

Systems often fail gradually before they fail visibly.

OMNIA-RADAR turns temporal structural movement into a reproducible audit:

    group observations by stream_id
    order each stream by time or step
    build a baseline window
    measure deviation from baseline
    measure step-to-step shock
    classify each observation as signal, drift, anomaly, or alert
    emit a reproducible certificate
    optionally fail CI when alerts appear

## Install

Clone the repository:

    git clone https://github.com/Tuttotorna/OMNIA-RADAR.git
    cd OMNIA-RADAR

Install locally:

    pip install -e .

The auditor only uses the Python standard library.

## Run

Run the sample audit:

    python -m omnia_radar_auditor.cli --input examples/sample_radar_stream.jsonl --out-dir report

Run and fail if alert is detected:

    python -m omnia_radar_auditor.cli --input examples/sample_radar_stream.jsonl --out-dir report --fail-on-alert

Run and fail if anomaly or alert is detected:

    python -m omnia_radar_auditor.cli --input examples/sample_radar_stream.jsonl --out-dir report --fail-on-anomaly

## Input format

The auditor accepts JSONL.

Required fields:

    stream_id
    step
    value

Optional fields:

    timestamp
    domain
    metric
    note

Example:

    {"stream_id":"omega_stream","step":1,"value":0.91}
    {"stream_id":"omega_stream","step":2,"value":0.90}
    {"stream_id":"omega_stream","step":3,"value":0.40}

Classification rule:

    signal  = stable movement inside baseline tolerance
    drift   = gradual deviation from baseline
    anomaly = strong deviation or shock
    alert   = critical deviation or repeated anomaly

## Output

The auditor writes:

    report.json
    report.csv
    report.html
    drift_events.jsonl
    anomaly_events.jsonl
    alert_events.jsonl
    certificate.json

Meaning:

    report.json
    Full structured radar analysis.

    report.csv
    Spreadsheet-friendly event summary.

    report.html
    Human-readable radar report.

    drift_events.jsonl
    One JSON object per drift event.

    anomaly_events.jsonl
    One JSON object per anomaly event.

    alert_events.jsonl
    One JSON object per alert event.

    certificate.json
    Reproducibility certificate with thresholds, counts, and boundary statement.

## CI gate

Fail when alert appears:

    python -m omnia_radar_auditor.cli --input examples/sample_radar_stream.jsonl --out-dir report --fail-on-alert

Fail when anomaly or alert appears:

    python -m omnia_radar_auditor.cli --input examples/sample_radar_stream.jsonl --out-dir report --fail-on-anomaly

Exit codes:

    0 = analysis completed without selected blocking condition
    2 = anomaly detected under --fail-on-anomaly
    3 = alert detected under --fail-on-alert or --fail-on-anomaly
    4 = invalid input or measurement error

## What this is not

This is not prediction.

It does not infer future truth.

It does not decide what action to take.

It measures structural movement inside the supplied stream boundary.

The boundary is explicit:

    measurement only;
    radar alert means structural deviation inside supplied streams,
    not semantic danger or future prediction.

## Why the rest of the repository still matters

The rest of this repository documents the radar concept:

    temporal structural monitoring
    signal movement
    drift
    anomaly
    alert
    baseline deviation
    shock detection
    measurement boundary

The code above is the operational entrypoint.

The repository below is the derivation path.

<!-- OMNIA_RADAR_AUDITOR_TOP_END -->

---

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
