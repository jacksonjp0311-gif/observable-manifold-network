import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"


class TestOMNSAV072ReadmeSelfOrganization(unittest.TestCase):
    def test_readme_current_state_is_versioned_and_self_org_section_remains(self):
        text = README.read_text(encoding="utf-8", errors="ignore")
        self.assertIn("Current software layer | OMN-SA v", text)
        self.assertIn("Current v0.7.2 README Self-Organization Audit", text)
        self.assertNotIn("expected after v0.7.1", text)

    def test_readme_profile_and_v08_visible(self):
        text = README.read_text(encoding="utf-8", errors="ignore")
        self.assertIn("RCC-N v1.7", text)
        self.assertIn("Full profile", text)
        self.assertIn("Current v0.8 Metric Availability and Residual Field Hardening", text)

    def test_self_organization_audit_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/release/audit_readme_self_organization.py"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

        report_path = ROOT / "reports" / "self_organization" / "latest_readme_self_organization_audit.json"
        report = json.loads(report_path.read_text(encoding="utf-8"))
        self.assertTrue(report["passed"], report)


if __name__ == "__main__":
    unittest.main()