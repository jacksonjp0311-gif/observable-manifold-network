import json
import shutil
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestOMNSAV090DeterministicModes(unittest.TestCase):
    def test_ci_mode_fixed_run_id_and_output_dir(self):
        out = ROOT / "outputs_ci_test"
        if out.exists():
            shutil.rmtree(out)

        cmd = [
            "python", "-m", "omn", "run",
            "--seed", "synthetic-toy",
            "--ci-mode",
            "--run-id", "omn_ci_mode_test",
            "--output-dir", "outputs_ci_test",
            "--no-write-report",
        ]
        result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

        data = json.loads(result.stdout)
        self.assertEqual(data["run_id"], "omn_ci_mode_test")
        self.assertEqual(data["execution_mode"]["mode"], "ci")
        self.assertTrue(data["execution_mode"]["deterministic_run_id"])

        evidence_path = ROOT / "outputs_ci_test" / "evidence" / "omn_ci_mode_test_evidence_package.json"
        self.assertTrue(evidence_path.exists())

        evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
        self.assertEqual(evidence["schema"], "OMN-SA-v0.9-evidence-package")
        self.assertEqual(evidence["execution_mode"]["mode"], "ci")
        self.assertEqual(evidence["execution_mode"]["output_dir"], "outputs_ci_test")

        shutil.rmtree(out)

    def test_help_exposes_execution_modes(self):
        result = subprocess.run(["python", "-m", "omn", "run", "--help"], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn("--run-id", result.stdout)
        self.assertIn("--ci-mode", result.stdout)
        self.assertIn("--release-mode", result.stdout)
        self.assertIn("--no-write-report", result.stdout)
        self.assertIn("--output-dir", result.stdout)


if __name__ == "__main__":
    unittest.main()
