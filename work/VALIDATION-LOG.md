# VALIDATION LOG

## Bootstrap baseline — 2026-08-17
- Source commit: `b7633f23aa67d26e77da50f56ba4f24e2b1b1518`
- Source DOCX SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Canonical Git blob SHA-1 cross-check: **PASS** (`afb77260a59c4eabf5664dd1919c03fc68cc5196`)
- ZIP/XML: **PASS/PASS**
- Footnotes/references: **469/469**, orphans 0, dangling 0, duplicates 0
- Fields: 520 total; TOC=1; PAGEREF=52; PAGE=1; ADDIN=466; Zotero item=465; bibliography=1
- Bookmarks 53/53; hyperlinks 52; comments 0; tracked revisions 0; sections 10
- Fourth Report accounting: 116; Fifth Report accounting: 94
- Result: **PASS**

## Bootstrap persistence checkpoint — 2026-08-17
- Commit: `026fe5d382d51a6c31b489a89498946d545587f4`
- Branch push: **PASS**
- Ledger boundary verification: `F4-116` followed by `F5-001`; terminal `F5-094` present
- Recovery DOCX blob equals canonical source blob: **PASS**
- Result: **PASS**

## F4-001–003 technical application — 2026-08-17
- Reproducible script: `work/apply_docx_edits.py`
- Expected reconstructed SHA-256: `40504b9d5b41ecae0ae9db64add341f37105e7bae1e8c0c164439ef3078fb5da`
- F4-001: APPLIED to uniquely resolved Önsöz paragraph
- F4-002: APPLIED to uniquely resolved Önsöz closing paragraph
- F4-003: APPLIED to uniquely resolved Giriş historical paragraph
- F4-003 footnote ID 2 preserved as a genuine Word footnote reference at the end of the rewritten supported claim
- ZIP integrity: **PASS**
- XML parse integrity: **PASS**
- Genuine footnotes/references: **469/469**
- Footnote ID/reference sets: **exact match to baseline**
- Normalized footnote text hashes: **exact match to baseline**
- Orphans/dangling/duplicates: **0/0/0**
- Field count/types/instruction hashes: **exact match to baseline**
- Zotero: **465 item + 1 bibliography**, unchanged
- Bookmarks, hyperlinks, comments, tracked revisions, section structure, Arabic/RTL: **unchanged**
- Protected OOXML parts unchanged: `word/footnotes.xml`, `word/styles.xml`, `word/numbering.xml`, `word/settings.xml`, `word/_rels/document.xml.rels`, footer/customXml related parts
- Expected changed part: `word/document.xml`
- Canonical source SHA-256 rechecked unchanged: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Render QA: **PENDING**. `render_docx.py`/LibreOffice conversion also hangs on the untouched canonical source, so no edit-specific visual failure is inferred and no item is marked VERIFIED from this evidence alone.
- Result: **TECHNICAL PASS; VISUAL PENDING**
