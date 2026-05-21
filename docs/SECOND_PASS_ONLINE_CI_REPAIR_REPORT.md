# Second-Pass Online CI Repair Report

Repository: OMNIA-RADAR

Timestamp UTC: 2026-05-21T18:58:19Z

Purpose:
Repair remaining red GitHub Actions after first ecosystem CI repair.

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
      "id": 26246569625,
      "name": "CI",
      "status": "completed",
      "conclusion": "failure",
      "html_url": "https://github.com/Tuttotorna/OMNIA-RADAR/actions/runs/26246569625",
      "created_at": "2026-05-21T18:53:37Z",
      "updated_at": "2026-05-21T18:54:01Z",
      "head_sha": "4cbc54b3e94170bf37ee62179ab7393ce98081b3"
    }
  ]
}

Failed online log samples before repair:
{
  "ok": true,
  "failed_runs": [
    {
      "id": 26246569625,
      "name": "CI",
      "status": "completed",
      "conclusion": "failure",
      "html_url": "https://github.com/Tuttotorna/OMNIA-RADAR/actions/runs/26246569625",
      "created_at": "2026-05-21T18:53:37Z",
      "updated_at": "2026-05-21T18:54:01Z",
      "head_sha": "4cbc54b3e94170bf37ee62179ab7393ce98081b3"
    }
  ],
  "samples": [
    {
      "run_id": 26246569625,
      "download_ok": true,
      "html_url": "https://github.com/Tuttotorna/OMNIA-RADAR/actions/runs/26246569625",
      "samples": [
        {
          "file": "0_test _ python-3.12.txt",
          "lines": [
            "2026-05-21T18:53:44.3970323Z \u001b[36;1mpython -m pip install pytest numpy matplotlib jsonschema\u001b[0m",
            "2026-05-21T18:53:45.7110190Z Collecting pytest",
            "2026-05-21T18:53:45.7671275Z   Downloading pytest-9.0.3-py3-none-any.whl.metadata (7.6 kB)",
            "2026-05-21T18:53:46.1345820Z Collecting iniconfig>=1.0.1 (from pytest)",
            "2026-05-21T18:53:46.1518721Z Collecting packaging>=22 (from pytest)",
            "2026-05-21T18:53:46.1674319Z Collecting pluggy<2,>=1.5 (from pytest)",
            "2026-05-21T18:53:46.1882487Z Collecting pygments>=2.7.2 (from pytest)",
            "2026-05-21T18:53:47.0039933Z Downloading pytest-9.0.3-py3-none-any.whl (375 kB)",
            "2026-05-21T18:53:47.3620933Z Installing collected packages: typing-extensions, six, rpds-py, pyparsing, pygments, pluggy, pillow, packaging, numpy, kiwisolver, iniconfig, fonttools, cycler, attrs, referencing, python-dateutil, pytest, contourpy, matplotlib, jsonschema-specifications, jsonschema",
            "2026-05-21T18:53:53.9322957Z Successfully installed attrs-26.1.0 contourpy-1.3.3 cycler-0.12.1 fonttools-4.63.0 iniconfig-2.3.0 jsonschema-4.26.0 jsonschema-specifications-2025.9.1 kiwisolver-1.5.0 matplotlib-3.10.9 numpy-2.4.6 packaging-26.2 pillow-12.2.0 pluggy-1.6.0 pygments-2.20.0 pyparsing-3.3.2 pytest-9.0.3 python-dateutil-2.9.0.post0 referencing-0.37.0 rpds-py-0.30.0 six-1.17.0 typing-extensions-4.15.0",
            "2026-05-21T18:53:56.3389898Z \u001b[36;1m  python -m pytest -q\u001b[0m",
            "2026-05-21T18:53:56.7678535Z ==================================== ERRORS ====================================",
            "2026-05-21T18:53:56.7679316Z _______________ ERROR collecting tests/test_backbone_observer.py _______________",
            "2026-05-21T18:53:56.7680622Z ImportError while importing test module '/home/runner/work/OMNIA-RADAR/OMNIA-RADAR/tests/test_backbone_observer.py'.",
            "2026-05-21T18:53:56.7682179Z Traceback:",
            "2026-05-21T18:53:56.7687979Z E   ModuleNotFoundError: No module named 'omnia'",
            "2026-05-21T18:53:56.7688617Z ________________ ERROR collecting tests/test_radar_collapse.py _________________",
            "2026-05-21T18:53:56.7689804Z ImportError while importing test module '/home/runner/work/OMNIA-RADAR/OMNIA-RADAR/tests/test_radar_collapse.py'.",
            "2026-05-21T18:53:56.7691381Z Traceback:",
            "2026-05-21T18:53:56.7696882Z E   ModuleNotFoundError: No module named 'omnia'",
            "2026-05-21T18:53:56.7697995Z ERROR tests/test_backbone_observer.py",
            "2026-05-21T18:53:56.7698456Z ERROR tests/test_radar_collapse.py",
            "2026-05-21T18:53:56.7699717Z !!!!!!!!!!!!!!!!!!! Interrupted: 2 errors during collection !!!!!!!!!!!!!!!!!!!!",
            "2026-05-21T18:53:56.7700495Z 2 errors in 0.14s",
            "2026-05-21T18:53:56.7928242Z ##[error]Process completed with exit code 2."
          ]
        },
        {
          "file": "1_test _ python-3.11.txt",
          "lines": [
            "2026-05-21T18:53:44.5982706Z \u001b[36;1mpython -m pip install pytest numpy matplotlib jsonschema\u001b[0m",
            "2026-05-21T18:53:48.8334432Z Collecting pytest",
            "2026-05-21T18:53:48.9011976Z   Downloading pytest-9.0.3-py3-none-any.whl.metadata (7.6 kB)",
            "2026-05-21T18:53:49.2274841Z Collecting iniconfig>=1.0.1 (from pytest)",
            "2026-05-21T18:53:49.2441153Z Collecting packaging>=22 (from pytest)",
            "2026-05-21T18:53:49.2608937Z Collecting pluggy<2,>=1.5 (from pytest)",
            "2026-05-21T18:53:49.2834573Z Collecting pygments>=2.7.2 (from pytest)",
            "2026-05-21T18:53:50.0518643Z Downloading pytest-9.0.3-py3-none-any.whl (375 kB)",
            "2026-05-21T18:53:50.3924141Z Installing collected packages: typing-extensions, six, rpds-py, pyparsing, pygments, pluggy, pillow, packaging, numpy, kiwisolver, iniconfig, fonttools, cycler, attrs, referencing, python-dateutil, pytest, contourpy, matplotlib, jsonschema-specifications, jsonschema",
            "2026-05-21T18:53:55.3673643Z Successfully installed attrs-26.1.0 contourpy-1.3.3 cycler-0.12.1 fonttools-4.63.0 iniconfig-2.3.0 jsonschema-4.26.0 jsonschema-specifications-2025.9.1 kiwisolver-1.5.0 matplotlib-3.10.9 numpy-2.4.6 packaging-26.2 pillow-12.2.0 pluggy-1.6.0 pygments-2.20.0 pyparsing-3.3.2 pytest-9.0.3 python-dateutil-2.9.0.post0 referencing-0.37.0 rpds-py-0.30.0 six-1.17.0 typing-extensions-4.15.0",
            "2026-05-21T18:53:58.5810991Z \u001b[36;1m  python -m pytest -q\u001b[0m",
            "2026-05-21T18:53:59.2173532Z ==================================== ERRORS ====================================",
            "2026-05-21T18:53:59.2174822Z _______________ ERROR collecting tests/test_backbone_observer.py _______________",
            "2026-05-21T18:53:59.2176203Z ImportError while importing test module '/home/runner/work/OMNIA-RADAR/OMNIA-RADAR/tests/test_backbone_observer.py'.",
            "2026-05-21T18:53:59.2178190Z Traceback:",
            "2026-05-21T18:53:59.2184188Z E   ModuleNotFoundError: No module named 'omnia'",
            "2026-05-21T18:53:59.2184788Z ________________ ERROR collecting tests/test_radar_collapse.py _________________",
            "2026-05-21T18:53:59.2185790Z ImportError while importing test module '/home/runner/work/OMNIA-RADAR/OMNIA-RADAR/tests/test_radar_collapse.py'.",
            "2026-05-21T18:53:59.2187255Z Traceback:",
            "2026-05-21T18:53:59.2192587Z E   ModuleNotFoundError: No module named 'omnia'",
            "2026-05-21T18:53:59.2193681Z ERROR tests/test_backbone_observer.py",
            "2026-05-21T18:53:59.2194104Z ERROR tests/test_radar_collapse.py",
            "2026-05-21T18:53:59.2195076Z !!!!!!!!!!!!!!!!!!! Interrupted: 2 errors during collection !!!!!!!!!!!!!!!!!!!!",
            "2026-05-21T18:53:59.2195631Z 2 errors in 0.13s",
            "2026-05-21T18:53:59.2401989Z ##[error]Process completed with exit code 2."
          ]
        },
        {
          "file": "test _ python-3.11/4_Install tooling.txt",
          "lines": [
            "2026-05-21T18:53:44.5982702Z \u001b[36;1mpython -m pip install pytest numpy matplotlib jsonschema\u001b[0m",
            "2026-05-21T18:53:48.8334345Z Collecting pytest",
            "2026-05-21T18:53:48.9011903Z   Downloading pytest-9.0.3-py3-none-any.whl.metadata (7.6 kB)",
            "2026-05-21T18:53:49.2274795Z Collecting iniconfig>=1.0.1 (from pytest)",
            "2026-05-21T18:53:49.2441106Z Collecting packaging>=22 (from pytest)",
            "2026-05-21T18:53:49.2608909Z Collecting pluggy<2,>=1.5 (from pytest)",
            "2026-05-21T18:53:49.2834527Z Collecting pygments>=2.7.2 (from pytest)",
            "2026-05-21T18:53:50.0518636Z Downloading pytest-9.0.3-py3-none-any.whl (375 kB)",
            "2026-05-21T18:53:50.3924100Z Installing collected packages: typing-extensions, six, rpds-py, pyparsing, pygments, pluggy, pillow, packaging, numpy, kiwisolver, iniconfig, fonttools, cycler, attrs, referencing, python-dateutil, pytest, contourpy, matplotlib, jsonschema-specifications, jsonschema",
            "2026-05-21T18:53:55.3673354Z Successfully installed attrs-26.1.0 contourpy-1.3.3 cycler-0.12.1 fonttools-4.63.0 iniconfig-2.3.0 jsonschema-4.26.0 jsonschema-specifications-2025.9.1 kiwisolver-1.5.0 matplotlib-3.10.9 numpy-2.4.6 packaging-26.2 pillow-12.2.0 pluggy-1.6.0 pygments-2.20.0 pyparsing-3.3.2 pytest-9.0.3 python-dateutil-2.9.0.post0 referencing-0.37.0 rpds-py-0.30.0 six-1.17.0 typing-extensions-4.15.0"
          ]
        },
        {
          "file": "test _ python-3.11/6_Run tests when tests exist.txt",
          "lines": [
            "2026-05-21T18:53:58.5810989Z \u001b[36;1m  python -m pytest -q\u001b[0m",
            "2026-05-21T18:53:59.2173500Z ==================================== ERRORS ====================================",
            "2026-05-21T18:53:59.2174816Z _______________ ERROR collecting tests/test_backbone_observer.py _______________",
            "2026-05-21T18:53:59.2176196Z ImportError while importing test module '/home/runner/work/OMNIA-RADAR/OMNIA-RADAR/tests/test_backbone_observer.py'.",
            "2026-05-21T18:53:59.2178184Z Traceback:",
            "2026-05-21T18:53:59.2184184Z E   ModuleNotFoundError: No module named 'omnia'",
            "2026-05-21T18:53:59.2184784Z ________________ ERROR collecting tests/test_radar_collapse.py _________________",
            "2026-05-21T18:53:59.2185783Z ImportError while importing test module '/home/runner/work/OMNIA-RADAR/OMNIA-RADAR/tests/test_radar_collapse.py'.",
            "2026-05-21T18:53:59.2187251Z Traceback:",
            "2026-05-21T18:53:59.2192583Z E   ModuleNotFoundError: No module named 'omnia'",
            "2026-05-21T18:53:59.2193678Z ERROR tests/test_backbone_observer.py",
            "2026-05-21T18:53:59.2194100Z ERROR tests/test_radar_collapse.py",
            "2026-05-21T18:53:59.2194615Z !!!!!!!!!!!!!!!!!!! Interrupted: 2 errors during collection !!!!!!!!!!!!!!!!!!!!",
            "2026-05-21T18:53:59.2195626Z 2 errors in 0.13s",
            "2026-05-21T18:53:59.2401956Z ##[error]Process completed with exit code 2."
          ]
        },
        {
          "file": "test _ python-3.12/4_Install tooling.txt",
          "lines": [
            "2026-05-21T18:53:44.3970316Z \u001b[36;1mpython -m pip install pytest numpy matplotlib jsonschema\u001b[0m",
            "2026-05-21T18:53:45.7110097Z Collecting pytest",
            "2026-05-21T18:53:45.7671189Z   Downloading pytest-9.0.3-py3-none-any.whl.metadata (7.6 kB)",
            "2026-05-21T18:53:46.1345763Z Collecting iniconfig>=1.0.1 (from pytest)",
            "2026-05-21T18:53:46.1518659Z Collecting packaging>=22 (from pytest)",
            "2026-05-21T18:53:46.1674260Z Collecting pluggy<2,>=1.5 (from pytest)",
            "2026-05-21T18:53:46.1882394Z Collecting pygments>=2.7.2 (from pytest)",
            "2026-05-21T18:53:47.0039920Z Downloading pytest-9.0.3-py3-none-any.whl (375 kB)",
            "2026-05-21T18:53:47.3620885Z Installing collected packages: typing-extensions, six, rpds-py, pyparsing, pygments, pluggy, pillow, packaging, numpy, kiwisolver, iniconfig, fonttools, cycler, attrs, referencing, python-dateutil, pytest, contourpy, matplotlib, jsonschema-specifications, jsonschema",
            "2026-05-21T18:53:53.9322652Z Successfully installed attrs-26.1.0 contourpy-1.3.3 cycler-0.12.1 fonttools-4.63.0 iniconfig-2.3.0 jsonschema-4.26.0 jsonschema-specifications-2025.9.1 kiwisolver-1.5.0 matplotlib-3.10.9 numpy-2.4.6 packaging-26.2 pillow-12.2.0 pluggy-1.6.0 pygments-2.20.0 pyparsing-3.3.2 pytest-9.0.3 python-dateutil-2.9.0.post0 referencing-0.37.0 rpds-py-0.30.0 six-1.17.0 typing-extensions-4.15.0"
          ]
        },
        {
          "file": "test _ python-3.12/6_Run tests when tests exist.txt",
          "lines": [
            "2026-05-21T18:53:56.3389896Z \u001b[36;1m  python -m pytest -q\u001b[0m",
            "2026-05-21T18:53:56.7678528Z ==================================== ERRORS ====================================",
            "2026-05-21T18:53:56.7679310Z _______________ ERROR collecting tests/test_backbone_observer.py _______________",
            "2026-05-21T18:53:56.7680603Z ImportError while importing test module '/home/runner/work/OMNIA-RADAR/OMNIA-RADAR/tests/test_backbone_observer.py'.",
            "2026-05-21T18:53:56.7682175Z Traceback:",
            "2026-05-21T18:53:56.7687975Z E   ModuleNotFoundError: No module named 'omnia'",
            "2026-05-21T18:53:56.7688612Z ________________ ERROR collecting tests/test_radar_collapse.py _________________",
            "2026-05-21T18:53:56.7689790Z ImportError while importing test module '/home/runner/work/OMNIA-RADAR/OMNIA-RADAR/tests/test_radar_collapse.py'.",
            "2026-05-21T18:53:56.7691377Z Traceback:",
            "2026-05-21T18:53:56.7696879Z E   ModuleNotFoundError: No module named 'omnia'",
            "2026-05-21T18:53:56.7697992Z ERROR tests/test_backbone_observer.py",
            "2026-05-21T18:53:56.7698452Z ERROR tests/test_radar_collapse.py",
            "2026-05-21T18:53:56.7698984Z !!!!!!!!!!!!!!!!!!! Interrupted: 2 errors during collection !!!!!!!!!!!!!!!!!!!!",
            "2026-05-21T18:53:56.7700490Z 2 errors in 0.14s",
            "2026-05-21T18:53:56.7928217Z ##[error]Process completed with exit code 2."
          ]
        }
      ]
    }
  ]
}

Patch:
{
  "ci_changed": true,
  "legacy_non_dot_github_removed": [],
  "duplicate_test_workflows_removed": [],
  "python_version_policy": "3.12 only",
  "omnia_required_doi_command_present": null
}

Local tests:
{
  "status": "pass",
  "passed": 12,
  "failed": 0,
  "errors": 0,
  "returncode": 0,
  "summary": "12 passed in 2.01s"
}

Push:
null

After online check:
null
