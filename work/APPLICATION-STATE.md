# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint basis: `82b0a1826956f4c137ef376166c08876d61b6231` (metadata checkpoint commit follows this basis)

## Source / reports
- Source manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: `final/fourth-report-v2.md` — 116 items
- Fifth Report: `final/fifth-report-locked.md` — 94 items

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: `F4-096`
- Next Fourth Report item: `F4-097`
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (do not start until Fourth Report validation passes)

## Current working state
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-096.docx`
- Current working DOCX SHA-256: `67791838653b64426378747d1fd4f4a304afe7d38e2c13cf0b7da60972117e41`
- Last known good commit basis: `82b0a1826956f4c137ef376166c08876d61b6231`
- Last known good DOCX: `artifacts/checkpoints/manuscript-working-f4-096.docx`
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
- F4-073–095 remain intact and validated from prior durable checkpoints.
- F4-096: the general waqf framing now separates meaning/nahw/rivayat from specific rasm-related written cues.
- FN413–416 source-backed examples and the 4.5 heading remain unchanged; F4-097 is next.
- The visible Mehdevi work note under 4.5 remains intentionally pending for F4-098.
- Derived TOC field has not been recalculated; final Word field/TOC refresh remains required after editorial application.

## Holds / validation
- Open HOLD items: none.
- Last validation result: **PASS**.
- Deterministic replay/idempotency: PASS.
- Technical validation: PASS (`work/runtime/F4-096-TECHNICAL-VALIDATION.txt`).
- Bounded visual QA: PASS, 4/4 pages inspected (`work/F4-096-VISUAL-QA.md`).

## Exact next action
Read and apply only F4-097 to the current F4-096 binary. Reframe rasm reports as complementary written evidence rather than a constitutive source of qiraat; preserve FN417+ source structure and leave the visible Mehdevi work note/date corrections for F4-098. Run deterministic replay, technical validation and bounded visual QA. Do not repeat `F4-001`–`F4-096`.
