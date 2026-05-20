# RADAR Overview

OMNIA-RADAR is the structural signal detection layer of the MB-X.01 / OMNIA ecosystem.

It exists because not every trace, output, or representation should immediately be treated as a full measurement target.

Canonical boundary:

    measurement != inference != decision

---

## RADAR pipeline

The core pipeline is:

    candidate trace
      -> signal scan
      -> anomaly / persistence / drift
      -> measurement candidate
      -> external validation

Meaning:

| Stage | Role |
|---|---|
| candidate trace | The object, output, trace, or sequence being scanned |
| signal scan | The detection procedure |
| anomaly | Unexpected structure |
| persistence | Signal that survives basic variation |
| drift | Signal movement across observations |
| measurement candidate | Something worth sending to OMNIA |
| external validation | Artifact testing outside RADAR |

---

## What makes OMNIA-RADAR different

OMNIA-RADAR is not trying to answer:

    Is this true?

It asks:

    Is there a structural signal worth measuring?

This is a narrower claim.

That narrowness is intentional.

---

## Correct use

Correct use:

    scan candidate traces
    detect possible structural signal
    mark anomaly, persistence, or drift
    send relevant candidates to OMNIA
    validate artifacts externally

Incorrect use:

    treat detection as proof
    treat anomaly as verdict
    treat persistence as semantic truth
    treat drift as final failure
    treat RADAR as a security scanner

---

## Relation to OMNIA

RADAR detects structural signal candidates.

OMNIA measures structural behavior.

OMNIA-VALIDATION validates artifacts and claims.

