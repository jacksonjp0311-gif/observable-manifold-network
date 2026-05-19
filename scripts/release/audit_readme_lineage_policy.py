from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"

NON_CLAIM_BOUNDARY = (
    "README lineage-policy audit checks current-state, registry-state, AI policy, and historical lineage surfaces. "
    "It does not prove code correctness, empirical validation, causality, mechanism, production readiness, "
    "AI understanding, or GMN replication."
)


def main() -> int:
    text = README.read_text(encoding="utf-8", errors="ignore")

    current_is_v082_or_newer = (
        "Current software layer | OMN-SA v0.8.2" in text
        or "Current software layer | OMN-SA v0.8.3" in text
        or "Current software layer | OMN-SA v0.9" in text
        or "Current software layer | OMN-SA v1." in text
    )

    ai_tracking_is_v082_or_newer = (
        "Current software architecture layer: OMN-SA v0.8.2" in text
        or "Current software architecture layer: OMN-SA v0.8.3" in text
        or "Current software architecture layer: OMN-SA v0.9" in text
        or "Current software architecture layer: OMN-SA v1." in text
    )

    checks = {
        "current_health_v082_or_newer": current_is_v082_or_newer,
        "ai_tracking_v082_or_newer": ai_tracking_is_v082_or_newer,
        "ai_readme_update_policy_present": "## AI README Update Policy" in text,
        "policy_lists_required_zones": "Required root README update zones" in text,
        "current_stack_v082": "omn_sa_v0_8_2_readme_lineage_policy.md" in text,
        "current_stack_v081": "omn_sa_v0_8_1_validation_compatibility_repair.md" in text,
        "current_stack_v08": "omn_sa_v0_8_metric_availability_residual_hardening.md" in text,
        "architecture_chain_v082": "OMN-SA v0.8.2 README lineage and AI update policy" in text,
        "bottom_v08_section_present": "## OMN-SA v0.8 Metric Availability and Residual Field Hardening" in text,
        "bottom_v081_section_present": "## OMN-SA v0.8.1 Validation Compatibility Repair" in text,
        "bottom_v082_section_present": "## OMN-SA v0.8.2 README Lineage and AI Update Policy" in text,
        "loose_chain_extensions_removed": "Current architecture chain extension:" not in text,
        "v08_metric_availability_declared": "`omega_residual_weight` | 8 / 8" in text,
    }

    missing = [key for key, value in checks.items() if not value]

    report = {
        "schema": "OMN-SA-v0.8.2-readme-lineage-policy-audit",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "passed": len(missing) == 0,
        "checks": checks,
        "missing": missing,
        "non_claim_boundary": NON_CLAIM_BOUNDARY,
    }

    out_dir = ROOT / "reports" / "readme_policy"
    out_dir.mkdir(parents=True, exist_ok=True)

    json_path = out_dir / "latest_readme_lineage_policy_audit.json"
    md_path = out_dir / "latest_readme_lineage_policy_audit.md"

    json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    lines = [
        "# OMN-SA v0.8.2 README Lineage Policy Audit",
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