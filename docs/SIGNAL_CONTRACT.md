# Signal Contract

This document defines the public shape expected from OMNIA-RADAR detection results.

The goal is clarity.

A reviewer should understand what was scanned, what signal was detected, and what the detection does not prove.

---

## Detection unit

A RADAR detection result should contain:

| Component | Required | Meaning |
|---|---:|---|
| case_id | yes | Stable identifier for the detection case |
| candidate_ref | yes | The trace, output, representation, or sequence being scanned |
| scan_mode | yes | The detection mode or protocol |
| anomaly_signal | preferred | Unexpected structural behavior |
| persistence_signal | preferred | Signal stability across basic checks |
| drift_signal | preferred | Signal movement across observations |
| radar_result | yes | no_signal, candidate, anomaly, persistent, drifting, or inconclusive |
| measurement_candidate | preferred | Whether the case should be sent to OMNIA |
| limitation | yes | What the detection does not prove |
| external_validation | yes | How the result should be validated later |

---

## Minimal JSON shape

A minimal RADAR artifact can use this shape:

    {{
      "case_id": "radar-example-001",
      "candidate_ref": "path-or-description",
      "scan_mode": "declared scan mode",
      "anomaly_signal": "declared signal or null",
      "persistence_signal": "declared signal or null",
      "drift_signal": "declared signal or null",
      "radar_result": "no_signal | candidate | anomaly | persistent | drifting | inconclusive",
      "measurement_candidate": true,
      "boundary": "measurement != inference != decision",
      "limitation": "What this detection does not prove",
      "external_validation": "Validate through OMNIA-VALIDATION or declared artifact checks"
    }}

---

## Result vocabulary

Use a small vocabulary:

    no_signal
    candidate
    anomaly
    persistent
    drifting
    inconclusive

Meaning:

- no_signal: no relevant signal detected under declared scan;
- candidate: a possible signal should be measured;
- anomaly: unexpected structure appears;
- persistent: signal survives basic checks;
- drifting: signal moves across observations;
- inconclusive: evidence is insufficient.

---

## No silent promotion

A detection result must not silently become a final measurement.

A detected anomaly is not a verdict.

A persistent signal is not semantic truth.

A measurement candidate is not a decision.

