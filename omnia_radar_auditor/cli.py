import argparse
import sys
from pathlib import Path

from .core import analyze_observations, read_jsonl, write_all_reports


def main():
    parser = argparse.ArgumentParser(
        prog="omnia-radar-audit",
        description="Audit signal, drift, anomaly, and alert states across supplied observation streams.",
    )

    parser.add_argument("--input", required=True, help="JSONL file with stream_id, step, and value observations.")
    parser.add_argument("--out-dir", default="omnia_radar_report", help="Output directory.")
    parser.add_argument("--baseline-window", type=int, default=3, help="Number of first observations used as baseline.")
    parser.add_argument("--drift-threshold", type=float, default=0.10, help="Radar score threshold above which an event is drift.")
    parser.add_argument("--anomaly-threshold", type=float, default=0.30, help="Radar score threshold above which an event is anomaly.")
    parser.add_argument("--alert-threshold", type=float, default=0.55, help="Radar score threshold above which an event is alert.")
    parser.add_argument("--fail-on-anomaly", action="store_true", help="Exit with code 2 if anomaly appears, or 3 if alert appears.")
    parser.add_argument("--fail-on-alert", action="store_true", help="Exit with code 3 if alert appears.")

    args = parser.parse_args()

    try:
        observations = read_jsonl(args.input)
        result = analyze_observations(
            observations=observations,
            baseline_window=args.baseline_window,
            drift_threshold=args.drift_threshold,
            anomaly_threshold=args.anomaly_threshold,
            alert_threshold=args.alert_threshold,
        )
        write_all_reports(args.out_dir, result)
    except Exception as e:
        print("ERROR:", str(e))
        sys.exit(4)

    s = result["summary"]

    print("")
    print("OMNIA RADAR AUDIT")
    print("=================")
    print(f"input:             {args.input}")
    print(f"total_streams:     {s['total_streams']}")
    print(f"total_events:      {s['total_events']}")
    print(f"signal:            {s['signal']}")
    print(f"drift:             {s['drift']}")
    print(f"anomaly:           {s['anomaly']}")
    print(f"alert:             {s['alert']}")
    print(f"signal_rate:       {s['signal_rate']:.6f}")
    print(f"drift_rate:        {s['drift_rate']:.6f}")
    print(f"anomaly_rate:      {s['anomaly_rate']:.6f}")
    print(f"alert_rate:        {s['alert_rate']:.6f}")
    print(f"max_radar_score:   {s['max_radar_score']}")
    print(f"worst_stream_id:   {s['worst_stream_id']}")
    print(f"worst_step:        {s['worst_step']}")
    print("")
    print(f"WROTE: {Path(args.out_dir) / 'report.json'}")
    print(f"WROTE: {Path(args.out_dir) / 'report.csv'}")
    print(f"WROTE: {Path(args.out_dir) / 'report.html'}")
    print(f"WROTE: {Path(args.out_dir) / 'drift_events.jsonl'}")
    print(f"WROTE: {Path(args.out_dir) / 'anomaly_events.jsonl'}")
    print(f"WROTE: {Path(args.out_dir) / 'alert_events.jsonl'}")
    print(f"WROTE: {Path(args.out_dir) / 'certificate.json'}")
    print("")

    if args.fail_on_alert and s["alert"] > 0:
        sys.exit(3)

    if args.fail_on_anomaly:
        if s["alert"] > 0:
            sys.exit(3)
        if s["anomaly"] > 0:
            sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
