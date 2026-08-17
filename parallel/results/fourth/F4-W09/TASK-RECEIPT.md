# TASK RECEIPT — F4-W09

- Task: `F4-W09`
- Assigned items: `F4-108–110`
- Worker branch: `worker/f4/w09-108-110`
- Orchestration ref: `orchestration/f4f5-parallel-v1`
- Orchestration commit: `5e7bdf4cd24d45e06e733da87b2e695c75751226`
- Required logical baseline: `F4-047`
- Required baseline SHA-256: `6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7`
- Baseline verification: **NOT EXECUTABLE IN THIS WORKER RUNTIME**
- Worker disposition: `DEPENDENCY_BLOCKED`

## Binding instructions read

1. `parallel/tasks/fourth/F4-W09.md`
2. `parallel/AGENTS.md`
3. `parallel/WORKER-CONTRACT.md`
4. `parallel/AUDIT-PROTOCOL.md`
5. root `AGENTS.md`
6. `work/APPLICATION-STATE.md` for the frozen F4-047 replay/hash authority

## Blocking condition

The shared worker contract requires reconstructing the logical F4-047 DOCX and verifying the exact SHA-256 before any assigned edit. In this execution environment, the GitHub connector can read text files and mutate repository state but returns the binary DOCX only as a response-truncated base64 payload; the local container cannot resolve GitHub for `git clone` or direct raw download. Therefore the authoritative DOCX and full replay inputs cannot be materialized byte-completely for hashing/replay.

Per the contract's fail-closed baseline rule, no F4-108–110 edit was attempted.