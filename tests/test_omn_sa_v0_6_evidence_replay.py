import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from omn.core.evidence_replay import latest_evidence_package, replay_latest
from omn.core.run_ledger import append_run_record, verify_ledger
from omn.core.run_compare import compare_evidence_records


class TestOMNSAV06EvidenceReplay(unittest.TestCase):
    def test_latest_evidence_package_exists_after_seed_run(self):
        subprocess.run(
            [sys.executable, "-m", "omn", "run", "--seed", "synthetic-toy"],
            cwd=ROOT,
            check=True,
            text=True,
            capture_output=True,
        )
        path = latest_evidence_package(str(ROOT))
        self.assertIsNotNone(path)

    def test_replay_latest_evidence(self):
        subprocess.run(
            [sys.executable, "-m", "omn", "run", "--seed", "synthetic-toy"],
            cwd=ROOT,
            check=True,
            text=True,
            capture_output=True,
        )
        replay = replay_latest(str(ROOT))
        self.assertEqual(replay["schema"], "OMN-SA-v0.6-evidence-replay-record")
        self.assertIn("failure_flags", replay)
        self.assertIn("non_claim_boundary", replay)

    def test_ledger_append_and_verify(self):
        record = append_run_record(str(ROOT), {"run_id": "test-v0-6", "seed": "synthetic-toy"})
        self.assertIn("record_hash", record)
        report = verify_ledger(str(ROOT))
        self.assertTrue(report["passed"], report)

    def test_compare_evidence_records_shape(self):
        before = {
            "run_id": "a",
            "metrics": {"validation": {"rmse": 1.0, "mae": 0.5, "delta_phi_residual": 0.2, "omega_residual_weight": 0.8}},
        }
        after = {
            "run_id": "b",
            "metrics": {"validation": {"rmse": 0.5, "mae": 0.25, "delta_phi_residual": 0.1, "omega_residual_weight": 0.9}},
        }
        comparison = compare_evidence_records(before, after)
        self.assertEqual(comparison["schema"], "OMN-SA-v0.6-evidence-comparison")
        self.assertEqual(comparison["before_run_id"], "a")
        self.assertEqual(comparison["after_run_id"], "b")
        self.assertEqual(len(comparison["comparisons"]), 4)

    def test_validation_script_passes(self):
        subprocess.run(
            [sys.executable, "-m", "omn", "run", "--seed", "synthetic-toy"],
            cwd=ROOT,
            check=True,
            text=True,
            capture_output=True,
        )
        result = subprocess.run(
            [sys.executable, "scripts/validation/validate_evidence_replay.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        report_path = ROOT / "reports" / "evidence_replay" / "latest_evidence_replay_validation.json"
        self.assertTrue(report_path.exists())
        report = json.loads(report_path.read_text(encoding="utf-8"))
        self.assertTrue(report["passed"])


if __name__ == "__main__":
    unittest.main()