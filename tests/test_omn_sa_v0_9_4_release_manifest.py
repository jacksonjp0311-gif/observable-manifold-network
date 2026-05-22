import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestOMNSAV094ReleaseManifest(unittest.TestCase):
    def test_release_manifest_exists_and_is_bounded(self):
        manifest_json = ROOT / "releases" / "omn_sa_v0_9_4_release_manifest.json"
        manifest_md = ROOT / "releases" / "omn_sa_v0_9_4_release_manifest.md"

        self.assertTrue(manifest_json.exists())
        self.assertTrue(manifest_md.exists())

        manifest = json.loads(manifest_json.read_text(encoding="utf-8"))
        self.assertEqual(manifest["schema"], "OMN-SA-v0.9.4-release-manifest")
        self.assertEqual(manifest["version"], "OMN-SA v0.9.4")
        self.assertEqual(manifest["test_count_expected"], 67)
        self.assertIn("validation_commands", manifest)
        self.assertIn("non_claim_boundary", manifest)
        self.assertIn("does not prove code correctness", manifest["non_claim_boundary"])
        self.assertEqual(manifest["required_surfaces"]["release_manifest_json"], "releases/omn_sa_v0_9_4_release_manifest.json")

        text = manifest_md.read_text(encoding="utf-8")
        self.assertIn("No release without a machine-readable version seal", text)
        self.assertIn("Boundary", text)

    def test_readme_registry_and_checker_reference_v094(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Current software layer | OMN-SA v0.9.4", readme)
        self.assertIn("releases/omn_sa_v0_9_4_release_manifest.json", readme)
        self.assertIn("OMN-SA v0.9.4 release manifest / version seal", readme)

        result = subprocess.run(
            [
                "python",
                "scripts/release/update_version_surfaces.py",
                "--check",
                "--version",
                "OMN-SA v0.9.4",
                "--tests",
                "67",
                "--patch-name",
                "OMN-SA v0.9.4 release manifest / version seal",
            ],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Version surface check passed.", result.stdout)


if __name__ == "__main__":
    unittest.main()
