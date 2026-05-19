from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict


def load_schema_contract(repo_root: str, relative_path: str) -> Dict[str, Any]:
    path = Path(repo_root) / relative_path
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def validate_required_keys(payload: Dict[str, Any], contract: Dict[str, Any]) -> Dict[str, Any]:
    required = contract.get("required_keys", [])
    missing = [key for key in required if key not in payload]
    return {
        "schema_id": contract.get("schema_id"),
        "missing": missing,
        "passed": not missing,
        "boundary": contract.get("boundary", "Schema contract validation is not truth."),
    }