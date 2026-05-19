import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestOMNSAV071RCCNProfile(unittest.TestCase):
    def test_profile_config_exists_and_declares_full(self):
        path = ROOT / "docs" / "context" / "rcc_nexus_profile_v1_7.json"
        self.assertTrue(path.exists())
        data = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(data["schema"], "RCC-N-v1.7-profile-config")
        self.assertEqual(data["repository"]["adoption_profile"], "Full")
        self.assertTrue(data["profile_selection"]["lightest_sufficient_profile"])
        self.assertTrue(data["gen_boundary"]["rccn_v1_7_is_not_gen_v1_0"])

    def test_rcc_nexus_v1_7_profile_checker_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/rcc/check_rcc_nexus_v1_7_profile.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

        report_path = ROOT / "reports" / "rcc_nexus" / "latest_rcc_nexus_v1_7_profile_check.json"
        self.assertTrue(report_path.exists())

        report = json.loads(report_path.read_text(encoding="utf-8"))
        self.assertTrue(report["passed"], report)
        self.assertEqual(report["declared_profile"], "Full")
        self.assertEqual(report["recommended_profile"], "Full")

    def test_injected_theory_and_architecture_exist(self):
        required = [
            "docs/injected_theory/rcc_n_v1_7_adoption_profiles.md",
            "docs/injections/rcc_n_v1_7_injection_record.md",
            "docs/software_architecture/omn_sa_v0_7_1_rcc_n_v1_7_profile_injection.md",
            "docs/benchmarks/omn_sa_v0_7_1_rcc_n_v1_7_profile_metrics.md",
            "visuals/omn_sa/omn_sa_v0_7_1_rcc_n_v1_7_profile.svg",
        ]
        for rel in required:
            self.assertTrue((ROOT / rel).exists(), rel)


if __name__ == "__main__":
    unittest.main()