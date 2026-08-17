# F4-W08 Task Receipt

- Task: `F4-W08`
- Scope: `F4-100`–`F4-107` only
- Worker branch: `worker/f4/w08-100-107`
- Orchestration branch: `orchestration/f4f5-parallel-v1`
- Orchestration commit read: `5e7bdf4cd24d45e06e733da87b2e695c75751226`
- Frozen application checkpoint: `c473b24d3f6f24508c761805218bbaa29686b47c`
- Expected canonical source: `source/manuscript/current/redaktorden_gelen.docx`
- Expected canonical source SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Required logical baseline: `F4-047`
- Required logical DOCX SHA-256: `6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7`
- Baseline manifest read: `parallel/baselines/F4-047-BASELINE.json`

## Binding instructions read

- `parallel/tasks/fourth/F4-W08.md`
- `parallel/AGENTS.md`
- `parallel/WORKER-CONTRACT.md`
- `parallel/INTEGRATION-PROTOCOL.md`
- `parallel/AUDIT-PROTOCOL.md`
- root `AGENTS.md`
- `parallel/MASTER-PLAN.md` for frozen checkpoint/ownership context

## Baseline gate

`DEPENDENCY_BLOCKED`.

The repository metadata and frozen-baseline manifest were accessible, and the accepted Fourth Report wording for F4-100–107 was inspected. The execution environment, however, could not materialize the binary canonical DOCX or a reconstructed F4-047 DOCX into the local runtime. Therefore the mandated source→F4-047 replay could not be executed and the required logical SHA-256 could not be independently recomputed.

Under §3 of `parallel/WORKER-CONTRACT.md`, failure to reproduce and verify the F4-047 logical baseline is a hard stop. No substantive DOCX edit was performed and no canonical application state was touched.
