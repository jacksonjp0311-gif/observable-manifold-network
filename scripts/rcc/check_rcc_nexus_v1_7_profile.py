from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime, timezone
from typing import Any, Dict, List


ROOT = Path(__file__).resolve().parents[2]

PROFILES = ["Lite", "Standard", "Full", "Federated", "Critical"]
PROFILE_RANK = {
    "Lite": 1,
    "Standard": 2,
    "Full": 3,
    "Federated": 4,
    "Critical": 5,
}

NON_CLAIM_BOUNDARY = (
    "RCC-N v1.7 profile checks verify profile declaration, minimal viable RCC-N, "
    "utility-evidence boundaries, corrective governance, and GEN-R boundary. "
    "They do not prove code correctness, patch safety, empirical validation, "
    "causality, mechanism, AI understanding, production readiness, GMN replication, "
    "or full GEN v1.0."
)


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return {"_load_error": str(exc)}


def clamp01(value: Any) -> float:
    try:
        return max(0.0, min(1.0, float(value)))
    except Exception:
        return 0.0


def governance_need(selection: Dict[str, Any]) -> float:
    weights = {
        "risk": 0.25,
        "complexity": 0.20,
        "validation_need": 0.20,
        "federation_need": 0.20,
        "public_claim_surface": 0.15,
    }
    return round(sum(weights[key] * clamp01(selection.get(key, 0.0)) for key in weights), 4)


def recommended_profile(score: float, selection: Dict[str, Any]) -> str:
    risk = clamp01(selection.get("risk", 0.0))
    validation = clamp01(selection.get("validation_need", 0.0))
    federation = clamp01(selection.get("federation_need", 0.0))
    claims = clamp01(selection.get("public_claim_surface", 0.0))

    if risk >= 0.80 or validation >= 0.80 or claims >= 0.80:
        return "Critical"
    if federation >= 0.70:
        return "Federated"
    if score >= 0.50:
        return "Full"
    if score >= 0.25:
        return "Standard"
    return "Lite"


def finding(code: str, severity: str, message: str) -> Dict[str, str]:
    return {"code": code, "severity": severity, "message": message}


