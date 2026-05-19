from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional


NON_CLAIM_BOUNDARY = (
    "Evidence drift comparison checks run-to-run continuity, artifact replay status, "
    "claim-status stability, and metric availability. It does not prove code correctness, "
    "empirical validation, causality, mechanism, production readiness, AI understanding, "
    "or GMN replication."
)


def list_evidence_packages(repo_root: str) -> List[Path]:
    root = Path(repo_root)
    evidence_dir = root / "outputs" / "evidence"
    if not evidence_dir.exists():
        return []
    return sorted(evidence_dir.glob("*_evidence_package.json"), key=lambda p: p.stat().st_mtime)


def load_json(path: Path) -> Dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        payload["_path"] = str(path)
        return payload
    except Exception as exc:
        return {
            "_path": str(path),
            "_load_error": str(exc),
        }


def safe_float(value: Any) -> Optional[float]:
    try:
        if value is None:
            return None
        return float(value)
    except Exception:
        return None


def get_nested(payload: Dict[str, Any], path: List[str]) -> Any:
    current: Any = payload
    for key in path:
        if not isinstance(current, dict):
            return None
        current = current.get(key)
    return current


def metric_snapshot(payload: Dict[str, Any]) -> Dict[str, Optional[float]]:
    metric_paths = {
        "rmse": ["metrics", "validation", "rmse"],
        "mae": ["metrics", "validation", "mae"],
        "delta_phi_residual": ["metrics", "validation", "delta_phi_residual"],
        "omega_residual_weight": ["metrics", "validation", "omega_residual_weight"],
    }

    return {
        name: safe_float(get_nested(payload, path))
        for name, path in metric_paths.items()
    }


def declared_artifact_count(payload: Dict[str, Any]) -> int:
    artifacts = payload.get("artifacts", {})
    if isinstance(artifacts, dict):
        count = 0
        for value in artifacts.values():
            if isinstance(value, dict):
                count += len([v for v in value.values() if v])
            elif isinstance(value, list):
                count += len(value)
            elif value:
                count += 1
        return count
    return 0


def evidence_record(payload: Dict[str, Any]) -> Dict[str, Any]:
    claim_status = payload.get("claim_status", {})
    if not isinstance(claim_status, dict):
        claim_status = {}

    return {
        "run_id": payload.get("run_id"),
        "seed": payload.get("seed"),
        "path": payload.get("_path"),
        "computed_status": claim_status.get("computed_status"),
        "benchmark_class": claim_status.get("benchmark_class"),
        "overpromotion_blocked": claim_status.get("overpromotion_blocked"),
        "declared_artifact_count": declared_artifact_count(payload),
        "metrics": metric_snapshot(payload),
        "load_error": payload.get("_load_error"),
    }


def compare_metric_series(records: List[Dict[str, Any]], metric: str) -> Dict[str, Any]:
    values: List[float] = []
    unavailable = 0

    for record in records:
        value = record.get("metrics", {}).get(metric)
        if value is None:
            unavailable += 1
        else:
            values.append(float(value))

    if not values:
        return {
            "metric": metric,
            "available": 0,
            "unavailable": unavailable,
            "min": None,
            "max": None,
            "spread": None,
            "status": "unavailable",
        }

    return {
        "metric": metric,
        "available": len(values),
        "unavailable": unavailable,
        "min": min(values),
        "max": max(values),
        "spread": max(values) - min(values),
        "status": "computed",
    }


def evidence_drift_report(repo_root: str, limit: int = 8) -> Dict[str, Any]:
    packages = list_evidence_packages(repo_root)
    selected_paths = packages[-limit:]
    payloads = [load_json(path) for path in selected_paths]
    records = [evidence_record(payload) for payload in payloads]

    load_errors = [record for record in records if record.get("load_error")]
    seeds = sorted(set([record.get("seed") for record in records if record.get("seed")]))
    statuses = sorted(set([record.get("computed_status") for record in records if record.get("computed_status")]))
    benchmark_classes = sorted(set([record.get("benchmark_class") for record in records if record.get("benchmark_class")]))

    metric_reports = [
        compare_metric_series(records, "rmse"),
        compare_metric_series(records, "mae"),
        compare_metric_series(records, "delta_phi_residual"),
        compare_metric_series(records, "omega_residual_weight"),
    ]

    artifact_counts = [record.get("declared_artifact_count", 0) for record in records]
    artifact_count_spread = (max(artifact_counts) - min(artifact_counts)) if artifact_counts else 0

    overpromotion_flags = [
        record for record in records
        if record.get("overpromotion_blocked") is not True
    ]

    passed = (
        len(records) >= 2
        and not load_errors
        and not overpromotion_flags
        and artifact_count_spread == 0
    )

    return {
        "schema": "OMN-SA-v0.7-evidence-drift-report",
        "evidence_package_count": len(packages),
        "compared_count": len(records),
        "records": records,
        "seeds_seen": seeds,
        "claim_statuses_seen": statuses,
        "benchmark_classes_seen": benchmark_classes,
        "artifact_count_spread": artifact_count_spread,
        "metric_drift": metric_reports,
        "load_error_count": len(load_errors),
        "overpromotion_flag_count": len(overpromotion_flags),
        "passed": passed,
        "failure_flags": [] if passed else build_failure_flags(records, load_errors, overpromotion_flags, artifact_count_spread),
        "non_claim_boundary": NON_CLAIM_BOUNDARY,
    }


