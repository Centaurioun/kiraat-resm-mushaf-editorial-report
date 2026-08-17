# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint basis: `ad255fdf3c4fa7a1c91abac216eafcb6e80e602d` (metadata checkpoint commit follows this basis)

## Source / reports
- Source manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: `final/fourth-report-v2.md` — 116 items
- Fifth Report: `final/fifth-report-locked.md` — 94 items

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: `F4-097`
- Next Fourth Report item: `F4-098`
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (do not start until Fourth Report validation passes)

## Current working state
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-097.docx`
- Current working DOCX SHA-256: `9f76e4b8a98a70a8af42a73b261945378c5bd423d94903b4ac20a94b2880f5da`
- Last known good commit basis: `ad255fdf3c4fa7a1c91abac216eafcb6e80e602d`
- Last known good DOCX: `artifacts/checkpoints/manuscript-working-f4-097.docx`
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
- F4-073–096 remain intact and validated from prior durable checkpoints.
- F4-097: rasm reports are now treated as complementary written evidence rather than a constitutive qiraat source.
- F4-098 editor-note/date/attribution corrections in 4.5 remain next and untouched.
- Derived TOC field has not been recalculated; final Word field/TOC refresh remains required after editorial application.

## Holds / validation
- Open HOLD items: none.
- Last validation result: **PASS**.
- Deterministic replay/idempotency: PASS.
- Technical validation: PASS (`work/runtime/F4-097-TECHNICAL-VALIDATION.txt`).
- Bounded visual QA: PASS, 5/5 pages inspected (`work/F4-097-VISUAL-QA.md`).

## Exact next action
Read and apply only F4-098 to the current F4-097 binary. Remove visible work notes, correct first-use death dates exactly as the Fourth Report specifies, and attribute the universal-hikma claim to the relevant authors rather than the book voice. Preserve all affected footnotes/RTL/source material and do not pre-apply F4-099+. Run deterministic replay, technical validation and bounded visual QA. Do not repeat `F4-001`–`F4-097`.
