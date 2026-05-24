import subprocess
import sys

from omnia_radar_auditor.core import (
    Observation,
    analyze_observations,
    char_similarity,
    normalize_value,
    numeric_deviation,
    parse_number,
    read_jsonl,
    structural_deviation,
)


def test_normalize_value():
    assert normalize_value("  STOP!! ") == "stop"
    assert normalize_value("A   B") == "a b"


def test_parse_number():
    assert parse_number("1.25") == 1.25
    assert parse_number("-2") == -2.0
    assert parse_number("abc") is None


def test_numeric_deviation_small():
    assert numeric_deviation(0.99, 1.0) < 0.02


def test_numeric_deviation_large():
    assert numeric_deviation(0.2, 1.0) >= 0.55


def test_structural_deviation_stable():
    assert structural_deviation("STOP", "stop") == 0.0


def test_structural_deviation_large():
    assert structural_deviation("CONTINUE", "STOP") >= 0.30


def test_char_similarity_identity():
    assert char_similarity("abc", "abc") == 1.0


def test_analyze_observations_counts():
    observations = [
        Observation("s1", 1, "1.0", "", "", "", ""),
        Observation("s1", 2, "1.0", "", "", "", ""),
        Observation("s1", 3, "1.0", "", "", "", ""),
        Observation("s1", 4, "0.7", "", "", "", ""),
        Observation("s1", 5, "0.2", "", "", "", ""),
        Observation("s2", 1, "CONTINUE", "", "", "", ""),
        Observation("s2", 2, "CONTINUE", "", "", "", ""),
        Observation("s2", 3, "STOP", "", "", "", ""),
    ]

    result = analyze_observations(observations, baseline_window=2)
    assert result["summary"]["total_streams"] == 2
    assert result["summary"]["total_events"] == 8
    assert result["summary"]["alert"] >= 1
    assert "certificate" in result


def test_read_jsonl(tmp_path):
    p = tmp_path / "stream.jsonl"
    p.write_text(
        '{"stream_id":"x","step":1,"value":1}\n'
        '{"stream_id":"x","step":2,"value":1}\n',
        encoding="utf-8",
    )

    rows = read_jsonl(str(p))
    assert len(rows) == 2
    assert rows[0].stream_id == "x"


def test_duplicate_rejected(tmp_path):
    p = tmp_path / "stream.jsonl"
    p.write_text(
        '{"stream_id":"x","step":1,"value":1}\n'
        '{"stream_id":"x","step":1,"value":2}\n',
        encoding="utf-8",
    )

    try:
        read_jsonl(str(p))
        assert False, "expected duplicate error"
    except ValueError as e:
        assert "Duplicate" in str(e)


def test_cli_writes_reports(tmp_path):
    input_path = tmp_path / "stream.jsonl"
    out_dir = tmp_path / "report"

    input_path.write_text(
        '{"stream_id":"a","step":1,"value":1.0}\n'
        '{"stream_id":"a","step":2,"value":1.0}\n'
        '{"stream_id":"a","step":3,"value":1.0}\n'
        '{"stream_id":"a","step":4,"value":0.2}\n',
        encoding="utf-8",
    )

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "omnia_radar_auditor.cli",
            "--input",
            str(input_path),
            "--out-dir",
            str(out_dir),
        ],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    assert result.returncode == 0
    assert (out_dir / "report.json").exists()
    assert (out_dir / "report.csv").exists()
    assert (out_dir / "report.html").exists()
    assert (out_dir / "drift_events.jsonl").exists()
    assert (out_dir / "anomaly_events.jsonl").exists()
    assert (out_dir / "alert_events.jsonl").exists()
    assert (out_dir / "certificate.json").exists()


def test_cli_fail_on_alert(tmp_path):
    input_path = tmp_path / "stream.jsonl"
    out_dir = tmp_path / "report"

    input_path.write_text(
        '{"stream_id":"a","step":1,"value":1.0}\n'
        '{"stream_id":"a","step":2,"value":1.0}\n'
        '{"stream_id":"a","step":3,"value":1.0}\n'
        '{"stream_id":"a","step":4,"value":0.1}\n',
        encoding="utf-8",
    )

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "omnia_radar_auditor.cli",
            "--input",
            str(input_path),
            "--out-dir",
            str(out_dir),
            "--fail-on-alert",
        ],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    assert result.returncode == 3


def test_cli_stable_only_passes_gate(tmp_path):
    input_path = tmp_path / "stream.jsonl"
    out_dir = tmp_path / "report"

    input_path.write_text(
        '{"stream_id":"a","step":1,"value":1.0}\n'
        '{"stream_id":"a","step":2,"value":1.001}\n'
        '{"stream_id":"a","step":3,"value":1.0}\n'
        '{"stream_id":"a","step":4,"value":1.002}\n',
        encoding="utf-8",
    )

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "omnia_radar_auditor.cli",
            "--input",
            str(input_path),
            "--out-dir",
            str(out_dir),
            "--fail-on-anomaly",
        ],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    assert result.returncode == 0
