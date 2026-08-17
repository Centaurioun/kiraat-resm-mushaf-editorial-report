# VALIDATION LOG

## Bootstrap baseline — 2026-08-17
Source SHA-256 `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`; ZIP/XML PASS; genuine footnotes/references 469/469; orphans/dangling/duplicates 0/0/0; fields 520; TOC 1; PAGEREF 52; PAGE 1; ADDIN 466; Zotero item 465 + bibliography 1; bookmarks 53/53; hyperlinks 52; comments/revisions 0; sections 10; F4 count 116; F5 count 94. Result **PASS**.

## Bootstrap persistence — 2026-08-17
Commit `026fe5d382d51a6c31b489a89498946d545587f4`; recovery DOCX equals canonical source blob. Result **PASS**.

## F4-001–003 — 2026-08-17
Replay commit `46a5014e1c87bce2bceda20278481055975ccb39`; reconstructed SHA `40504b9d5b41ecae0ae9db64add341f37105e7bae1e8c0c164439ef3078fb5da`; footnotes/fields/Zotero/protected OOXML preserved; 12-page bounded QA slice inspected 12/12, including footnote 2. Verification commit `551ae04f8be22d979432011d99d1c81ccbabf8be`. Result **PASS**.

## F4-004–005 technical — 2026-08-17
- F4-004 current paragraph index 23: target sentence replaced only; genuine footnote 3 and all surrounding paragraph content preserved.
- F4-005 current paragraph index 24: target final sentence replaced only.
- Current SHA-256: `567f7847958364b27d68c45c073481c9d7e6030bba561d7d0dc011d8c0cf6355`
- ZIP/XML: **PASS/PASS**
- Footnotes/references: **469/469**; sets unchanged; orphans/dangling/duplicates 0/0/0
- `word/footnotes.xml`: unchanged from baseline
- Word fields and field types: exact baseline match; Zotero 465 + 1 unchanged
- Bookmarks/hyperlinks/comments/revisions/sections/Arabic/RTL: unchanged
- Protected core OOXML unchanged except expected `word/document.xml`
- Replay script commit: `8ba3fe378240d3d42e0c62b0cc7e9936c907bdf8`
- Replay on already-correct F4-001–005 DOCX returns all items `ALREADY_SATISFIED` and produces byte-identical SHA: **IDEMPOTENCY PASS**

## F4-004–005 visual — 2026-08-17
- QA-only slice: body paragraphs 0–59, 12 rendered pages.
- Pages 1–4 and 10–12: pixel-hash unchanged from prior validated slice.
- Pages 5–9: reflowed and individually visually inspected; no clipping, overlap, footnote overflow, abnormal whitespace or unexpected formatting caused by edits.
- Page 5: F4-004 replacement clean; footnote 3 marker/text preserved.
- Page 6: F4-005 replacement clean.
- Result: **PASS**.

## F4-006 high-risk structural checkpoint — 2026-08-17
- Application/recovery replay commit: `dd41275b91dfaa7dffce0cb43e7b5e823db73756`.
- Ledger recording commit: `90f473c52b404507eb0ccbb5928d65ccfa179f34`.
- Pre-F4-006 verified input SHA-256: `567f7847958364b27d68c45c073481c9d7e6030bba561d7d0dc011d8c0cf6355` — exact match to F4-001–005 state.
- F4-006 output SHA-256: `33743240d3bd6e1f5eda2efabf8ef5dfa66cbec9a5f655923206563ab605bb93`.
- Replay on F4-006 output: F4-001–006 all already satisfied; rerun output SHA identical (`33743240d3bd6e1f5eda2efabf8ef5dfa66cbec9a5f655923206563ab605bb93`). **IDEMPOTENCY PASS**.
- Body paragraphs: **711 baseline → 705 current**.
- Accepted three F4-006 replacement paragraphs each occur exactly once.
- Removed only six true repetition/superseded detailed-plan paragraphs from the former contiguous Giriş cluster.
- Preserved unique paragraphs beginning `Çalışmanın son halkasında...`, `Yöntem bakımından kitap...`, and `Araştırmanın kaynak zemini...`; normalized text hashes are exactly unchanged versus F4-005.
- Genuine footnotes/references: **469/469**; exact ID/reference sets unchanged.
- Orphans/dangling/duplicates: **0/0/0**.
- Footnote 7 remains in the preserved `Çalışmanın son halkasında...` paragraph and retains its semantic attachment.
- `word/footnotes.xml`: byte-hash unchanged from canonical baseline.
- Word field instructions: **520/520**; TOC 1; PAGEREF 52; REF 0; PAGE 1; ADDIN 466.
- Zotero item fields: **465**; bibliography field: **1**; aggregate field-instruction hash unchanged.
- `word/styles.xml`, `word/numbering.xml`, `word/settings.xml`, `word/_rels/document.xml.rels`: exact baseline hashes; only expected `word/document.xml` changed among protected core parts.
- ZIP/package integrity: **PASS**.
- XML parse integrity: **PASS**.
- Canonical source rechecked: SHA-256 `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`; Git blob `afb77260a59c4eabf5664dd1919c03fc68cc5196` unchanged.
- Fourth Report blob on application branch equals source-commit blob: `e880124fb0bdb72afb29cf10927e2dd15bae0676`.
- Fifth Report blob on application branch equals source-commit blob: `b2e184bf45c13fb548cd13ee2e4f829a52b4bb69`.
- Bounded QA-only slice: CURRENT body paragraphs 0–59 rendered successfully as **14 pages**.
- Visual inspection: **14/14 pages inspected**. F4-006 consolidation appears clean on pages 8–9; footnote 7 marker and note text render normally; no clipping, overlap, footnote overflow, unexpected font changes or structural pagination defect caused by this edit. Existing red editorial markings elsewhere in the source are not F4-006 defects and remain for later accepted report items.
- Full-document PDF export remains a baseline renderer issue shared by the untouched source; final all-page visual acceptance remains mandatory.
- Edited binary persistence: current GitHub connector has no local-file parameter for binary DOCX upload; no false binary-persistence claim is made. Deterministic replay, exact output hash, ledger, state and validation evidence are durable.
- Result: **PASS — F4-006 STRUCTURAL CHECKPOINT VALIDATED**.
