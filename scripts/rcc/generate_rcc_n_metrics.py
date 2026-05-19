from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Dict


ROOT = Path(__file__).resolve().parents[2]

BOUNDARY = (
    "RCC-N metrics measure repository orientation, routing, context coverage, "
    "validation linkage, and non-claim discipline. They do not prove code correctness, "
    "patch safety, empirical validation, causality, mechanism, AI understanding, "
    "production readiness, or GMN replication."
)


def exists(rel: str) -> bool:
    return (ROOT / rel).exists()


def read(rel: str) -> str:
    path = ROOT / rel
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


def score_presence(items) -> float:
    if not items:
        return 0.0
    return sum(1 for item in items if exists(item)) / len(items)


def score_markers(path: str, markers) -> float:
    text = read(path)
    if not markers:
        return 0.0
    return sum(1 for marker in markers if marker in text) / len(markers)


def mini_readme_coverage() -> float:
    report_path = ROOT / "reports" / "mini_readmes" / "latest_mini_readme_audit.json"
    if report_path.exists():
        data = json.loads(report_path.read_text(encoding="utf-8"))
        return float(data.get("coverage", 0.0))
    return 0.0


def load_rcc_nci() -> float:
    candidates = [
        ROOT / "reports" / "rcc_nexus" / "latest_rcc_nexus_check.json",
        ROOT / "docs" / "context" / "drift" / "latest_rcc_nexus_report.json",
    ]
    for path in candidates:
        if path.exists():
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
                return float(data.get("nci_self", 0.0))
            except Exception:
                pass
    return 0.0


def compute_metrics() -> Dict[str, object]:
    required_context = [
        "README.md",
        "AGENTS.md",
        "README_90_SECONDS.md",
        "docs/context/repository_context_index.json",
        "docs/context/rcc_nexus_index.json",
        "docs/context/validation_surface.md",
        "rcc/nexus/route_map.json",
        "rcc/nexus/rcc_nexus_protocol.md",
        "rcc/nexus/task_routing_matrix.md",
        "rcc/nexus/agent_handoff_contract.md",
    ]

    validation_files = [
        "scripts/rcc/check_rcc_nexus.py",
        "scripts/validation/validate_architecture_contracts.py",
        "scripts/validation/validate_modular_runtime.py",
        "scripts/validation/validate_graph_engine.py",
        "tests",
        ".github/workflows/ci.yml",
    ]

    evidence_files = [
        "outputs/evidence",
        "outputs/state",
        "outputs/reports",
        "outputs/ledger",
        "reports/rcc_nexus",
        "reports/architecture",
        "reports/graph_engine",
        "reports/modular_runtime",
    ]

    readme_markers = [
        "Human Director Box",
        "PART I",
        "PART II",
        "PART III",
        "RCC Nexus Echo Location",
        "Non-Claim Locks",
        "AI Operating Contract",
        "Current v0.4 Metrics Snapshot",
        "OMN-SA v0.4",
    ]

    route_markers = [
        "non_claim_boundary",
        "route",
        "validation",
    ]

    metrics = {
        "context_surface_coverage": score_presence(required_context),
        "validation_surface_coverage": score_presence(validation_files),
        "evidence_surface_coverage": score_presence(evidence_files),
        "readme_marker_coverage": score_markers("README.md", readme_markers),
        "route_map_marker_coverage": score_markers("rcc/nexus/route_map.json", route_markers),
        "mini_readme_coverage": mini_readme_coverage(),
        "nci_self": load_rcc_nci(),
    }

    weighted = (
        0.18 * metrics["context_surface_coverage"]
        + 0.16 * metrics["validation_surface_coverage"]
        + 0.14 * metrics["evidence_surface_coverage"]
        + 0.16 * metrics["readme_marker_coverage"]
        + 0.10 * metrics["route_map_marker_coverage"]
        + 0.16 * metrics["mini_readme_coverage"]
        + 0.10 * metrics["nci_self"]
    )

    regular_readme_baseline = {
        "context_surface_coverage": 0.25,
        "validation_surface_coverage": 0.10,
        "evidence_surface_coverage": 0.10,
        "readme_marker_coverage": 0.20,
        "route_map_marker_coverage": 0.00,
        "mini_readme_coverage": 0.00,
        "nci_self": 0.00,
    }

    baseline_weighted = (
        0.18 * regular_readme_baseline["context_surface_coverage"]
        + 0.16 * regular_readme_baseline["validation_surface_coverage"]
        + 0.14 * regular_readme_baseline["evidence_surface_coverage"]
        + 0.16 * regular_readme_baseline["readme_marker_coverage"]
        + 0.10 * regular_readme_baseline["route_map_marker_coverage"]
        + 0.16 * regular_readme_baseline["mini_readme_coverage"]
        + 0.10 * regular_readme_baseline["nci_self"]
    )

    return {
        "schema": "RCC-N-v0.5-effectiveness-metrics",
        "metrics": metrics,
        "rcc_n_effectiveness_score": weighted,
        "regular_readme_baseline_score": baseline_weighted,
        "lift_over_regular_readme": weighted - baseline_weighted,
        "boundary": BOUNDARY,
    }


