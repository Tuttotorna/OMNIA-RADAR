# Ecosystem Role

    Repository: `OMNIA-RADAR`

    Last hardening pass: `2026-05-21T14:03:44Z`

    ## Role

    Structural detection and drift surfacing layer.

    ## Status

    `official adapter`

    ## Contract

    Detects candidate structural signals before or around full OMNIA measurement.

    ## Boundary

    This repository belongs to the MB-X.01 / OMNIA ecosystem.

    The common boundary is:

    ```text
    measurement != inference != decision
    ```

    Structural measurement may expose stability, instability, drift, collapse, invariance or boundary conditions.
    It does not by itself declare semantic truth and does not make external decisions.

    ## Backbone

    The operational backbone is:

    - `OMNIA`
- `omnia-limit`
- `OMNIA-VALIDATION`

    ## Satellite / adapter layer

    Current satellite or adapter repositories are:

    - `OMNIABASE`
- `OMNIA-RADAR`
- `OMNIA-SECURITY`
- `OMNIA-CRYPTO`
- `OMNIAMIND`
- `OMNIA-THREE-BODY`
- `OMNIA-INVARIANCE`
- `OMNIA-CONSTANT`

    ## Recommended integration direction

    ```text
    RADAR detects
    OMNIA measures
    INVARIANCE tests survival under transformation
    LIMIT stops or certifies boundary conditions
    VALIDATION records evidence and regression
    ```

    ## Public positioning

    The shortest public statement is:

    ```text
    OMNIA measures structural stability beyond correctness.
    ```
