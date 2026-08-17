# NEXT HANDOFF

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Checkpoint basis HEAD: `ad255fdf3c4fa7a1c91abac216eafcb6e80e602d` plus this metadata checkpoint commit
- Current phase: `FOURTH_APPLY`

## Resume boundary
- Last completed item: `F4-097`
- Next item: `F4-098`
- DO-NOT-REPEAT: `F4-001`–`F4-097`

## Working manuscript
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-097.docx`
- Current working SHA-256: `9f76e4b8a98a70a8af42a73b261945378c5bd423d94903b4ac20a94b2880f5da`
- Last known good DOCX: same path above

## Integrity snapshot
- Footnotes/references: 469/469; orphans/dangling/duplicates: 0/0/0
- Word fields: 520; ADDIN: 466; Zotero: 465 item + 1 bibliography
- Bookmarks: 53/53; hyperlinks: 52; RTL inventory canonical-equal
- Protected OOXML: baseline-identical

## Latest structural state
- F4-073–096 remain intact and validated from prior durable checkpoints.
- F4-097: rasm reports are now treated as complementary written evidence rather than a constitutive qiraat source.
- F4-098 editor-note/date/attribution corrections in 4.5 remain next and untouched.
- Derived TOC field has not been recalculated; final Word field/TOC refresh remains required after editorial application.

## Evidence
- Replay: `work/apply_f4_097.py`
- Candidate: `artifacts/checkpoints/manuscript-working-f4-097.docx`
- SHA: `work/runtime/F4-097-SHA256.txt`
- Postflight: `work/runtime/F4-097-POSTFLIGHT.txt`
- Technical validation: `work/runtime/F4-097-TECHNICAL-VALIDATION.txt`
- QA PDF: `work/runtime/F4-097-QA.pdf`
- Human visual review: `work/F4-097-VISUAL-QA.md` — 5/5 PASS

## Open HOLDs
none

## Exact next action
Read and apply only F4-098 to the current F4-097 binary. Remove visible work notes, correct first-use death dates exactly as the Fourth Report specifies, and attribute the universal-hikma claim to the relevant authors rather than the book voice. Preserve all affected footnotes/RTL/source material and do not pre-apply F4-099+. Run deterministic replay, technical validation and bounded visual QA. Do not repeat `F4-001`–`F4-097`.
