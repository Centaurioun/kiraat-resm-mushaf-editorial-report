# NEXT HANDOFF

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Checkpoint basis HEAD: `df5fb58e683ae258e7e8b2eecee27287c2b3c7ea` plus this metadata checkpoint commit
- Current phase: `FOURTH_APPLY`

## Resume boundary
- Last completed item: `F4-114`
- Next item: `F4-115`
- DO-NOT-REPEAT: `F4-001`–`F4-114`

## Working manuscript
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-114.docx`
- Current working SHA-256: `419bc27be6a259d03f42ed7da7f7bbf0b1f64c9af3ab6ed78393f6aa9a96ca56`
- Last known good DOCX: same path above

## Integrity snapshot
- Footnotes/references: 469/469; orphans/dangling/duplicates: 0/0/0
- Word fields: 520; ADDIN: 466; Zotero: 465 item + 1 bibliography
- Bookmarks: 53/53; hyperlinks: 52; RTL inventory canonical-equal
- Protected OOXML: baseline-identical except explicitly authorized footnote-text changes inherited from F4-112/F4-113; F4-114 changes only bibliography result text in `word/document.xml`

## Latest structural state
- F4-073–113 remain intact and validated from prior durable checkpoints.
- F4-114: Kahraman bibliography record no longer carries the malformed DOI URL; Maşalı bibliography DOI is `https://doi.org/10.56361/usul.173700` with one DOI prefix.
- F4-114 changed only visible bibliography result text at P578 and P599; Word/Zotero field instructions and hyperlink structures remain preserved.
- Current body paragraph count remains 676; all 469 footnote identities/references, 520 fields, Zotero/ADDIN fields, bookmarks, hyperlinks and RTL structural inventory remain preserved.

## Evidence
- Replay: `work/apply_f4_114.py`
- Candidate: `artifacts/checkpoints/manuscript-working-f4-114.docx`
- SHA: `work/runtime/F4-114-SHA256.txt`
- Preflight: `work/runtime/F4-114-PREFLIGHT.txt`
- Postflight: `work/runtime/F4-114-POSTFLIGHT.txt`
- Technical validation: `work/runtime/F4-114-TECHNICAL-VALIDATION.txt`
- Human visual review: `work/F4-114-VISUAL-QA.md` — 4/4 pages PASS
- Visual workflow: run 32080808433 / artifact 9305055721

## Open HOLDs
none

## Exact next action
Apply only F4-115 against the current durable F4-114 binary. First verify the exact report-prescribed edition-use decisions against current footnote and bibliography evidence: keep İbn Ebû Dâvud 2002 and remove unused 2006; retain both Süleymân b. Necâh 2000 and 1999 because both are cited; keep İbn Kuteybe en-Neccâr record and remove unused 1999 el-Asfar record. Do not pre-apply F4-116 or repeat `F4-001`–`F4-114`.
