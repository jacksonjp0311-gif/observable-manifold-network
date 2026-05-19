from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from omn.core.evidence_drift import evidence_drift_report, write_evidence_drift_outputs


NON_CLAIM_BOUNDARY = (
    "Metric availability validation checks whether evidence packages expose residual fields "
    "for comparison. It does not prove code correctness, empirical validation, causality, "
    "mechanism, production readiness, AI understanding, or GMN replication."
)

REQUIRED_METRICS = [
    "rmse",
    "mae",
    "delta_phi_residual",
    "omega_residual_weight",
]


def metric_availability_summary(report: Dict[str, Any]) -> Dict[str, Any]:
    metric_drift = report.get("metric_drift", [])
    rows = []
    all_available = True

    for item in metric_drift:
        metric = item.get("metric")
        available = int(item.get("available") or 0)
        unavailable = int(item.get("unavailable") or 0)
        total = available + unavailable
        availability = (available / total) if total else 0.0
        status = "available" if availability == 1.0 else ("partial" if availability > 0 else "unavailable")
        if metric in REQUIRED_METRICS and availability < 1.0:
            all_available = False
        rows.append({
            "metric": metric,
            "available": available,
            "unavailable": unavailable,
            "availability": availability,
            "status": status,
            "min": item.get("min"),
            "max": item.get("max"),
            "spread": item.get("spread"),
        })

    return {
        "schema": "OMN-SA-v0.8-metric-availability-summary",
        "all_required_metrics_available": all_available,
        "compared_count": report.get("compared_count"),
        "metric_rows": rows,
        "non_claim_boundary": NON_CLAIM_BOUNDARY,
    }


def render_markdown(payload: Dict[str, Any]) -> str:
    summary = payload["summary"]
    lines = [
        "# OMN-SA v0.8 Metric Availability Report",
        "",
        f"- Passed: {payload['passed']}",
        f"- Compared evidence packages: {summary['compared_count']}",
        "",
        "## Metric Availability",
        "",
        "| Metric | Available | Unavailable | Availability | Status | Min | Max | Spread |",
        "|---|---:|---:|---:|---|---:|---:|---:|",
    ]

    for row in summary["metric_rows"]:
        def fmt(value: Any) -> str:
            if value is None:
                return "n/a"
            try:
                return f"{float(value):.6g}"
            except Exception:
                return str(value)

        lines.append(
            f"| {row['metric']} | {row['available']} | {row['unavailable']} | "
            f"{row['availability']:.3f} | {row['status']} | {fmt(row['min'])} | {fmt(row['max'])} | {fmt(row['spread'])} |"
        )

    lines.extend([
        "",
        "## Interpretation",
        "",
        "v0.8 passes when all required residual fields are available in the compared evidence packages.",
        "",
        "## Boundary",
        "",
        payload["non_claim_boundary"],
        "",
    ])

    return "\n".join(lines)


