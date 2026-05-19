from __future__ import annotations

from typing import Any, Dict, List


BLOCKED_STATUS = "blocked"
DEMO_STATUS = "demo-only"
RUNTIME_STATUS = "runtime-validated"
BENCHMARK_STATUS = "benchmark-supported"


def compute_claim_status(evidence: Dict[str, Any]) -> Dict[str, Any]:
    failure_flags: List[str] = []

    if not evidence:
        failure_flags.append("missing_evidence")

    if not evidence.get("source_boundary"):
        failure_flags.append("missing_source_boundary")

    artifacts = evidence.get("artifacts", {})
    if not artifacts:
        failure_flags.append("missing_artifacts")

    if not evidence.get("claim_status"):
        failure_flags.append("missing_claim_status")

    audit = evidence.get("audit", {})
    if audit and audit.get("passed") is False:
        failure_flags.append("audit_not_passed")

    baseline_equivalent = evidence.get("baselines", {}).get("baseline_equivalent")
    topology = evidence.get("topology_sensitivity", {})
    topology_sensitive = bool(topology.get("sensitive", False))

    if failure_flags:
        status = BLOCKED_STATUS
    else:
        status = evidence.get("claim_status", {}).get("computed_status") or RUNTIME_STATUS

    if baseline_equivalent is True and status == BENCHMARK_STATUS:
        status = RUNTIME_STATUS

    if topology_sensitive and status == BENCHMARK_STATUS:
        status = RUNTIME_STATUS

    return {
        "computed_status": status,
        "failure_flags": failure_flags,
        "allowed_claim": "Local runtime evidence may support implementation behavior only.",
        "prohibited_claim": "This run does not prove causality, mechanism, biological equivalence, physical manifold identity, empirical validation, production readiness, AI understanding, or GMN replication.",
        "overpromotion_blocked": True,
        "baseline_equivalent": baseline_equivalent,
        "topology_sensitive": topology_sensitive,
    }


def claim_gate_passed(claim_status: Dict[str, Any]) -> bool:
    return bool(claim_status.get("overpromotion_blocked")) and claim_status.get("computed_status") != BLOCKED_STATUS