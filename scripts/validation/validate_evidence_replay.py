import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from omn.core.evidence_replay import replay_latest
from omn.core.run_ledger import append_run_record, verify_ledger


def main() -> int:
    replay = replay_latest(str(ROOT))

    record = {
        "run_id": replay.get("run_id"),
        "seed": replay.get("seed"),
        "evidence_path": replay.get("evidence_path"),
        "replay_passed": replay.get("passed"),
        "declared_artifact_count": replay.get("declared_artifact_count", 0),
        "missing_artifact_count": len(replay.get("missing_artifacts", [])),
    }

    ledger_record = append_run_record(str(ROOT), record)
    ledger_report = verify_ledger(str(ROOT))

    report = {
        "schema": "OMN-SA-v0.6-evidence-replay-validation-report",
        "passed": bool(replay.get("passed")) and bool(ledger_report.get("passed")),
        "replay": replay,
        "ledger_record": ledger_record,
        "ledger_integrity": ledger_report,
        "non_claim_boundary": "Evidence replay and ledger integrity validate local artifact continuity. They do not prove code correctness, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.",
    }

    out_dir = ROOT / "reports" / "evidence_replay"
    out_dir.mkdir(parents=True, exist_ok=True)

    out_path = out_dir / "latest_evidence_replay_validation.json"
    out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    md_path = out_dir / "latest_evidence_replay_validation.md"
    md_path.write_text(
        "\n".join([
            "# Evidence Replay Validation",
            "",
            f"- Passed: {report['passed']}",
            f"- Run ID: {replay.get('run_id')}",
            f"- Evidence path: {replay.get('evidence_path')}",
            f"- Declared artifacts: {replay.get('declared_artifact_count')}",
            f"- Missing artifacts: {len(replay.get('missing_artifacts', []))}",
            f"- Ledger records: {ledger_report.get('records')}",
            "",
            "## Boundary",
            "",
            report["non_claim_boundary"],
            "",
        ]),
        encoding="utf-8",
    )

    print(json.dumps(report, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())