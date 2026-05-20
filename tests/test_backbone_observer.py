from omnia_radar import observe_backbone_envelope, observe_measurement


def test_observe_measurement_stop_flow():
    measurement = {
        "drift_score": 0.44,
        "perturbation_step": 4,
        "gate_status": "STOP",
        "omega": 0.82,
        "sei": 0.01,
        "iri": 0.99,
    }

    observation = observe_measurement(
        measurement,
        target_repository="OMNIA-RADAR",
        certificate_id="radar-stop-cert",
        timestamp="2026-05-20T20:00:00Z",
    )

    assert observation["observer"] == "OMNIA-RADAR"
    assert observation["role"] == "observer"
    assert observation["observed_status"] == "GATE_CLOSED_SATURATION_REACHED"
    assert observation["certificate_id"] == "radar-stop-cert"
    assert observation["target_repository"] == "OMNIA-RADAR"
    assert observation["saturation_detected"] is True
    assert observation["ast_deformation_index"] == 0.44
    assert observation["perturbation_step"] == 4
    assert observation["backbone_contract_preserved"] is True


def test_observe_measurement_continue_flow():
    measurement = {
        "delta_omega": 0.12,
        "perturbation_step": 1,
        "gate_status": "CONTINUE",
        "omega": 0.91,
        "sei": 0.20,
        "iri": 0.40,
        "reason": "Additional measurement still yields structural information",
    }

    observation = observe_measurement(
        measurement,
        target_repository="OMNIA-RADAR",
        certificate_id="radar-continue-cert",
        timestamp="2026-05-20T20:00:00Z",
    )

    assert observation["observer"] == "OMNIA-RADAR"
    assert observation["role"] == "observer"
    assert observation["observed_status"] == "GATE_OPEN_MEASUREMENT_REQUIRED"
    assert observation["certificate_id"] == "radar-continue-cert"
    assert observation["target_repository"] == "OMNIA-RADAR"
    assert observation["saturation_detected"] is False
    assert observation["ast_deformation_index"] == 0.12
    assert observation["perturbation_step"] == 1
    assert observation["backbone_contract_preserved"] is True


def test_observe_existing_envelope_without_redefinition():
    envelope = {
        "envelope_id": "env-test",
        "timestamp": "2026-05-20T20:00:00Z",
        "validation_status": "GATE_CLOSED_SATURATION_REACHED",
        "details": {
            "target_repository": "OMNIA",
            "certificate_id": "existing-cert",
            "saturation_detected": True,
            "ast_deformation_index": 0.99,
            "perturbation_step": 7,
        },
    }

    observation = observe_backbone_envelope(envelope)

    assert observation["observer"] == "OMNIA-RADAR"
    assert observation["role"] == "observer"
    assert observation["observed_status"] == "GATE_CLOSED_SATURATION_REACHED"
    assert observation["target_repository"] == "OMNIA"
    assert observation["certificate_id"] == "existing-cert"
    assert observation["saturation_detected"] is True
    assert observation["ast_deformation_index"] == 0.99
    assert observation["perturbation_step"] == 7
    assert observation["backbone_contract_preserved"] is True
