import csv
import json
import math
import re
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional


@dataclass(frozen=True)
class Observation:
    stream_id: str
    step: float
    value: str
    timestamp: str
    domain: str
    metric: str
    note: str


@dataclass(frozen=True)
class RadarEvent:
    stream_id: str
    step: float
    timestamp: str
    value: str
    status: str
    baseline_value: Optional[float]
    numeric_value: Optional[float]
    deviation_score: float
    shock_score: float
    radar_score: float
    metric: str
    domain: str
    note: str


def normalize_value(value: Any) -> str:
    text = "" if value is None else str(value)
    text = text.strip().lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-z0-9\.\-\+\s]", "", text)
    return text.strip()


def parse_number(value: Any) -> Optional[float]:
    text = normalize_value(value)
    if not text:
        return None

    if re.fullmatch(r"[-+]?\d+(\.\d+)?", text):
        try:
            return float(text)
        except Exception:
            return None

    return None


def char_similarity(a: str, b: str) -> float:
    na = normalize_value(a)
    nb = normalize_value(b)

    if na == nb:
        return 1.0

    if not na or not nb:
        return 0.0

    m = len(na)
    n = len(nb)
    previous = list(range(n + 1))

    for i in range(1, m + 1):
        current = [i] + [0] * n
        for j in range(1, n + 1):
            cost = 0 if na[i - 1] == nb[j - 1] else 1
            current[j] = min(previous[j] + 1, current[j - 1] + 1, previous[j - 1] + cost)
        previous = current

    distance = previous[n]
    scale = max(m, n)
    return max(0.0, 1.0 - (distance / scale))


def numeric_deviation(value: float, baseline: float) -> float:
    scale = max(abs(value), abs(baseline), 1.0)
    return round(abs(value - baseline) / scale, 12)


def numeric_shock(current: float, previous: Optional[float]) -> float:
    if previous is None:
        return 0.0
    scale = max(abs(current), abs(previous), 1.0)
    return round(abs(current - previous) / scale, 12)


def structural_deviation(value: str, baseline: str) -> float:
    return round(1.0 - char_similarity(value, baseline), 12)


def read_jsonl(path: str) -> List[Observation]:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(path)

    observations = []

    with p.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            raw = line.strip()
            if not raw:
                continue

            try:
                obj = json.loads(raw)
            except json.JSONDecodeError as e:
                raise ValueError("Invalid JSONL at line " + str(line_no) + ": " + str(e))

            for field in ["stream_id", "step", "value"]:
                if field not in obj:
                    raise ValueError("Missing required field '" + field + "' at line " + str(line_no))

            try:
                step = float(obj["step"])
            except Exception:
                raise ValueError("Invalid numeric step at line " + str(line_no))

            observations.append(
                Observation(
                    stream_id=str(obj["stream_id"]),
                    step=step,
                    value=str(obj["value"]),
                    timestamp=str(obj.get("timestamp", "")),
                    domain=str(obj.get("domain", "")),
                    metric=str(obj.get("metric", "")),
                    note=str(obj.get("note", "")),
                )
            )

    if not observations:
        raise ValueError("No observations found in " + path)

    seen = set()
    for obs in observations:
        key = (obs.stream_id, obs.step, obs.metric)
        if key in seen:
            raise ValueError("Duplicate stream_id + step + metric: " + obs.stream_id + " / " + str(obs.step) + " / " + obs.metric)
        seen.add(key)

    return observations


def group_observations(observations: List[Observation]) -> Dict[str, List[Observation]]:
    grouped = defaultdict(list)
    for obs in observations:
        grouped[obs.stream_id].append(obs)
    return dict(grouped)


def classify_event(
    deviation_score: float,
    shock_score: float,
    previous_status: str,
    drift_threshold: float,
    anomaly_threshold: float,
    alert_threshold: float,
) -> str:
    radar_score = max(deviation_score, shock_score)

    if radar_score >= alert_threshold:
        return "alert"

    if radar_score >= anomaly_threshold:
        if previous_status == "anomaly":
            return "alert"
        return "anomaly"

    if radar_score >= drift_threshold:
        return "drift"

    return "signal"


