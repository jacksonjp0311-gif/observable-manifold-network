import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from omn.core.evidence_drift import evidence_drift_report, write_evidence_drift_outputs


class TestOMNSAV07EvidenceDrift(unittest.TestCase):
    def test_evidence_drift_report_shape(self):
        subprocess.run([sys.executable, "-m", "omn", "run", "--seed", "synthetic-toy"], cwd=ROOT, check=True, capture_output=True, text=True)
        subprocess.run([sys.executable, "-m", "omn", "run", "--seed", "artifact-graph"], cwd=ROOT, check=True, capture_output=True, text=True)

        report = evidence_drift_report(str(ROOT), limit=8)
        self.assertEqual(report["schema"], "OMN-SA-v0.7-evidence-drift-report")
        self.assertGreaterEqual(report["compared_count"], 2)
        self.assertIn("artifact_count_spread", report)
        self.assertIn("metric_drift", report)
        self.assertIn("non_claim_boundary", report)

    def test_evidence_drift_outputs_written(self):
        report = evidence_drift_report(str(ROOT), limit=8)
        outputs = write_evidence_drift_outputs(str(ROOT), report)

        for path in outputs.values():
            self.assertTrue(Path(path).exists(), path)

    def test_evidence_drift_validation_script_passes(self):
        subprocess.run([sys.executable, "-m", "omn", "run", "--seed", "synthetic-toy"], cwd=ROOT, check=True, capture_output=True, text=True)
        subprocess.run([sys.executable, "-m", "omn", "run", "--seed", "artifact-graph"], cwd=ROOT, check=True, capture_output=True, text=True)

        result = subprocess.run(
            [sys.executable, "scripts/validation/validate_evidence_drift.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

        validation_path = ROOT / "reports" / "evidence_drift" / "latest_evidence_drift_validation.json"
        self.assertTrue(validation_path.exists())

        validation = json.loads(validation_path.read_text(encoding="utf-8"))
        self.assertTrue(validation["passed"], validation)

    def test_dashboard_path_exists_after_validation(self):
        subprocess.run(
            [sys.executable, "scripts/validation/validate_evidence_drift.py"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        chart = ROOT / "visuals" / "omn_sa" / "omn_sa_v0_7_evidence_drift_dashboard.svg"
        self.assertTrue(chart.exists())


if __name__ == "__main__":
    unittest.main()