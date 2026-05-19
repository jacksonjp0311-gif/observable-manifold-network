import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"


class TestOMNSAV082ReadmeLineagePolicy(unittest.TestCase):
    def test_ai_update_policy_present(self):
        text = README.read_text(encoding="utf-8", errors="ignore")
        self.assertIn("## AI README Update Policy", text)
        self.assertIn("Required root README update zones", text)
        self.assertIn("Top dashboard without bottom lineage is incomplete.", text)

    def test_bottom_v08_and_v081_sections_present(self):
        text = README.read_text(encoding="utf-8", errors="ignore")
        self.assertIn("## OMN-SA v0.8 Metric Availability and Residual Field Hardening", text)
        self.assertIn("## OMN-SA v0.8.1 Validation Compatibility Repair", text)
        self.assertIn("## OMN-SA v0.8.2 README Lineage and AI Update Policy", text)
        self.assertNotIn("Current architecture chain extension:", text)

    def test_lineage_policy_audit_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/release/audit_readme_lineage_policy.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

        report = json.loads((ROOT / "reports" / "readme_policy" / "latest_readme_lineage_policy_audit.json").read_text(encoding="utf-8"))
        self.assertTrue(report["passed"], report)


if __name__ == "__main__":
    unittest.main()