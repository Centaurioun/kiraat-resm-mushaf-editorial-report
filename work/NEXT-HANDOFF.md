# NEXT HANDOFF

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Checkpoint basis HEAD: `1562e396962bce48ab2c81c6a3c1b8aad70a599e` plus this metadata checkpoint commit
- Current phase: `FOURTH_APPLY`

## Resume boundary
- Last completed item: `F4-099`
- Next item: `F4-100`
- DO-NOT-REPEAT: `F4-001`–`F4-099`

## Working manuscript
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-099.docx`
- Current working SHA-256: `3c3a18fdd19dff05f2bb7e3a03979bc5eb0769085a36b7b2e1c4a61a81d4f8c0`
- Last known good DOCX: same path above

## Integrity snapshot
- Footnotes/references: 469/469; orphans/dangling/duplicates: 0/0/0
- Word fields: 520; ADDIN: 466; Zotero: 465 item + 1 bibliography
- Bookmarks: 53/53; hyperlinks: 52; RTL inventory canonical-equal
- Protected OOXML: baseline-identical

## Latest structural state
- F4-073–098 remain intact and validated from prior durable checkpoints.
- F4-099: a single report-approved historical transition paragraph now bridges classical rasm transmission and the modern print-mushaf section.
- The bookmark-backed 4.6 heading and FN438+ source material remain preserved; F4-100+ has not been pre-applied.
- Derived TOC field has not been recalculated; final Word field/TOC refresh remains required after editorial application.

## Evidence
- Replay: `work/apply_f4_099.py`
- Candidate: `artifacts/checkpoints/manuscript-working-f4-099.docx`
- SHA: `work/runtime/F4-099-SHA256.txt`
- Postflight: `work/runtime/F4-099-POSTFLIGHT.txt`
- Technical validation: `work/runtime/F4-099-TECHNICAL-VALIDATION.txt`
- QA PDF: `work/runtime/F4-099-QA.pdf`
- Human visual review: `work/F4-099-VISUAL-QA.md` — 3/3 PASS

## Open HOLDs
none

## Exact next action
Read and apply only F4-100 to the current F4-099 binary. At the 4.7 opening, replace the claim that the absence of dotting/vocalization in early mushafs was fundamentally a conscious mechanism for preserving multiple qiraat with the report-approved historically cautious formulation. Preserve all affected footnotes/RTL/source material and do not pre-apply F4-101+. Run deterministic replay, technical validation and bounded visual QA. Do not repeat `F4-001`–`F4-099`.
