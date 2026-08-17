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

Full-document PDF export remains a baseline LibreOffice issue shared by untouched source; final all-page acceptance is still required.
