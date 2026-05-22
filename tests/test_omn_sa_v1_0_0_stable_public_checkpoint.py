import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestOMNSAV100StablePublicCheckpoint(unittest.TestCase):
    def test_v100_release_manifest_exists_and_is_bounded(self):
        manifest_path = ROOT / "releases" / "omn_sa_v1_0_0_stable_public_runtime_checkpoint.json"
        summary_path = ROOT / "releases" / "omn_sa_v1_0_0_stable_public_runtime_checkpoint.md"

        self.assertTrue(manifest_path.exists())
        self.assertTrue(summary_path.exists())

        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        self.assertEqual(manifest["schema"], "OMN-SA-v1.0.0-stable-public-runtime-checkpoint")
        self.assertEqual(manifest["version"], "OMN-SA v1.0.0")
        self.assertEqual(manifest["expected_tests"], 73)
        self.assertEqual(manifest["classification"], "stable-public-runtime-checkpoint")
        self.assertIn("non_claim_boundary", manifest)
        self.assertIn("does not prove code correctness", manifest["non_claim_boundary"])

    def test_v100_readme_and_version_surfaces_are_aligned(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Current software layer | OMN-SA v1.0.0", readme)
        self.assertIn("Current tests | 73 OK", readme)
        self.assertIn("stable public runtime checkpoint", readme)
        self.assertIn("releases/omn_sa_v1_0_0_stable_public_runtime_checkpoint.json", readme)

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

    def test_v100_readiness_gate_still_passes(self):
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


if __name__ == "__main__":
    unittest.main()
