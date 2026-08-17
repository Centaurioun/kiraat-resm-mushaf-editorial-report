# NEXT HANDOFF

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Checkpoint basis HEAD: `bfc768dcd8af60dcee52ed2944e7720ef1c2e1f2` plus this metadata checkpoint commit
- Current phase: `FOURTH_APPLY`

## Resume boundary
- Last completed item: `F4-091`
- Next item: `F4-092`
- DO-NOT-REPEAT: `F4-001`–`F4-091`

## Working manuscript
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-091.docx`
- Current working SHA-256: `85fe7159297c0d7ca2c477a871af1655571e14fd7b68f44abe7040b7994bb222`
- Last known good DOCX: same path above

## Integrity snapshot
- Footnotes/references: 469/469; orphans/dangling/duplicates: 0/0/0
- Word fields: 520; ADDIN: 466; Zotero: 465 item + 1 bibliography
- Bookmarks: 53/53; hyperlinks: 52; RTL inventory canonical-equal
- Protected OOXML: baseline-identical

## Latest structural state
- F4-073–090 remain intact and validated from prior durable checkpoints.
- F4-091: the Ibn Shanbudh case is no longer reduced to rasm nonconformity alone; FN391 remains attached to the bounded case summary.
- F4-092 begins in the following FN392–393 paragraph and remains pending.
- Derived TOC field has not been recalculated; final Word field/TOC refresh remains required after editorial application.

## Evidence
- Replay: `work/apply_f4_091.py`
- Candidate: `artifacts/checkpoints/manuscript-working-f4-091.docx`
- Candidate commit: `99a3565ce4b027b8a27dfc94c6197967d081b3b9`
- SHA: `work/runtime/F4-091-SHA256.txt`
- Postflight: `work/runtime/F4-091-POSTFLIGHT.txt`
- Technical validation: `work/runtime/F4-091-TECHNICAL-VALIDATION.txt`
- QA PDF: `work/runtime/F4-091-QA.pdf`
- Human visual review: `work/F4-091-VISUAL-QA.md` — 4/4 PASS

## Open HOLDs
none

## Exact next action
Read and apply only F4-092 to the current F4-091 binary. Preserve the F4-091 Ibn Shanbudh paragraph/FN391 and do not collapse later F4-093+ material. Run deterministic replay, technical validation and bounded visual QA. Do not repeat `F4-001`–`F4-091`.
