from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Optional


def latest_evidence_path(repo_root: str) -> Optional[Path]:
    evidence_dir = Path(repo_root) / "outputs" / "evidence"
    if not evidence_dir.exists():
        return None
    candidates = sorted(evidence_dir.glob("*_evidence_package.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    return candidates[0] if candidates else None


def load_latest_evidence(repo_root: str) -> Dict[str, Any]:
    path = latest_evidence_path(repo_root)
    if path is None:
        return {}
    with path.open("r", encoding="utf-8") as f:
        payload = json.load(f)
    payload["_loaded_from"] = str(path)
    return payload


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")