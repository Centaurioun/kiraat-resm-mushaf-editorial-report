# NEXT HANDOFF

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current phase: `FINALIZATION`

## Resume boundary
- Fourth Report: F4-001–F4-116 complete — DO NOT REPEAT.
- Fifth Report: F5-001–F5-094 complete — DO NOT REPEAT.
- Finalization item 1, Word field refresh: **COMPLETED / PASS**.
- Finalization item 2, full-document acceptance/layout QA: **COMPLETED / PASS**.
- Finalization item 3, editorial/red-mark cleanup: **COMPLETED / PASS**.
- Next task: finalization item 4, publishing-file freeze / final delivery artifact.

## Accepted editorial baseline
- `artifacts/checkpoints/manuscript-working-f5-094.docx`
- SHA-256: `81f97403c0cfcf151260ab7018077145ba260c4fe4f30ca5fe2d3b501d093571`

## Current finalization candidate
- `artifacts/finalization/manuscript-editorial-marks-cleaned.docx`
- SHA-256: `67fc2e5e047957c2dd7ece5f065e612e1b51a331c9894bbb9d20d9b5b49e09f4`
- Body paragraphs: 674; accepted narrative/body text preserved.
- Footnote references: 469/469; orphan/dangling/duplicate 0/0/0.
- Zotero/ADDIN: 466 preserved.
- TOC: 1; PAGEREF: 46; PAGE: 1.
- Bookmarks: 53/53; hyperlinks: 46.
- Package direct red font `FF0000`: 0.
- Word field recalculation on open: `w:updateFields=true`.
- Tracked changes/comments: 0/0.

## Item 3 evidence
- Adjudication: `work/FINALIZATION-ITEM3-ADJUDICATION.md`.
- Deterministic runner: `work/finalize_cleanup_editorial_red.py`.
- Replay: `work/runtime/FINALIZATION-ITEM3-RED-CLEANUP-REPLAY.txt` — APPLIED then ALREADY_SATISFIED; BYTE_IDENTICAL=PASS.
- SHA: `work/runtime/FINALIZATION-ITEM3-RED-CLEANUP-SHA256.txt`.
- Structural validator: `work/runtime/FINALIZATION-ITEM3-RED-CLEANUP-VALIDATION.txt` — PASS.
- Application workflow: run `32192429391`.
- Removed direct red formatting: 296 nodes from `word/document.xml` + 27 from `word/footnotes.xml`; remaining FF0000 = 0.
- Full SHA-locked QA export: run `32192519908`, artifact `9344704641`, P0–P673.
- Full render: 112 pages.
- Visual QA: `work/FINALIZATION-ITEM3-VISUAL-QA.md` — PASS; 47 pages pixel-identical to accepted item 2 and all 65 changed pages manually re-inspected.
- Visual diff receipt: `work/runtime/FINALIZATION-ITEM3-VISUAL-DIFF.txt`.
- Status: `work/FINALIZATION-ITEM3-STATUS.md`.

## Engine note
Microsoft Word is not available in this runtime. LibreOffice is used for render/QA only. The accepted candidate remains the controlled OOXML artifact and carries `w:updateFields=true` so Word can recalculate derived fields when opened there.

## Open HOLDs
none

## Exact next action
On the user's next `devam et`, execute **only finalization item 4**: freeze `artifacts/finalization/manuscript-editorial-marks-cleaned.docx` SHA `67fc2e5e047957c2dd7ece5f065e612e1b51a331c9894bbb9d20d9b5b49e09f4` as the final publishing/delivery candidate, run final immutable package/integrity checks, create the final named delivery DOCX plus checksum/receipt, and close the finalization phase. Do not alter scientific/editorial text unless a new adjudicated defect is discovered.
