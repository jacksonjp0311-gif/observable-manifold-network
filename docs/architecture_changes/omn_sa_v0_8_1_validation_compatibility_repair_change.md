# OMN-SA v0.8.1 Validation Compatibility Repair Change

## Change Type

Post-v0.8 validator repair.

## Reason

v0.8 metric availability passed, but legacy tests and audits still encoded old current-state expectations from v0.7.2 and v0.7.3.

## Change

Historical validation now checks historical sections and lineage markers. Current validation checks v0.8.

## Boundary

This is a compatibility repair. It does not alter the scientific or runtime claim boundary.