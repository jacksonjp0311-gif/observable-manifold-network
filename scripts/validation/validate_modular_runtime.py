import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from omn.core.modular_runtime import run_modular, validate_modular_runtime


def main() -> int:
    module_report = validate_modular_runtime(str(ROOT))
    run_report = run_modular("synthetic-toy", str(ROOT))

    report = {
        "schema": "OMN-SA-v0.3-modular-runtime-validation-report",
        "passed": bool(module_report["passed"]) and bool(run_report["claim_gate"]["overpromotion_blocked"]),
        "module_report": module_report,
        "run_report_path": "reports/modular_runtime/latest_modular_runtime_report.json",
        "run_id": run_report.get("run_id"),
        "non_claim_boundary": "Modular runtime validation checks contract wrapping and runtime emission. It does not prove empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.",
    }

    out_dir = ROOT / "reports" / "modular_runtime"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "latest_modular_runtime_validation.json"
    out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(json.dumps(report, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())