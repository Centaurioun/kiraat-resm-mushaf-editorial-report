# NEXT HANDOFF

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Checkpoint basis HEAD: `524d765f930ee80cf63898767672149c7206aa4d` plus this metadata checkpoint commit
- Current phase: `FOURTH_APPLY`

## Resume boundary
- Last completed item: `F4-111`
- Next item: `F4-112`
- DO-NOT-REPEAT: `F4-001`–`F4-111`

## Working manuscript
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-111.docx`
- Current working SHA-256: `4c9eba6d4ca9e65dc7148921c8331a21f4768ecc3aed65c9c0deda0ff98166c9`
- Last known good DOCX: same path above

## Integrity snapshot
- Footnotes/references: 469/469; orphans/dangling/duplicates: 0/0/0
- Word fields: 520; ADDIN: 466; Zotero: 465 item + 1 bibliography
- Bookmarks: 53/53; hyperlinks: 52; RTL inventory canonical-equal
- Protected OOXML: baseline-identical

## Latest structural state
- F4-073–110 remain intact and validated from prior durable checkpoints.
- F4-111: main-text house style now uses `Kur’an` and curated specific-name `İmam Mushaf` without altering bibliography, direct quotations, italic work titles or footnotes.
- Current body paragraph count remains 676; all 469 footnote identities, 520 fields, bookmarks and protected OOXML remain preserved.
- F4-112+ has not been pre-applied. Derived TOC field remains stale pending final Word refresh.

## Evidence
- Preflight: `work/runtime/F4-111-PREFLIGHT.txt`
- Replay: `work/apply_f4_111.py`
- Candidate: `artifacts/checkpoints/manuscript-working-f4-111.docx`
- SHA: `work/runtime/F4-111-SHA256.txt`
- Postflight: `work/runtime/F4-111-POSTFLIGHT.txt`
- Technical validation: `work/runtime/F4-111-TECHNICAL-VALIDATION.txt`
- Human visual review: `work/F4-111-VISUAL-QA.md` — 19/19 representative pages PASS

## Open HOLDs
none

## Exact next action
Apply only F4-112 to current F4-111. Remove the surviving editorial/work notes from genuine footnotes 32, 41 and 105 while preserving the bibliographic citation content and the footnote IDs/references. Because `word/footnotes.xml` must change for this accepted item, use a footnote-specific validation that proves only the targeted footnote text changed and all 469 IDs/reference identities, fields, body XML structure and all other protected parts remain intact. Do not pre-apply F4-113+. Run deterministic replay and footnote-aware visual/technical QA. Do not repeat `F4-001`–`F4-111`.
