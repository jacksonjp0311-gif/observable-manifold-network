import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from omn.core.topology_ensemble import run_threshold_ensemble


def main() -> int:
    columns = {
        "x": [0, 1, 2, 3, 4, 5],
        "y": [0, 2, 4, 6, 8, 10],
        "z": [5, 4, 3, 2, 1, 0],
    }

    report = run_threshold_ensemble(
        columns=columns,
        run_id="omn_sa_v0_5_topology_ensemble_validation",
        thresholds=[0.10, 0.25, 0.50, 0.90],
    )

    out_dir = ROOT / "reports" / "topology_ensemble"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "latest_topology_ensemble_validation.json"
    out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(json.dumps(report, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())