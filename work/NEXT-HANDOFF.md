# NEXT HANDOFF

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Checkpoint basis HEAD: `0694386d412e3ffc7eb3276ab5fc013eb1aa2eba` plus this metadata checkpoint commit
- Current phase: `FOURTH_APPLY`

## Resume boundary
- Last completed item: `F4-113`
- Next item: `F4-114`
- DO-NOT-REPEAT: `F4-001`–`F4-113`

## Working manuscript
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-113.docx`
- Current working SHA-256: `e4287570d99f9d3c20f96752497787e6d97f6a07047555ecbe5c05e5c69bdac1`
- Last known good DOCX: same path above

## Integrity snapshot
- Footnotes/references: 469/469; orphans/dangling/duplicates: 0/0/0
- Word fields: 520; ADDIN: 466; Zotero: 465 item + 1 bibliography
- Bookmarks: 53/53; hyperlinks: 52; RTL inventory canonical-equal
- Protected OOXML: baseline-identical except explicitly authorized footnote-text changes in `word/footnotes.xml`; target footnote structure unchanged

## Latest structural state
- F4-073–112 remain intact and validated from prior durable checkpoints.
- F4-113: genuine footnote text house style now uses `Dânî`, `Zürkânî`, `Suyûtî` for the targeted author-name variants and an articleless sura-name convention in explicit verified Qur'anic verse references.
- Bibliographic work titles and unrelated article-bearing lexical contexts are preserved; no F4-114 transliteration work has been pre-applied.
- Current body paragraph count remains 676; all 469 footnote identities/references, 520 fields, Zotero/ADDIN fields, bookmarks, hyperlinks and RTL structural inventory remain preserved.

## Evidence
- Replay: `work/apply_f4_113.py`
- Candidate: `artifacts/checkpoints/manuscript-working-f4-113.docx`
- SHA: `work/runtime/F4-113-SHA256.txt`
- Preflight: `work/runtime/F4-113-PREFLIGHT.txt`
- Postflight: `work/runtime/F4-113-POSTFLIGHT.txt`
- Technical validation: `work/runtime/F4-113-TECHNICAL-VALIDATION.txt`
- Human visual review: `work/F4-113-VISUAL-QA.md` — 19/19 pages PASS across three representative slices
- Visual Slice A: run 32079868743 / artifact 9304743549 / 8 pages
- Visual Slice B: run 32080087101 / artifact 9304818453 / 4 pages
- Visual Slice C: run 32080209568 / artifact 9304867454 / 7 pages

## Open HOLDs
none

## Exact next action
Fetch the exact F4-114 item from `final/fourth-report-v2.md`, resolve it against the current durable F4-113 binary, run a read-only preflight, and apply only F4-114 if unambiguous. Do not pre-apply F4-115+ or repeat `F4-001`–`F4-113`.
