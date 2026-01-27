from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass(frozen=True)
class RadarInput:
    omega_coherence: float  # [0,1]
    sei: float              # [0,1]
    iri: float              # [0,1]
    drift: float            # [0,1] 0=stable, 1=unstable
    meta: Optional[Dict[str, Any]] = None


@dataclass(frozen=True)
class RadarOutput:
    radar_score: float
    drift_gate: float
    flags: List[str]
    breakdown: Dict[str, float]