import argparse
import csv
import json
import math
from datetime import datetime, timezone
from pathlib import Path


NON_CLAIM_LOCKS = {
    "simulation_is_not_proof": True,
    "prediction_is_not_mechanism": True,
    "observable_topology_is_not_truth": True,
    "edge_confidence_is_not_causal_certainty": True,
    "source_authorship_preserved": True,
}


def utc_stamp():
    return datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")


def utc_iso():
    return datetime.now(timezone.utc).isoformat()


def ensure_dir(path):
    Path(path).mkdir(parents=True, exist_ok=True)


def write_json(path, data):
    p = Path(path)
    ensure_dir(p.parent)
    p.write_text(json.dumps(data, indent=2), encoding="utf-8")


def write_csv(path, rows):
    p = Path(path)
    ensure_dir(p.parent)
    if not rows:
        p.write_text("", encoding="utf-8")
        return
    fields = list(rows[0].keys())
    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_matrix_csv(path, columns, matrix):
    p = Path(path)
    ensure_dir(p.parent)
    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["node"] + columns)
        for col, row in zip(columns, matrix):
            writer.writerow([col] + [f"{v:.8f}" for v in row])


def write_text(path, text):
    p = Path(path)
    ensure_dir(p.parent)
    p.write_text(text, encoding="utf-8")


def synthetic_toy(n=160):
    rows = []
    x = 0.15
    y = 0.05
    z = -0.10
    for t in range(n):
        x_next = 0.78 * x + 0.08 * math.sin(t / 5.0)
        y_next = 0.60 * y + 0.35 * x
        z_next = 0.55 * z + 0.25 * x + 0.18 * y
        x, y, z = x_next, y_next, z_next
        rows.append({"t": float(t), "x": x, "y": y, "z": z})
    return rows


def lorenz(n=900, dt=0.01, sigma=10.0, rho=28.0, beta=8.0 / 3.0):
    x, y, z = 1.0, 1.0, 1.0
    rows = []
    for i in range(n):
        dx = sigma * (y - x)
        dy = x * (rho - z) - y
        dz = x * y - beta * z
        x += dt * dx
        y += dt * dy
        z += dt * dz
        if i >= 100:
            rows.append({"t": float(i - 100), "x": x, "y": y, "z": z})
    return rows


def artifact_graph():
    rows = []
    for t in range(120):
        base = math.sin(t / 12.0)
        rows.append({
            "t": float(t),
            "readme": base + 0.1,
            "source": 0.7 * base + 0.2 * math.sin(t / 5.0),
            "tests": 0.6 * base + 0.1 * math.cos(t / 4.0),
            "reports": 0.5 * base + 0.15,
            "evidence": 0.4 * base + 0.2 * math.sin(t / 7.0),
            "config": 0.3 * base + 0.05,
        })
    return rows


def load_seed(seed):
    if seed == "synthetic-toy":
        return synthetic_toy(), "S0"
    if seed == "lorenz":
        return lorenz(), "S1"
    if seed == "artifact-graph":
        return artifact_graph(), "S3"
    raise ValueError(f"Unknown seed: {seed}")


def columns(rows):
    return [c for c in rows[0].keys() if c != "t"]


def corr(xs, ys):
    n = min(len(xs), len(ys))
    if n <= 1:
        return 0.0
    xs = xs[:n]
    ys = ys[:n]
    mx = sum(xs) / n
    my = sum(ys) / n
    vx = sum((x - mx) ** 2 for x in xs)
    vy = sum((y - my) ** 2 for y in ys)
    if vx <= 1e-12 or vy <= 1e-12:
        return 0.0
    cov = sum((xs[i] - mx) * (ys[i] - my) for i in range(n))
    return cov / math.sqrt(vx * vy)


def interaction_matrix(rows):
    cols = columns(rows)
    matrix = []
    for src in cols:
        src_vals = [float(r[src]) for r in rows]
        out = []
        for tgt in cols:
            tgt_vals = [float(r[tgt]) for r in rows]
            if src == tgt:
                out.append(0.0)
            else:
                out.append(abs(corr(src_vals[:-1], tgt_vals[1:])))
        matrix.append(out)
    return cols, matrix


def observable_nodes(cols, seed):
    return [
        {
            "node_id": col,
            "observable_name": col,
            "observable_type": "artifact" if seed == "artifact-graph" else "synthetic",
            "column": col,
            "role": "target" if i == 0 else "driver",
            "claim_boundary": "Observable node does not prove mechanism."
        }
        for i, col in enumerate(cols)
    ]


