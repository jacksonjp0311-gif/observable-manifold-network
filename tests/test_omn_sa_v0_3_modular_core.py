import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from omn.core.artifact_audit import minimal_evidence_keys
from omn.core.claim_gate import compute_claim_status
from omn.core.contracts import minimal_graph_contract, non_claim_locks
from omn.core.modular_runtime import run_modular, validate_modular_runtime


class TestOMNSAV03ModularCore(unittest.TestCase):
    def test_non_claim_locks_include_v0_3_boundaries(self):
        locks = non_claim_locks()
        self.assertTrue(locks["simulation_is_not_proof"])
        self.assertTrue(locks["schema_validation_is_not_truth"])
        self.assertTrue(locks["rcc_nexus_is_not_ai_understanding"])
        self.assertTrue(locks["gmn_authorship_preserved"])

    def test_minimal_graph_contract_validates_boundaries(self):
        contract = minimal_graph_contract(
            run_id="test",
            nodes=[{"node_id": "x", "observable_name": "x", "claim_boundary": "Observable node does not prove mechanism."}],
            edges=[{"source": "x", "target": "y", "edge_type": "correlation", "claim_boundary": "Edge confidence is not causal certainty."}],
        )
        self.assertTrue(contract["valid"])
        self.assertEqual(contract["failure_flags"], [])

    def test_claim_gate_blocks_empty_evidence(self):
        claim = compute_claim_status({})
        self.assertEqual(claim["computed_status"], "blocked")
        self.assertTrue(claim["overpromotion_blocked"])
        self.assertIn("does not prove causality", claim["prohibited_claim"])

    def test_minimal_evidence_key_audit(self):
        audit = minimal_evidence_keys({"run_id": "x"})
        self.assertFalse(audit["passed"])
        self.assertIn("claim_status", audit["missing"])

    def test_modular_runtime_validation_and_run(self):
        module_report = validate_modular_runtime(str(ROOT))
        self.assertTrue(module_report["passed"], module_report)

        run_report = run_modular("synthetic-toy", str(ROOT))
        self.assertEqual(run_report["schema"], "OMN-SA-v0.3-modular-runtime-envelope")
        self.assertTrue(run_report["legacy_runtime_used"])
        self.assertTrue(run_report["claim_gate"]["overpromotion_blocked"])

        report_path = ROOT / "reports" / "modular_runtime" / "latest_modular_runtime_report.json"
        self.assertTrue(report_path.exists())
        parsed = json.loads(report_path.read_text(encoding="utf-8"))
        self.assertEqual(parsed["schema"], "OMN-SA-v0.3-modular-runtime-envelope")


if __name__ == "__main__":
    unittest.main()