# Quickstart RADAR

This document gives the fastest path to seeing OMNIA-RADAR as a structural signal detection layer.

The public mental model is:

    candidate trace -> signal scan -> anomaly / persistence / drift -> measurement candidate

---

## Clean install

    git clone https://github.com/Tuttotorna/OMNIA-RADAR.git
    cd OMNIA-RADAR
    python -m pip install -e .
    pytest

---

## What to look for

After installation and tests, look for the smallest available example.

The point is not to prove the whole ecosystem.

The point is to identify:

    What candidate trace is being scanned?
    What signal scan is applied?
    Is an anomaly detected?
    Does a signal persist?
    Does the signal drift?
    What becomes a measurement candidate?
    What does the scan not prove?

---

## Expected detection behavior

A good OMNIA-RADAR path should produce a detection artifact.

It should not silently become:

    semantic judgment
    final decision
    full measurement
    truth certificate
    security scan
    cryptographic proof

---

## Public compression

    OMNIA-RADAR detects possible structural signals.
    OMNIA measures structural behavior.
    OMNIA-VALIDATION tests artifacts.

