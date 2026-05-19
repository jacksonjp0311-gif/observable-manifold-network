from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from omn.core.artifact_audit import audit_declared_paths, minimal_evidence_keys
from omn.core.claim_gate import compute_claim_status
from omn.core.contracts import non_claim_locks
from omn.core.runtime import run as legacy_run


def run_modular(seed: str, repo_root: str) -> Dict[str, Any]:
    evidence = legacy_run(seed, repo_root)

    claim_gate = compute_claim_status(evidence)
    key_audit = minimal_evidence_keys(evidence)
    path_audit = audit_declared_paths(evidence, repo_root)

    envelope = {
        "schema": "OMN-SA-v0.3-modular-runtime-envelope",
        "run_id": evidence.get("run_id"),
        "seed": seed,
        "legacy_runtime_used": True,
        "modular_layer": {
            "contracts": "omn.core.contracts",
            "claim_gate": "omn.core.claim_gate",
            "artifact_audit": "omn.core.artifact_audit",
            "schema_contracts": "omn.core.schema_contracts",
        },
        "claim_gate": claim_gate,
        "evidence_key_audit": key_audit,
        "artifact_path_audit": path_audit,
        "non_claim_locks": non_claim_locks(),
        "evidence_package": evidence.get("evidence_package") or evidence.get("artifacts", {}).get("evidence_package"),
        "boundary": "The v0.3 modular wrapper validates contracts around the current runtime. It does not prove empirical validity, causality, mechanism, production readiness, AI understanding, or GMN replication.",
    }

    out_dir = Path(repo_root) / "reports" / "modular_runtime"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "latest_modular_runtime_report.json"
    out_path.write_text(json.dumps(envelope, indent=2), encoding="utf-8")

    return envelope


def validate_modular_runtime(repo_root: str) -> Dict[str, Any]:
    root = Path(repo_root)
    required_modules = [
        "src/omn/core/contracts.py",
        "src/omn/core/claim_gate.py",
        "src/omn/core/artifact_audit.py",
        "src/omn/core/schema_contracts.py",
        "src/omn/core/modular_runtime.py",
    ]
    missing = [path for path in required_modules if not (root / path).exists()]

    return {
        "schema": "OMN-SA-v0.3-modular-runtime-validation",
        "passed": not missing,
        "missing": missing,
        "boundary": "Modular runtime validation checks module presence, not code correctness or scientific validation.",
    }