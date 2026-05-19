import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"


class TestOMNSAV072ReadmeSelfOrganization(unittest.TestCase):
    def test_readme_current_state_is_v072(self):
        text = README.read_text(encoding="utf-8", errors="ignore")
        self.assertIn("Current software layer | OMN-SA v0.7.2", text)
        self.assertIn("Current software architecture layer: OMN-SA v0.7.2", text)
        self.assertNotIn("expected after v0.7.1", text)

    def test_readme_profile_and_next_weakness_visible(self):
        text = README.read_text(encoding="utf-8", errors="ignore")
        self.assertIn("RCC-N v1.7", text)
        self.assertIn("Full profile", text)
        self.assertTrue("v0.8 residual" in text or "v0.8 residual metrics" in text)

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