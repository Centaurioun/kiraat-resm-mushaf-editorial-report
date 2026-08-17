# VALIDATION LOG

## Baseline
Canonical source SHA-256 `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`; footnotes/references 469/469; orphan/dangling/duplicate 0/0/0; fields 520; Zotero 465 item + 1 bibliography; bookmarks 53/53; hyperlinks 52; sections 10; RTL inventory 365. Fourth Report 116 items; Fifth Report 94 items.

## Prior validated boundaries
- F4-001–006: validated, including high-risk F4-006 structural consolidation.
- F4-007–011: replay `86f99b2186711a7d94159d9c1b7413b0248a0c5c`; citation/visual checkpoint PASS.
- F4-012–017: replay `d533b450b20729130e850d7cbf37256a8e192306`; structural/citation checkpoint PASS.
- F4-018–022: replay `7d32131a8681b3334cb405a68f79c2494b8db5e7`; checkpoint PASS.
- F4-023–027: replay `a7e987b2ae84ada927b082974f5d90f4896d43d4`; checkpoint PASS.
- F4-028–032: replay `30bf55f09fa02d4b805d6695c149061f2b24031d`; output SHA `7623dbd834b79effef62991932ec3d506cb7d6e4b77db0c976c495b50a24b127`; 25-page bounded QA PASS.

## F4-033–037 checkpoint — 2026-08-17
- Input: validated F4-032 logical state.
- Durable replay: `work/apply_f4_033_037.py`, commit `58d891d493331863b9f8fdfb0436267a97d33f4e`.
- Durable ledger: `b0faacdd905a2da8b03a758ace888c3534a85102`.
- Output SHA-256: `94bbdeec878f57d4d97f54ad393bddc79074230ec69886e1f0a455bbe483ed3a`.
- Second replay returns F4-033–037 already satisfied and produces exactly the same SHA. **BYTE IDEMPOTENCY PASS**.
- Body paragraphs: **697 → 695** in this batch; baseline 711.
- F4-033: existing safe blank separator before 1.6 converted to the report transition; no protected structure involved.
- F4-034: three consecutive meta-introduction paragraphs consolidated to one direct conceptual paragraph; two true repetitions removed.
- F4-035: source paragraph had genuine footnotes 101/102/103. Rather than delete note 101 with the over-strong Cevherî attribution, its limited source-supported writing-order proposition was retained. Note 102 now follows only Cevherî's lexical `resm` evidence; note 103 follows the statement that technical resm terminology systematizes in Dânî and later resm literature. Cevherî is no longer credited with personally narrating the detailed technical-term history.
- F4-036: genuine footnote 100 remains on the first sentence defining the technical mushaf-ilimleri use of `resm`; the lügavî restart was removed.
- F4-037: Kastallânî is the first current body occurrence, so `(ö. 923/1517)` was retained while its work note was deleted. Bâkıllânî had appeared earlier, so the repeated malformed `(ö. 403/10113 ... )` date/work note was removed. Footnote 105's own embedded editorial note was deliberately not edited under F4-037; F4-112 later governs footnote-only editorial-note cleanup.
- Genuine footnotes/references: **469/469**; exact sets baseline-identical; orphan/dangling/duplicate **0/0/0**.
- Aggregate Word fields: **520/520**; type inventory exact baseline match.
- Zotero: **465 item + 1 bibliography**; RTL **365/365**; bookmarks 53/53; hyperlinks 52; comments/revisions 0/0; sections 10.
- Protected `word/footnotes.xml`, `word/styles.xml`, `word/numbering.xml`, `word/settings.xml`, `word/_rels/document.xml.rels`: exact baseline hashes.
- ZIP/package integrity PASS; all XML/rels parse PASS.
- QA-only first 155 current body paragraphs rendered as **32 pages**. All pages reviewed in contact-sheet form; pages 23–25 and 30–32 inspected full resolution.
- First visual pass found unintended inherited italics over the new F4-035 paragraph because the source paragraph's first run was italic. The replay helper was corrected to reject italic/bold/red/protected template runs; document and render were regenerated. Final affected text is regular black body text.
- No clipping, overlap, footnote overflow, abnormal whitespace, unintended style/color propagation or edit-caused pagination defect after correction.
- Result: **PASS — F4-033–037 CHECKPOINT VALIDATED**.