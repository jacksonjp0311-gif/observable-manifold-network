from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List


NON_CLAIM_BOUNDARY = (
    "Run ledger integrity checks append-only continuity and hash chaining for local run records. "
    "It does not prove code correctness, empirical validation, causality, mechanism, "
    "production readiness, AI understanding, or GMN replication."
)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def record_hash(record: Dict[str, Any]) -> str:
    copy = dict(record)
    copy.pop("record_hash", None)
    canonical = json.dumps(copy, sort_keys=True, separators=(",", ":"))
    return sha256_text(canonical)


def ledger_path(repo_root: str) -> Path:
    return Path(repo_root) / "outputs" / "ledger" / "omn_run_ledger_v0_6.jsonl"


def append_run_record(repo_root: str, record: Dict[str, Any]) -> Dict[str, Any]:
    path = ledger_path(repo_root)
    path.parent.mkdir(parents=True, exist_ok=True)

    previous_hash = None

    if path.exists():
        lines = [line for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
        if lines:
            try:
                previous_hash = json.loads(lines[-1]).get("record_hash")
            except Exception:
                previous_hash = None

    enriched = dict(record)
    enriched["schema"] = "OMN-SA-v0.6-run-ledger-record"
    enriched["previous_hash"] = previous_hash
    enriched["non_claim_boundary"] = NON_CLAIM_BOUNDARY
    enriched["record_hash"] = record_hash(enriched)

    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(enriched, sort_keys=True) + "\n")

    return enriched


def read_ledger(repo_root: str) -> List[Dict[str, Any]]:
    path = ledger_path(repo_root)
    if not path.exists():
        return []

    records: List[Dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except Exception:
            records.append({"_parse_error": line})
    return records


def verify_ledger(repo_root: str) -> Dict[str, Any]:
    records = read_ledger(repo_root)
    failures: List[str] = []

    previous = None

    for index, record in enumerate(records):
        if "_parse_error" in record:
            failures.append(f"parse_error:{index}")
            continue

        expected = record_hash(record)
        actual = record.get("record_hash")

        if expected != actual:
            failures.append(f"hash_mismatch:{index}")

        if record.get("previous_hash") != previous:
            failures.append(f"previous_hash_mismatch:{index}")

        previous = actual

    return {
        "schema": "OMN-SA-v0.6-run-ledger-integrity-report",
        "records": len(records),
        "passed": not failures,
        "failure_flags": failures,
        "ledger_path": str(ledger_path(repo_root)),
        "non_claim_boundary": NON_CLAIM_BOUNDARY,
    }