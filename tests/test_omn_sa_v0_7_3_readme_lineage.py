import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"


class TestOMNSAV073ReadmeLineage(unittest.TestCase):
    def test_archived_v07_section_present(self):
        text = README.read_text(encoding="utf-8", errors="ignore")
        self.assertIn("## OMN-SA v0.7 Evidence Drift Comparison and Multi-Run Stability Dashboard", text)
        self.assertIn("No evidence package is mature until it can be compared across runs.", text)
        self.assertIn("delta_phi_residual", text)
        self.assertIn("omega_residual_weight", text)

    def test_ai_tracking_typo_removed(self):
        text = README.read_text(encoding="utf-8", errors="ignore")
        self.assertNotIn("OMN-SA v0.7.2.2", text)

    def test_v07_lineage_audit_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/release/audit_readme_v0_7_lineage.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

        report = json.loads((ROOT / "reports" / "self_organization" / "latest_readme_v0_7_lineage_audit.json").read_text(encoding="utf-8"))
        self.assertTrue(report["passed"], report)


if __name__ == "__main__":
    unittest.main()