# OMNIA-RADAR · Emergence Beyond Limit v3A

## Status

PARTIAL PASS (real-like scenario)

---

## Objective

Test OMNIA-RADAR on real-like text to evaluate whether it can distinguish between:

- human coherent text  
- degraded (LLM-like collapse) text  
- corrupted (noise-like) text  

---

## Dataset

Three categories:

### A — Human

Natural language sentences with:

- semantic coherence  
- structural variability  
- moderate repetition  

---

### B — Degraded

Simulated LLM failure patterns:

- word repetition loops  
- local collapse  
- reduced diversity  

---

### C — Corrupted

Artificially damaged text:

- shuffled word blocks  
- random noise injection  
- broken structure  

---

## Metrics

RADAR score (structure-only):

- compression ratio  
- entropy  
- n-gram entropy  
- autocorrelation  
- repetition ratio  

Interpretation:

```text
higher score → more structural regularity
lower score → closer to random noise


---

Results

mean human score:     1.834790
mean degraded score:  2.097762
mean corrupted score: 1.499944

Observed ordering:

degraded > human > corrupted


---

Interpretation

This result is correct under a structural lens.

RADAR measures:

regularity, repetition, compression

NOT:

semantic coherence or quality


---

Key Finding

degraded LLM-like text appears MORE structured than human text

Because:

repetition increases compressibility

loops reduce entropy

structure becomes mechanically rigid



---

Implication

structure != coherence != meaning

Specifically:

high structure can indicate degeneration

lower structure can indicate natural variability



---

Consequence for OMNIA-RADAR

RADAR alone cannot classify:

good vs bad
correct vs incorrect
meaningful vs meaningless

It can only detect:

presence and intensity of structure


---

Failure of v4 (Combined Gate)

Attempted integration with a coherence proxy failed:

all cases collapsed to UNCERTAIN

Reason:

coherence proxy was insufficient
thresholds were arbitrary


---

Conclusion

OMNIA-RADAR v3A demonstrates:

robust detection of structural patterns in real-like text

But also shows:

structure alone is not enough to evaluate validity


---

System Interpretation

RADAR → detects structure (including pathological structure)

OMNIA → must determine whether structure is coherent or degenerate


---

Next Step

Integrate OMNIA real metrics (Ω, IRI, SEI) instead of proxy coherence

Goal:

separate:
- coherent structure
- degenerate structure
- noise


---

Summary

v1 → strong structure detection
v2 → weak structure detection
v3A → structure vs noise vs degeneration (structural view)

v4 → failed classification → confirms need for real OMNIA layer