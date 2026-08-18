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
- Accepted finalization candidate: `artifacts/finalization/manuscript-field-refreshed.docx`
- Candidate SHA-256: `a5ee8d96fe870086a54da1b6feb95749e443907b97f8e8bfa5b16cae199814c5`
- Method: surgical OOXML refresh of generated TOC cache plus `w:updateFields=true`; no LibreOffice-saved round-trip accepted.
- Six obsolete generated TOC entries were removed; 46 current TOC entries remain.
- Updated cached TOC page values were independently recomputed in memory and match 46/46.
- Deterministic replay: first pass applied; second pass already satisfied; byte-idempotency PASS (`work/runtime/FINAL-FIELD-REFRESH-REPLAY.txt`).
- Structural validator: PASS (`work/runtime/FINAL-FIELD-REFRESH-VALIDATION.txt`).
- Focused field/front-matter visual QA: PASS, 6/6 pages (`work/FINAL-FIELD-REFRESH-VISUAL-QA.md`).
- Microsoft Word is not available in the execution runtime; the candidate therefore carries `w:updateFields=true` so Word can recalculate fields against Word pagination when opened.

## Field-refreshed candidate integrity
- Body paragraphs: 674; accepted narrative/body-text hash preserved.
- Genuine footnote references: 469/469; orphan/dangling/duplicate: 0/0/0.
- Zotero/ADDIN fields: 466 preserved.
- Derived fields after stale-TOC removal: TOC 1; PAGEREF 46; PAGE 1.
- Bookmarks: 53/53 preserved.
- Generated TOC hyperlinks: 46; the reduction from 52 is intentional because six obsolete TOC entries were removed after earlier accepted structural edits.
- `word/document.xml` and `word/settings.xml` are the only package parts changed by field refresh; protected narrative text and other package parts remain preserved.
- Word open-time refresh: `w:updateFields=true`.

## Prior validation retained
- Fourth Report global validation: PASS (`work/runtime/FOURTH-VALIDATE-FINAL.txt`).
- Fifth Report final technical validation: PASS (`work/runtime/F5-094-REPLAY.txt`).
- Fifth Report pre-finalization full narrative visual QA: PASS, 120/120 pages (`work/F5-094-VISUAL-QA.md`).

## Exact next action
Perform **finalization item 2 only**: full-document acceptance/layout QA against `artifacts/finalization/manuscript-field-refreshed.docx` SHA `a5ee8d96fe870086a54da1b6feb95749e443907b97f8e8bfa5b16cae199814c5`. Inspect the complete rendered manuscript and record any layout/format defects. Do not begin editorial-mark cleanup or final publishing-file freeze until item 2 is completed.