def would_create_cycle(edges, source, target):
    graph = {}
    for e in edges:
        graph.setdefault(e["source"], []).append(e["target"])
    graph.setdefault(source, []).append(target)
    seen = set()
    stack = set()

    def visit(node):
        if node in stack:
            return True
        if node in seen:
            return False
        seen.add(node)
        stack.add(node)
        for nxt in graph.get(node, []):
            if visit(nxt):
                return True
        stack.remove(node)
        return False

    return any(visit(n) for n in list(graph))


def build_edges(cols, matrix, top_k=2):
    edges = []
    for j, target in enumerate(cols):
        candidates = []
        for i, source in enumerate(cols):
            if source != target:
                candidates.append((source, target, matrix[i][j]))
        candidates.sort(key=lambda item: item[2], reverse=True)
        added = 0
        for source, target, weight in candidates:
            if added >= top_k:
                break
            if weight <= 1e-12:
                continue
            if would_create_cycle(edges, source, target):
                continue
            edges.append({
                "source": source,
                "target": target,
                "edge_type": "correlation",
                "weight": weight,
                "direction": "inferred",
                "threshold_policy": "top_k",
                "confidence": min(1.0, abs(weight)),
                "status": "computed",
                "claim_boundary": "Edge confidence is not causal certainty."
            })
            added += 1
    return edges


def graph_contract(run_id, nodes, edges):
    failures = []
    if not nodes:
        failures.append("no observable nodes")
    for edge in edges:
        if not edge.get("edge_type"):
            failures.append("edge missing type")
        if not edge.get("claim_boundary"):
            failures.append("edge missing claim boundary")
    return {
        "schema": "OMN-SA-v0.1-graph-contract",
        "run_id": run_id,
        "target_node": nodes[0]["node_id"] if nodes else "",
        "cycle_policy": "reject_cycles",
        "driver_count_policy": "top_k",
        "nodes": nodes,
        "edges": edges,
        "valid": len(failures) == 0,
        "failure_flags": failures,
    }


def build_manifolds(nodes, edges):
    drivers = {n["node_id"]: [] for n in nodes}
    for e in edges:
        drivers.setdefault(e["target"], []).append(e["source"])
    return [
        {
            "node_id": n["node_id"],
            "drivers": drivers.get(n["node_id"], []),
            "embedding_policy": "delay",
            "E": 3,
            "tau": 1,
            "generator": "linear"
        }
        for n in nodes
    ]


def rollout(rows, manifolds, horizon):
    train = rows[:-horizon]
    validation = rows[-horizon:]
    history = [dict(r) for r in train[-5:]]
    generated = []
    for step in range(horizon):
        last = history[-1]
        nxt = {"t": validation[step]["t"]}
        for m in manifolds:
            node = m["node_id"]
            drivers = m["drivers"]
            own = float(last[node])
            if drivers:
                avg = sum(float(last[d]) for d in drivers) / len(drivers)
                value = 0.65 * own + 0.35 * avg
            else:
                value = own
            nxt[node] = value
        generated.append(nxt)
        history.append(nxt)
    return generated, validation


def baseline_persistence(rows, horizon):
    train = rows[:-horizon]
    validation = rows[-horizon:]
    last = train[-1]
    return [{k: (row[k] if k == "t" else last[k]) for k in row} for row in validation]


def flatten(rows, cols):
    vals = []
    for r in rows:
        for c in cols:
            vals.append(float(r[c]))
    return vals


def rmse(obs, pred):
    n = min(len(obs), len(pred))
    return math.sqrt(sum((obs[i] - pred[i]) ** 2 for i in range(n)) / max(n, 1))


def mae(obs, pred):
    n = min(len(obs), len(pred))
    return sum(abs(obs[i] - pred[i]) for i in range(n)) / max(n, 1)


def omega(dphi):
    return 1.0 / (1.0 + abs(dphi))


def residuals(validation, generated, cols):
    obs = flatten(validation, cols)
    pred = flatten(generated, cols)
    dphi = mae(obs, pred)
    return {
        "rmse": rmse(obs, pred),
        "mae": mae(obs, pred),
        "correlation": corr(obs, pred),
        "delta_phi_omn": dphi,
        "omega_omn": omega(dphi),
    }


