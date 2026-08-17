# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint basis: `6e5fe666e32638957b2937d74fa1f63519d290d1` (metadata checkpoint commit follows this basis)

## Source / reports
- Source manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: `final/fourth-report-v2.md` — 116 items
- Fifth Report: `final/fifth-report-locked.md` — 94 items

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: `F4-102`
- Next Fourth Report item: `F4-103`
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (do not start until Fourth Report validation passes)

## Current working state
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-102.docx`
- Current working DOCX SHA-256: `38561f498d0abacc3dacea2bb35b92aa1ed4abe67d8b767657ea80e759ff69e8`
- Last known good commit basis: `6e5fe666e32638957b2937d74fa1f63519d290d1`
- Last known good DOCX: `artifacts/checkpoints/manuscript-working-f4-102.docx`
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
- F4-073–101 remain intact and validated from prior durable checkpoints.
- F4-102: 4.7 begins with the print/resm problem; unique pre-print historical evidence is compressed rather than silently discarded.
- Current body paragraph count remains 677; FN454/FN455 identities and all protected OOXML remain preserved.
- F4-103+ has not been pre-applied. Derived TOC field has not been recalculated; final Word field/TOC refresh remains required.

## Holds / validation
- Open HOLD items: none.
- Last validation result: **PASS**.
- Deterministic replay/idempotency: PASS.
- Technical validation: PASS (`work/runtime/F4-102-TECHNICAL-VALIDATION.txt`).
- Bounded visual QA: PASS, 4/4 pages inspected (`work/F4-102-VISUAL-QA.md`).

## Exact next action
Read and apply only F4-103 to the current F4-102 binary. Correct the 1201/1787 Saint Petersburg statement by removing the unsupported `Mevlây Osman (?)` attribution and using only the report-authorized safe core naming II. Katerina's order. Establish the genuine attached footnote mapping/support before preserving or relocating any reference. Do not pre-apply F4-104+. Run deterministic replay, technical validation and bounded visual QA. Do not repeat `F4-001`–`F4-102`.
