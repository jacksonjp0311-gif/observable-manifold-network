from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"

NON_CLAIM_BOUNDARY = (
    "README v0.8 metric availability audit checks current-state orientation and metric dashboard presence. "
    "It does not prove code correctness, empirical validation, causality, mechanism, production readiness, "
    "AI understanding, or GMN replication."
)


def main() -> int:
    text = README.read_text(encoding="utf-8", errors="ignore")

    checks = {
        "current_layer_v08": "Current software layer | OMN-SA v0.8" in text,
        "metric_availability_section_present": "Current v0.8 Metric Availability and Residual Field Hardening" in text,
        "metric_chart_present": "visuals/omn_sa/omn_sa_v0_8_metric_availability.svg" in text,
        "rmse_path_present": "metrics.validation.rmse" in text,
        "mae_path_present": "metrics.validation.mae" in text,
        "delta_phi_path_present": "metrics.validation.delta_phi_residual" in text,
        "omega_path_present": "metrics.validation.omega_residual_weight" in text,
        "v08_chain_present": "OMN-SA v0.8 metric availability and residual field hardening" in text,
    }

    missing = [key for key, value in checks.items() if not value]

    report = {
        "schema": "OMN-SA-v0.8-readme-metric-availability-audit",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "passed": len(missing) == 0,
        "checks": checks,
        "missing": missing,
        "non_claim_boundary": NON_CLAIM_BOUNDARY,
    }

    out_dir = ROOT / "reports" / "metric_availability"
    out_dir.mkdir(parents=True, exist_ok=True)

    (out_dir / "latest_readme_v0_8_metric_availability_audit.json").write_text(json.dumps(report, indent=2), encoding="utf-8")

    lines = [
        "# OMN-SA v0.8 README Metric Availability Audit",
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

    (out_dir / "latest_readme_v0_8_metric_availability_audit.md").write_text("\n".join(lines), encoding="utf-8")

    print(json.dumps(report, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())