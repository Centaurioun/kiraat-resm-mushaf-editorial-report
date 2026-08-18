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
- Deterministic replay/idempotency and structural validation: PASS.

### Item 2 — Full-document acceptance/layout QA: **COMPLETED / PASS**
- Candidate remained byte-identical to the accepted item-1 candidate: SHA `a5ee8d96fe870086a54da1b6feb95749e443907b97f8e8bfa5b16cae199814c5`.
- Full SHA-locked QA export: run `32189159596`, artifact `9343561312`, P0–P673.
- Complete render: 112 pages; every page inspected, **112/112 PASS** (`work/FINALIZATION-ITEM2-ACCEPTANCE-QA.md`).
- No clipping, overlap, missing text/glyphs, footnote overflow, heading/page-number damage, Arabic/RTL rendering defect, unexpected blank page, destructive pagination defect, or TOC-layout break was found.
- The sparse final Conclusion page is valid content flow, not a blank-page defect.
- Pre-existing red-font editorial markings remain visible on a number of narrative pages. They are not item-2 layout failures and are reserved for finalization item 3.

## Current candidate integrity
- Body paragraphs: 674; accepted narrative/body-text hash preserved.
- Genuine footnote references: 469/469; orphan/dangling/duplicate: 0/0/0.
- Zotero/ADDIN fields: 466 preserved.
- Derived fields: TOC 1; PAGEREF 46; PAGE 1.
- Bookmarks: 53/53 preserved.
- Generated TOC hyperlinks: 46; six obsolete generated TOC entries were intentionally removed during item 1.
- Word open-time refresh: `w:updateFields=true`.

## Prior validation retained
- Fourth Report global validation: PASS (`work/runtime/FOURTH-VALIDATE-FINAL.txt`).
- Fifth Report final technical validation: PASS (`work/runtime/F5-094-REPLAY.txt`).
- Fifth Report pre-finalization full narrative visual QA: PASS, 120/120 pages (`work/F5-094-VISUAL-QA.md`).
- Finalization item 2 full-document layout QA: PASS, 112/112 pages (`work/FINALIZATION-ITEM2-ACCEPTANCE-QA.md`).

## Exact next action
Perform **finalization item 3 only**: identify, adjudicate, and clean the remaining editorial/red-font markings in `artifacts/finalization/manuscript-field-refreshed.docx` SHA `a5ee8d96fe870086a54da1b6feb95749e443907b97f8e8bfa5b16cae199814c5`, preserving accepted scientific text unless a marking itself encodes an unresolved editorial instruction. Do not begin final publishing-file freeze (item 4) until item 3 is completed and revalidated.
