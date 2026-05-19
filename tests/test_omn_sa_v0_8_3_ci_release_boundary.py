import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CI = ROOT / ".github" / "workflows" / "ci.yml"
RELEASE = ROOT / "scripts" / "release" / "run_release_validation.ps1"
README = ROOT / "README.md"


class TestOMNSAV083CIReleaseBoundary(unittest.TestCase):
    def test_ci_is_smoke_gate(self):
        text = CI.read_text(encoding="utf-8", errors="ignore")
        self.assertIn("Run unit tests", text)
        self.assertIn("Run CLI smoke check", text)
        self.assertIn("CI is a non-release smoke gate", text)

    def test_ci_does_not_run_artifact_refresh_validators(self):
        text = CI.read_text(encoding="utf-8", errors="ignore")
        forbidden = [
            "validate_evidence_drift.py",
            "validate_metric_availability.py",
            "validate_evidence_replay.py",
            "generate_rcc_n_metrics.py",
            "audit_mini_readmes.py",
            "python -m omn run",
        ]
        for item in forbidden:
            self.assertNotIn(item, text)

    def test_release_script_contains_artifact_validators(self):
        text = RELEASE.read_text(encoding="utf-8", errors="ignore")
        self.assertIn("artifact-emitting release validation", text)
        self.assertIn("validate_evidence_drift.py", text)
        self.assertIn("validate_metric_availability.py", text)
        self.assertIn("validate_evidence_replay.py", text)

    def test_readme_mentions_v083_boundary(self):
        text = README.read_text(encoding="utf-8", errors="ignore")
        self.assertIn("OMN-SA v0.8.3 CI / Release Boundary Separation", text)
        self.assertIn("CI verifies committed state.", text)
        self.assertIn("Release validation refreshes evidence state.", text)


if __name__ == "__main__":
    unittest.main()