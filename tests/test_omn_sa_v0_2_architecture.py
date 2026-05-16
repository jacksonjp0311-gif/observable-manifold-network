import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestOMNSAV02Architecture(unittest.TestCase):
    def test_v0_2_architecture_doc_exists_and_preserves_boundaries(self):
        path = ROOT / "docs" / "software_architecture" / "omn_sa_v0_2_software_architecture.md"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        self.assertIn("OMN-SA v0.2", text)
        self.assertIn("CI, Modular Runtime, Schema Validation, and RCC-N Drift Hardening", text)
        self.assertIn("CI is not correctness", text)
        self.assertIn("RCC-N is not AI understanding", text)
        self.assertIn("GMN authorship remains with Park et al.", text)

    def test_schema_contracts_exist(self):
        for rel in [
            "schemas/omn/evidence_package.schema.json",
            "schemas/omn/graph_contract.schema.json",
            "schemas/rcc_nexus/route_map.schema.json",
            "schemas/rcc_nexus/rcc_nexus_index.schema.json",
        ]:
            path = ROOT / rel
            self.assertTrue(path.exists(), rel)
            data = json.loads(path.read_text(encoding="utf-8"))
            self.assertIn("schema_id", data)
            self.assertIn("required_keys", data)
            self.assertIn("non_claim_lock", data)

    def test_architecture_contract_validator_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/validation/validate_architecture_contracts.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        report_path = ROOT / "reports" / "architecture" / "latest_omn_sa_v0_2_architecture_validation.json"
        self.assertTrue(report_path.exists())
        report = json.loads(report_path.read_text(encoding="utf-8"))
        self.assertTrue(report["passed"])


if __name__ == "__main__":
    unittest.main()