def build_failure_flags(
    records: List[Dict[str, Any]],
    load_errors: List[Dict[str, Any]],
    overpromotion_flags: List[Dict[str, Any]],
    artifact_count_spread: int,
) -> List[str]:
    flags: List[str] = []
    if len(records) < 2:
        flags.append("fewer_than_two_evidence_packages")
    if load_errors:
        flags.append("evidence_load_errors_present")
    if overpromotion_flags:
        flags.append("overpromotion_block_missing_or_false")
    if artifact_count_spread != 0:
        flags.append("artifact_count_spread_nonzero")
    return flags


def write_evidence_drift_outputs(repo_root: str, report: Dict[str, Any]) -> Dict[str, str]:
    root = Path(repo_root)

    report_dir = root / "reports" / "evidence_drift"
    report_dir.mkdir(parents=True, exist_ok=True)

    docs_dir = root / "docs" / "benchmarks"
    docs_dir.mkdir(parents=True, exist_ok=True)

    visuals_dir = root / "visuals" / "omn_sa"
    visuals_dir.mkdir(parents=True, exist_ok=True)

    json_path = report_dir / "latest_evidence_drift_report.json"
    md_path = report_dir / "latest_evidence_drift_report.md"
    docs_md_path = docs_dir / "omn_sa_v0_7_evidence_drift_metrics.md"
    svg_path = visuals_dir / "omn_sa_v0_7_evidence_drift_dashboard.svg"

    json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    md = render_markdown(report)
    md_path.write_text(md, encoding="utf-8")
    docs_md_path.write_text(md, encoding="utf-8")
    svg_path.write_text(render_svg(report), encoding="utf-8")

    return {
        "json": str(json_path),
        "md": str(md_path),
        "docs_md": str(docs_md_path),
        "svg": str(svg_path),
    }


