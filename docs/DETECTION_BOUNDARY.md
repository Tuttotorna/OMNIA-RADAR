# Detection Boundary

OMNIA-RADAR follows the ecosystem boundary:

    measurement != inference != decision

For this repository, the operational version is stricter:

    detection != measurement != inference != decision

---

## Meaning

Detection means:

    identify possible structural signal candidates under declared scan conditions.

Measurement means:

    quantify or evaluate structural behavior under declared conditions.

Inference means:

    interpret the measurement or detection.

Decision means:

    act on the interpretation.

OMNIA-RADAR detects.

It does not measure fully.

It does not infer.

It does not decide.

---

## Allowed claims

OMNIA-RADAR may claim:

- a candidate was scanned;
- a signal candidate was detected;
- an anomaly appeared under declared scan conditions;
- a signal persisted across declared checks;
- a signal drifted across observations;
- a candidate should be sent to OMNIA or validation.

---

## Disallowed claims

OMNIA-RADAR should not claim by itself:

- this is semantically true;
- this is semantically false;
- this is a final structural measurement;
- this is a security vulnerability;
- this is a cryptographic weakness;
- this downstream decision is correct.

---

## Rule

The output must preserve the distinction:

    detection signal
    measurement candidate
    structural measurement
    interpretation
    external decision

