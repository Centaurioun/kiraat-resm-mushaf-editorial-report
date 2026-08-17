# F4-W08 Integrator Handoff

## Worker disposition

`DEPENDENCY_BLOCKED`

Assigned scope: `F4-100`–`F4-107` only.

No assigned item is claimed `READY_FOR_INTEGRATION` because the mandatory F4-047 logical baseline could not be reconstructed/materialized and its SHA-256 could not be independently verified in this worker runtime.

## Durable package

Result directory: `parallel/results/fourth/F4-W08/`

- `TASK-RECEIPT.md`
- `ITEM-RESULTS.jsonl`
- `REPLAY-SPEC.md`
- `REPLAY-BLOCKER.json`
- `CITATION-MAP.md`
- `VALIDATION.md`
- `VISUAL-QA.md`
- `HANDOFF.md`

The content package immediately before this handoff file was committed at:

`f07d76afa2dba49ba8eb2bc534967c0d5b9f7c08`

The branch HEAD containing this handoff is the authoritative worker handoff state; integrator should resolve the current `worker/f4/w08-100-107` HEAD when ingesting.

## What was established safely

- The Fourth Report instructions for all eight assigned items were read and converted into a fail-closed replay specification.
- The source extraction contains all major 4.6/4.7 anchors relevant to the assigned cluster.
- F4-103's uncertain `Mevlây Osman (?)` identity is explicitly excluded from the authorized safe replacement.
- F4-104 and F4-105 are constrained to multicausal formulations.
- F4-107 source text preserves a real distinction between the 1873 permission/decision and the 1874 actual printing; the extracted statement carries marker `[^462]`.

## Blocking dependency

The worker contract requires a source→F4-047 replay and exact logical SHA check before edits. The expected logical SHA is:

`6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7`

The repository binary DOCX could not be materialized into the available execution runtime, so this prerequisite could not be executed. Consequently genuine Word footnotes, fields, Zotero structures, bookmarks, hyperlinks, RTL runs, OOXML integrity and visual render could not be checked on an edited document.

## Integrator action

Do **not** treat this package as proven replay. Re-run F4-W08 from a runtime that can reconstruct/materialize the frozen F4-047 DOCX. Once the exact SHA gate passes, use `REPLAY-SPEC.md` to perform unique-anchor targeting, genuine footnote proposition mapping, bounded technical validation and visual QA. If any target is absent/non-unique or any footnote destination is unsafe, fail closed per the worker/integration protocols.

## Scope/protection confirmation

- no `main` mutation;
- no canonical application branch mutation;
- no protected canonical `work/` state mutation;
- no `source/` mutation;
- no Fifth Report work;
- no other worker item work;
- no merge performed.

Worker stops here at task boundary.
