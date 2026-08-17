# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Source commit: `b7633f23aa67d26e77da50f56ba4f24e2b1b1518`
- Source manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Source manuscript Git blob: `afb77260a59c4eabf5664dd1919c03fc68cc5196`
- Fourth Report: `final/fourth-report-v2.md` — **116 items**
- Fifth Report: `final/fifth-report-locked.md` — **94 items**

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: `F4-005`
- Next Fourth Report item: `F4-006`
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (blocked)

## Working / recovery
- Current logical working DOCX: generated from canonical source by `work/apply_docx_edits.py`
- Current working SHA-256 through F4-005: `567f7847958364b27d68c45c073481c9d7e6030bba561d7d0dc011d8c0cf6355`
- Last known good persisted DOCX binary: `artifacts/checkpoints/manuscript-working-bootstrap.docx`
- Last known good binary commit: `026fe5d382d51a6c31b489a89498946d545587f4`
- Last known good reproducible edited-state commit: `8ba3fe378240d3d42e0c62b0cc7e9936c907bdf8`
- Replay idempotency: **PASS, byte-identical** when rerun on the F4-001–005 desired state.
- Connector limitation: edited local DOCX binary cannot be uploaded through the current GitHub connector; replay script + hashes + ledger + validation are persisted instead. No false binary-persistence claim is made.

## Footnotes
- Baseline/current genuine footnotes: **469 / 469**
- Baseline/current body references: **469 / 469**
- ID/reference sets: unchanged
- Orphans: **0**
- Dangling references: **0**
- Duplicate references: **0**
- `word/footnotes.xml`: byte-hash unchanged from baseline
- F4-003: footnote 2 retained with rewritten claim
- F4-004: footnote 3 remains intact in the edited paragraph

## Word / Zotero / OOXML
- Word field instructions: **520 / 520**
- TOC 1; PAGEREF 52; PAGE 1; ADDIN 466
- Zotero item fields 465; bibliography 1
- Field instruction hashes unchanged
- Bookmarks/hyperlinks/comments/revisions/sections unchanged
- Arabic/RTL inventory unchanged
- ZIP/package integrity: **PASS**
- XML parse integrity: **PASS**
- Only `word/document.xml` changed among the protected core parts.

## Completed edits
- F4-001: VERIFIED
- F4-002: VERIFIED
- F4-003: VERIFIED
- F4-004: VERIFIED — targeted sentence-level replacement; footnote 3 preserved
- F4-005: VERIFIED — targeted final-sentence replacement
- Current structural-edit state: no section/heading movement yet
- Open HOLD items: none

## Visual QA
- Full-document PDF export hangs identically on untouched canonical source.
- Bounded QA slice body paragraphs 0–59 renders successfully as 12 pages.
- F4-004/005 batch: pages 1–4 and 10–12 pixel-hash unchanged; reflowed pages 5–9 visually inspected individually and PASS.
- Full all-page visual acceptance remains mandatory at FINAL_VALIDATE.

- Last validation result: **PASS — F4-001–005**
- Exact next action: inspect the three F4-006 anchor paragraphs and all intervening paragraphs/footnotes in the CURRENT document; implement the accepted three-paragraph consolidation structurally without losing unique sourced material or citation placement; checkpoint immediately after F4-006.
