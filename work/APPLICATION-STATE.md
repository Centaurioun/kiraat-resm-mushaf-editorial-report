# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current phase: `FINALIZATION`

## Source / reports
- Source manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: `final/fourth-report-v2.md` — 116 items — complete
- Fifth Report: `final/fifth-report-locked.md` — 94 items — complete
- Last fully completed Fourth Report item: `F4-116`
- Last fully completed Fifth Report item: `F5-094`
- Next Fourth/Fifth item: none
- Open report HOLDs: none

## Accepted editorial baseline
- Durable F5-094 DOCX: `artifacts/checkpoints/manuscript-working-f5-094.docx`
- SHA-256: `81f97403c0cfcf151260ab7018077145ba260c4fe4f30ca5fe2d3b501d093571`
- Body paragraphs: 674
- Fourth/Fifth scientific and editorial corrections remain frozen and must not be reopened without a new adjudicated issue.

## Finalization progress

### Item 1 — Word field refresh: **COMPLETED / PASS**
- Accepted field-refreshed candidate: `artifacts/finalization/manuscript-field-refreshed.docx`
- SHA-256: `a5ee8d96fe870086a54da1b6feb95749e443907b97f8e8bfa5b16cae199814c5`
- Six obsolete generated TOC entries removed; 46 current TOC entries retained.
- `w:updateFields=true`; deterministic replay and structural validation PASS.

### Item 2 — Full-document acceptance/layout QA: **COMPLETED / PASS**
- Full field-refreshed candidate rendered as 112 pages.
- 112/112 pages accepted (`work/FINALIZATION-ITEM2-ACCEPTANCE-QA.md`).
- No clipping, overlap, missing text/glyphs, footnote overflow, heading/page-number damage, Arabic/RTL rendering defect, unexpected blank page, destructive pagination defect, or TOC-layout break.

### Item 3 — Editorial/red-mark cleanup: **COMPLETED / PASS**
- Input: `artifacts/finalization/manuscript-field-refreshed.docx` SHA `a5ee8d96fe870086a54da1b6feb95749e443907b97f8e8bfa5b16cae199814c5`.
- Accepted cleaned candidate: `artifacts/finalization/manuscript-editorial-marks-cleaned.docx`.
- Candidate SHA-256: `67fc2e5e047957c2dd7ece5f065e612e1b51a331c9894bbb9d20d9b5b49e09f4`.
- Inventory/adjudication: direct red formatting was revision/editorial markup, not coherent semantic emphasis (`work/FINALIZATION-ITEM3-ADJUDICATION.md`).
- Removed only `w:color w:val="FF0000"`: 296 nodes from `word/document.xml` and 27 from `word/footnotes.xml`; remaining package FF0000 = 0.
- No wording, footnote text, citation identity, fields, bookmarks, hyperlinks, RTL content, paragraph order, tracked changes, or comments altered.
- Deterministic replay: first pass APPLIED, second pass ALREADY_SATISFIED, byte-idempotency PASS (`work/runtime/FINALIZATION-ITEM3-RED-CLEANUP-REPLAY.txt`).
- Structural validator PASS: body 674; accepted body-text hash preserved; footnote-text hash preserved; genuine references 469/469; orphan/dangling/duplicate 0/0/0; ADDIN 466; TOC 1; PAGEREF 46; PAGE 1; bookmarks 53/53; hyperlinks 46; `w:updateFields=true`; tracked changes/comments 0/0 (`work/runtime/FINALIZATION-ITEM3-RED-CLEANUP-VALIDATION.txt`).
- SHA-locked full QA export: run `32192519908`, artifact `9344704641`, P0–P673.
- Complete render: 112 pages. 47 pages were exact pixel identities to the already accepted item-2 render; all 65 visually changed pages were manually re-inspected after cleanup. Full item-3 visual QA PASS (`work/FINALIZATION-ITEM3-VISUAL-QA.md`).

## Current candidate integrity
- Current finalization candidate: `artifacts/finalization/manuscript-editorial-marks-cleaned.docx`.
- SHA-256: `67fc2e5e047957c2dd7ece5f065e612e1b51a331c9894bbb9d20d9b5b49e09f4`.
- Body paragraphs: 674; accepted narrative/body-text hash preserved.
- Genuine footnote references: 469/469; orphan/dangling/duplicate: 0/0/0.
- Zotero/ADDIN fields: 466 preserved.
- Derived fields: TOC 1; PAGEREF 46; PAGE 1.
- Bookmarks: 53/53; hyperlinks: 46.
- Package direct red font `FF0000`: 0.
- Word open-time refresh: `w:updateFields=true`.

## Prior validation retained
- Fourth Report global validation: PASS (`work/runtime/FOURTH-VALIDATE-FINAL.txt`).
- Fifth Report final technical validation: PASS (`work/runtime/F5-094-REPLAY.txt`).
- Fifth Report pre-finalization full narrative visual QA: PASS, 120/120 pages (`work/F5-094-VISUAL-QA.md`).
- Finalization item 2 layout QA: PASS, 112/112 pages.
- Finalization item 3 red-mark cleanup: technical + structural + visual PASS.

## Exact next action
Perform **finalization item 4 only**: freeze `artifacts/finalization/manuscript-editorial-marks-cleaned.docx` SHA `67fc2e5e047957c2dd7ece5f065e612e1b51a331c9894bbb9d20d9b5b49e09f4` as the publishing/delivery candidate, run final immutable integrity/packaging checks, create the final named delivery artifact and receipt, and do not alter scientific/editorial text unless a new adjudicated defect is discovered.
