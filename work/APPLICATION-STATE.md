# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint basis: `ed58d62f363213647d63bdf8a262b440bf25bbf2` (metadata checkpoint commit follows this basis)

## Source / reports
- Source manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: `final/fourth-report-v2.md` — 116 items
- Fifth Report: `final/fifth-report-locked.md` — 94 items

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: `F4-092`
- Next Fourth Report item: `F4-093`
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (do not start until Fourth Report validation passes)

## Current working state
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-092.docx`
- Current working DOCX SHA-256: `0c6d7393e9eac0054ef8c9de7e27cc6dc257a741e54587df0f260c4512ce0d6f`
- Last known good commit basis: `ed58d62f363213647d63bdf8a262b440bf25bbf2`
- Last known good DOCX: `artifacts/checkpoints/manuscript-working-f4-092.docx`
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
- F4-073–091 remain intact and validated from prior durable checkpoints.
- F4-092: the FN392–393 paragraph now differentiates acceptance/status categories while preserving source-specific evidence.
- P377/FN394 remains the next untouched boundary; F4-093 is pending.
- Derived TOC field has not been recalculated; final Word field/TOC refresh remains required after editorial application.

## Holds / validation
- Open HOLD items: none.
- Last validation result: **PASS**.
- Deterministic replay/idempotency: PASS.
- Technical validation: PASS (`work/runtime/F4-092-TECHNICAL-VALIDATION.txt`).
- Bounded visual QA: PASS, 5/5 pages inspected (`work/F4-092-VISUAL-QA.md`).

## Exact next action
Read and apply only F4-093 to the current F4-092 binary. Preserve P376/FN392–393 and all source-backed 4.3 material; do not pre-apply F4-094+. Run deterministic replay, technical validation and bounded visual QA. Do not repeat `F4-001`–`F4-092`.
