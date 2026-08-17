# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint basis: `df5fb58e683ae258e7e8b2eecee27287c2b3c7ea` (metadata checkpoint commit follows this basis)

## Source / reports
- Source manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: `final/fourth-report-v2.md` — 116 items
- Fifth Report: `final/fifth-report-locked.md` — 94 items

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: `F4-114`
- Next Fourth Report item: `F4-115`
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (do not start until Fourth Report validation passes)

## Current working state
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-114.docx`
- Current working DOCX SHA-256: `419bc27be6a259d03f42ed7da7f7bbf0b1f64c9af3ab6ed78393f6aa9a96ca56`
- Last known good commit basis: `df5fb58e683ae258e7e8b2eecee27287c2b3c7ea`
- Last known good DOCX: `artifacts/checkpoints/manuscript-working-f4-114.docx`
- Current body paragraph count: 676

## Integrity
- Genuine footnotes/references: 469/469
- Orphan/dangling/duplicate references: 0/0/0
- Word field instructions: 520/520; ADDIN: 466/466
- Zotero: 465 item + 1 bibliography preserved
- Bookmarks: 53/53; hyperlinks: 52
- Arabic/RTL structural inventory: canonical-equal
- Protected OOXML parts: baseline-identical except explicitly authorized footnote-text changes inherited from F4-112/F4-113; F4-114 changes only bibliography result text in `word/document.xml`

## Structural-edit state
- F4-073–113 remain intact and validated from prior durable checkpoints.
- F4-114: Kahraman bibliography record no longer carries the malformed DOI URL; Maşalı bibliography DOI is `https://doi.org/10.56361/usul.173700` with one DOI prefix.
- F4-114 changed only visible bibliography result text at P578 and P599; Word/Zotero field instructions and hyperlink structures remain preserved.
- Current body paragraph count remains 676; all 469 footnote identities/references, 520 fields, Zotero/ADDIN fields, bookmarks, hyperlinks and RTL structural inventory remain preserved.

## Holds / validation
- Open HOLD items: none.
- Last validation result: **PASS**.
- Deterministic replay/idempotency: PASS.
- Technical validation: PASS (`work/runtime/F4-114-TECHNICAL-VALIDATION.txt`).
- Bounded visual QA: PASS, 4/4 pages inspected (`work/F4-114-VISUAL-QA.md`).

## Exact next action
Apply only F4-115 against the current durable F4-114 binary. First verify the exact report-prescribed edition-use decisions against current footnote and bibliography evidence: keep İbn Ebû Dâvud 2002 and remove unused 2006; retain both Süleymân b. Necâh 2000 and 1999 because both are cited; keep İbn Kuteybe en-Neccâr record and remove unused 1999 el-Asfar record. Do not pre-apply F4-116 or repeat `F4-001`–`F4-114`.
