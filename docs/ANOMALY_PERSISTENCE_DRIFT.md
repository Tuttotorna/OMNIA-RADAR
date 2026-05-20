# Anomaly, Persistence, Drift

This document defines the public intuition behind recurring OMNIA-RADAR signal classes.

---

## Anomaly

An anomaly is unexpected structure under a declared scan.

Public intuition:

    something appears that should be inspected

An anomaly is not automatically an error.

It is not automatically a failure.

It is a signal candidate.

---

## Persistence

Persistence means that a signal remains visible across declared checks or basic variations.

Public intuition:

    the signal did not vanish immediately

Persistence makes a signal more interesting.

It does not make it true.

---

## Drift

Drift means that a signal moves across observations, transformations, or time.

Public intuition:

    the signal is not static

Drift may indicate instability, regime movement, or structural change.

It does not automatically prove semantic failure.

---

## Combined signal

A signal that is anomalous, persistent, and drifting may be worth full OMNIA measurement.

RADAR should mark such cases as candidates.

It should not decide their final meaning.

---

## Boundary

These signals remain detection-level signals.

They are not:

- final truth;
- semantic proof;
- full measurement;
- downstream decision;
- security finding;
- cryptographic finding.

The boundary remains:

    measurement != inference != decision