def analyze_stream(
    stream_id: str,
    observations: List[Observation],
    baseline_window: int = 3,
    drift_threshold: float = 0.10,
    anomaly_threshold: float = 0.30,
    alert_threshold: float = 0.55,
) -> List[RadarEvent]:
    ordered = sorted(observations, key=lambda x: x.step)

    if baseline_window < 1:
        baseline_window = 1

    baseline_slice = ordered[:baseline_window]

    numeric_values = [parse_number(obs.value) for obs in ordered]
    all_numeric = all(v is not None for v in numeric_values)

    events = []
    previous_numeric = None
    previous_text = None
    previous_status = "signal"

    if all_numeric:
        baseline_numbers = [parse_number(obs.value) for obs in baseline_slice]
        baseline_value = sum(baseline_numbers) / len(baseline_numbers)
        baseline_text = ""
    else:
        baseline_value = None
        baseline_text = normalize_value(baseline_slice[0].value)

    for obs in ordered:
        numeric_value = parse_number(obs.value)

        if all_numeric:
            deviation = numeric_deviation(numeric_value, baseline_value)
            shock = numeric_shock(numeric_value, previous_numeric)
            previous_numeric = numeric_value
        else:
            deviation = structural_deviation(obs.value, baseline_text)
            shock = 0.0 if previous_text is None else structural_deviation(obs.value, previous_text)
            previous_text = obs.value

        status = classify_event(
            deviation_score=deviation,
            shock_score=shock,
            previous_status=previous_status,
            drift_threshold=drift_threshold,
            anomaly_threshold=anomaly_threshold,
            alert_threshold=alert_threshold,
        )

        radar_score = round(max(deviation, shock), 12)

        events.append(
            RadarEvent(
                stream_id=stream_id,
                step=obs.step,
                timestamp=obs.timestamp,
                value=obs.value,
                status=status,
                baseline_value=round(baseline_value, 12) if baseline_value is not None else None,
                numeric_value=numeric_value,
                deviation_score=deviation,
                shock_score=shock,
                radar_score=radar_score,
                metric=obs.metric,
                domain=obs.domain,
                note=obs.note,
            )
        )

        previous_status = status

    return events


def analyze_observations(
    observations: List[Observation],
    baseline_window: int = 3,
    drift_threshold: float = 0.10,
    anomaly_threshold: float = 0.30,
    alert_threshold: float = 0.55,
) -> Dict[str, Any]:
    grouped = group_observations(observations)

    events = []
    for stream_id, items in sorted(grouped.items()):
        events.extend(
            analyze_stream(
                stream_id=stream_id,
                observations=items,
                baseline_window=baseline_window,
                drift_threshold=drift_threshold,
                anomaly_threshold=anomaly_threshold,
                alert_threshold=alert_threshold,
            )
        )

    rows = [asdict(e) for e in events]

    signal_rows = [r for r in rows if r["status"] == "signal"]
    drift_rows = [r for r in rows if r["status"] == "drift"]
    anomaly_rows = [r for r in rows if r["status"] == "anomaly"]
    alert_rows = [r for r in rows if r["status"] == "alert"]

    total_events = len(rows)
    total_streams = len(grouped)
    worst = max(rows, key=lambda r: r["radar_score"]) if rows else None

    summary = {
        "total_streams": total_streams,
        "total_events": total_events,
        "signal": len(signal_rows),
        "drift": len(drift_rows),
        "anomaly": len(anomaly_rows),
        "alert": len(alert_rows),
        "signal_rate": round(len(signal_rows) / total_events, 12) if total_events else 0.0,
        "drift_rate": round(len(drift_rows) / total_events, 12) if total_events else 0.0,
        "anomaly_rate": round(len(anomaly_rows) / total_events, 12) if total_events else 0.0,
        "alert_rate": round(len(alert_rows) / total_events, 12) if total_events else 0.0,
        "max_radar_score": worst["radar_score"] if worst else None,
        "worst_stream_id": worst["stream_id"] if worst else None,
        "worst_step": worst["step"] if worst else None,
        "problem_solved": "Measures signal, drift, anomaly, and alert states across supplied observation streams.",
    }

    certificate = {
        "audit_type": "omnia_radar_audit",
        "summary": summary,
        "thresholds": {
            "baseline_window": baseline_window,
            "drift_threshold": drift_threshold,
            "anomaly_threshold": anomaly_threshold,
            "alert_threshold": alert_threshold,
        },
        "boundary": "measurement only; radar alert means structural deviation inside supplied streams, not semantic danger or future prediction",
        "measurement_language": [
            "stream_id",
            "step",
            "baseline_deviation",
            "shock_score",
            "radar_score",
            "signal_drift_anomaly_alert",
        ],
    }

    return {
        "summary": summary,
        "thresholds": {
            "baseline_window": baseline_window,
            "drift_threshold": drift_threshold,
            "anomaly_threshold": anomaly_threshold,
            "alert_threshold": alert_threshold,
        },
        "certificate": certificate,
        "events": rows,
    }


