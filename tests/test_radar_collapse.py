from __future__ import annotations

from omnia_radar.types import RadarInput
from omnia_radar.radar import radar_score


def test_radar_collapses_on_saturation() -> None:
    x = RadarInput(omega_coherence=0.9, sei=0.0, iri=0.2, drift=0.1)
    out = radar_score(x)
    assert out.radar_score == 0.0
    assert "SATURATED" in out.flags


def test_radar_collapses_on_irreversibility() -> None:
    x = RadarInput(omega_coherence=0.9, sei=0.8, iri=1.0, drift=0.1)
    out = radar_score(x)
    assert out.radar_score == 0.0
    assert "IRREVERSIBLE" in out.flags


def test_radar_collapses_on_unstable_drift() -> None:
    x = RadarInput(omega_coherence=0.9, sei=0.8, iri=0.2, drift=0.99)
    out = radar_score(x)
    assert out.radar_score == 0.0
    assert "DRIFT_UNSTABLE" in out.flags


def test_radar_positive_when_all_axes_pass() -> None:
    x = RadarInput(omega_coherence=0.9, sei=0.8, iri=0.2, drift=0.1)
    out = radar_score(x)
    assert out.radar_score > 0.0
    assert out.drift_gate > 0.0
    assert out.flags == []