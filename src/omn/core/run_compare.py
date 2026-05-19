from __future__ import annotations

from typing import Any, Dict, List, Optional


NON_CLAIM_BOUNDARY = (
    "Run comparison reports metric drift between evidence records. "
    "It does not prove correctness, empirical validation, causality, mechanism, "
    "production readiness, AI understanding, or GMN replication."
)


def safe_number(value: Any) -> Optional[float]:
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


def compare_metric(before: Dict[str, Any], after: Dict[str, Any], path: List[str]) -> Dict[str, Any]:
    left = safe_number(get_nested(before, path))
    right = safe_number(get_nested(after, path))

    if left is None or right is None:
        return {
            "path": ".".join(path),
            "before": left,
            "after": right,
            "delta": None,
            "status": "unavailable",
        }

    return {
        "path": ".".join(path),
        "before": left,
        "after": right,
        "delta": right - left,
        "status": "computed",
    }


def compare_evidence_records(before: Dict[str, Any], after: Dict[str, Any]) -> Dict[str, Any]:
    metric_paths = [
        ["metrics", "validation", "rmse"],
        ["metrics", "validation", "mae"],
        ["metrics", "validation", "delta_phi_residual"],
        ["metrics", "validation", "omega_residual_weight"],
    ]

    comparisons = [compare_metric(before, after, path) for path in metric_paths]

    return {
        "schema": "OMN-SA-v0.6-evidence-comparison",
        "before_run_id": before.get("run_id"),
        "after_run_id": after.get("run_id"),
        "comparisons": comparisons,
        "non_claim_boundary": NON_CLAIM_BOUNDARY,
    }