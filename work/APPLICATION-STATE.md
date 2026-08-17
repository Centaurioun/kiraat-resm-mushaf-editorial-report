# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint commit: `SELF` — resolve as the branch HEAD containing this state file
- Checkpoint parent HEAD: `90f473c52b404507eb0ccbb5928d65ccfa179f34`
- Source commit: `b7633f23aa67d26e77da50f56ba4f24e2b1b1518`
- Source manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Source manuscript Git blob: `afb77260a59c4eabf5664dd1919c03fc68cc5196`
- Fourth Report: `final/fourth-report-v2.md` — **116 items**
- Fourth Report blob verified unchanged: `e880124fb0bdb72afb29cf10927e2dd15bae0676`
- Fifth Report: `final/fifth-report-locked.md` — **94 items**
- Fifth Report blob verified unchanged: `b2e184bf45c13fb548cd13ee2e4f829a52b4bb69`

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: `F4-006`
- Next Fourth Report item: `F4-007`
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (blocked)

## Working / recovery
- Current logical working DOCX: deterministic output of `work/apply_docx_edits.py` applied to the canonical source
- Current working SHA-256 through F4-006: `33743240d3bd6e1f5eda2efabf8ef5dfa66cbec9a5f655923206563ab605bb93`
- Current working body paragraph count: **705** (baseline 711)
- Last known good reproducible edited-state commit: `dd41275b91dfaa7dffce0cb43e7b5e823db73756`
- Last known good logical DOCX: replay output SHA-256 `33743240d3bd6e1f5eda2efabf8ef5dfa66cbec9a5f655923206563ab605bb93`
- Last persisted DOCX binary in GitHub: `artifacts/checkpoints/manuscript-working-bootstrap.docx`
- Last persisted binary commit: `026fe5d382d51a6c31b489a89498946d545587f4`
- Binary persistence note: current GitHub connector exposes blob creation only from literal UTF-8/base64 content and does not accept a local-file reference for the edited DOCX. No false claim of edited-binary persistence is made; deterministic replay + exact hashes + ledger + validation remain the durable recovery route.
- Replay idempotency through F4-006: **PASS, byte-identical**; rerun SHA-256 remains `33743240d3bd6e1f5eda2efabf8ef5dfa66cbec9a5f655923206563ab605bb93` and F4-001–006 all report already satisfied.

## Footnotes
- Baseline/current genuine footnotes: **469 / 469**
- Baseline/current body references: **469 / 469**
- Genuine footnote ID set: unchanged
- Body reference ID set: unchanged
- Orphans: **0**
- Dangling references: **0**
- Duplicate references: **0**
- `word/footnotes.xml`: byte-hash unchanged from baseline
- F4-003: footnote 2 retained
- F4-004: footnote 3 retained
- F4-006: footnote 7 retained with the preserved source-backed paragraph beginning `Çalışmanın son halkasında...`

## Word / Zotero / OOXML
- Word field instructions baseline/current: **520 / 520**
- TOC 1; PAGEREF 52; REF 0; PAGE 1; ADDIN 466
- Zotero item fields 465; Zotero bibliography fields 1
- Aggregate field-instruction hash unchanged
- Bookmarks: 53 starts / 53 ends
- Hyperlinks: 52
- Comments: 0
- Tracked revisions: 0
- Sections: 10
- Arabic/RTL inventory unchanged
- ZIP/package integrity: **PASS**
- XML parse integrity: **PASS**
- Protected core OOXML unchanged except expected `word/document.xml`

## Completed edits
- F4-001: VERIFIED
- F4-002: VERIFIED
- F4-003: VERIFIED
- F4-004: VERIFIED
- F4-005: VERIFIED
- F4-006: STRUCTURALLY_APPLIED + checkpoint validation PASS
- F4-006 structural effect: in the former 12-paragraph Giriş cluster, replaced the scope/contribution/plan shells with the accepted three-paragraph consolidation; removed six true repetition/superseded plan paragraphs; preserved three unique source-backed paragraphs byte-for-text, including footnote 7.
- Current structural-edit state: Giriş structural consolidation completed; downstream positional assumptions invalidated and must be re-located from CURRENT DOCX.
- Open HOLD items: none

## Visual QA
- Full-document PDF export remains a baseline renderer problem shared by the untouched source; this does not waive final all-page acceptance.
- F4-006 bounded QA slice: current body paragraphs 0–59 rendered as **14 pages**.
- Visual inspection: **14/14 pages inspected**; no clipping, overlap, footnote overflow, abnormal whitespace caused by F4-006, unexpected font change, or pagination defect in the affected range.
- The QA slice is QA-only and is never used as manuscript source.

- Last validation result: **PASS — F4-006 technical + idempotency + 14/14-page bounded visual QA**
- DO-NOT-REPEAT: bootstrap and F4-001–006
- Exact next action: re-locate `F4-007` from the CURRENT F4-006 document, inspect its paragraph and any F5 overlap, apply the accepted Giriş transition replacement only if uniquely and safely resolved, then continue in bounded validated units.
