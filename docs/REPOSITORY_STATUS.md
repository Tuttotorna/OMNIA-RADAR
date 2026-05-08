# OMNIA-RADAR Repository Status

Generated / updated: 2026-05-08T18:54:19.899676+00:00

## Status

OMNIA-RADAR is an operational structural detection repository.

It contains:

- package code in `omnia_radar/`
- examples
- tests
- candidate traces
- result artifacts
- experimental documentation
- schema reference

## Cleanup performed

This cleanup strengthens public presentation:

- README.md rewritten with valid Markdown
- DOI badge corrected
- CITATION.cff added
- LICENSE added
- pyproject.toml corrected
- omnia_radar/__init__.py added
- docs/RADAR_SCOPE.md added
- docs/RESULTS_INDEX.md added
- docs/REPOSITORY_STATUS.md added
- tests/test_repository_smoke.py added
- GitHub About / Homepage / Topics aligned
- GitHub Release updated or created

## Current technical status

Clean-environment checks:

```text
import omnia_radar OK
pip install -e .  OK
pytest            expected pass
```

## Boundary

```text
measurement != inference != decision
structure != meaning
structure != truth
```

## DOI

```text
10.5281/zenodo.19829096
https://doi.org/10.5281/zenodo.19829096
```