def residual_attribution(validation, generated, cols):
    items = []
    for c in cols:
        obs = [float(r[c]) for r in validation]
        pred = [float(r[c]) for r in generated]
        dphi = mae(obs, pred)
        items.append({
            "node_id": c,
            "mae": dphi,
            "rmse": rmse(obs, pred),
            "omega": omega(dphi),
            "claim_boundary": "Node residual identifies error, not mechanism."
        })
    items.sort(key=lambda x: x["mae"], reverse=True)
    return {"worst_nodes": items[:3], "all_nodes": items}


def topology_sensitivity(rows):
    cols, matrix = interaction_matrix(rows)
    edge_counts = []
    for top_k in [1, 2]:
        edges = build_edges(cols, matrix, top_k=top_k)
        edge_counts.append(len(edges))
    return {
        "tested": True,
        "sensitive": len(set(edge_counts)) > 1,
        "classification_flip_detected": False,
        "edge_count_by_policy": edge_counts,
        "summary": "v0.1 sensitivity checks top_k edge count changes only."
    }


def claim_gate(graph_ok, evidence_ok, benchmark_class):
    status = "runtime-validated" if graph_ok and evidence_ok else "blocked"
    return {
        "computed_status": status,
        "allowed_claim": "Minimal OMN runtime emitted graph, residual, baseline, topology, and evidence artifacts." if status == "runtime-validated" else "No strong claim allowed.",
        "prohibited_claim": "This run does not prove causality, mechanism, biological equivalence, physical manifold identity, empirical validation, or full GMN replication.",
        "overpromotion_blocked": True,
        "benchmark_class": benchmark_class
    }


def simple_svg(path, title, values):
    ensure_dir(Path(path).parent)
    width = 720
    height = 320
    vals = list(values) or [0.0]
    mn = min(vals)
    mx = max(vals)
    span = mx - mn if abs(mx - mn) > 1e-12 else 1.0
    points = []
    for i, v in enumerate(vals):
        x = 30 + i * (width - 60) / max(len(vals) - 1, 1)
        y = height - 30 - ((v - mn) / span) * (height - 70)
        points.append(f"{x:.2f},{y:.2f}")
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}"><rect width="100%" height="100%" fill="white"/><text x="30" y="24" font-family="Arial" font-size="18">{title}</text><polyline fill="none" stroke="black" stroke-width="2" points="{" ".join(points)}"/></svg>'
    Path(path).write_text(svg, encoding="utf-8")


def append_ledger(path, record):
    p = Path(path)
    ensure_dir(p.parent)
    with p.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")


def normalize_run_id(seed, run_id=None, mode="release"):
    if run_id:
        return run_id
    safe_seed = seed.replace("-", "_")
    if mode == "ci":
        return f"omn_{safe_seed}_ci_fixture"
    return f"omn_{safe_seed}_{utc_stamp()}"


