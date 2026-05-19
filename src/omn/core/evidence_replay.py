from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional


NON_CLAIM_BOUNDARY = (
    "Evidence replay checks whether a stored evidence package can be reloaded, "
    "its declared artifacts can be inspected, and its claim boundaries remain present. "
    "It does not prove code correctness, empirical validation, causality, mechanism, "
    "production readiness, AI understanding, or GMN replication."
)


def list_evidence_packages(repo_root: str) -> List[Path]:
    root = Path(repo_root)
    evidence_dir = root / "outputs" / "evidence"
    if not evidence_dir.exists():
        return []
    return sorted(evidence_dir.glob("*_evidence_package.json"), key=lambda p: p.stat().st_mtime)


def latest_evidence_package(repo_root: str) -> Optional[Path]:
    packages = list_evidence_packages(repo_root)
    return packages[-1] if packages else None


def load_json(path: Path) -> Dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return {
            "_load_error": str(exc),
            "_path": str(path),
        }


def flatten_declared_paths(value: Any) -> List[str]:
    paths: List[str] = []

    if isinstance(value, str):
        if value.endswith((".json", ".jsonl", ".csv", ".md", ".png", ".svg", ".txt")) or "/" in value or "\\" in value:
            paths.append(value)

    elif isinstance(value, dict):
        for nested in value.values():
            paths.extend(flatten_declared_paths(nested))

    elif isinstance(value, list):
        for nested in value:
            paths.extend(flatten_declared_paths(nested))

    return paths


def replay_evidence(path: Path, repo_root: str) -> Dict[str, Any]:
    root = Path(repo_root)
    payload = load_json(path)

    declared = sorted(set(flatten_declared_paths(payload.get("artifacts", {}))))
    existing: List[str] = []
    missing: List[str] = []

    for rel in declared:
        candidate = root / rel
        if candidate.exists():
            existing.append(rel)
        else:
            missing.append(rel)

    claim_status = payload.get("claim_status", {})
    source_boundary = payload.get("source_boundary", {})
    metrics = payload.get("metrics", {})

    failure_flags: List[str] = []

    if "_load_error" in payload:
        failure_flags.append("evidence_json_load_error")
    if not source_boundary:
        failure_flags.append("missing_source_boundary")
    if not claim_status:
        failure_flags.append("missing_claim_status")
    if not metrics:
        failure_flags.append("missing_metrics")
    if missing:
        failure_flags.append("missing_declared_artifacts")

    return {
        "schema": "OMN-SA-v0.6-evidence-replay-record",
        "evidence_path": str(path.relative_to(root)) if path.is_relative_to(root) else str(path),
        "run_id": payload.get("run_id"),
        "seed": payload.get("seed"),
        "claim_status": claim_status,
        "declared_artifact_count": len(declared),
        "existing_artifacts": existing,
        "missing_artifacts": missing,
        "failure_flags": failure_flags,
        "passed": not failure_flags,
        "non_claim_boundary": NON_CLAIM_BOUNDARY,
    }


def replay_latest(repo_root: str) -> Dict[str, Any]:
    latest = latest_evidence_package(repo_root)
    if latest is None:
        return {
            "schema": "OMN-SA-v0.6-evidence-replay-record",
            "passed": False,
            "failure_flags": ["no_evidence_packages_found"],
            "non_claim_boundary": NON_CLAIM_BOUNDARY,
        }
    return replay_evidence(latest, repo_root)