from __future__ import annotations

from typing import Any

from omnia import build_boundary_certificate_from_measurement
from omnia_limit import validate_certificate
from omnia_validation.enveloper import process_boundary_step


def observe_backbone_envelope(envelope: dict[str, Any]) -> dict[str, Any]:
    """Observe a ValidationEnvelope without modifying backbone contracts.

    OMNIA-RADAR is an observer/consumer.

    It does not define BoundaryCertificate.
    It does not define ValidationEnvelope.
    It does not validate schema directly.
    It does not decide semantic truth.
    """

    status = envelope.get("validation_status")
    details = envelope.get("details", {})

    return {
        "observer": "OMNIA-RADAR",
        "role": "observer",
        "observed_status": status,
        "target_repository": details.get("target_repository"),
        "certificate_id": details.get("certificate_id"),
        "saturation_detected": details.get("saturation_detected"),
        "ast_deformation_index": details.get("ast_deformation_index"),
        "perturbation_step": details.get("perturbation_step"),
        "backbone_contract_preserved": True,
    }


def observe_measurement(
    measurement: dict[str, Any],
    *,
    target_repository: str = "OMNIA-RADAR",
    certificate_id: str | None = None,
    timestamp: str | None = None,
) -> dict[str, Any]:
    """Observe a measurement through the canonical OMNIA backbone.

    Flow:

    measurement
      -> OMNIA build_boundary_certificate_from_measurement()
      -> omnia-limit validate_certificate()
      -> OMNIA-VALIDATION process_boundary_step()
      -> ValidationEnvelope
      -> OMNIA-RADAR observation

    OMNIA-RADAR only observes the validated backbone output.
    """

    raw_certificate = build_boundary_certificate_from_measurement(
        measurement,
        target_repository=target_repository,
        certificate_id=certificate_id,
        timestamp=timestamp,
    )

    validate_certificate(raw_certificate)
    envelope = process_boundary_step(raw_certificate)

    return observe_backbone_envelope(envelope)