def render_svg(summary: Dict[str, Any]) -> str:
    rows = summary.get("metric_rows", [])
    lookup = {row["metric"]: row for row in rows}

    def pct(metric: str) -> float:
        return float(lookup.get(metric, {}).get("availability") or 0.0)

    values = {
        "RMSE": pct("rmse"),
        "MAE": pct("mae"),
        "DeltaPhi": pct("delta_phi_residual"),
        "Omega": pct("omega_residual_weight"),
    }

    bars = []
    y = 310
    colors = ["#38bdf8", "#34d399", "#fbbf24", "#a78bfa"]

    for i, pair in enumerate(values.items()):
        label, value = pair
        width = int(520 * value)
        color = colors[i % len(colors)]
        bars.append(f'''
    <text x="0" y="{y + 18}" fill="#cbd5e1" font-size="14">{label}</text>
    <rect x="180" y="{y}" width="520" height="24" rx="8" fill="#1e293b"/>
    <rect x="180" y="{y}" width="{width}" height="24" rx="8" fill="{color}"/>
    <text x="720" y="{y + 18}" fill="#f8fafc" font-size="14">{value:.3f}</text>
''')
        y += 46

    status = "passed" if summary["all_required_metrics_available"] else "attention"
    compared = summary.get("compared_count") or 0

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="620" viewBox="0 0 1040 620" role="img" aria-labelledby="title desc">
  <title id="title">OMN-SA v0.8 Metric Availability</title>
  <desc id="desc">Residual metric availability across compared evidence packages.</desc>
  <rect width="1040" height="620" rx="30" fill="#0f172a"/>

  <text x="52" y="60" fill="#f8fafc" font-family="Segoe UI, Arial" font-size="32" font-weight="700">OMN-SA v0.8 Metric Availability</text>
  <text x="52" y="92" fill="#cbd5e1" font-family="Segoe UI, Arial" font-size="15">Residual fields exposed in evidence packages for multi-run comparison.</text>

  <g transform="translate(52,128)">
    <rect x="0" y="0" width="285" height="122" rx="18" fill="#111827" stroke="#334155"/>
    <text x="22" y="34" fill="#93c5fd" font-family="Segoe UI, Arial" font-size="15" font-weight="700">Availability Check</text>
    <text x="22" y="72" fill="#f8fafc" font-family="Segoe UI, Arial" font-size="32" font-weight="700">{status}</text>
    <text x="22" y="100" fill="#cbd5e1" font-family="Segoe UI, Arial" font-size="13">required residual fields</text>

    <rect x="318" y="0" width="285" height="122" rx="18" fill="#111827" stroke="#334155"/>
    <text x="340" y="34" fill="#86efac" font-family="Segoe UI, Arial" font-size="15" font-weight="700">Compared Evidence</text>
    <text x="340" y="72" fill="#f8fafc" font-family="Segoe UI, Arial" font-size="32" font-weight="700">{compared}</text>
    <text x="340" y="100" fill="#cbd5e1" font-family="Segoe UI, Arial" font-size="13">latest packages</text>

    <rect x="636" y="0" width="285" height="122" rx="18" fill="#111827" stroke="#334155"/>
    <text x="658" y="34" fill="#fcd34d" font-family="Segoe UI, Arial" font-size="15" font-weight="700">Residual Schema</text>
    <text x="658" y="72" fill="#f8fafc" font-family="Segoe UI, Arial" font-size="32" font-weight="700">v0.8</text>
    <text x="658" y="100" fill="#cbd5e1" font-family="Segoe UI, Arial" font-size="13">metrics.validation block</text>
  </g>

  <g transform="translate(70,0)" font-family="Segoe UI, Arial">
    <text x="0" y="280" fill="#f8fafc" font-size="19" font-weight="700">Metric Availability Across Compared Packages</text>
    {''.join(bars)}
  </g>

  <text x="52" y="585" fill="#94a3b8" font-family="Segoe UI, Arial" font-size="12">Boundary: metric availability proves fields are exposed for comparison. It does not prove correctness, empirical validation, causality, mechanism, AI understanding, production readiness, or GMN replication.</text>
</svg>'''


def write_outputs(summary: Dict[str, Any], report: Dict[str, Any]) -> Dict[str, str]:
    report_dir = ROOT / "reports" / "metric_availability"
    report_dir.mkdir(parents=True, exist_ok=True)

    docs_dir = ROOT / "docs" / "benchmarks"
    docs_dir.mkdir(parents=True, exist_ok=True)

    visuals_dir = ROOT / "visuals" / "omn_sa"
    visuals_dir.mkdir(parents=True, exist_ok=True)

    json_path = report_dir / "latest_metric_availability_report.json"
    md_path = report_dir / "latest_metric_availability_report.md"
    docs_path = docs_dir / "omn_sa_v0_8_metric_availability_metrics.md"
    svg_path = visuals_dir / "omn_sa_v0_8_metric_availability.svg"

    payload = {
        "schema": "OMN-SA-v0.8-metric-availability-validation",
        "passed": summary["all_required_metrics_available"],
        "summary": summary,
        "evidence_drift_report": report,
        "non_claim_boundary": NON_CLAIM_BOUNDARY,
    }

    json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    md = render_markdown(payload)
    md_path.write_text(md, encoding="utf-8")
    docs_path.write_text(md, encoding="utf-8")
    svg_path.write_text(render_svg(summary), encoding="utf-8")

    return {
        "json": str(json_path),
        "md": str(md_path),
        "docs_md": str(docs_path),
        "svg": str(svg_path),
    }


def main() -> int:
    report = evidence_drift_report(str(ROOT), limit=8)
    write_evidence_drift_outputs(str(ROOT), report)
    summary = metric_availability_summary(report)
    outputs = write_outputs(summary, report)

    final = {
        "schema": "OMN-SA-v0.8-metric-availability-validation-result",
        "passed": summary["all_required_metrics_available"] and all(Path(path).exists() for path in outputs.values()),
        "summary": summary,
        "outputs": outputs,
        "non_claim_boundary": NON_CLAIM_BOUNDARY,
    }

    print(json.dumps(final, indent=2))
    return 0 if final["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())