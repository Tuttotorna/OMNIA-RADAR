#!/usr/bin/env python3
"""
Local validation helper for OMNIA ecosystem repositories.

This script is intentionally conservative:
- It checks whether a repository can be installed in editable mode when pyproject.toml exists.
- It runs pytest when tests/ exists.
- It does not decide scientific validity.
- It only reports packaging/test readiness.
"""

import os
import sys
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def run(cmd):
    print("$", " ".join(cmd))
    return subprocess.run(cmd, cwd=str(ROOT), text=True).returncode

def main():
    status = 0

    if (ROOT / "pyproject.toml").exists():
        status |= run([sys.executable, "-m", "pip", "install", "-e", "."])

    if (ROOT / "tests").exists():
        status |= run([sys.executable, "-m", "pytest", "-q"])
    else:
        print("No tests directory found.")

    return status

if __name__ == "__main__":
    raise SystemExit(main())
