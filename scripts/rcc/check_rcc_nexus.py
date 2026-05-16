import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]

REQUIRED_FILES = [
    "README.md",
    "README_90_SECONDS.md",
    "AGENTS.md",
    "docs/context/repository_context_index.json",
    "docs/context/rcc_nexus_index.json",
    "docs/context/validation_surface.md",
    "rcc/nexus/README.md",
    "rcc/nexus/route_map.json",
    "rcc/nexus/rcc_nexus_protocol.md",
    "rcc/nexus/task_routing_matrix.md",
    "rcc/nexus/echo_location_template.md",
    "rcc/nexus/agent_handoff_contract.md",
]

REQUIRED_README_MARKERS = [
    "# PART I - Human README",
    "# PART II - RCC Nexus README",
    "# PART III - AI Agent README",
    "## Human Director Box",
    "## RCC Nexus Echo Location",
]

NON_CLAIM_MARKERS = [
    "Navigation is not validation",
    "Context is not truth",
    "Observable topology is not truth",
    "Prediction is not mechanism",
    "Simulation is not proof",
]

ECHO_FOLDERS = [
    "docs",
    "docs/context",
    "docs/software_architecture",
    "docs/injections",
    "rcc/nexus",
    "src/omn",
    "src/omn/core",
    "src/omn/schemas",
    "configs",
    "examples",
    "tests",
    "scripts",
    "scripts/rcc",
    "outputs",
    "outputs/evidence",
    "reports/rcc_nexus",
]


def read_text(path):
    return path.read_text(encoding="utf-8") if path.exists() else ""


def main():
    missing = []
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            missing.append(rel)

    readme = read_text(ROOT / "README.md")
    missing_markers = [m for m in REQUIRED_README_MARKERS if m not in readme]
    missing_locks = [m for m in NON_CLAIM_MARKERS if m not in readme]

    echo_missing = []
    for rel in ECHO_FOLDERS:
        p = ROOT / rel / "README.md"
        text = read_text(p)
        if "## RCC Nexus Echo Location" not in text:
            echo_missing.append(str(p.relative_to(ROOT)))

    index_ok = False
    route_ok = False
    try:
        data = json.loads((ROOT / "docs/context/rcc_nexus_index.json").read_text(encoding="utf-8"))
        index_ok = data.get("schema") == "RCC-N-v1.0-nexus-index"
    except Exception:
        index_ok = False

    try:
        route = json.loads((ROOT / "rcc/nexus/route_map.json").read_text(encoding="utf-8"))
        route_ok = route.get("schema") == "RCC-N-v1.0-route-map"
    except Exception:
        route_ok = False

    total_checks = 6
    passed_checks = 0
    passed_checks += 1 if not missing else 0
    passed_checks += 1 if not missing_markers else 0
    passed_checks += 1 if not missing_locks else 0
    passed_checks += 1 if not echo_missing else 0
    passed_checks += 1 if index_ok else 0
    passed_checks += 1 if route_ok else 0

    nci = round(passed_checks / total_checks, 4)
    passed = passed_checks == total_checks

    report = {
        "schema": "RCC-N-v1.0-check-report",
        "repository": "observable-manifold-network",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "mode": "self",
        "passed": passed,
        "nci_self": nci,
        "missing_required_files": missing,
        "missing_readme_markers": missing_markers,
        "missing_non_claim_locks": missing_locks,
        "echo_location_missing": echo_missing,
        "index_ok": index_ok,
        "route_map_ok": route_ok,
        "non_claim_boundary": "RCC-N check improves navigation integrity. It does not prove code correctness, patch safety, empirical validation, causality, mechanism, or GMN replication."
    }

    out_dir = ROOT / "reports" / "rcc_nexus"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "latest_rcc_nexus_check.json").write_text(json.dumps(report, indent=2), encoding="utf-8")

    md = [
        "# Latest RCC Nexus Check",
        "",
        f"Timestamp: {report['timestamp']}",
        f"Passed: {report['passed']}",
        f"NCI self: {report['nci_self']}",
        "",
        "## Missing required files",
        "",
        *(f"- {x}" for x in missing),
        "",
        "## Missing README markers",
        "",
        *(f"- {x}" for x in missing_markers),
        "",
        "## Missing non-claim locks",
        "",
        *(f"- {x}" for x in missing_locks),
        "",
        "## Echo Location missing",
        "",
        *(f"- {x}" for x in echo_missing),
        "",
        "## Boundary",
        "",
        report["non_claim_boundary"],
        "",
    ]
    (out_dir / "latest_rcc_nexus_check.md").write_text("\n".join(md), encoding="utf-8")

    drift_dir = ROOT / "docs" / "context" / "drift"
    drift_dir.mkdir(parents=True, exist_ok=True)
    (drift_dir / "latest_rcc_nexus_report.md").write_text("\n".join(md), encoding="utf-8")

    print(json.dumps(report, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())