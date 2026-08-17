# NEXT HANDOFF

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Checkpoint basis HEAD: `dec9b20712554b3adaa87936d0406c51328ca64b` plus this metadata checkpoint commit
- Current phase: `FOURTH_APPLY`

## Resume boundary
- Last completed item: `F4-086`
- Next item: `F4-087`
- DO-NOT-REPEAT: `F4-001`–`F4-086`

## Working manuscript
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-086.docx`
- Current working SHA-256: `2d7e6dc15e60c4b85db6de9459cc5bdd24f41da98f77577d17871e68d477826c`
- Last known good DOCX: same path above

## Integrity snapshot
- Footnotes/references: 469/469; orphans/dangling/duplicates: 0/0/0
- Word fields: 520; ADDIN: 466; Zotero: 465 item + 1 bibliography
- Bookmarks: 53/53; hyperlinks: 52; RTL inventory canonical-equal
- Protected OOXML: baseline-identical

## Latest structural state
- F4-073–085 remain intact and validated from prior durable checkpoints.
- F4-086: 4.2 now carries an explicit category-differentiation synthesis without displacing source-specific examples or citations.
- F4-087 open editor note remains next; F4-088 active-agent wording remains pending.
- Derived TOC field has not been recalculated; final Word field/TOC refresh is required after editorial application.

## Evidence
- Replay: `work/apply_f4_086.py`
- Candidate: `artifacts/checkpoints/manuscript-working-f4-086.docx`
- Candidate commit: `0ac7c7dc0c2b6c0e07ceab8987c8aed0e4b23896`
- SHA: `work/runtime/F4-086-SHA256.txt`
- Postflight: `work/runtime/F4-086-POSTFLIGHT.txt`
- Technical validation: `work/runtime/F4-086-TECHNICAL-VALIDATION.txt`
- QA PDF: `work/runtime/F4-086-QA.pdf`
- Human visual review: `work/F4-086-VISUAL-QA.md` — 5/5 PASS

## Open HOLDs
none

## Exact next action
Apply F4-087 to the current F4-086 binary by removing only the explicit parenthetical editor note embedded in the FN377–378 paragraph and restoring normal spacing before `Bunun en meşhur örneklerinden biri...`. Preserve Arabic runs, FN377–378 and all surrounding text. Run deterministic replay, technical validation and bounded visual QA. Do not repeat `F4-001`–`F4-086`.
