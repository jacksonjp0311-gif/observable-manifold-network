# Task Routing Matrix

| Task | Required route | Validation |
|---|---|---|
| docs | README -> context index -> target README | python scripts/rcc/check_rcc_nexus.py |
| runtime | README -> src/omn/core README -> tests | python -m unittest discover -s tests |
| evidence | README -> outputs README -> evidence package | python -m omn validate |
| rcc | README -> rcc/nexus -> docs/context | python scripts/rcc/check_rcc_nexus.py |
| release | README -> evidence -> tests -> non-claim locks | tests plus evidence inspection |