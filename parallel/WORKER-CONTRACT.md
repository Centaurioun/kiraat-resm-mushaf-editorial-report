# SHARED WORKER CONTRACT

Every Fourth or Fifth worker is bound by this contract in addition to its specific task file.

## 1. Worker role

You are an isolated editorial application worker. Your job is to solve and prove only the report items assigned to you, then leave a deterministic handoff for the integrator. You are not the final integrator and you do not own the canonical application state.

## 2. Branch rule

Read the task from `orchestration/f4f5-parallel-v1`. Then create or use the exact worker branch named in that task, based on the current orchestration branch. Do not work directly on `main`, `editorial/apply-fourth-fifth-reports`, or another worker branch.

## 3. Baseline rule

For Fourth tasks, reconstruct the logical F4-047 document from the canonical source plus the existing replay pipeline and verify SHA-256 `6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7` before applying assigned edits. If this cannot be reproduced, stop and record `DEPENDENCY_BLOCKED`.

For Fifth tasks, require the later frozen F4 verified baseline specified by the Fifth task. If it does not yet exist, stop without editing.

## 4. Scope rule

Only assigned report item IDs may be substantively changed. Adjacent text may be touched only when strictly necessary to execute an assigned structural item, and that exact collateral region must be declared in the handoff.

Do not perform general proofreading, global style cleanup, unrelated typo correction, or another worker's item.

## 5. Source and citation rule

Use repository project sources only. The report item is the editorial instruction, but the current DOCX is authoritative for actual text, footnotes, fields, Arabic/RTL layout, bookmarks, and formatting.

Before deleting, consolidating, or rewriting a cited proposition, identify the genuine footnote(s) attached to it and determine what proposition each supports. Preserve citations only on materially supported claims. Never park a footnote on a generic synthesis sentence merely to preserve numbering.

If no safe destination exists, mark the item for `FOOTNOTE_PLACEMENT_CONFLICT` recommendation and do not guess.

## 6. Protected DOCX structures

Preserve genuine Word footnotes, field codes, Zotero ADDIN fields, bibliography field, bookmarks, hyperlinks, sections, styles, numbering, settings, document relationships, and Arabic/RTL runs unless the assigned report item explicitly requires a targeted change. Reuse existing Arabic/RTL runs where feasible rather than reconstructing them.

## 7. Deterministic targeting

Do not rely on paragraph number alone. Use semantic/exact text anchors plus local context and structural expectations. A replay must fail closed:

- 0 target matches → stop item;
- exactly 1 target match → eligible to apply;
- 2+ plausible matches → stop item.

Do not use fuzzy best-match application.

## 8. Replay artifact

For simple operations, produce an explicit deterministic edit specification or script. For complex structural operations, a custom deterministic replay script plus a human-readable replay specification is acceptable. The replay must be idempotent or explicitly detect an already-applied state without duplicating the edit.

## 9. Validation

At minimum compare pre/post:

- genuine footnote references and IDs;
- orphan/dangling/duplicate footnote state;
- Word field inventory;
- Zotero item/bibliography field counts;
- bookmarks;
- hyperlinks;
- RTL/Arabic runs relevant to the edit;
- comments/revisions;
- section count;
- ZIP/XML parse integrity;
- protected OOXML parts when applicable.

Unexpected changes outside assigned scope are a failure, not something to rationalize.

## 10. Visual QA

Render and inspect the affected region plus enough surrounding pages to detect pagination, clipping, overlap, footnote overflow, style propagation, heading damage, and Arabic/RTL rendering defects. A worker does not need to render the full book unless its structural edit genuinely spans a large portion.

## 11. Worker dispositions

Use worker-level dispositions only:

- `READY_FOR_INTEGRATION`
- `NEEDS_ADJUDICATION`
- `SOURCE_LIMITED_HOLD`
- `FAILED_VALIDATION`
- `DEPENDENCY_BLOCKED`

Do not mark an item canonically `VERIFIED`; that belongs to integration/audit.

## 12. Required output directory

Write only under the task-specific result directory declared by the task, normally:

`parallel/results/<wave>/<TASK-ID>/`

Required deliverables:

- `TASK-RECEIPT.md` — task ID, orchestration commit/ref used, baseline checked, report item IDs;
- `ITEM-RESULTS.jsonl` — one record per assigned item, including proposed canonical status and worker disposition;
- deterministic replay artifact(s) and `REPLAY-SPEC.md`;
- `CITATION-MAP.md` — affected genuine footnotes and supported propositions, or explicit `none`;
- `VALIDATION.md` — technical checks and exact exceptions;
- `VISUAL-QA.md` — rendered range and observations;
- `HANDOFF.md` — integrator-facing summary, dependencies, amber/red risks, and exact commit.

Do not update canonical `work/` state files.

## 13. Partial progress

If one item blocks, preserve completed independent items. Continue later assigned items only when they do not depend structurally or semantically on the blocked item. State the dependency decision explicitly.

## 14. Commit and handoff

Commit only your task outputs and any task-specific replay code/spec on your worker branch. Do not merge. Do not open-endedly continue into another task. End with a concise handoff telling the coordinator which assigned items are ready, blocked, or require adjudication.
