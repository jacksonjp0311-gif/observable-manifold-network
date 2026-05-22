import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestOMNSAV093ReadmeRegistryAutopatcher(unittest.TestCase):
    def test_autopatcher_script_exposes_required_surfaces(self):
        script = ROOT / "scripts" / "release" / "update_version_surfaces.py"
        self.assertTrue(script.exists())
        text = script.read_text(encoding="utf-8")
        required = [
            "README current health snapshot",
            "README current versioned documentation stack",
            "README architecture chain",
            "AI version tracking contract",
            "bottom lineage section",
            "CI required markers",
            "DOCS_REGISTRY.md",
            "public metrics references",
            "No version bump without automated registry-surface verification",
        ]
        for item in required:
            self.assertIn(item, text)

    def test_current_version_surfaces_pass_check(self):
        result = subprocess.run(
            [
                "python",
                "scripts/release/update_version_surfaces.py",
                "--check",
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
        self.assertIn("Version surface check passed.", result.stdout)


if __name__ == "__main__":
    unittest.main()
