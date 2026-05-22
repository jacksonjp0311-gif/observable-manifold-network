import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestOMNSAV095V10ReadinessGate(unittest.TestCase):
    def test_readiness_gate_script_and_report_exist(self):
        script = ROOT / "scripts" / "release" / "check_v1_0_readiness.py"
        report_json = ROOT / "reports" / "readiness" / "latest_v1_0_readiness_report.json"
        report_md = ROOT / "reports" / "readiness" / "latest_v1_0_readiness_report.md"

        self.assertTrue(script.exists())
        self.assertTrue(report_json.exists())
        self.assertTrue(report_md.exists())

        report = json.loads(report_json.read_text(encoding="utf-8"))
        self.assertEqual(report["schema"], "OMN-SA-v0.9.5-v1.0-readiness-report")
        self.assertEqual(report["version"], "OMN-SA v0.9.5")
        self.assertEqual(report["target"], "OMN-SA v1.0.0")
        self.assertEqual(report["readiness_classification"], "v1.0-ready-candidate")
        self.assertIn("non_claim_boundary", report)
        self.assertIn("does not prove code correctness", report["non_claim_boundary"])

        text = report_md.read_text(encoding="utf-8")
        self.assertIn("No v1.0 without a readiness classifier", text)

    def test_readiness_gate_passes_without_clean_requirement(self):
        result = subprocess.run(
            [
                "python",
                "scripts/release/check_v1_0_readiness.py",
                "--version",
                "OMN-SA v1.0.0",
                "--tests",
                "73",
                "--patch-name",
                "OMN-SA v1.0.0 stable public runtime checkpoint",
            ],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        data = json.loads(result.stdout)
        self.assertTrue(data["passed"])
        self.assertEqual(data["readiness_classification"], "v1.0-ready-candidate")

    def test_readme_references_readiness_gate(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Current software layer | OMN-SA v1.0.0", readme)
        self.assertIn("v1.0 readiness gate", readme)
        self.assertIn("reports/readiness/latest_v1_0_readiness_report.json", readme)


if __name__ == "__main__":
    unittest.main()
