# VALIDATION LOG

## Baseline
Canonical source SHA-256 `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`; footnotes/references 469/469; orphan/dangling/duplicate 0/0/0; fields 520; Zotero 465 item + 1 bibliography; bookmarks 53/53; hyperlinks 52; sections 10; RTL inventory 365. Fourth Report 116 items; Fifth Report 94 items.

## Prior validated boundaries
- F4-001–006: validated, including high-risk F4-006 structural consolidation.
- F4-007–011: replay `86f99b2186711a7d94159d9c1b7413b0248a0c5c`; citation/visual checkpoint PASS.
- F4-012–017: replay `d533b450b20729130e850d7cbf37256a8e192306`; structural/citation checkpoint PASS.
- F4-018–022: replay `7d32131a8681b3334cb405a68f79c2494b8db5e7`; checkpoint PASS.
- F4-023–027: replay `a7e987b2ae84ada927b082974f5d90f4896d43d4`; output SHA `fe24f174ad7826dba8045a2584bc62e1b8a6ced867c8fbf2041da272f8fc3448`; 23-page bounded QA PASS.

## F4-028–032 checkpoint — 2026-08-17
- Input: validated F4-027 logical state.
- Durable replay: `work/apply_f4_028_032.py`, commit `30bf55f09fa02d4b805d6695c149061f2b24031d`.
- Durable ledger: `75a27b5c7be2863ae25b1b37a50a768021fae6c0`.
- Output SHA-256: `7623dbd834b79effef62991932ec3d506cb7d6e4b77db0c976c495b50a24b127`.
- Second replay returns all F4-028–032 targets already satisfied and produces exactly the same SHA. **BYTE IDEMPOTENCY PASS**.
- Body paragraphs: **700 → 697** in this batch; baseline 711.
- F4-028: duplicated second `Hülasa` conclusion replaced with the report's direct transition to the mushaf-count section.
- F4-029: the six-copy certainty was not merely softened locally; the section was made internally consistent. The main certainty paragraph was replaced by the report's cautious multi-rivâyet synthesis, with a limited Kevserî sentence retained because genuine footnote 88 specifically supports that view. Footnote 88 remains immediately after that Kevserî sentence. Three uncited later paragraphs that reasserted the same six-copy certainty/repetition were removed; no unique citation was lost.
- F4-030: Ebû Şâme corrected from `665/1276` to `665/1267`; Ahvâzî death date removed. Existing notes 85/86 retained.
- F4-031: unknown death marker after Amr b. Kays removed; note 87 retained.
- F4-032: opening contemporary-research paragraph replaced by the report-approved non-unified frame, including Hamîdullah `ö. 2002`. The later sentence claiming that six copies had become a shared contemporary consensus was replaced with an explicit statement that the studies differ in criteria and conclusions; notes 94/95 and their source-specific propositions were preserved.
- Genuine footnotes/references: **469/469**; exact sets baseline-identical; orphan/dangling/duplicate **0/0/0**.
- Aggregate Word field instructions: **520/520**; types unchanged (TOC 1; PAGEREF 52; PAGE 1; ADDIN 466).
- Zotero inventory: **465 item + 1 bibliography**.
- RTL inventory: **365/365**. The pre-existing RTL spacer in the footnote-88 paragraph was deliberately preserved rather than silently deleted during reconstruction.
- Bookmarks 53/53; hyperlinks 52; comments/revisions 0/0; sections 10.
- Protected `word/footnotes.xml`, `word/styles.xml`, `word/numbering.xml`, `word/settings.xml`, `word/_rels/document.xml.rels`: exact baseline hashes.
- ZIP/package integrity PASS; all XML/rels parse PASS.
- QA-only first 115 current body paragraphs rendered as **25 pages**. Full contact-sheet scan completed; pages 20–25 inspected full resolution, including the F4-028 transition, Ebû Şâme/Amr b. Kays passages, footnote-88 synthesis, contemporary-literature frame and section boundary.
- No clipping, overlap, footnote overflow, unintended red/font/style propagation or edit-caused pagination defect. Existing red editorial notes are inherited source content and remain for later report items.
- Result: **PASS — F4-028–032 CHECKPOINT VALIDATED**.