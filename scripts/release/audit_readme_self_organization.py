from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"

NON_CLAIM_BOUNDARY = (
    "README self-organization audit checks current-state orientation and archive separation. "
    "It does not prove code correctness, patch safety, empirical validation, causality, "
    "mechanism, AI understanding, production readiness, or GMN replication."
)


def main() -> int:
    text = README.read_text(encoding="utf-8", errors="ignore")

    checks = {
        "health_snapshot_current_layer_present": "Current software layer | OMN-SA v" in text,
        "health_snapshot_not_pending_commit": "pending-v0.8.0" not in text and "pending-v0.8" not in text,
        "no_expected_tests_wording": "expected after v0.7.1" not in text,
        "ai_tracking_present": "Current software architecture layer:" in text,
        "rcc_v17_visible": "RCC-N v1.7 adoption-profile governance" in text or "RCC-N v1.7 Full profile governance" in text,
        "self_org_section_present": "Current v0.7.2 README Self-Organization Audit" in text,
        "current_stack_present": "Current Versioned Documentation Stack" in text,
        "v071_profile_still_visible": "omn_sa_v0_7_1_rcc_n_v1_7_profile_injection.md" in text,
        "v08_metric_layer_visible": "Current v0.8 Metric Availability and Residual Field Hardening" in text,
        "archived_v04_not_current": "## Archived v0.4 Metrics Snapshot" in text,
    }

    missing = [key for key, value in checks.items() if not value]

    report = {
        "schema": "OMN-SA-v0.8.1-readme-self-organization-audit",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "passed": len(missing) == 0,
        "checks": checks,
        "missing": missing,
        "non_claim_boundary": NON_CLAIM_BOUNDARY,
    }

    out_dir = ROOT / "reports" / "self_organization"
    out_dir.mkdir(parents=True, exist_ok=True)

    json_path = out_dir / "latest_readme_self_organization_audit.json"
    md_path = out_dir / "latest_readme_self_organization_audit.md"

    json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    lines = [
        "# OMN-SA README Self-Organization Audit",
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
    md_path.write_text("\n".join(lines), encoding="utf-8")

    print(json.dumps(report, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())