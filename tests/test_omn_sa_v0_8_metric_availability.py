import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestOMNSAV08MetricAvailability(unittest.TestCase):
    def test_runtime_emits_canonical_metric_block(self):
        result = subprocess.run(
            [sys.executable, "-m", "omn", "run", "--seed", "synthetic-toy"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

        payload = json.loads(result.stdout)
        evidence_path = ROOT / payload["evidence_package"]
        self.assertTrue(evidence_path.exists())

        evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
        self.assertEqual(evidence["schema"], "OMN-SA-v0.8-evidence-package")
        self.assertIn("validation", evidence["metrics"])
        self.assertIn("baseline", evidence["metrics"])

        validation = evidence["metrics"]["validation"]
        for key in ["rmse", "mae", "correlation", "delta_phi_residual", "omega_residual_weight"]:
            self.assertIn(key, validation)
            self.assertIsInstance(validation[key], (float, int))

    def test_metric_availability_validator_passes(self):
        for seed in ["synthetic-toy", "lorenz", "artifact-graph"]:
            result = subprocess.run(
                [sys.executable, "-m", "omn", "run", "--seed", seed],
                cwd=ROOT,
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

        result = subprocess.run(
            [sys.executable, "scripts/validation/validate_metric_availability.py"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

        report_path = ROOT / "reports" / "metric_availability" / "latest_metric_availability_report.json"
        report = json.loads(report_path.read_text(encoding="utf-8"))
        self.assertTrue(report["passed"], report)

    def test_readme_v08_audit_passes(self):
        subprocess.run(
            [sys.executable, "scripts/release/canonicalize_readme_v0_8.py"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )

        result = subprocess.run(
            [sys.executable, "scripts/release/audit_readme_v0_8_metric_availability.py"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()