# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint basis: `1465236630cd0299cd9aeb8dedbcf46751880ae4` (metadata checkpoint commit follows this basis)

## Source / reports
- Source manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: `final/fourth-report-v2.md` — 116 items
- Fifth Report: `final/fifth-report-locked.md` — 94 items

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: `F4-093`
- Next Fourth Report item: `F4-094`
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (do not start until Fourth Report validation passes)

## Current working state
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-093.docx`
- Current working DOCX SHA-256: `3a2c3f5b16a889de359ed59c859a2eeff4d9610b76b92c7af023858e8a9a5a06`
- Last known good commit basis: `1465236630cd0299cd9aeb8dedbcf46751880ae4`
- Last known good DOCX: `artifacts/checkpoints/manuscript-working-f4-093.docx`
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
- F4-073–092 remain intact and validated from prior durable checkpoints.
- F4-093: 4.3 now closes with a direct conceptual bridge into preference/tawjih/waqf rather than another broad rasm-authority conclusion.
- The bookmark-backed 4.4 heading and FN400+ opening material remain unchanged; F4-094 is next.
- Derived TOC field has not been recalculated; final Word field/TOC refresh remains required after editorial application.

## Holds / validation
- Open HOLD items: none.
- Last validation result: **PASS**.
- Deterministic replay/idempotency: PASS.
- Technical validation: PASS (`work/runtime/F4-093-TECHNICAL-VALIDATION.txt`).
- Bounded visual QA: PASS, 4/4 pages inspected (`work/F4-093-VISUAL-QA.md`).

## Exact next action
Read and apply only F4-094 to the current F4-093 binary. Preserve the F4-093 transition, bookmark-backed 4.4 heading and source-backed FN400+ material except where F4-094 explicitly requires a scoped heading/opening correction. Run deterministic replay, technical validation and bounded visual QA. Do not repeat `F4-001`–`F4-093`.