def main() -> int:
    profile_path = ROOT / "docs" / "context" / "rcc_nexus_profile_v1_7.json"
    profile = load_json(profile_path)

    findings: List[Dict[str, str]] = []

    if not profile:
        findings.append(finding("RCCN093", "error", "RCC-N v1.7 profile config missing."))
    if profile.get("_load_error"):
        findings.append(finding("RCCN093", "error", f"RCC-N v1.7 profile config load error: {profile.get('_load_error')}"))

    repo = profile.get("repository", {})
    declared = repo.get("adoption_profile")

    if declared not in PROFILES:
        findings.append(finding("RCCN093", "error", f"Missing or invalid adoption profile: {declared}"))

    selection = profile.get("profile_selection", {})
    computed_score = governance_need(selection)
    recommended = recommended_profile(computed_score, selection)

    if declared in PROFILES:
        if PROFILE_RANK[declared] < PROFILE_RANK[recommended]:
            findings.append(finding("RCCN095", "error", f"Repository may be under-governed: declared {declared}, recommended {recommended}."))
        if PROFILE_RANK[declared] > PROFILE_RANK[recommended] + 1:
            findings.append(finding("RCCN094", "warning", f"Repository may be over-governed: declared {declared}, recommended {recommended}."))

    minimal = profile.get("minimal_viable_rccn", {})
    required_minimal = [
        "public_spine_present",
        "readme_trisection_present",
        "ai_agent_section_present",
        "major_echo_locations_present",
        "validation_commands_declared",
        "non_claim_locks_present",
        "done_criteria_present",
    ]
    missing_minimal = [key for key in required_minimal if minimal.get(key) is not True]
    if missing_minimal:
        findings.append(finding("RCCN096", "error", f"Minimal viable RCC-N missing: {missing_minimal}"))

    utility = profile.get("utility_evidence", {})
    if utility.get("claims_rccn_improves_maintenance") is True:
        if utility.get("baseline_comparison_present") is not True:
            findings.append(finding("RCCN098", "error", "Utility claim made without baseline comparison."))
        if utility.get("task_trace_present") is not True or utility.get("validation_outcome_present") is not True:
            findings.append(finding("RCCN099", "error", "Utility claim made without task trace and validation outcome."))
        if utility.get("cost_accounting_present") is not True:
            findings.append(finding("RCCN100", "warning", "Utility claim made without governance cost accounting."))

    corrective = profile.get("corrective_governance", {})
    if corrective.get("correction_is_not_deletion") is not True or corrective.get("history_must_be_preserved") is not True:
        findings.append(finding("RCCN102", "error", "Corrective governance history preservation lock missing."))

    gen = profile.get("gen_boundary", {})
    if gen.get("claims_full_gen_v1_0") is True or gen.get("rccn_v1_7_is_not_gen_v1_0") is not True:
        findings.append(finding("RCCN105", "warning", "GEN boundary is unclear or overclaimed."))

    locks = profile.get("non_claim_locks", {})
    required_locks = [
        "profile_adoption_is_not_validation",
        "minimal_compliance_is_not_full_compliance",
        "utility_claims_require_baseline_comparison",
        "governance_cost_must_be_disclosed_for_utility_claims",
        "correction_is_not_deletion",
        "rccn_is_repository_profile_not_full_gen",
        "validation_remains_required",
    ]
    missing_locks = [key for key in required_locks if locks.get(key) is not True]
    if missing_locks:
        findings.append(finding("RCCN106", "blocking", f"Missing RCC-N v1.7 non-claim locks: {missing_locks}"))

    status = "pass"
    if any(item["severity"] == "blocking" for item in findings):
        status = "blocked"
    elif any(item["severity"] == "error" for item in findings):
        status = "manual_review_required"
    elif findings:
        status = "warning"

    report = {
        "schema": "RCC-N-v1.7-profile-check-report",
        "repository": "observable-manifold-network",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "status": status,
        "passed": status == "pass",
        "declared_profile": declared,
        "computed_governance_need": computed_score,
        "recommended_profile": recommended,
        "lightest_sufficient_profile": declared == recommended,
        "minimal_viable_rccn_passed": not missing_minimal,
        "utility_status": utility.get("utility_status"),
        "claims_rccn_improves_maintenance": utility.get("claims_rccn_improves_maintenance"),
        "gen_boundary": "GEN-R",
        "rccn_v1_7_is_not_gen_v1_0": gen.get("rccn_v1_7_is_not_gen_v1_0"),
        "findings": findings,
        "non_claim_boundary": NON_CLAIM_BOUNDARY,
    }

    out_dir = ROOT / "reports" / "rcc_nexus"
    out_dir.mkdir(parents=True, exist_ok=True)

    (out_dir / "latest_rcc_nexus_v1_7_profile_check.json").write_text(json.dumps(report, indent=2), encoding="utf-8")

    md = [
        "# RCC-N v1.7 Profile Check",
        "",
        f"- Passed: {report['passed']}",
        f"- Status: {report['status']}",
        f"- Declared profile: {report['declared_profile']}",
        f"- Computed governance need: {report['computed_governance_need']}",
        f"- Recommended profile: {report['recommended_profile']}",
        f"- Lightest sufficient profile: {report['lightest_sufficient_profile']}",
        f"- Minimal viable RCC-N passed: {report['minimal_viable_rccn_passed']}",
        f"- Utility status: {report['utility_status']}",
        f"- GEN boundary: {report['gen_boundary']}",
        "",
        "## Findings",
        "",
    ]

    if findings:
        for item in findings:
            md.append(f"- {item['severity']} {item['code']}: {item['message']}")
    else:
        md.append("- None")

    md.extend([
        "",
        "## Boundary",
        "",
        NON_CLAIM_BOUNDARY,
        "",
    ])

    (out_dir / "latest_rcc_nexus_v1_7_profile_check.md").write_text("\n".join(md), encoding="utf-8")

    print(json.dumps(report, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())