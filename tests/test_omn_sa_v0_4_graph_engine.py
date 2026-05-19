import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from omn.core.graph_engine import build_graph_engine_state
from omn.core.interactions import compute_interaction_matrix, matrix_edges, pearson
from omn.core.observables import build_observable_set, validate_observables
from omn.core.residuals import omega_from_delta_phi, residual_record


class TestOMNSAV04GraphEngine(unittest.TestCase):
    def test_observables_validate(self):
        obs = build_observable_set({"x": [1, 2, 3], "y": ["1", "2", "3"]})
        report = validate_observables(obs)
        self.assertTrue(report["passed"])
        self.assertEqual(report["count"], 2)

    def test_interaction_matrix_and_edges(self):
        obs = build_observable_set({"x": [1, 2, 3, 4], "y": [2, 4, 6, 8], "z": [4, 3, 2, 1]})
        matrix = compute_interaction_matrix(obs)
        self.assertEqual(len(matrix["names"]), 3)
        self.assertAlmostEqual(pearson([1, 2, 3], [2, 4, 6]), 1.0)
        edges = matrix_edges(matrix, threshold=0.20)
        self.assertGreaterEqual(len(edges), 2)
        for edge in edges:
            self.assertIn("claim_boundary", edge)
            self.assertIn("not causal certainty", edge["claim_boundary"])

    def test_graph_engine_state_valid(self):
        state = build_graph_engine_state({"x": [1, 2, 3], "y": [2, 4, 6]}, "test-run", threshold=0.20)
        self.assertEqual(state["schema"], "OMN-SA-v0.4-graph-engine-state")
        self.assertTrue(state["graph_contract"]["valid"])
        self.assertGreaterEqual(state["edge_count"], 1)

    def test_residual_record(self):
        rec = residual_record([1, 2, 3], [1, 2, 4])
        self.assertIn("delta_phi", rec)
        self.assertIn("omega", rec)
        self.assertAlmostEqual(omega_from_delta_phi(rec["delta_phi"]), rec["omega"])

    def test_graph_engine_validation_script_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/validation/validate_graph_engine.py"],
            cwd=ROOT,
            text=True,
            capture_output=True
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        report_path = ROOT / "reports" / "graph_engine" / "latest_graph_engine_validation.json"
        self.assertTrue(report_path.exists())
        report = json.loads(report_path.read_text(encoding="utf-8"))
        self.assertTrue(report["passed"])


if __name__ == "__main__":
    unittest.main()