def render_markdown(report: Dict[str, Any]) -> str:
    lines = [
        "# OMN-SA v0.7 Evidence Drift Metrics",
        "",
        "## Summary",
        "",
        f"- Passed: {report['passed']}",
        f"- Evidence packages found: {report['evidence_package_count']}",
        f"- Evidence packages compared: {report['compared_count']}",
        f"- Seeds seen: {', '.join(report['seeds_seen']) if report['seeds_seen'] else 'none'}",
        f"- Claim statuses seen: {', '.join(report['claim_statuses_seen']) if report['claim_statuses_seen'] else 'none'}",
        f"- Benchmark classes seen: {', '.join(report['benchmark_classes_seen']) if report['benchmark_classes_seen'] else 'none'}",
        f"- Artifact count spread: {report['artifact_count_spread']}",
        f"- Load errors: {report['load_error_count']}",
        f"- Overpromotion flag count: {report['overpromotion_flag_count']}",
        "",
        "## Metric Drift",
        "",
        "| Metric | Available | Unavailable | Min | Max | Spread | Status |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]

    for metric in report["metric_drift"]:
        def fmt(value):
            return "n/a" if value is None else f"{value:.6g}"
        lines.append(
            f"| {metric['metric']} | {metric['available']} | {metric['unavailable']} | "
            f"{fmt(metric['min'])} | {fmt(metric['max'])} | {fmt(metric['spread'])} | {metric['status']} |"
        )

    lines.extend([
        "",
        "## Compared Records",
        "",
        "| Run ID | Seed | Claim status | Benchmark | Artifact count |",
        "|---|---|---|---|---:|",
    ])

    for record in report["records"]:
        lines.append(
            f"| {record.get('run_id')} | {record.get('seed')} | {record.get('computed_status')} | "
            f"{record.get('benchmark_class')} | {record.get('declared_artifact_count')} |"
        )

    lines.extend([
        "",
        "## Failure Flags",
        "",
    ])

    if report["failure_flags"]:
        for flag in report["failure_flags"]:
            lines.append(f"- {flag}")
    else:
        lines.append("- None")

    lines.extend([
        "",
        "## Boundary",
        "",
        report["non_claim_boundary"],
        "",
    ])

    return "\n".join(lines)


def render_svg(report: Dict[str, Any]) -> str:
    compared = int(report.get("compared_count", 0))
    artifact_spread = int(report.get("artifact_count_spread", 0))
    load_errors = int(report.get("load_error_count", 0))
    overpromotion = int(report.get("overpromotion_flag_count", 0))
    passed = "passed" if report.get("passed") else "attention"

    stability_width = 520 if report.get("passed") else 260
    artifact_width = 520 if artifact_spread == 0 else 260
    load_width = 520 if load_errors == 0 else 260
    claim_width = 520 if overpromotion == 0 else 260

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="620" viewBox="0 0 1040 620" role="img" aria-labelledby="title desc">
  <title id="title">OMN-SA v0.7 Evidence Drift Dashboard</title>
  <desc id="desc">Multi-run evidence drift comparison dashboard.</desc>
  <rect width="1040" height="620" rx="30" fill="#0f172a"/>

  <text x="52" y="60" fill="#f8fafc" font-family="Segoe UI, Arial" font-size="32" font-weight="700">OMN-SA v0.7 Evidence Drift Dashboard</text>
  <text x="52" y="92" fill="#cbd5e1" font-family="Segoe UI, Arial" font-size="15">Multi-run evidence comparison, claim stability, artifact-count stability, and drift visibility</text>

  <g transform="translate(52,128)">
    <rect x="0" y="0" width="285" height="122" rx="18" fill="#111827" stroke="#334155"/>
    <text x="22" y="34" fill="#93c5fd" font-family="Segoe UI, Arial" font-size="15" font-weight="700">Evidence Compared</text>
    <text x="22" y="72" fill="#f8fafc" font-family="Segoe UI, Arial" font-size="32" font-weight="700">{compared}</text>
    <text x="22" y="100" fill="#cbd5e1" font-family="Segoe UI, Arial" font-size="13">latest evidence packages</text>

    <rect x="318" y="0" width="285" height="122" rx="18" fill="#111827" stroke="#334155"/>
    <text x="340" y="34" fill="#86efac" font-family="Segoe UI, Arial" font-size="15" font-weight="700">Drift Check</text>
    <text x="340" y="72" fill="#f8fafc" font-family="Segoe UI, Arial" font-size="32" font-weight="700">{passed}</text>
    <text x="340" y="100" fill="#cbd5e1" font-family="Segoe UI, Arial" font-size="13">multi-run surface</text>

    <rect x="636" y="0" width="285" height="122" rx="18" fill="#111827" stroke="#334155"/>
    <text x="658" y="34" fill="#fcd34d" font-family="Segoe UI, Arial" font-size="15" font-weight="700">Artifact Spread</text>
    <text x="658" y="72" fill="#f8fafc" font-family="Segoe UI, Arial" font-size="32" font-weight="700">{artifact_spread}</text>
    <text x="658" y="100" fill="#cbd5e1" font-family="Segoe UI, Arial" font-size="13">declared artifact-count drift</text>
  </g>

  <g transform="translate(70,310)" font-family="Segoe UI, Arial">
    <text x="0" y="-30" fill="#f8fafc" font-size="19" font-weight="700">Run-to-Run Stability Surfaces</text>

    <text x="0" y="22" fill="#cbd5e1" font-size="14">Overall evidence drift</text>
    <rect x="210" y="4" width="520" height="24" rx="8" fill="#1e293b"/>
    <rect x="210" y="4" width="{stability_width}" height="24" rx="8" fill="#38bdf8"/>
    <text x="750" y="22" fill="#f8fafc" font-size="14">{passed}</text>

    <text x="0" y="68" fill="#cbd5e1" font-size="14">Artifact count stability</text>
    <rect x="210" y="50" width="520" height="24" rx="8" fill="#1e293b"/>
    <rect x="210" y="50" width="{artifact_width}" height="24" rx="8" fill="#34d399"/>
    <text x="750" y="68" fill="#f8fafc" font-size="14">spread {artifact_spread}</text>

    <text x="0" y="114" fill="#cbd5e1" font-size="14">Load integrity</text>
    <rect x="210" y="96" width="520" height="24" rx="8" fill="#1e293b"/>
    <rect x="210" y="96" width="{load_width}" height="24" rx="8" fill="#fbbf24"/>
    <text x="750" y="114" fill="#f8fafc" font-size="14">{load_errors} errors</text>

    <text x="0" y="160" fill="#cbd5e1" font-size="14">Claim overpromotion guard</text>
    <rect x="210" y="142" width="520" height="24" rx="8" fill="#1e293b"/>
    <rect x="210" y="142" width="{claim_width}" height="24" rx="8" fill="#a78bfa"/>
    <text x="750" y="160" fill="#f8fafc" font-size="14">{overpromotion} flags</text>
  </g>

  <text x="52" y="585" fill="#94a3b8" font-family="Segoe UI, Arial" font-size="12">Boundary: evidence drift comparison measures local continuity and run-to-run stability. It does not prove correctness, empirical validation, causality, mechanism, AI understanding, production readiness, or GMN replication.</text>
</svg>'''