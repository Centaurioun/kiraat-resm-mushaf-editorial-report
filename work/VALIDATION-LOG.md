# VALIDATION LOG

## Bootstrap baseline — 2026-08-17
Canonical source SHA-256 `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`; ZIP/XML PASS; genuine footnotes/references 469/469; orphan/dangling/duplicate 0/0/0; fields 520; Zotero 465 item + 1 bibliography; bookmarks 53/53; hyperlinks 52; sections 10. Fourth Report 116 items; Fifth Report 94 items. **PASS**.

## Prior validated boundaries
- F4-001–006: completed; F4-006 structural output SHA `33743240d3bd6e1f5eda2efabf8ef5dfa66cbec9a5f655923206563ab605bb93`; 14/14 bounded QA PASS.
- F4-007–011: replay `86f99b2186711a7d94159d9c1b7413b0248a0c5c`; output SHA `577badf47a383f0fed2324efc5e984c1dec7ca258998b328a858360f8805a2fd`; citation-safe F4-008 and structural F4-011; 15/15 bounded QA PASS.
- F4-012–017: replay `d533b450b20729130e850d7cbf37256a8e192306`; pipeline output SHA `9b983dcebda782bf1b5bbb69134dde43b0b45b5119ae63d5aa4f2379ec57885a`; notes 19–30 safely preserved; 19/19 bounded QA PASS.

## F4-018–022 checkpoint — 2026-08-17
- Input: validated F4-017 pipeline state.
- Durable replay script: `work/apply_f4_018_022.py`, commit `7d32131a8681b3334cb405a68f79c2494b8db5e7`.
- Ledger commit: `10bcd454d33399979e83c7d6ee90dfad34fe191f`.
- Output SHA-256: `209b3a6e7719f44b7e9ed2b1a25b2992d00cdc7b6afa7e580fccd6f5d81c36f1`.
- Replay on output returns F4-018–022 all already satisfied; rerun SHA identical. **BYTE IDEMPOTENCY PASS**.
- Body paragraphs remain **700**.
- F4-018: final two cem sentences rewritten per Fourth Report while retaining introductory context. Footnote 31 remains after the nüzûl-era written-record proposition; footnote 32 remains after the Ebû Bekir formal-derleme proposition.
- F4-019: Hârice corrected to Zeyd b. Sâbit's son Hârice b. Zeyd (ö. 100/718-19); note 35 preserved.
- F4-021: broken Zeyd sentence repaired; full paragraph note inventory remains 34/35/36/37.
- F4-020: Ebû Bekir-era material standardized as `suhuf`; paragraph note inventory remains 43/44/45.
- F4-022: Mervân b. Hakem date corrected to 65/685 and target terminology to `sahifeler`; note 44 remains attached.
- Genuine footnotes/references: **469/469**; exact ID/reference sets match baseline; orphan/dangling/duplicate **0/0/0**.
- `word/footnotes.xml`, styles, numbering, settings and document relationships: exact baseline hashes.
- Word field instructions: **520/520**, including TOC 1, PAGEREF 52, REF 0, PAGE 1, Zotero ADDIN 466.
- Zotero inventory: **465 item + 1 bibliography**.
- ZIP/package integrity PASS; all XML/rels parse PASS.
- QA-only first 90 body paragraphs rendered as **21 pages**. Pages 13–21 inspected; key changed pages 13–15 separately inspected at full resolution.
- No clipping, overlap, footnote overflow, unintended style/color propagation, or edit-caused pagination defect.
- Result: **PASS — F4-018–022 CHECKPOINT VALIDATED**.