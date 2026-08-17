# NEXT HANDOFF

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Checkpoint basis HEAD: `a1a1d224abbb83bd2650b28319c566ead4bc1f83` plus this metadata checkpoint commit
- Current phase: `FOURTH_APPLY`

## Resume boundary
- Last completed item: `F4-082`
- Next item: `F4-083`
- DO-NOT-REPEAT: `F4-001`–`F4-082`

## Working manuscript
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-082.docx`
- Current working SHA-256: `299bed4bcf3fa1b479ec1ff1b6ee1baa0f7aa4210dd47f789cdf1f35cc81bbad`
- Last known good DOCX: same path above

## Integrity snapshot
- Footnotes/references: 469/469; orphans/dangling/duplicates: 0/0/0
- Word fields: 520; ADDIN: 466; Zotero: 465 item + 1 bibliography
- Bookmarks: 53/53; hyperlinks: 52; RTL inventory canonical-equal
- Protected OOXML: baseline-identical

## Latest structural state
- F4-073–081 remain intact and validated from prior durable checkpoints.
- F4-082: explicit transition now links the separated historical/normative rasm discussion to the Fourth Section's concrete qiraat-use questions, using an existing safe empty paragraph and preserving all heading/bookmark structures.
- Fourth Section content remains otherwise unchanged; F4-083 is the next substantive opening correction.
- Derived TOC field has not been recalculated; final Word field/TOC refresh is required after editorial application.

## Evidence
- Replay: `work/apply_f4_082.py`
- Candidate: `artifacts/checkpoints/manuscript-working-f4-082.docx`
- Candidate commit: `ed3719283c97f7fff7e00a46803369c9525955af`
- SHA: `work/runtime/F4-082-SHA256.txt`
- Postflight: `work/runtime/F4-082-POSTFLIGHT.txt`
- Technical validation: `work/runtime/F4-082-TECHNICAL-VALIDATION.txt`
- QA PDF: `work/runtime/F4-082-QA.pdf`
- Human visual review: `work/F4-082-VISUAL-QA.md` — 4/4 PASS

## Open HOLDs
none

## Exact next action
Apply F4-083 to the current F4-082 binary. Reframe the opening of Fourth Section 4.1 so rasm is not described as an autonomous source/agent producing or selecting qiraat. Use the report-approved formulation: `Resm-i Osmânî, kırâat rivâyetlerini meydana getiren bağımsız bir kaynak değildir. Bununla birlikte rivâyetle nakledilen okuyuşların müşterek mushaf yazısıyla bağdaşma durumunu göstermesi bakımından tespit ve tahditte kullanılan önemli verilerden biridir. Okuyuşun varlığı ve edâsı rivâyet yoluyla bilinir; resm ise bu okuyuşun Osmânî mushafların yazılı çerçevesi içindeki konumunu değerlendirmeye katkı sağlar.` Preserve source-backed evidence and footnotes; reduce only unnecessary repeated cem/istinsah history where report-approved. Run deterministic replay, technical validation and bounded visual QA. Do not repeat `F4-001`–`F4-082`.
