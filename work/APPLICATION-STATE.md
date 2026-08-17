# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint basis: `bfc768dcd8af60dcee52ed2944e7720ef1c2e1f2` (metadata checkpoint commit follows this basis)

## Source / reports
- Source manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: `final/fourth-report-v2.md` — 116 items
- Fifth Report: `final/fifth-report-locked.md` — 94 items

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: `F4-091`
- Next Fourth Report item: `F4-092`
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (do not start until Fourth Report validation passes)

## Current working state
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-091.docx`
- Current working DOCX SHA-256: `85fe7159297c0d7ca2c477a871af1655571e14fd7b68f44abe7040b7994bb222`
- Last known good commit basis: `bfc768dcd8af60dcee52ed2944e7720ef1c2e1f2`
- Last known good DOCX: `artifacts/checkpoints/manuscript-working-f4-091.docx`
- Current body paragraph count: 677

## Integrity
- Genuine footnotes/references: 469/469
- Orphan/dangling/duplicate references: 0/0/0
- Word field instructions: 520/520; ADDIN: 466/466
- Zotero: 465 item + 1 bibliography preserved
- Bookmarks: 53/53; hyperlinks: 52
- Arabic/RTL structural inventory: canonical-equal
- Protected OOXML parts: baseline-identical

## Structural-edit state
- F4-073–090 remain intact and validated from prior durable checkpoints.
- F4-091: the Ibn Shanbudh case is no longer reduced to rasm nonconformity alone; FN391 remains attached to the bounded case summary.
- F4-092 begins in the following FN392–393 paragraph and remains pending.
- Derived TOC field has not been recalculated; final Word field/TOC refresh remains required after editorial application.

## Holds / validation
- Open HOLD items: none.
- Last validation result: **PASS**.
- Deterministic replay/idempotency: PASS.
- Technical validation: PASS (`work/runtime/F4-091-TECHNICAL-VALIDATION.txt`).
- Bounded visual QA: PASS, 4/4 pages inspected (`work/F4-091-VISUAL-QA.md`).

## Exact next action
Read and apply only F4-092 to the current F4-091 binary. Preserve the F4-091 Ibn Shanbudh paragraph/FN391 and do not collapse later F4-093+ material. Run deterministic replay, technical validation and bounded visual QA. Do not repeat `F4-001`–`F4-091`.
