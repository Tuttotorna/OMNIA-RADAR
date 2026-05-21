#!/usr/bin/env python3
"""
Local validation helper for OMNIA ecosystem repositories.

This helper avoids accidental import shadowing between sibling repositories.
In particular, lon-mirror contains a local omnia/ directory, while the
canonical OMNIA package must be loaded from the OMNIA repository.
"""

import os
import sys
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKDIR = ROOT.parent
OMNIA_DIR = WORKDIR / "OMNIA"
OMNIA_LIMIT_DIR = WORKDIR / "omnia-limit"
OMNIA_VALIDATION_DIR = WORKDIR / "OMNIA-VALIDATION"
OMNIA_INVARIANCE_DIR = WORKDIR / "OMNIA-INVARIANCE"


def run(cmd, env=None):
    print("$", " ".join(str(x) for x in cmd))
    return subprocess.run(cmd, cwd=str(ROOT), text=True, env=env).returncode


def main():
    env = os.environ.copy()
    env["OMNIA_SOURCE_DIR"] = str(OMNIA_DIR)

    priority = [
        str(OMNIA_DIR),
        str(OMNIA_LIMIT_DIR),
        str(OMNIA_VALIDATION_DIR),
        str(OMNIA_INVARIANCE_DIR),
    ]

    existing = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = os.pathsep.join([p for p in priority if Path(p).exists()] + ([existing] if existing else []))

    status = 0

    for dep in [OMNIA_DIR, OMNIA_LIMIT_DIR, OMNIA_VALIDATION_DIR, OMNIA_INVARIANCE_DIR]:
        if dep.exists() and (dep / "pyproject.toml").exists() and dep != ROOT:
            status |= run([sys.executable, "-m", "pip", "install", "-e", str(dep)], env=env)

    if (ROOT / "pyproject.toml").exists():
        status |= run([sys.executable, "-m", "pip", "install", "-e", "."], env=env)

    if (ROOT / "tests").exists():
        status |= run([sys.executable, "-m", "pytest", "-q"], env=env)
    else:
        print("No tests directory found.")

    return status


if __name__ == "__main__":
    raise SystemExit(main())
