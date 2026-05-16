import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from omn.core.runtime import run


class TestGraphContracts(unittest.TestCase):
    def test_graph_contract_edges_are_typed_and_bounded(self):
        evidence = run("synthetic-toy", str(ROOT))
        graph_path = Path(evidence["artifacts"]["graph_contract"])
        self.assertTrue(graph_path.exists())

        graph = json.loads(graph_path.read_text(encoding="utf-8"))
        self.assertTrue(graph["valid"])
        self.assertGreaterEqual(len(graph["nodes"]), 1)

        for edge in graph["edges"]:
            self.assertIn("edge_type", edge)
            self.assertTrue(edge["edge_type"])
            self.assertIn("claim_boundary", edge)
            self.assertIn("not causal certainty", edge["claim_boundary"])

    def test_evidence_contains_baseline_and_topology_sensitivity(self):
        evidence = run("artifact-graph", str(ROOT))
        self.assertIn("baselines", evidence)
        self.assertIn("topology_sensitivity", evidence)
        self.assertIn("baseline_equivalent", evidence["baselines"])
        self.assertTrue(evidence["topology_sensitivity"]["tested"])

    def test_claim_gate_blocks_overpromotion(self):
        evidence = run("lorenz", str(ROOT))
        claim_status = evidence["claim_status"]
        self.assertTrue(claim_status["overpromotion_blocked"])
        self.assertIn("does not prove causality", claim_status["prohibited_claim"])
        self.assertIn(claim_status["computed_status"], ["blocked", "demo-only", "runtime-validated"])


if __name__ == "__main__":
    unittest.main()