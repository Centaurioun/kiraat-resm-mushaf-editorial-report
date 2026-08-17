# VALIDATION LOG

## Bootstrap baseline — 2026-08-17
- Source commit: `b7633f23aa67d26e77da50f56ba4f24e2b1b1518`
- Source DOCX SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Canonical Git blob SHA-1: `afb77260a59c4eabf5664dd1919c03fc68cc5196`
- ZIP/XML: **PASS/PASS**
- Footnotes/references: **469/469**, orphans 0, dangling 0, duplicates 0
- Fields: 520 total; TOC=1; PAGEREF=52; PAGE=1; ADDIN=466; Zotero item=465; bibliography=1
- Bookmarks 53/53; hyperlinks 52; comments 0; tracked revisions 0; sections 10
- Fourth Report accounting: 116; Fifth Report accounting: 94
- Result: **PASS**

## Bootstrap persistence checkpoint — 2026-08-17
- Commit: `026fe5d382d51a6c31b489a89498946d545587f4`
- Branch push: **PASS**
- Ledger boundary: F4-001..F4-116 + F5-001..F5-094, 210 records
- Recovery DOCX blob equals canonical source blob: **PASS**
- Result: **PASS**

## F4-001–003 technical application — 2026-08-17
- Reproducible script commit: `46a5014e1c87bce2bceda20278481055975ccb39`
- Reconstructed working SHA-256: `40504b9d5b41ecae0ae9db64add341f37105e7bae1e8c0c164439ef3078fb5da`
- F4-001: authoritative Önsöz paragraph replacement
- F4-002: authoritative Önsöz closing paragraph replacement
- F4-003: authoritative Giriş historical paragraph replacement; genuine footnote ID 2 preserved at the supported rewritten claim
- ZIP/XML: **PASS/PASS**
- Genuine footnotes/references: **469/469**; exact ID/reference sets unchanged
- Normalized footnote text hashes: exact baseline match
- Orphans/dangling/duplicates: **0/0/0**
- Field counts/types/instruction hashes: exact baseline match
- Zotero 465 item + 1 bibliography: unchanged
- Bookmarks/hyperlinks/comments/revisions/sections/Arabic/RTL: unchanged
- Protected OOXML parts unchanged except expected `word/document.xml`
- Canonical source SHA rechecked unchanged
- Technical result: **PASS**

## F4-001–003 visual validation — 2026-08-17
- Full-document direct PDF export: **environment/baseline failure**; the untouched canonical DOCX exhibits the same LibreOffice PDF-export hang.
- Diagnostic: DOCX→ODT succeeds; PDF export hangs both directly and from ODT.
- Safe workaround: `work/slice_docx_for_qa.py` created a temporary QA-only slice of current body paragraphs 0–59; the manuscript source and working package were not rebuilt from this slice.
- QA slice render: **PASS**, 12 pages.
- Pages visually inspected: **12/12**.
- F4-001 new Önsöz paragraph: visually clean.
- F4-002 new Önsöz closing paragraph: visually clean.
- F4-003 new Giriş paragraph: visually clean; superscript footnote 2 remains at the new paragraph end; footnote text continues normally; no clipping/overlap.
- No abnormal whitespace, unexpected font changes, orphan headings or footnote overflow attributable to F4-001–003.
- Ledger status F4-001–003: **VERIFIED**.
- Result: **PASS for the affected rendered range**. Full-document all-page visual acceptance remains mandatory at FINAL_VALIDATE.
