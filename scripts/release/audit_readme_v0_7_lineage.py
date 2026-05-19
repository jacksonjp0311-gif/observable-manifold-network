from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"

NON_CLAIM_BOUNDARY = (
    "README v0.7 lineage audit checks documentation continuity and current-state orientation. "
    "It does not prove code correctness, empirical validation, causality, mechanism, production readiness, "
    "AI understanding, or GMN replication."
)

def main() -> int:
    text = README.read_text(encoding="utf-8", errors="ignore")

    checks = {
        "archived_v07_bottom_section_present": "## OMN-SA v0.7 Evidence Drift Comparison and Multi-Run Stability Dashboard" in text,
        "v07_dashboard_path_present": "visuals/omn_sa/omn_sa_v0_7_evidence_drift_dashboard.svg" in text,
        "v07_known_metric_weakness_present": "delta_phi_residual" in text and "omega_residual_weight" in text,
        "v08_target_present": "OMN-SA v0.8" in text or "v0.8 residual metrics" in text,
        "ai_tracking_typo_removed": "OMN-SA v0.7.2.2" not in text,
        "current_tests_44": "| Current tests | 44 OK |" in text,
    }

    missing = [key for key, value in checks.items() if not value]

    report = {
        "schema": "OMN-SA-v0.7.3-readme-lineage-audit",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "passed": len(missing) == 0,
        "checks": checks,
        "missing": missing,
        "non_claim_boundary": NON_CLAIM_BOUNDARY,
    }

    out_dir = ROOT / "reports" / "self_organization"
    out_dir.mkdir(parents=True, exist_ok=True)

    (out_dir / "latest_readme_v0_7_lineage_audit.json").write_text(json.dumps(report, indent=2), encoding="utf-8")

    lines = [
        "# OMN-SA v0.7.3 README v0.7 Lineage Audit",
        "",
        f"- Passed: {report['passed']}",
        "",
        "## Checks",
        "",
        "| Check | Result |",
        "|---|---:|",
    ]

    for key, value in checks.items():
        lines.append(f"| {key} | {value} |")

    lines.extend(["", "## Missing", ""])

    if missing:
        for item in missing:
            lines.append(f"- {item}")
    else:
        lines.append("- None")

    lines.extend(["", "## Boundary", "", NON_CLAIM_BOUNDARY, ""])

    (out_dir / "latest_readme_v0_7_lineage_audit.md").write_text("\n".join(lines), encoding="utf-8")

    print(json.dumps(report, indent=2))
    return 0 if report["passed"] else 1

if __name__ == "__main__":
    raise SystemExit(main())