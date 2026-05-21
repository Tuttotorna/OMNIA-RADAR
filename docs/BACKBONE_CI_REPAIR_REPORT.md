# Backbone CI Repair Report

Repository: OMNIA-RADAR

Timestamp UTC: 2026-05-21T19:05:35Z

Purpose:
Repair remaining red GitHub Actions caused by missing online backbone package installation.

No release was created.
No tag was created.
Only CI workflow files and this repair report were changed.

Boundary:
measurement != inference != decision

Before:
{
  "green": false,
  "status": "failed",
  "reason": "At least one Actions run for current HEAD failed.",
  "runs": [
    {
      "id": 26246941177,
      "name": "CI",
      "status": "completed",
      "conclusion": "failure",
      "html_url": "https://github.com/Tuttotorna/OMNIA-RADAR/actions/runs/26246941177",
      "created_at": "2026-05-21T19:00:53Z",
      "updated_at": "2026-05-21T19:01:18Z",
      "head_sha": "d5db2b5a03e0f0c5cc2ec222c84a009704edce02"
    }
  ]
}

Patch:
{
  "ci_changed": true,
  "legacy_non_dot_github_removed": [],
  "duplicate_test_workflows_removed": [],
  "python_version_policy": "3.12 only",
  "backbone_installs": {
    "OMNIA": true,
    "omnia-limit": true,
    "OMNIA-INVARIANCE": true
  },
  "required_omnia_doi_command_present": null
}

Local tests:
{
  "status": "pass",
  "passed": 12,
  "failed": 0,
  "errors": 0,
  "returncode": 0,
  "summary": "12 passed in 1.47s"
}

Push:
null

After online check:
null

After failed logs:
null
