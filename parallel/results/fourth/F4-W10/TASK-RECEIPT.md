# F4-W10 Task Receipt

- Worker: `F4-W10`
- Scope: `F4-112`, `F4-114`, `F4-115`, `F4-116` only.
- Worker branch: `worker/f4/w10-footnotes-bibliography`
- Orchestration base: `orchestration/f4f5-parallel-v1` at `5e7bdf4cd24d45e06e733da87b2e695c75751226`.
- Result directory: `parallel/results/fourth/F4-W10/`.
- Explicit exclusions observed: `F4-111`, `F4-113`, all other Fourth workers, all Fifth Report work, `main`, and the canonical application branch.

## Binding authority read

1. `parallel/tasks/fourth/F4-W10.md`
2. `parallel/AGENTS.md`
3. `parallel/WORKER-CONTRACT.md`
4. `parallel/AUDIT-PROTOCOL.md`
5. `parallel/INTEGRATION-PROTOCOL.md`
6. root `AGENTS.md`

No external bibliography research was used. All citation/edition decisions below are based on repository evidence.

## Frozen dependency

`parallel/baselines/F4-047-BASELINE.json` identifies the required logical F4-047 DOCX SHA-256 as:

`6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7`

The repository's F4-047 validation record reports the expected inventory: 469 genuine footnotes, 469 footnote references, 520 fields, 465 Zotero item fields, 1 Zotero bibliography field, 365 RTL markers, 53/53 bookmark start/end IDs, 52 hyperlinks, 10 sections, no comments/revisions, and valid ZIP/XML structure.

## Worker disposition

`READY_FOR_INTEGRATION`

The replay is deterministic, fail-closed, baseline-SHA-aware, and synthetically tested for idempotency. This runtime could not materialize the 406,091-byte GitHub DOCX into the local execution container, so **no claim is made that the worker replay itself was executed against the real F4-047 binary here**. The replay therefore carries an explicit exact-SHA worker-proof gate plus full integration-time validation requirements. Content/citation ambiguity is resolved; binary replay and visual QA remain mandatory integration gates.
