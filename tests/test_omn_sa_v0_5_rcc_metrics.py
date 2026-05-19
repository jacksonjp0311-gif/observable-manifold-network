import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from omn.core.topology_ensemble import run_threshold_ensemble


class TestOMNSAV05RCCMetrics(unittest.TestCase):
    def test_topology_ensemble_runs(self):
        report = run_threshold_ensemble(
            {"x": [0, 1, 2], "y": [0, 2, 4], "z": [2, 1, 0]},
            "test",
            [0.1, 0.5, 0.9],
        )
        self.assertEqual(report["schema"], "OMN-SA-v0.5-topology-ensemble")
        self.assertTrue(report["passed"])
        self.assertIn("edge_stability", report)
        self.assertIn("classification_flip_detected", report)

    def test_mini_readme_audit_script(self):
        result = subprocess.run(
            [sys.executable, "scripts/rcc/audit_mini_readmes.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        path = ROOT / "reports" / "mini_readmes" / "latest_mini_readme_audit.json"
        self.assertTrue(path.exists())
        report = json.loads(path.read_text(encoding="utf-8"))
        self.assertGreaterEqual(report["coverage"], 0.90)

    def test_rcc_n_metrics_script(self):
        subprocess.run(
            [sys.executable, "scripts/rcc/audit_mini_readmes.py"],
            cwd=ROOT,
            check=True,
            text=True,
            capture_output=True,
        )
        result = subprocess.run(
            [sys.executable, "scripts/rcc/generate_rcc_n_metrics.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        report_path = ROOT / "reports" / "rcc_nexus" / "latest_rcc_n_effectiveness_metrics.json"
        chart_path = ROOT / "visuals" / "rcc_nexus" / "rcc_n_effectiveness_v0_5.svg"
        self.assertTrue(report_path.exists())
        self.assertTrue(chart_path.exists())
        report = json.loads(report_path.read_text(encoding="utf-8"))
        self.assertGreater(report["rcc_n_effectiveness_score"], report["regular_readme_baseline_score"])
        self.assertIn("lift_over_regular_readme", report)


if __name__ == "__main__":
    unittest.main()