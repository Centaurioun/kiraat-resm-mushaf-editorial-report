# NEXT HANDOFF

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Checkpoint basis HEAD: `347545c6f74a5b9c55e39fc8d19d2914b7c00035` plus this metadata checkpoint commit
- Current phase: `FOURTH_APPLY`

## Resume boundary
- Last completed item: `F4-087`
- Next item: `F4-088`
- DO-NOT-REPEAT: `F4-001`–`F4-087`

## Working manuscript
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-087.docx`
- Current working SHA-256: `cedcc233e5e3ce9150f3ebbd66b199075517dcac4a7d771a455a03db5e16a3ce`
- Last known good DOCX: same path above

## Integrity snapshot
- Footnotes/references: 469/469; orphans/dangling/duplicates: 0/0/0
- Word fields: 520; ADDIN: 466; Zotero: 465 item + 1 bibliography
- Bookmarks: 53/53; hyperlinks: 52; RTL inventory canonical-equal
- Protected OOXML: baseline-identical

## Latest structural state
- F4-073–086 remain intact and validated from prior durable checkpoints.
- F4-087: the open inline editor note in the FN377–378 paragraph has been removed without moving citations or Arabic runs.
- F4-088 active-agent/curatorial-authority wording in 4.2 is next; F4-089 Ibn Masud intent language remains pending.
- Derived TOC field has not been recalculated; final Word field/TOC refresh is required after editorial application.

## Evidence
- Replay: `work/apply_f4_087.py`
- Candidate: `artifacts/checkpoints/manuscript-working-f4-087.docx`
- Candidate commit: `a49959ebcc7cf55aece1874636838e083da536af`
- SHA: `work/runtime/F4-087-SHA256.txt`
- Postflight: `work/runtime/F4-087-POSTFLIGHT.txt`
- Technical validation: `work/runtime/F4-087-TECHNICAL-VALIDATION.txt`
- QA PDF: `work/runtime/F4-087-QA.pdf`
- Human visual review: `work/F4-087-VISUAL-QA.md` — 4/4 PASS

## Open HOLDs
none

## Exact next action
Apply F4-088 to the current F4-087 binary. Replace the 4.2 sentence that makes `Osmânî resm` an active selecting/curatorial authority with the report-approved distinction: the Uthmanic recension and subsequent common mushaf acceptance form the determining historical framework, while rasm is one written criterion for evaluating whether transmitted material accords with the common mushaf. Preserve surrounding source-backed paragraphs and footnotes; do not resolve F4-089 prematurely. Run deterministic replay, technical validation and bounded visual QA. Do not repeat `F4-001`–`F4-087`.
