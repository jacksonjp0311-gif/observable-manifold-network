import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from omn.core.evidence_io import write_json
from omn.core.graph_engine import build_graph_engine_state, graph_engine_parity_summary
from omn.core.runtime import run as legacy_run


def main() -> int:
    run_id = "omn_sa_v0_4_graph_engine_validation"

    columns = {
        "x": [0.0, 1.0, 2.0, 3.0, 4.0],
        "y": [0.0, 2.0, 4.0, 6.0, 8.0],
        "z": [4.0, 3.0, 2.0, 1.0, 0.0]
    }

    legacy_evidence = legacy_run("synthetic-toy", str(ROOT))
    graph_state = build_graph_engine_state(columns, run_id=run_id, threshold=0.20)
    parity = graph_engine_parity_summary(legacy_evidence, graph_state)

    report = {
        "schema": "OMN-SA-v0.4-graph-engine-validation-report",
        "passed": bool(graph_state["graph_contract"]["valid"]) and bool(parity["passed"]),
        "graph_state": graph_state,
        "parity": parity,
        "legacy_run_id": legacy_evidence.get("run_id"),
        "non_claim_boundary": "Graph engine validation checks modular graph-contract extraction and parity surfaces. It does not prove causality, mechanism, empirical validation, production readiness, AI understanding, or GMN replication."
    }

    out_path = ROOT / "reports" / "graph_engine" / "latest_graph_engine_validation.json"
    write_json(out_path, report)
    print(json.dumps(report, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())