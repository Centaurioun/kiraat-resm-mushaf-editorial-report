# VALIDATION LOG

## Baseline
Canonical source SHA-256 `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`; footnotes/references 469/469; orphan/dangling/duplicate 0/0/0; fields 520; Zotero 465 item + 1 bibliography; bookmarks 53/53; hyperlinks 52; sections 10; RTL inventory 365. Fourth Report 116 items; Fifth Report 94 items.

## Prior validated boundaries
- F4-001–006: validated, including high-risk F4-006 structural consolidation.
- F4-007–011: replay `86f99b2186711a7d94159d9c1b7413b0248a0c5c`; checkpoint PASS.
- F4-012–017: replay `d533b450b20729130e850d7cbf37256a8e192306`; checkpoint PASS.
- F4-018–022: replay `7d32131a8681b3334cb405a68f79c2494b8db5e7`; checkpoint PASS.
- F4-023–027: replay `a7e987b2ae84ada927b082974f5d90f4896d43d4`; checkpoint PASS.
- F4-028–032: replay `30bf55f09fa02d4b805d6695c149061f2b24031d`; checkpoint PASS.
- F4-033–037: replay `58d891d493331863b9f8fdfb0436267a97d33f4e`; output SHA `94bbdeec878f57d4d97f54ad393bddc79074230ec69886e1f0a455bbe483ed3a`; 32-page bounded QA PASS after catching/fixing inherited italics.

## F4-038–042 checkpoint — 2026-08-17
- Input: validated F4-037 logical state.
- Durable replay: `work/apply_f4_038_042.py`, commit `89f8263a3fb90454727660654d103e6e2c132c16`.
- Durable ledger: `5969a0c676c80dadb1963c4245127d617c101f99`.
- Output SHA-256: `e23e7c57a52b5ef6f95c3f36ea2ab614274464bff6e65803198c5c868cb1181c`.
- Second replay returns all F4-038–042 targets already satisfied and produces exactly the same SHA. **BYTE IDEMPOTENCY PASS**.
- Body paragraphs: **695 → 696** because F4-042 adds one report-approved distinction paragraph after the existing 1.8 heading.
- F4-038: Ebû Ubeyde's role is now described as an important early appearance of resm thinking rather than a retrospectively complete technical formulation. Genuine footnote 108 retained at paragraph end.
- F4-039: Dânî paragraph rewritten with notes 110/111 preserved in source order; Ebû Dâvud paragraph rewritten with note 112 preserved. The unique intervening Dânî/kırâat paragraph was intentionally left in place because the Fourth Report's explicit repetition target was the Dânî and Ebû Dâvud framing paragraphs, not that source-specific discussion.
- F4-040: Zerkeşî paragraph now distinguishes transmitted mushaf writing from later kıyasî imlâ and explicitly avoids assigning a special conscious intention to every divergence. Notes 113/114/115 preserved in ascending source order.
- F4-041: Motzki/Sinai paragraph rewritten exactly within the report's authorized scope; footnote 119 retained. A cross-check of the report did not authorize deleting the separate Déroche paragraph, so it remains for any later specifically applicable item.
- F4-042: a new normal paragraph inserted immediately after the existing 1.8 heading. The heading's bookmark start/end remain unchanged; the original first 1.8 paragraph and its note 121 were not modified.
- Genuine footnotes/references: **469/469**; exact ID/reference sets baseline-identical; orphan/dangling/duplicate **0/0/0**.
- Word fields: **520/520**; field-type inventory exact baseline match. Zotero **465 item + 1 bibliography**.
- RTL **365/365**; bookmarks 53/53; hyperlinks 52; comments/revisions 0/0; sections 10.
- Protected `word/footnotes.xml`, `word/styles.xml`, `word/numbering.xml`, `word/settings.xml`, `word/_rels/document.xml.rels`: exact baseline hashes.
- ZIP/package integrity PASS; all XML/rels parse PASS.
- QA-only first 175 body paragraphs rendered as **35 pages**; all pages reviewed in contact-sheet form. Pages 26–29 inspected at full resolution, covering F4-038, both F4-039 targets, F4-040, F4-041, the 1.8 heading, inserted F4-042 paragraph, and the original following note-121 paragraph.
- No clipping, overlap, footnote overflow, abnormal whitespace, unintended style/color propagation or edit-caused pagination defect.
- Result: **PASS — F4-038–042 CHECKPOINT VALIDATED**.