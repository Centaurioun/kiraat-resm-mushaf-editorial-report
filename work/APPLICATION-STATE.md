# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint basis: `01d6cd673b7126a493a8dd2b9c96e1fc8f62ced5` (metadata checkpoint commit follows this basis)

## Source / reports
- Source manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: `final/fourth-report-v2.md` — 116 items
- Fifth Report: `final/fifth-report-locked.md` — 94 items

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: `F4-115`
- Next Fourth Report item: `F4-116`
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (do not start until Fourth Report validation passes)

## Current working state
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-115.docx`
- Current working DOCX SHA-256: `73ccdd0b5e0c63450cf611d175e5fcf547ac0b9a9aaaf11bf09a4e5db5c996bf`
- Last known good commit basis: `01d6cd673b7126a493a8dd2b9c96e1fc8f62ced5`
- Last known good DOCX: `artifacts/checkpoints/manuscript-working-f4-115.docx`
- Current body paragraph count: 674

## Integrity
- Genuine footnotes/references: 469/469
- Orphan/dangling/duplicate references: 0/0/0
- Word field instructions: 520/520; ADDIN: 466/466
- Zotero: 465 item + 1 bibliography preserved
- Bookmarks: 53/53; hyperlinks: 52
- Arabic/RTL structural inventory: canonical-equal
- Protected OOXML parts: baseline-identical except explicitly authorized footnote-text changes inherited from F4-112/F4-113; F4-114/F4-115 modify only bibliography result content/paragraphs in `word/document.xml` while Word/Zotero field instructions remain preserved

## Structural-edit state
- F4-073–114 remain intact and validated from prior durable checkpoints.
- F4-115: unused bibliography records for İbn Ebû Dâvud 2006 and İbn Kuteybe el-Asfar 1999 are removed only after manuscript-use matching.
- F4-115 preserves the cited İbn Ebû Dâvud Vâiz 2002 and İbn Kuteybe en-Neccâr records, and preserves both Süleymân b. Necâh editions because FN109 and FN373 cite different editions.
- Current body paragraph count is 674; all 469 footnote identities/references, 520 fields, Zotero/ADDIN fields, bookmarks, hyperlinks and RTL structural inventory remain preserved.

## Holds / validation
- Open HOLD items: none.
- Last validation result: **PASS**.
- Deterministic replay/idempotency: PASS.
- Technical validation: PASS (`work/runtime/F4-115-TECHNICAL-VALIDATION.txt`).
- Bounded visual QA: PASS, 9/9 pages inspected (`work/F4-115-VISUAL-QA.md`).

## Exact next action
Apply only F4-116 against the current durable F4-115 binary. Reconfirm all Ebû Şâme `el-Murşidu’l-vecîz` footnote citations and match short volume/page references to the 1975 Tayyar Altıkulaç and 1993 Velîd Müsâid et-Tabatabâî bibliography editions. Keep 1993; retain 1975 only if current manuscript evidence proves actual use. If short citations cannot be safely edition-resolved from manuscript sequence, HOLD at F4-116. Do not enter FIFTH_APPLY before F4-116 is resolved and FOURTH_VALIDATE passes.
