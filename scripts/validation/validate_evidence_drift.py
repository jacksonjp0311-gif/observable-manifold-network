import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from omn.core.evidence_drift import evidence_drift_report, write_evidence_drift_outputs


def main() -> int:
    report = evidence_drift_report(str(ROOT), limit=8)
    outputs = write_evidence_drift_outputs(str(ROOT), report)

    validation = {
        "schema": "OMN-SA-v0.7-evidence-drift-validation",
        "passed": bool(report.get("passed")) and all(Path(path).exists() for path in outputs.values()),
        "report": report,
        "outputs": outputs,
        "non_claim_boundary": "Evidence drift validation checks multi-run continuity and dashboard emission. It does not prove correctness, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.",
    }

    out_path = ROOT / "reports" / "evidence_drift" / "latest_evidence_drift_validation.json"
    out_path.write_text(json.dumps(validation, indent=2), encoding="utf-8")

    print(json.dumps(validation, indent=2))
    return 0 if validation["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())