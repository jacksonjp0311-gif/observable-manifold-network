import json
import shutil
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestOMNSAV091StableEvidenceIndex(unittest.TestCase):
    def test_ci_pointer_and_index_are_written(self):
        out = ROOT / "outputs_index_test"
        if out.exists():
            shutil.rmtree(out)

        run_cmd = [
            "python", "-m", "omn", "run",
            "--seed", "synthetic-toy",
            "--ci-mode",
            "--run-id", "omn_index_ci_fixture",
            "--output-dir", "outputs_index_test",
            "--no-write-report",
        ]
        result = subprocess.run(run_cmd, cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

        index_path = out / "evidence" / "evidence_index.json"
        latest_ci = out / "evidence" / "latest_ci_fixture.json"
        latest_any = out / "evidence" / "latest_evidence.json"
        self.assertTrue(index_path.exists())
        self.assertTrue(latest_ci.exists())
        self.assertTrue(latest_any.exists())

        index = json.loads(index_path.read_text(encoding="utf-8"))
        self.assertEqual(index["schema"], "OMN-SA-v0.9.1-evidence-index")
        self.assertEqual(index["record_count"], 1)
        self.assertIn("ci", index["modes_seen"])

        pointer = json.loads(latest_ci.read_text(encoding="utf-8"))
        self.assertEqual(pointer["schema"], "OMN-SA-v0.9.1-evidence-pointer")
        self.assertEqual(pointer["mode"], "ci")
        self.assertEqual(pointer["run_id"], "omn_index_ci_fixture")
        self.assertTrue(pointer["evidence_path"].endswith("omn_index_ci_fixture_evidence_package.json"))

        latest = subprocess.run(
            ["python", "-m", "omn", "report-latest", "--output-dir", "outputs_index_test", "--mode", "ci"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(latest.returncode, 0)
        self.assertIn("omn_index_ci_fixture_evidence_package.json", latest.stdout)

        validate = subprocess.run(
            ["python", "-m", "omn", "validate", "--output-dir", "outputs_index_test", "--mode", "ci"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(validate.returncode, 0, validate.stdout + validate.stderr)
        validation = json.loads(validate.stdout)
        self.assertTrue(validation["valid"])

        shutil.rmtree(out)

    def test_index_evidence_command_is_exposed(self):
        result = subprocess.run(["python", "-m", "omn", "--help"], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn("index-evidence", result.stdout)


if __name__ == "__main__":
    unittest.main()
