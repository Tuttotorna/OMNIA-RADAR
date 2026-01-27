# OMNIA-RADAR (MB-X.01)

OMNIA-RADAR: structural opportunity detector  
(SEI-high / IRI-low growth zones)

This repository is part of the **MB-X.01 / OMNIA** ecosystem.

Canonical architecture and full map:  
https://github.com/Tuttotorna/lon-mirror/blob/main/ECOSYSTEM.md

---

**Author:** Massimiliano Brighindi  
**Signature:** MB-X.01 / Omniabase±  
**Contact:** brighissimo@gmail.com  

---

## Overview

**OMNIA-RADAR** is a structural opportunity detector.

It uses OMNIA measurements to identify domains where:

- **SEI is high** → structure is still extractable  
- **IRI is low** → no irreversible collapse has occurred  
- **Drift is controlled** → growth regime, not fragmentation  

RADAR does not optimize or decide.

It measures where growth is still possible beyond **OMNIA-LIMIT**.

---

## Core Idea

OMNIA-LIMIT marks saturation.

OMNIA-RADAR maps the remaining space:

- **LIMIT → excluded**  
- **Residual → opportunity**

Growth exists only outside the structural boundary.

---

## Structural Outputs

Given candidate trajectories or domains, RADAR measures:

- **Ω** coherence  
- **SEI** saturation gradient  
- **IRI** irreversibility risk  
- **OpportunityScore** ranking (RADAR)

Highest score = maximum remaining growth zone.

---

## Repository Contents

- `radar_scan.py`  
  Opportunity scanner computing Ω / SEI / IRI means across candidates

- `candidates/`  
  Folder containing domain trajectories in JSONL format

- Example candidate:  
  `candidates/human_trajectory.jsonl`

---

## Run

Place candidate domains in:

- `candidates/*.jsonl`

Then execute:

```bash
python radar_scan.py

Output:

Ω mean coherence

SEI mean saturation gradient

IRI mean irreversibility risk

OpportunityScore ranking



---

Notes

OMNIA-RADAR is measurement only.

It does not predict outcomes, enforce policy, or interpret meaning.

It is a structural sensor locating where:

saturation is not reached

irreversibility is minimal

opportunity remains measurable



---

MB-X.01 / OMNIA
Massimiliano Brighindi