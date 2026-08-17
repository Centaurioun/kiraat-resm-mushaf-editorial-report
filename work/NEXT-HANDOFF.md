# NEXT HANDOFF

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Checkpoint basis HEAD: `7be56d5640002fca2594b06c891a8ec46cab1c18` plus this metadata checkpoint commit
- Current phase: `FOURTH_APPLY`

## Resume boundary
- Last completed item: `F4-112`
- Next item: `F4-113`
- DO-NOT-REPEAT: `F4-001`–`F4-112`

## Working manuscript
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-112.docx`
- Current working SHA-256: `58e23edd3cdbffbacaf8a2e14fc2dff5ea5357dd76b15cda30c4d31820e12e9a`
- Last known good DOCX: same path above

## Integrity snapshot
- Footnotes/references: 469/469; orphans/dangling/duplicates: 0/0/0
- Word fields: 520; ADDIN: 466; Zotero: 465 item + 1 bibliography
- Bookmarks: 53/53; hyperlinks: 52; RTL inventory canonical-equal
- Protected OOXML: baseline-identical

## Latest structural state
- F4-073–111 remain intact and validated from prior durable checkpoints.
- F4-112: genuine footnotes 32, 41 and 105 now contain only their bibliographic citation text; editor/work notes are removed.
- Current body paragraph count remains 676; all 469 footnote identities/references, 520 fields, bookmarks, hyperlinks and body XML structure remain preserved.
- F4-113+ has not been pre-applied. Derived TOC field remains stale pending final Word refresh.

## Evidence
- Replay: `work/apply_f4_112.py`
- Candidate: `artifacts/checkpoints/manuscript-working-f4-112.docx`
- SHA: `work/runtime/F4-112-SHA256.txt`
- Postflight: `work/runtime/F4-112-POSTFLIGHT.txt`
- Technical validation: `work/runtime/F4-112-TECHNICAL-VALIDATION.txt`
- Human visual review: `work/F4-112-VISUAL-QA.md` — 3/3 real target pages PASS using prefix render

## Open HOLDs
none

## Exact next action
Apply only F4-113 to current F4-112. Inventory author-name article variants and sura-name article variants in genuine footnotes before editing. Normalize author-name house-style forms such as `ez-Zürkânî`, `es-Suyûtî`, `ed-Dânî` to `Zürkânî`, `Suyûtî`, `Dânî` only where they function as author names; do not mechanically strip articles from sura names, work titles or other lexical contexts. Establish and apply one internally consistent sura-name article convention without altering bibliographic titles. Use footnote-specific validation and identity-preserving visual QA. Do not pre-apply F4-114+ or repeat `F4-001`–`F4-112`.
