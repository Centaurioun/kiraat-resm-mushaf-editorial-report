# SHARED WORKER CONTRACT

Revision: **2**. `parallel/BASELINE-AMENDMENT-001.md` is binding and controls over the earlier binary-only baseline gate.

Every Fourth or Fifth worker is bound by this contract in addition to its specific task file.

## 1. Worker role

You are an isolated editorial application worker. Your job is to solve and prove only the report items assigned to you, then leave a deterministic handoff for the integrator. You are not the final integrator and you do not own the canonical application state.

## 2. Branch rule

Read the task from `orchestration/f4f5-parallel-v1`. Then create or use the exact worker branch named in that task. Do not work directly on `main`, `editorial/apply-fourth-fifth-reports`, or another worker branch.

If your worker branch was created from an earlier orchestration commit, you must still read the **latest** `parallel/WORKER-CONTRACT.md` and `parallel/BASELINE-AMENDMENT-001.md` from `orchestration/f4f5-parallel-v1` before continuing.

## 3. Frozen Fourth checkpoint

For Fourth tasks, confirm from GitHub durable state that:

- canonical application checkpoint is `c473b24d3f6f24508c761805218bbaa29686b47c`;
- F4-001–047 are completed and F4-048 is next;
- canonical source SHA-256 is `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`;
- Fourth Report V2 and the existing F4 replay/state evidence are readable.

GitHub durable state records F4-047 package SHA `6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7`. A coordinator runtime recovered a semantically/structurally matching prior F4-047 local package with a different whole-file SHA; see `BASELINE-AMENDMENT-001.md`. Until High integration adjudicates that package-level discrepancy, **whole-DOCX SHA reproduction is not a worker-stage hard gate**.

For Fifth tasks, the later frozen F4 verified baseline remains mandatory. If that Fifth phase gate does not yet exist, stop without editing.

## 4. Worker execution modes

### Mode A — FULL_BINARY
Use when you can materialize the required DOCX binary locally. Apply your assigned changes to a temporary worker copy, run deterministic replay/idempotency checks, technical validation and bounded visual QA.

### Mode B — CONNECTOR_ONLY_PREPARATION
Use when repository/project text is accessible but the DOCX binary cannot be materialized.

In Mode B, binary unavailability alone is **not** `DEPENDENCY_BLOCKED`. You must still perform all safely possible editorial work:

- locate assigned targets using the canonical manuscript/extracted manuscript, accepted report, prior replay/state evidence and exact semantic anchors;
- determine the report-authorized final wording/structure;
- prepare deterministic semantic targeting and replay code/specification where possible;
- map available citation/footnote evidence to the propositions being preserved, rewritten or removed;
- identify every point that still requires actual OOXML/footnote/field confirmation;
- mark binary technical validation and visual QA as deferred to the integrator.

A safely prepared Mode-B item uses worker disposition:

`READY_FOR_INTEGRATION_DEFERRED_BINARY_QA`

Do not claim that such an item has already been applied to or verified in the canonical DOCX.

Use `DEPENDENCY_BLOCKED` only when even a safe editorial/replay package cannot be prepared from repository evidence or a real semantic/structural prerequisite is missing.

## 5. Scope rule

Only assigned report item IDs may be substantively changed. Adjacent text may be touched only when strictly necessary to execute an assigned structural item, and that exact collateral region must be declared in the handoff.

Do not perform general proofreading, global style cleanup, unrelated typo correction, or another worker's item.

## 6. Source and citation rule

Use repository project sources only. No external web research. The report item is the editorial instruction; the current DOCX is authoritative for actual formatting, genuine footnotes, fields, Arabic/RTL layout, bookmarks and other OOXML details.

In Mode B, use repository textual/extracted evidence for preparation but explicitly defer any fact that can only be proven from the actual OOXML package.

Before deleting, consolidating or rewriting a cited proposition, identify the genuine footnote(s) attached to it as far as repository evidence permits and determine what proposition each supports. Preserve citations only on materially supported claims. Never park a footnote on a generic synthesis sentence merely to preserve numbering.

If no safe citation destination can be established, recommend `FOOTNOTE_PLACEMENT_CONFLICT`; do not guess.

## 7. Protected DOCX structures

