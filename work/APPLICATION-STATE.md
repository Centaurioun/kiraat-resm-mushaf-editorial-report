# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint basis: `4a43d0c24cac51c6f5b927829057b362c9e55b61` (metadata checkpoint commit follows this basis)

## Source / reports
- Source manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: `final/fourth-report-v2.md` — 116 items
- Fifth Report: `final/fifth-report-locked.md` — 94 items

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: `F4-094`
- Next Fourth Report item: `F4-095`
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (do not start until Fourth Report validation passes)

## Current working state
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-094.docx`
- Current working DOCX SHA-256: `523fcf36cae029c4761e254a378beda7f378499ed8a0b13bcf0371cd83079894`
- Last known good commit basis: `4a43d0c24cac51c6f5b927829057b362c9e55b61`
- Last known good DOCX: `artifacts/checkpoints/manuscript-working-f4-094.docx`
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
- F4-073–093 remain intact and validated from prior durable checkpoints.
- F4-094: the bookmark-backed 4.4 heading now uses the report-approved relationship wording rather than one-way causal 'effect' language.
- FN400+ 4.4 opening material remains source-backed and unchanged; F4-095 is next.
- Derived TOC field has not been recalculated; final Word field/TOC refresh remains required after editorial application.

## Holds / validation
- Open HOLD items: none.
- Last validation result: **PASS**.
- Deterministic replay/idempotency: PASS.
- Technical validation: PASS (`work/runtime/F4-094-TECHNICAL-VALIDATION.txt`).
- Bounded visual QA: PASS, 4/4 pages inspected (`work/F4-094-VISUAL-QA.md`).

## Exact next action
Read and apply only F4-095 to the current F4-094 binary. Preserve the F4-094 bookmark-backed heading and all source-backed material except where F4-095 explicitly narrows the portrayal of qiraat imams as selectors. Run deterministic replay, technical validation and bounded visual QA. Do not repeat `F4-001`–`F4-094`.
