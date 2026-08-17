# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Source commit verified to contain all authoritative inputs: `b7633f23aa67d26e77da50f56ba4f24e2b1b1518`

## Authoritative sources
- Source manuscript path: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Source manuscript Git blob SHA-1: `afb77260a59c4eabf5664dd1919c03fc68cc5196`
- Canonical source remains unmodified.
- Fourth Report path: `final/fourth-report-v2.md`
- Fourth Report parsed item count: **116**
- Fifth Report path: `final/fifth-report-locked.md`
- Fifth Report parsed item count: **94**

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: `F4-003`
- Next Fourth Report item: `F4-004`
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (blocked until Fourth Report validation passes)

## Working document / recovery
- Current logical working DOCX: reconstruct from `artifacts/checkpoints/manuscript-working-bootstrap.docx` with `work/apply_docx_edits.py`.
- Reconstructed F4-001–003 SHA-256: `40504b9d5b41ecae0ae9db64add341f37105e7bae1e8c0c164439ef3078fb5da`
- Last known good commit with persisted DOCX binary: `026fe5d382d51a6c31b489a89498946d545587f4`
- Last known good DOCX binary: `artifacts/checkpoints/manuscript-working-bootstrap.docx`
- Last known good reproducible application commit: `46a5014e1c87bce2bceda20278481055975ccb39`
- Binary transport limitation: current GitHub connector does not expose a local-file upload route for the edited DOCX. No false binary-persistence claim is made; deterministic replay script, hashes, ledger, validation and handoff are persisted.

## Footnote state after F4-001–003
- Baseline/current genuine footnotes: **469 / 469**
- Baseline/current body references: **469 / 469**
- Genuine footnote ID/reference sets: unchanged
- Normalized footnote text hashes: unchanged
- Orphan footnotes: **0**
- Dangling references: **0**
- Duplicate references: **0**
- F4-003 affected footnote ID: **2**, reference remains attached to the rewritten historical paragraph.

## Word / Zotero / OOXML state after F4-001–003
- Word field instructions: **520 / 520**, exact instruction hashes unchanged
- TOC 1; PAGEREF 52; PAGE 1; ADDIN 466
- Zotero item fields 465; bibliography field 1
- Bookmarks/hyperlinks/comments/tracked revisions/sections unchanged
- Arabic/RTL inventory unchanged
- `word/document.xml`: expected changed part
- `word/footnotes.xml`, `word/styles.xml`, `word/numbering.xml`, `word/settings.xml`, `word/_rels/document.xml.rels`: unchanged
- ZIP/package integrity: **PASS**
- XML parse integrity: **PASS**

## Editing / validation state
- `F4-001`: `VERIFIED`
- `F4-002`: `VERIFIED`
- `F4-003`: `VERIFIED`
- Visual QA: full-document PDF export hangs identically on untouched canonical source. A temporary QA-only paragraph slice (body paragraphs 0–59) from the validated current package rendered successfully to **12 pages**, and **12/12 pages were visually inspected**. No clipping, overlap, font anomaly or footnote-placement defect was found; footnote 2 is visible at the end of the new F4-003 paragraph and its footnote text flows normally.
- Current structural-edit state: no heading/section movement or numbering change yet.
- Open HOLD items: none
- Last validation result: **PASS — F4-001–003 technical + 12/12 relevant-slice visual QA**
- Exact next action: apply `F4-004` against the CURRENT reconstructed document using a targeted in-paragraph replacement that preserves footnote 3 and all surrounding content; then apply `F4-005`, validate, checkpoint, and only then begin high-risk `F4-006` structural consolidation.
