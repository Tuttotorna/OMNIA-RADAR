# Production Readiness Notes

Repository: `OMNIA-RADAR`

Last hardening pass: `2026-05-21T14:03:44Z`

## Current role

Structural detection and drift surfacing layer.

## Current maturity label

`official adapter`

## Minimum readiness checklist

- [ ] Full test suite runs in GitHub Actions.
- [ ] CI supports Python 3.10, 3.11 and 3.12 where applicable.
- [ ] Runtime dependencies are explicit in `pyproject.toml`.
- [ ] Development dependencies are explicit.
- [ ] Boundary statement is present and consistent.
- [ ] Examples do not imply semantic truth or autonomous decision.
- [ ] Validation artifacts are reproducible.
- [ ] Release tag and package version are aligned.
- [ ] No workflow is stored outside `.github/workflows`.
- [ ] Security-sensitive naming is bounded by clear disclaimers.

## Required public boundary

```text
measurement != inference != decision
```

## Operational interpretation

This repository should be treated as part of a layered system, not as an isolated oracle.

The defensible interpretation is:

```text
output = structural measurement artifact
decision = external responsibility
semantics = outside the measurement contract
```

## Next hardening step

Run:

```bash
python scripts/local_validate.py
```

Then verify that the GitHub Actions workflow passes on the default branch.

<!-- CI_REPAIR_PASS_2026_05_21 -->

## CI repair pass

Last repair pass: `2026-05-21T14:19:12Z`

This pass preserves repository-specific CI assertions while also running the full test suite.

It also avoids accidental local-package shadowing by using `OMNIA_SOURCE_DIR` and by prioritizing the canonical `OMNIA` checkout in CI.
