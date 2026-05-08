
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_public_entrypoints_exist():
    required = [
        "README.md",
        "LICENSE",
        "CITATION.cff",
        "pyproject.toml",
        "RADAR_SCHEMA.md",
        "docs/RADAR_SCOPE.md",
        "docs/RESULTS_INDEX.md",
        "docs/REPOSITORY_STATUS.md",
    ]
    for rel in required:
        assert (ROOT / rel).exists(), rel

def test_core_directories_exist():
    for rel in ["docs", "examples", "results", "tests", "omnia_radar"]:
        assert (ROOT / rel).exists(), rel

def test_key_examples_exist():
    required = [
        "examples/minimal_radar_demo.py",
        "examples/radar_demo.py",
        "examples/radar_minimal.py",
        "examples/radar_sample.json",
    ]
    for rel in required:
        assert (ROOT / rel).exists(), rel

def test_package_files_exist():
    required = [
        "omnia_radar/__init__.py",
        "omnia_radar/radar.py",
        "omnia_radar/types.py",
    ]
    for rel in required:
        assert (ROOT / rel).exists(), rel

def test_readme_boundary_terms():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "measurement != inference != decision" in text
    assert "not a truth oracle" in text
    assert "not a semantic judge" in text
    assert "Decision remains external" in text
    assert "structure != meaning" in text
