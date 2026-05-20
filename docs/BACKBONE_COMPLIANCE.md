# OMNIA-RADAR Backbone Compliance

## Role

OMNIA-RADAR is an observer/consumer.

It observes validated backbone output.

It is not the measurement engine.

It is not the boundary validator.

It is not the validation control plane.

It is not a decision engine.

## Canonical flow

OMNIA-RADAR observes the existing backbone:

measurement
  -> OMNIA build_boundary_certificate_from_measurement()
  -> BoundaryCertificate
  -> omnia-limit validate_certificate()
  -> OMNIA-VALIDATION process_boundary_step()
  -> ValidationEnvelope
  -> OMNIA-RADAR observation

## Public API

OMNIA-RADAR exposes:

observe_measurement(...)
observe_backbone_envelope(...)

## Contract rule

OMNIA-RADAR does not redefine BoundaryCertificate.

OMNIA-RADAR does not redefine ValidationEnvelope.

OMNIA-RADAR does not bypass omnia-limit.

OMNIA-RADAR does not bypass OMNIA-VALIDATION.

OMNIA-RADAR observes the result of the backbone.

## Boundary

measurement != validation
validation != orchestration
orchestration != decision
observation != validation
observation != decision

OMNIA-RADAR stays in the observer/consumer layer.