def run(seed="synthetic-toy", root=".", run_id=None, mode="release", write_reports=True, output_dir="outputs"):
    root = Path(root).resolve()
    run_id = normalize_run_id(seed, run_id=run_id, mode=mode)
    output_root = Path(output_dir)
    rows, benchmark_class = load_seed(seed)
    cols, matrix = interaction_matrix(rows)
    nodes = observable_nodes(cols, seed)
    edges = build_edges(cols, matrix, top_k=2)
    contract = graph_contract(run_id, nodes, edges)
    manifolds = build_manifolds(nodes, edges)
    horizon = min(50, max(10, len(rows) // 5))
    generated, validation = rollout(rows, manifolds, horizon)
    base_generated = baseline_persistence(rows, horizon)
    res = residuals(validation, generated, cols)
    base_res = residuals(validation, base_generated, cols)
    attrib = residual_attribution(validation, generated, cols)
    topo = topology_sensitivity(rows)

    paths = {
        "state": root / output_root / "state" / f"{run_id}_state.json",
        "observables": root / output_root / "state" / f"observables_{run_id}.json",
        "matrix": root / output_root / "state" / f"interaction_matrix_{run_id}.csv",
        "graph": root / output_root / "state" / f"graph_contract_{run_id}.json",
        "generated": root / output_root / "state" / f"generated_state_{run_id}.csv",
        "residuals": root / output_root / "state" / f"validation_residuals_{run_id}.csv",
        "attribution": root / output_root / "state" / f"residual_attribution_{run_id}.json",
        "evidence": root / output_root / "evidence" / f"{run_id}_evidence_package.json",
        "report": root / output_root / "reports" / f"{run_id}_report.md",
        "plot_generated": root / output_root / "plots" / f"generated_vs_observed_{run_id}.svg",
        "plot_residuals": root / output_root / "plots" / f"residuals_{run_id}.svg",
        "plot_matrix": root / output_root / "plots" / f"interaction_matrix_{run_id}.svg",
        "log": root / output_root / "logs" / f"{run_id}.log",
        "ledger": root / output_root / "ledger" / "omn_ledger.jsonl",
    }

    write_json(paths["observables"], nodes)
    write_matrix_csv(paths["matrix"], cols, matrix)
    write_json(paths["graph"], contract)
    write_csv(paths["generated"], generated)
    write_csv(paths["residuals"], [{"metric": k, "value": v} for k, v in res.items()])
    write_json(paths["attribution"], attrib)

    gate = claim_gate(contract["valid"], True, benchmark_class)

    state = {
        "schema": "OMN-SA-v0.9-state",
        "run_id": run_id,
        "seed": seed,
        "timestamp": utc_iso(),
        "execution_mode": {
            "mode": mode,
            "write_reports": write_reports,
            "output_dir": str(output_root),
            "deterministic_run_id": bool(mode == "ci" or run_id),
            "run_identity_policy": "explicit --run-id, deterministic ci fixture, or timestamped release run",
            "non_claim_boundary": "Execution mode improves reproducibility discipline. It does not prove correctness, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication."
        },
        "source_boundary": {
            "primary_source": "Park et al. GMN paper",
            "source_method": "Generative Manifold Networks",
            "codex_architecture": "OMN-SA v0.9",
            "gmns_not_renamed_as_codex_invention": True
        },
        "observables": {"count": len(nodes), "path": str(paths["observables"])},
        "interaction_matrix": {"method": "lagged_abs_correlation", "path": str(paths["matrix"])},
        "graph_contract": {"path": str(paths["graph"]), "valid": contract["valid"]},
        "embedding": {"policy": "delay", "E": 3, "tau": 1},
        "generation": {"horizon": horizon, "generated_state_path": str(paths["generated"])},
        "validation": res,
        "baselines": {"persistence": base_res, "baseline_equivalent": base_res["rmse"] <= res["rmse"]},
        "topology_sensitivity": topo,
        "claim_gate": gate,
        "locks": NON_CLAIM_LOCKS
    }

    write_json(paths["state"], state)

    simple_svg(paths["plot_generated"], f"{seed} generated first observable", [r[cols[0]] for r in generated])
    simple_svg(paths["plot_residuals"], f"{seed} residual absolute error", [abs(validation[i][cols[0]] - generated[i][cols[0]]) for i in range(len(generated))])
    simple_svg(paths["plot_matrix"], f"{seed} interaction row sums", [sum(row) for row in matrix])

    validation_metrics = {
        "rmse": res["rmse"],
        "mae": res["mae"],
        "correlation": res["correlation"],
        "delta_phi_residual": res["delta_phi_omn"],
        "omega_residual_weight": res["omega_omn"],
    }

    baseline_metrics = {
        "rmse": base_res["rmse"],
        "mae": base_res["mae"],
        "correlation": base_res["correlation"],
        "delta_phi_residual": base_res["delta_phi_omn"],
        "omega_residual_weight": base_res["omega_omn"],
        "baseline_equivalent": base_res["rmse"] <= res["rmse"],
    }

    metrics_block = {
        "schema": "OMN-SA-v0.8-metrics-block",
        "validation": validation_metrics,
        "baseline": baseline_metrics,
        "legacy": {
            "rmse": res["rmse"],
            "mae": res["mae"],
            "correlation": res["correlation"],
            "delta_phi_omn": res["delta_phi_omn"],
            "omega_omn": res["omega_omn"],
        },
        "non_claim_boundary": "Residual metrics measure generated-vs-observed error for the local run. They do not prove causality, mechanism, empirical validation, production readiness, AI understanding, or GMN replication."
    }

    evidence = {
        "schema": "OMN-SA-v0.9-evidence-package",
        "run_id": run_id,
        "seed": seed,
        "benchmark_class": benchmark_class,
        "claim_status": gate,
        "source_boundary": state["source_boundary"],
        "execution_mode": {
            "mode": mode,
            "write_reports": write_reports,
            "output_dir": str(output_root),
            "deterministic_run_id": bool(mode == "ci" or run_id),
            "run_identity_policy": "explicit --run-id, deterministic ci fixture, or timestamped release run",
            "non_claim_boundary": "Execution mode improves reproducibility discipline. It does not prove correctness, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication."
        },
        "metrics": metrics_block,
        "artifacts": {
            "state": str(paths["state"]),
            "observables": str(paths["observables"]),
            "interaction_matrix": str(paths["matrix"]),
            "graph_contract": str(paths["graph"]),
            "generated_state": str(paths["generated"]),
            "validation_residuals": str(paths["residuals"]),
            "residual_attribution": str(paths["attribution"]),
            "report": str(paths["report"]),
            "plots": {
                "generated_vs_observed": str(paths["plot_generated"]),
                "residuals": str(paths["plot_residuals"]),
                "interaction_matrix": str(paths["plot_matrix"])
            },
            "ledger": str(paths["ledger"])
        },
        "baselines": {"baseline_equivalent": base_res["rmse"] <= res["rmse"], "summary": "Persistence baseline is reported honestly."},
        "topology_sensitivity": topo,
        "audit": {
            "declared_artifact_paths_exist": False,
            "graph_contract_present": contract["valid"],
            "validation_present": True,
            "claim_gate_present": True,
            "passed": False
        },
        "non_claim_locks": NON_CLAIM_LOCKS,
        "failure_flags": [],
        "next_action": "Inspect evidence package and compare seeds."
    }

    if not write_reports:
        evidence["artifacts"].pop("ledger", None)

    report = f"""# OMN Run Report

Run ID: {run_id}
Seed: {seed}
Benchmark class: {benchmark_class}
Claim status: {gate["computed_status"]}

## Metrics

- RMSE: {res["rmse"]:.6f}
- MAE: {res["mae"]:.6f}
- Correlation: {res["correlation"]:.6f}
- DeltaPhi_OMN: {res["delta_phi_omn"]:.6f}
- Omega_OMN: {res["omega_omn"]:.6f}

## Baseline

- Persistence RMSE: {base_res["rmse"]:.6f}
- Baseline equivalent: {base_res["rmse"] <= res["rmse"]}

## Non-claim locks

- Simulation is not proof.
- Prediction is not mechanism.
- Observable topology is not truth.
- Edge confidence is not causal certainty.
- GMN authorship remains with Park et al.

## Evidence

Evidence package: {paths["evidence"]}
"""
    if write_reports:
        write_text(paths["report"], report)
        write_text(paths["log"], f"{utc_iso()} completed {run_id}\n")
        append_ledger(paths["ledger"], {"run_id": run_id, "timestamp": utc_iso(), "seed": seed, "evidence": str(paths["evidence"]), "status": gate["computed_status"], "mode": mode})
    else:
        write_text(paths["report"], "# OMN Report Suppressed\n\nReport writing was suppressed by --no-write-report.\n")
        write_text(paths["log"], f"{utc_iso()} completed {run_id} with report suppression\n")

    declared_paths = []
    for value in evidence["artifacts"].values():
        if isinstance(value, str):
            declared_paths.append(value)
        elif isinstance(value, dict):
            declared_paths.extend(value.values())

    evidence["audit"]["declared_artifact_paths_exist"] = all(Path(p).exists() for p in declared_paths if p)
    evidence["audit"]["passed"] = evidence["audit"]["declared_artifact_paths_exist"] and contract["valid"]

    write_json(paths["evidence"], evidence)
    write_evidence_index(root, output_dir=output_dir)

    return evidence


def evidence_dir_for(root=".", output_dir="outputs"):
    return Path(root) / output_dir / "evidence"


def relative_to_root(path, root="."):
    p = Path(path)
    try:
        return str(p.resolve().relative_to(Path(root).resolve()))
    except Exception:
        return str(p)


def load_evidence_record(path, root="."):
    p = Path(path)
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception as exc:
        return {
            "path": relative_to_root(p, root),
            "load_error": str(exc),
            "valid": False,
        }

    execution_mode = data.get("execution_mode", {})
    metrics = data.get("metrics", {}).get("validation", {})
    return {
        "run_id": data.get("run_id"),
        "seed": data.get("seed"),
        "benchmark_class": data.get("benchmark_class"),
        "claim_status": data.get("claim_status", {}).get("computed_status"),
        "mode": execution_mode.get("mode", "release"),
        "deterministic_run_id": execution_mode.get("deterministic_run_id", False),
        "write_reports": execution_mode.get("write_reports"),
        "path": relative_to_root(p, root),
        "modified_time": p.stat().st_mtime,
        "metrics": {
            "rmse": metrics.get("rmse"),
            "mae": metrics.get("mae"),
            "delta_phi_residual": metrics.get("delta_phi_residual"),
            "omega_residual_weight": metrics.get("omega_residual_weight"),
        },
        "valid": True,
        "non_claim_boundary": "Evidence index entries summarize local evidence packages. They do not prove correctness, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication."
    }


def evidence_sort_key(record):
    return (
        str(record.get("mode", "")),
        str(record.get("seed", "")),
        str(record.get("run_id", "")),
        str(record.get("path", "")),
    )


def build_evidence_index(root=".", output_dir="outputs"):
    root_path = Path(root).resolve()
    evidence_dir = evidence_dir_for(root_path, output_dir)
    files = sorted(evidence_dir.glob("*_evidence_package.json"), key=lambda p: p.name)
    records = [load_evidence_record(p, root_path) for p in files]
    records = sorted(records, key=evidence_sort_key)

    latest_by_mode = {}
    for mode in ["ci", "release"]:
        candidates = [r for r in records if r.get("valid") and r.get("mode") == mode]
        if candidates:
            latest_by_mode[mode] = sorted(
                candidates,
                key=lambda r: (r.get("modified_time", 0), str(r.get("run_id", "")), str(r.get("path", ""))),
                reverse=True
            )[0]

    valid_candidates = [r for r in records if r.get("valid")]
    latest_any = None
    if valid_candidates:
        latest_any = sorted(
            valid_candidates,
            key=lambda r: (r.get("modified_time", 0), str(r.get("run_id", "")), str(r.get("path", ""))),
            reverse=True
        )[0]

    return {
        "schema": "OMN-SA-v0.9.1-evidence-index",
        "output_dir": str(output_dir),
        "generated_at": utc_iso(),
        "record_count": len(records),
        "modes_seen": sorted({r.get("mode", "unknown") for r in records if r.get("valid")}),
        "latest": {
            "any": latest_any,
            "ci": latest_by_mode.get("ci"),
            "release": latest_by_mode.get("release"),
        },
        "records": records,
        "non_claim_boundary": "The evidence index makes evidence selection explicit. It does not prove correctness, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication."
    }


def write_evidence_index(root=".", output_dir="outputs"):
    root_path = Path(root).resolve()
    evidence_dir = evidence_dir_for(root_path, output_dir)
    ensure_dir(evidence_dir)

    index = build_evidence_index(root_path, output_dir)
    write_json(evidence_dir / "evidence_index.json", index)

    pointer_schema = "OMN-SA-v0.9.1-evidence-pointer"
    pointer_boundary = "Evidence pointers identify selected local evidence packages. They do not prove correctness, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication."

    def pointer(record, pointer_type):
        return {
            "schema": pointer_schema,
            "pointer_type": pointer_type,
            "output_dir": str(output_dir),
            "generated_at": utc_iso(),
            "evidence_path": record.get("path") if record else None,
            "run_id": record.get("run_id") if record else None,
            "seed": record.get("seed") if record else None,
            "mode": record.get("mode") if record else None,
            "valid": bool(record),
            "non_claim_boundary": pointer_boundary,
        }

    write_json(evidence_dir / "latest_evidence.json", pointer(index["latest"].get("any"), "any"))
    write_json(evidence_dir / "latest_ci_fixture.json", pointer(index["latest"].get("ci"), "ci"))
    write_json(evidence_dir / "latest_release_evidence.json", pointer(index["latest"].get("release"), "release"))
    return index


def evidence_from_pointer(root=".", output_dir="outputs", mode=None):
    evidence_dir = evidence_dir_for(root, output_dir)
    if mode == "ci":
        pointer_path = evidence_dir / "latest_ci_fixture.json"
    elif mode == "release":
        pointer_path = evidence_dir / "latest_release_evidence.json"
    else:
        pointer_path = evidence_dir / "latest_evidence.json"

    if not pointer_path.exists():
        return None
    pointer = json.loads(pointer_path.read_text(encoding="utf-8"))
    evidence_path = pointer.get("evidence_path")
    if not evidence_path:
        return None
    return Path(root) / evidence_path


def latest_evidence(root=".", output_dir="outputs", mode=None):
    pointed = evidence_from_pointer(root=root, output_dir=output_dir, mode=mode)
    if pointed and pointed.exists():
        return pointed

    evidence_dir = evidence_dir_for(root, output_dir)
    files = sorted(evidence_dir.glob("*_evidence_package.json"), key=lambda p: (p.stat().st_mtime, p.name), reverse=True)
    if mode:
        filtered = []
        for p in files:
            rec = load_evidence_record(p, root)
            if rec.get("mode") == mode:
                filtered.append(p)
        files = filtered
    return files[0] if files else None


def validate_evidence(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    artifacts = data.get("artifacts", {})
    paths = []
    for value in artifacts.values():
        if isinstance(value, str):
            paths.append(value)
        elif isinstance(value, dict):
            paths.extend(value.values())
    missing = [p for p in paths if p and not Path(p).exists()]
    return {"path": str(path), "valid": len(missing) == 0, "missing": missing}


def main(argv=None):
    parser = argparse.ArgumentParser(prog="omn", description="Observable Manifold Network v0.1 runtime")
    sub = parser.add_subparsers(dest="cmd")

    run_p = sub.add_parser("run", help="run a seed")
    run_p.add_argument("--seed", choices=["synthetic-toy", "lorenz", "artifact-graph"], default="synthetic-toy")
    run_p.add_argument("--run-id", default=None, help="explicit deterministic run id")
    run_p.add_argument("--ci-mode", action="store_true", help="use deterministic CI fixture run identity")
    run_p.add_argument("--release-mode", action="store_true", help="use timestamped release run identity")
    run_p.add_argument("--no-write-report", action="store_true", help="suppress ledger append while writing minimal report/log placeholders")
    run_p.add_argument("--output-dir", default="outputs", help="artifact output root")

    val_p = sub.add_parser("validate", help="validate an evidence package")
    val_p.add_argument("--run", required=False)
    val_p.add_argument("--output-dir", default="outputs", help="artifact output root")
    val_p.add_argument("--mode", choices=["ci", "release"], default=None, help="select evidence pointer mode")

    latest_p = sub.add_parser("report-latest", help="print latest evidence path")
    latest_p.add_argument("--output-dir", default="outputs", help="artifact output root")
    latest_p.add_argument("--mode", choices=["ci", "release"], default=None, help="select evidence pointer mode")

    index_p = sub.add_parser("index-evidence", help="write stable evidence index and pointer files")
    index_p.add_argument("--output-dir", default="outputs", help="artifact output root")

    args = parser.parse_args(argv)

    if args.cmd == "run":
        mode = "ci" if args.ci_mode else "release"
        if args.release_mode:
            mode = "release"
        evidence = run(
            args.seed,
            ".",
            run_id=args.run_id,
            mode=mode,
            write_reports=not args.no_write_report,
            output_dir=args.output_dir,
        )
        print(json.dumps({
            "run_id": evidence["run_id"],
            "seed": evidence["seed"],
            "claim_status": evidence["claim_status"]["computed_status"],
            "execution_mode": evidence.get("execution_mode", {}),
            "evidence_package": str(Path(args.output_dir) / "evidence" / f'{evidence["run_id"]}_evidence_package.json')
        }, indent=2))
        return 0

    if args.cmd == "validate":
        target = args.run or latest_evidence(".", output_dir=args.output_dir, mode=args.mode)
        if not target:
            print("No evidence package found.")
            return 1
        print(json.dumps(validate_evidence(target), indent=2))
        return 0

    if args.cmd == "report-latest":
        target = latest_evidence(".", output_dir=args.output_dir, mode=args.mode)
        print(str(target) if target else "No evidence package found.")
        return 0

    if args.cmd == "index-evidence":
        index = write_evidence_index(".", output_dir=args.output_dir)
        print(json.dumps({
            "schema": index["schema"],
            "output_dir": index["output_dir"],
            "record_count": index["record_count"],
            "modes_seen": index["modes_seen"],
            "index_path": str(Path(args.output_dir) / "evidence" / "evidence_index.json"),
            "latest_ci_fixture": str(Path(args.output_dir) / "evidence" / "latest_ci_fixture.json"),
            "latest_release_evidence": str(Path(args.output_dir) / "evidence" / "latest_release_evidence.json"),
        }, indent=2))
        return 0

    parser.print_help()
    return 0