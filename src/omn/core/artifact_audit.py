from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List


def _flatten_paths(value: Any) -> List[str]:
    paths: List[str] = []

    if isinstance(value, str):
        if value and ("/" in value or "\\" in value or value.endswith((".json", ".csv", ".md", ".png", ".txt", ".jsonl"))):
            paths.append(value)

    if isinstance(value, dict):
        for nested in value.values():
            paths.extend(_flatten_paths(nested))

    if isinstance(value, list):
        for nested in value:
            paths.extend(_flatten_paths(nested))

    return paths


def audit_declared_paths(evidence: Dict[str, Any], repo_root: str) -> Dict[str, Any]:
    root = Path(repo_root)
    declared = sorted(set(_flatten_paths(evidence.get("artifacts", {}))))
    missing: List[str] = []

    for rel in declared:
        candidate = root / rel
        if not candidate.exists():
            missing.append(rel)

    return {
        "declared_count": len(declared),
        "missing": missing,
        "passed": len(missing) == 0,
        "boundary": "Artifact path audit checks declared file existence, not scientific validity or code correctness.",
    }


def minimal_evidence_keys(evidence: Dict[str, Any]) -> Dict[str, Any]:
    required = [
        "run_id",
        "seed",
        "claim_status",
        "source_boundary",
        "metrics",
        "artifacts",
        "baselines",
        "topology_sensitivity",
    ]
    missing = [key for key in required if key not in evidence]
    return {
        "required": required,
        "missing": missing,
        "passed": not missing,
        "boundary": "Evidence key audit checks contract completeness, not empirical validation.",
    }