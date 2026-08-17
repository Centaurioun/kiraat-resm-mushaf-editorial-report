# NEXT HANDOFF

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Checkpoint basis HEAD: `82b0a1826956f4c137ef376166c08876d61b6231` plus this metadata checkpoint commit
- Current phase: `FOURTH_APPLY`

## Resume boundary
- Last completed item: `F4-096`
- Next item: `F4-097`
- DO-NOT-REPEAT: `F4-001`–`F4-096`

## Working manuscript
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-096.docx`
- Current working SHA-256: `67791838653b64426378747d1fd4f4a304afe7d38e2c13cf0b7da60972117e41`
- Last known good DOCX: same path above

## Integrity snapshot
- Footnotes/references: 469/469; orphans/dangling/duplicates: 0/0/0
- Word fields: 520; ADDIN: 466; Zotero: 465 item + 1 bibliography
- Bookmarks: 53/53; hyperlinks: 52; RTL inventory canonical-equal
- Protected OOXML: baseline-identical

## Latest structural state
- F4-073–095 remain intact and validated from prior durable checkpoints.
- F4-096: the general waqf framing now separates meaning/nahw/rivayat from specific rasm-related written cues.
- FN413–416 source-backed examples and the 4.5 heading remain unchanged; F4-097 is next.
- The visible Mehdevi work note under 4.5 remains intentionally pending for F4-098.
- Derived TOC field has not been recalculated; final Word field/TOC refresh remains required after editorial application.

## Evidence
- Replay: `work/apply_f4_096.py`
- Candidate: `artifacts/checkpoints/manuscript-working-f4-096.docx`
- SHA: `work/runtime/F4-096-SHA256.txt`
- Postflight: `work/runtime/F4-096-POSTFLIGHT.txt`
- Technical validation: `work/runtime/F4-096-TECHNICAL-VALIDATION.txt`
- QA PDF: `work/runtime/F4-096-QA.pdf`
- Human visual review: `work/F4-096-VISUAL-QA.md` — 4/4 PASS

## Open HOLDs
none

## Exact next action
Read and apply only F4-097 to the current F4-096 binary. Reframe rasm reports as complementary written evidence rather than a constitutive source of qiraat; preserve FN417+ source structure and leave the visible Mehdevi work note/date corrections for F4-098. Run deterministic replay, technical validation and bounded visual QA. Do not repeat `F4-001`–`F4-096`.