Preserve genuine Word footnotes, field codes, Zotero ADDIN fields, bibliography field, bookmarks, hyperlinks, sections, styles, numbering, settings, document relationships and Arabic/RTL runs unless the assigned report item explicitly requires a targeted change. Reuse existing Arabic/RTL runs where feasible rather than reconstructing them.

Mode-B workers must encode these preservation requirements into their replay/handoff even though actual package confirmation is deferred.

## 8. Deterministic targeting

Do not rely on paragraph number alone. Use semantic/exact text anchors plus local context and structural expectations. A replay must fail closed:

- 0 target matches → stop item or require adjudication;
- exactly 1 target match → eligible to apply;
- 2+ plausible matches → stop item or require adjudication.

Do not use fuzzy best-match application.

## 9. Replay artifact

For simple operations, produce an explicit deterministic edit specification or script. For complex structural operations, a custom deterministic replay script plus a human-readable replay specification is acceptable.

Replay logic must be idempotent or explicitly detect an already-applied state without duplicating the edit.

A Mode-B replay may be unexecuted locally; if so, label it clearly as `UNEXECUTED_CONNECTOR_ONLY` and enumerate every integrator validation it requires. Do not fabricate a PASS.

## 10. Validation

### Mode A minimum validation
Compare pre/post:

- genuine footnote references and IDs;
- orphan/dangling/duplicate footnote state;
- Word field inventory;
- Zotero item/bibliography fields;
- bookmarks;
- hyperlinks;
- RTL/Arabic runs relevant to the edit;
- comments/revisions;
- section count;
- ZIP/XML parse integrity;
- protected OOXML parts when applicable.

Unexpected changes outside assigned scope are a failure.

### Mode B validation record
`VALIDATION.md` must state `DEFERRED_BINARY_QA` and list the exact checks the integrator must perform. Textual anchor uniqueness, report compliance, citation reasoning and scope compliance should still be checked from available repository evidence.

## 11. Visual QA

Mode A: render and inspect the affected region plus enough surrounding pages to detect pagination, clipping, overlap, footnote overflow, style propagation, heading damage and Arabic/RTL rendering defects.

Mode B: do not pretend to render. `VISUAL-QA.md` must state `NOT_RUN_CONNECTOR_ONLY — mandatory at integration` and identify the pages/section span that the integrator should inspect.

## 12. Worker dispositions

Use worker-level dispositions only:

- `READY_FOR_INTEGRATION`
- `READY_FOR_INTEGRATION_DEFERRED_BINARY_QA`
- `NEEDS_ADJUDICATION`
- `SOURCE_LIMITED_HOLD`
- `FAILED_VALIDATION`
- `DEPENDENCY_BLOCKED`

Do not mark an item canonically `VERIFIED`; that belongs to integration/audit.

## 13. Required output directory

Write only under the task-specific result directory declared by the task, normally:

`parallel/results/<wave>/<TASK-ID>/`

Required deliverables:

- `TASK-RECEIPT.md` — task ID, orchestration ref/commit used, execution mode, baseline evidence checked, report item IDs;
- `ITEM-RESULTS.jsonl` — one record per assigned item, including proposed canonical status and worker disposition;
- deterministic replay artifact(s) and `REPLAY-SPEC.md`;
- `CITATION-MAP.md` — affected citations/footnotes and supported propositions, with deferred OOXML confirmations identified where necessary;
- `VALIDATION.md` — actual checks run plus exact deferred checks;
- `VISUAL-QA.md` — actual rendered range or explicit connector-only deferral;
- `HANDOFF.md` — integrator-facing summary, dependencies, amber/red risks and exact worker commit.

Do not update canonical `work/` state files.

## 14. Partial progress

If one item blocks, preserve completed independent items. Continue later assigned items only when they do not depend structurally or semantically on the blocked item. State the dependency decision explicitly.

## 15. Integration authority

For every Mode-B item, the High integrator must perform actual DOCX target resolution, mutation, citation/footnote inspection, OOXML validation, deterministic replay/idempotency and bounded visual QA before advancing canonical ledger state.

Worker branch files are evidence packages. Worker branches themselves are never merged into the canonical application branch.

## 16. Commit and handoff

Commit only your task outputs and any task-specific replay code/spec on your worker branch. Do not merge. Do not open-endedly continue into another task. End with a concise handoff telling the coordinator which assigned items are ready, deferred-binary-QA, blocked or require adjudication.
