# CODEX ΔΦ — OMN-SA v0.8.1 Validation Compatibility and Lineage Audit Repair

## Purpose

OMN-SA v0.8 successfully repaired metric availability, but legacy validation surfaces still assumed older current-state values.

v0.8.1 repairs the compatibility layer so historical audits validate historical lineage while current-state audits validate the active v0.8 stack.

## Repairs

- v0.7.2 README self-organization audit accepts current v0.8 health while preserving v0.7.2 section checks.
- v0.7.3 README lineage audit no longer requires the current test count to remain 44.
- runtime tests accept the v0.8 evidence schema and verify canonical metrics.validation fields.
- README current architecture stack is updated to v0.8.
- docs registry points active software architecture to v0.8/v0.8.1.

## Boundary

This repair fixes validator compatibility and documentation alignment. It does not prove code correctness, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.