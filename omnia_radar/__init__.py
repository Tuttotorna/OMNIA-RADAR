"""OMNIA-RADAR package.

Structural detection, drift surfacing, and signal persistence scanning layer.

Boundary:
    measurement != inference != decision
"""

__version__ = "1.0.0"

from omnia_radar.backbone_observer import (
    observe_backbone_envelope,
    observe_measurement,
)

__all__ = [
    "observe_backbone_envelope",
    "observe_measurement",
]
