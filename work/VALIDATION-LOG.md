# VALIDATION LOG

## Bootstrap baseline — 2026-08-17
Source SHA-256 `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`; ZIP/XML PASS; genuine footnotes/references 469/469; orphans/dangling/duplicates 0/0/0; fields 520; TOC 1; PAGEREF 52; PAGE 1; ADDIN 466; Zotero item 465 + bibliography 1; bookmarks 53/53; hyperlinks 52; comments/revisions 0; sections 10; F4 116 items; F5 94 items. **PASS**.

## Prior validated checkpoints — 2026-08-17
- F4-001–003: replay `46a5014e1c87bce2bceda20278481055975ccb39`; QA PASS.
- F4-004–005: replay `8ba3fe378240d3d42e0c62b0cc7e9936c907bdf8`; output SHA `567f7847958364b27d68c45c073481c9d7e6030bba561d7d0dc011d8c0cf6355`; QA PASS.
- F4-006 high-risk structural checkpoint: replay `dd41275b91dfaa7dffce0cb43e7b5e823db73756`; output SHA `33743240d3bd6e1f5eda2efabf8ef5dfa66cbec9a5f655923206563ab605bb93`; 711→705 paragraphs; 14/14 bounded visual QA PASS.
- F4-007–011: replay `86f99b2186711a7d94159d9c1b7413b0248a0c5c`; output SHA `577badf47a383f0fed2324efc5e984c1dec7ca258998b328a858360f8805a2fd`; 705→704 paragraphs. F4-008 notes 15/16 semantically preserved; F4-011 inherited red style caught and corrected; 15/15 bounded visual QA PASS.

## F4-012–017 high-risk structural checkpoint — 2026-08-17
- Input: validated F4-011 logical state.
- Durable batch replay script: `work/apply_f4_012_017.py` at commit `d533b450b20729130e850d7cbf37256a8e192306`.
- Durable ledger commit: `154d696611e3b97fc92595982fa240097f89e7fe`.
- Deterministic recovery pipeline output SHA-256: `9b983dcebda782bf1b5bbb69134dde43b0b45b5119ae63d5aa4f2379ec57885a`.
- Rerun on output: all F4-012–017 targets already satisfied; byte-identical SHA `9b983dcebda782bf1b5bbb69134dde43b0b45b5119ae63d5aa4f2379ec57885a`. **IDEMPOTENCY PASS**.
- Body paragraphs: **704 → 700** in this batch; baseline 711.
- F4-012: source paragraphs carrying notes 19, 20 and 21 consolidated into one report-approved opening. Notes retained in ascending order and remain attached to the surviving synthesis; no note deleted or reassigned to unrelated prose.
- F4-013: missing terminal period restored only; notes 22/23 unchanged.
- F4-014 + F4-016: shared Medine paragraph edited in-place. Explicit work note removed; second/third reasons merged; over-strong evidentiary wording weakened. Genuine notes 24/25/26 remained in the paragraph and in original source order.
- F4-015: three-paragraph two-model discussion consolidated to the cautious report-approved synthesis. Genuine notes 28/29/30 retained on the sentence summarizing the two source families; no citation deleted.
- F4-017: repetitive 1.3 opening replaced with direct Ebû Bekir cem transition; no protected structures in target.
- Genuine footnotes/references: **469/469**; exact ID/reference sets unchanged; orphans/dangling/duplicates **0/0/0**.
- `word/footnotes.xml`: exact canonical hash.
- Aggregate field instructions: **520/520**; TOC 1; PAGEREF 52; REF 0; PAGE 1; ADDIN 466; aggregate field hash unchanged.
- Zotero: **465 item + 1 bibliography**, unchanged.
- Protected `styles.xml`, `numbering.xml`, `settings.xml`, `document.xml.rels`, and `footnotes.xml`: exact baseline hashes. Expected text changes confined to `word/document.xml` among protected core parts.
- ZIP integrity **PASS**; all XML parts parse **PASS**.
- Independent monolithic application and durable two-script pipeline produce canonically identical `word/document.xml`. The raw package SHA differs only because of XML serialization; durable pipeline SHA above is authoritative.
- QA-only first-80-paragraph slice rendered as **19 pages**. **19/19 pages visually inspected**; affected pages 12–13 inspected at full resolution.
- Durable pipeline QA render compared against independent validation render: **19/19 PNG files pixel-hash identical**.
- No clipping, overlap, footnote overflow, unexpected whitespace, unintended color/font propagation, or batch-caused pagination defect.
- Result: **PASS — F4-012–017 STRUCTURAL CHECKPOINT VALIDATED**.