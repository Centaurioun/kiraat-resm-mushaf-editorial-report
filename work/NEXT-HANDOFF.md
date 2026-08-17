# NEXT HANDOFF

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Checkpoint basis HEAD: `4a43d0c24cac51c6f5b927829057b362c9e55b61` plus this metadata checkpoint commit
- Current phase: `FOURTH_APPLY`

## Resume boundary
- Last completed item: `F4-094`
- Next item: `F4-095`
- DO-NOT-REPEAT: `F4-001`–`F4-094`

## Working manuscript
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-094.docx`
- Current working SHA-256: `523fcf36cae029c4761e254a378beda7f378499ed8a0b13bcf0371cd83079894`
- Last known good DOCX: same path above

## Integrity snapshot
- Footnotes/references: 469/469; orphans/dangling/duplicates: 0/0/0
- Word fields: 520; ADDIN: 466; Zotero: 465 item + 1 bibliography
- Bookmarks: 53/53; hyperlinks: 52; RTL inventory canonical-equal
- Protected OOXML: baseline-identical

## Latest structural state
- F4-073–093 remain intact and validated from prior durable checkpoints.
- F4-094: the bookmark-backed 4.4 heading now uses the report-approved relationship wording rather than one-way causal 'effect' language.
- FN400+ 4.4 opening material remains source-backed and unchanged; F4-095 is next.
- Derived TOC field has not been recalculated; final Word field/TOC refresh remains required after editorial application.

## Evidence
- Replay: `work/apply_f4_094.py`
- Candidate: `artifacts/checkpoints/manuscript-working-f4-094.docx`
- SHA: `work/runtime/F4-094-SHA256.txt`
- Postflight: `work/runtime/F4-094-POSTFLIGHT.txt`
- Technical validation: `work/runtime/F4-094-TECHNICAL-VALIDATION.txt`
- QA PDF: `work/runtime/F4-094-QA.pdf`
- Human visual review: `work/F4-094-VISUAL-QA.md` — 4/4 PASS

## Open HOLDs
none

## Exact next action
Read and apply only F4-095 to the current F4-094 binary. Preserve the F4-094 bookmark-backed heading and all source-backed material except where F4-095 explicitly narrows the portrayal of qiraat imams as selectors. Run deterministic replay, technical validation and bounded visual QA. Do not repeat `F4-001`–`F4-094`.