def write_chart(report: Dict[str, object]) -> None:
    metrics = report["metrics"]
    score = float(report["rcc_n_effectiveness_score"])
    baseline = float(report["regular_readme_baseline_score"])

    categories = [
        ("Context", metrics["context_surface_coverage"]),
        ("Validation", metrics["validation_surface_coverage"]),
        ("Evidence", metrics["evidence_surface_coverage"]),
        ("README", metrics["readme_marker_coverage"]),
        ("Routes", metrics["route_map_marker_coverage"]),
        ("Mini READMEs", metrics["mini_readme_coverage"]),
        ("NCI", metrics["nci_self"]),
    ]

    rows = []
    y = 150
    for label, value in categories:
        width = int(520 * float(value))
        rows.append(f'<text x="60" y="{y+18}" fill="#cbd5e1" font-family="Segoe UI, Arial" font-size="14">{label}</text>')
        rows.append(f'<rect x="190" y="{y}" width="520" height="24" rx="8" fill="#1e293b"/>')
        rows.append(f'<rect x="190" y="{y}" width="{width}" height="24" rx="8" fill="#38bdf8"/>')
        rows.append(f'<text x="730" y="{y+18}" fill="#f8fafc" font-family="Segoe UI, Arial" font-size="14">{value:.2f}</text>')
        y += 42

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="980" height="560" viewBox="0 0 980 560">
  <rect width="980" height="560" rx="28" fill="#0f172a"/>
  <text x="48" y="58" fill="#f8fafc" font-family="Segoe UI, Arial" font-size="30" font-weight="700">RCC-N Effectiveness Metrics</text>
  <text x="48" y="88" fill="#cbd5e1" font-family="Segoe UI, Arial" font-size="15">Repository orientation, validation linkage, mini README coverage, and navigation discipline</text>

  <rect x="48" y="105" width="884" height="1" fill="#334155"/>

  {''.join(rows)}

  <g transform="translate(60,470)">
    <text x="0" y="0" fill="#f8fafc" font-family="Segoe UI, Arial" font-size="18" font-weight="700">Overall</text>
    <text x="0" y="34" fill="#38bdf8" font-family="Segoe UI, Arial" font-size="28" font-weight="700">RCC-N {score:.2f}</text>
    <text x="220" y="34" fill="#94a3b8" font-family="Segoe UI, Arial" font-size="28" font-weight="700">Regular README {baseline:.2f}</text>
    <text x="560" y="34" fill="#86efac" font-family="Segoe UI, Arial" font-size="28" font-weight="700">Lift +{(score-baseline):.2f}</text>
  </g>

  <text x="48" y="540" fill="#94a3b8" font-family="Segoe UI, Arial" font-size="12">Boundary: RCC-N metrics measure navigation and context discipline, not code correctness, empirical validation, causality, mechanism, AI understanding, production readiness, or GMN replication.</text>
</svg>'''

    out = ROOT / "visuals" / "rcc_nexus" / "rcc_n_effectiveness_v0_5.svg"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(svg, encoding="utf-8")


def main() -> int:
    report = compute_metrics()

    out_dir = ROOT / "reports" / "rcc_nexus"
    out_dir.mkdir(parents=True, exist_ok=True)

    json_path = out_dir / "latest_rcc_n_effectiveness_metrics.json"
    md_path = ROOT / "docs" / "benchmarks" / "rcc_n_effectiveness_metrics_v0_5.md"
    csv_path = ROOT / "docs" / "benchmarks" / "rcc_n_effectiveness_metrics_v0_5.csv"

    json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["metric", "score"])
        for key, value in report["metrics"].items():
            writer.writerow([key, value])
        writer.writerow(["rcc_n_effectiveness_score", report["rcc_n_effectiveness_score"]])
        writer.writerow(["regular_readme_baseline_score", report["regular_readme_baseline_score"]])
        writer.writerow(["lift_over_regular_readme", report["lift_over_regular_readme"]])

    md = [
        "# RCC-N Effectiveness Metrics v0.5",
        "",
        "## Summary",
        "",
        f"- RCC-N effectiveness score: {report['rcc_n_effectiveness_score']:.3f}",
        f"- Regular README structural baseline: {report['regular_readme_baseline_score']:.3f}",
        f"- Lift over baseline: {report['lift_over_regular_readme']:.3f}",
        "",
        "## Metrics",
        "",
        "| Metric | Score |",
        "|---|---:|",
    ]

    for key, value in report["metrics"].items():
        md.append(f"| {key} | {value:.3f} |")

    md.extend([
        "",
        "## Boundary",
        "",
        report["boundary"],
        "",
    ])

    md_path.write_text("\n".join(md), encoding="utf-8")

    write_chart(report)

    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())