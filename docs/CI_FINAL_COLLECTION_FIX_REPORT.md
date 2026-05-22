# CI Final Collection Fix Report

Repository: OMNIA-RADAR

Timestamp UTC: 2026-05-22T03:05:11Z

Purpose:
Fix online CI failures caused by pytest collecting _backbone repository tests and by missing omnia_validation installation.

No release was created.
No tag was created.

Boundary:
measurement != inference != decision

Patch:
{
  "ci_changed": true,
  "pytest_ini_changed": true,
  "python_version_policy": "3.12 only",
  "runs_local_tests_only": true,
  "omniavalidation_checkout_present": true,
  "omniavalidation_install_present": true,
  "backbone_excluded_from_pytest": true,
  "required_omnia_doi_command_present": null
}

Local tests:
{
  "status": "pass",
  "passed": 12,
  "failed": 0,
  "errors": 0,
  "returncode": 0,
  "summary": "12 passed in 1.80s"
}

Push:
null

After online check:
null

After failed logs:
null
