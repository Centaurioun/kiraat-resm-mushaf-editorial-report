# NEXT HANDOFF

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Checkpoint basis HEAD: `01d6cd673b7126a493a8dd2b9c96e1fc8f62ced5` plus this metadata checkpoint commit
- Current phase: `FOURTH_APPLY`

## Resume boundary
- Last completed item: `F4-115`
- Next item: `F4-116`
- DO-NOT-REPEAT: `F4-001`–`F4-115`

## Working manuscript
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-115.docx`
- Current working SHA-256: `73ccdd0b5e0c63450cf611d175e5fcf547ac0b9a9aaaf11bf09a4e5db5c996bf`
- Last known good DOCX: same path above

## Integrity snapshot
- Footnotes/references: 469/469; orphans/dangling/duplicates: 0/0/0
- Word fields: 520; ADDIN: 466; Zotero: 465 item + 1 bibliography
- Bookmarks: 53/53; hyperlinks: 52; RTL inventory canonical-equal
- Protected OOXML: baseline-identical except explicitly authorized footnote-text changes inherited from F4-112/F4-113; F4-114/F4-115 modify only bibliography result content/paragraphs in `word/document.xml` while Word/Zotero field instructions remain preserved

## Latest structural state
- F4-073–114 remain intact and validated from prior durable checkpoints.
- F4-115: unused bibliography records for İbn Ebû Dâvud 2006 and İbn Kuteybe el-Asfar 1999 are removed only after manuscript-use matching.
- F4-115 preserves the cited İbn Ebû Dâvud Vâiz 2002 and İbn Kuteybe en-Neccâr records, and preserves both Süleymân b. Necâh editions because FN109 and FN373 cite different editions.
- Current body paragraph count is 674; all 469 footnote identities/references, 520 fields, Zotero/ADDIN fields, bookmarks, hyperlinks and RTL structural inventory remain preserved.

## Evidence
- Replay: `work/apply_f4_115.py`
- Candidate: `artifacts/checkpoints/manuscript-working-f4-115.docx`
- SHA: `work/runtime/F4-115-SHA256.txt`
- Preflight: `work/runtime/F4-115-PREFLIGHT.txt`
- Postflight: `work/runtime/F4-115-POSTFLIGHT.txt`
- Technical validation: `work/runtime/F4-115-TECHNICAL-VALIDATION.txt`
- Human visual review: `work/F4-115-VISUAL-QA.md` — 9/9 pages PASS
- Visual workflow: run 32081290071 / artifact 9305200072

## Open HOLDs
none

## Exact next action
Apply only F4-116 against the current durable F4-115 binary. Reconfirm all Ebû Şâme `el-Murşidu’l-vecîz` footnote citations and match short volume/page references to the 1975 Tayyar Altıkulaç and 1993 Velîd Müsâid et-Tabatabâî bibliography editions. Keep 1993; retain 1975 only if current manuscript evidence proves actual use. If short citations cannot be safely edition-resolved from manuscript sequence, HOLD at F4-116. Do not enter FIFTH_APPLY before F4-116 is resolved and FOURTH_VALIDATE passes.
