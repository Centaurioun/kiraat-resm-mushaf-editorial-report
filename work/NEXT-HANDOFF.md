# NEXT HANDOFF

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Checkpoint basis HEAD: `f755fa1188cdb034947f006f9f247a2876f169cb` plus this metadata checkpoint commit
- Current phase: `FOURTH_APPLY`

## Resume boundary
- Last completed item: `F4-095`
- Next item: `F4-096`
- DO-NOT-REPEAT: `F4-001`–`F4-095`

## Working manuscript
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-095.docx`
- Current working SHA-256: `00eae3a5b7299a0522979562d73e1d4bbe52ff7c205ee59c37f09ba3b4b817ea`
- Last known good DOCX: same path above

## Integrity snapshot
- Footnotes/references: 469/469; orphans/dangling/duplicates: 0/0/0
- Word fields: 520; ADDIN: 466; Zotero: 465 item + 1 bibliography
- Bookmarks: 53/53; hyperlinks: 52; RTL inventory canonical-equal
- Protected OOXML: baseline-identical

## Latest structural state
- F4-073–094 remain intact and validated from prior durable checkpoints.
- F4-095: the FN401 imam-preference paragraph now foregrounds received rivayat/teaching and multi-factor evaluation rather than independent selector agency.
- FN402–403 and later 4.4 material remain untouched; F4-096 is next.
- Derived TOC field has not been recalculated; final Word field/TOC refresh remains required after editorial application.

## Evidence
- Replay: `work/apply_f4_095.py`
- Candidate: `artifacts/checkpoints/manuscript-working-f4-095.docx`
- SHA: `work/runtime/F4-095-SHA256.txt`
- Postflight: `work/runtime/F4-095-POSTFLIGHT.txt`
- Technical validation: `work/runtime/F4-095-TECHNICAL-VALIDATION.txt`
- QA PDF: `work/runtime/F4-095-QA.pdf`
- Human visual review: `work/F4-095-VISUAL-QA.md` — 4/4 PASS

## Open HOLDs
none

## Exact next action
Read and apply only F4-096 to the current F4-095 binary. Distinguish meaning/nahw/rivayat-based waqf from rasm-related written cues such as wasl-fasl and word boundaries; preserve source-backed examples and do not pre-apply F4-097+. Run deterministic replay, technical validation and bounded visual QA. Do not repeat `F4-001`–`F4-095`.