def write_json(path: str, obj: Any) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_csv_report(path: str, result: Dict[str, Any]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

    fields = [
        "stream_id",
        "step",
        "timestamp",
        "status",
        "value",
        "baseline_value",
        "numeric_value",
        "deviation_score",
        "shock_score",
        "radar_score",
        "metric",
        "domain",
        "note",
    ]

    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()

        for row in result["events"]:
            writer.writerow({k: row.get(k, "") for k in fields})


def html_escape(x: Any) -> str:
    return str(x).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def write_html_report(path: str, result: Dict[str, Any]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

    summary = result["summary"]

    rows = []
    for r in result["events"]:
        if r["status"] == "signal":
            continue

        rows.append(
            "<tr>"
            + "<td>" + html_escape(r["stream_id"]) + "</td>"
            + "<td>" + html_escape(r["step"]) + "</td>"
            + "<td>" + html_escape(r["status"]) + "</td>"
            + "<td>" + html_escape(r["value"]) + "</td>"
            + "<td>" + html_escape(r["deviation_score"]) + "</td>"
            + "<td>" + html_escape(r["shock_score"]) + "</td>"
            + "<td>" + html_escape(r["radar_score"]) + "</td>"
            + "<td>" + html_escape(r["note"]) + "</td>"
            + "</tr>"
        )

    html = """
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>OMNIA Radar Report</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      margin: 32px;
      line-height: 1.45;
    }}
    table {{
      border-collapse: collapse;
      width: 100%;
    }}
    th, td {{
      border: 1px solid #ddd;
      padding: 8px;
      vertical-align: top;
    }}
    th {{
      background: #f2f2f2;
    }}
    .box {{
      background: #f8f8f8;
      padding: 16px;
      margin-bottom: 24px;
      border: 1px solid #eee;
    }}
  </style>
</head>
<body>
  <h1>OMNIA Radar Report</h1>

  <div class="box">
    <p><b>Total streams:</b> {total_streams}</p>
    <p><b>Total events:</b> {total_events}</p>
    <p><b>Signal:</b> {signal}</p>
    <p><b>Drift:</b> {drift}</p>
    <p><b>Anomaly:</b> {anomaly}</p>
    <p><b>Alert:</b> {alert}</p>
    <p><b>Max radar score:</b> {max_radar_score}</p>
    <p><b>Worst stream:</b> {worst_stream_id}</p>
  </div>

  <h2>Drift / Anomaly / Alert Events</h2>

  <table>
    <tr>
      <th>Stream</th>
      <th>Step</th>
      <th>Status</th>
      <th>Value</th>
      <th>Deviation</th>
      <th>Shock</th>
      <th>Radar score</th>
      <th>Note</th>
    </tr>
    {rows}
  </table>

  <h2>Boundary</h2>
  <p>Radar alert means structural deviation inside supplied streams. This is not semantic danger or future prediction.</p>
</body>
</html>
""".format(
        total_streams=summary["total_streams"],
        total_events=summary["total_events"],
        signal=summary["signal"],
        drift=summary["drift"],
        anomaly=summary["anomaly"],
        alert=summary["alert"],
        max_radar_score=summary["max_radar_score"],
        worst_stream_id=summary["worst_stream_id"],
        rows="".join(rows),
    )

    p.write_text(html, encoding="utf-8")


def write_event_jsonl(path: str, result: Dict[str, Any], status: str) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

    with p.open("w", encoding="utf-8") as f:
        for r in result["events"]:
            if r["status"] == status:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")


def write_all_reports(out_dir: str, result: Dict[str, Any]) -> None:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    write_json(str(out / "report.json"), result)
    write_csv_report(str(out / "report.csv"), result)
    write_html_report(str(out / "report.html"), result)
    write_event_jsonl(str(out / "drift_events.jsonl"), result, "drift")
    write_event_jsonl(str(out / "anomaly_events.jsonl"), result, "anomaly")
    write_event_jsonl(str(out / "alert_events.jsonl"), result, "alert")
    write_json(str(out / "certificate.json"), result["certificate"])
