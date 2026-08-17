# VALIDATION LOG

## Baseline
Canonical SHA-256 `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`; footnotes/references 469/469; orphan/dangling/duplicate 0/0/0; Word fields 520; Zotero 465 item + 1 bibliography; protected OOXML inventory locked. Fourth Report 116 items; Fifth Report 94 items.

## Prior validated boundaries
- F4-001–006: validated, including high-risk F4-006 structural consolidation.
- F4-007–011: replay `86f99b2186711a7d94159d9c1b7413b0248a0c5c`; validated citation and visual checkpoint.
- F4-012–017: replay `d533b450b20729130e850d7cbf37256a8e192306`; validated structural/citation checkpoint.
- F4-018–022: replay `7d32131a8681b3334cb405a68f79c2494b8db5e7`; output SHA `209b3a6e7719f44b7e9ed2b1a25b2992d00cdc7b6afa7e580fccd6f5d81c36f1`; 21-page bounded QA PASS.

## F4-023–027 checkpoint — 2026-08-17
- Durable replay: `work/apply_f4_023_027.py`, commit `a7e987b2ae84ada927b082974f5d90f4896d43d4`.
- Ledger commit: `d06c188c7130336b9a5f672b95f0f0ad63959caf`.
- Output SHA-256: `fe24f174ad7826dba8045a2584bc62e1b8a6ced867c8fbf2041da272f8fc3448`.
- Second replay returns all five items already satisfied and produces identical SHA. **BYTE IDEMPOTENCY PASS**.
- Body paragraphs remain **700**.
- F4-023: unsupported direct causal interpretation of Mervân's action via yedi harf/arza-i âhire removed; report-approved source-level distinction inserted.
- F4-024: prior paragraph carried footnote 49 (`Taberî, Câmiu'l-beyân 1/42; Sicistânî, Kitâbu'l-mesâhif 1/211`). Replacement frames arza-i âhire as one explanatory view; note 49 was preserved immediately after the sentence describing the son-mukabele/arza reference rather than attached to the later caution sentence.
- F4-025: written-memory complementarity restored for Ebû Bekir cem; no protected structure affected.
- F4-026: no earlier body occurrence of `Taberî` exists before the target; therefore first introduction was corrected to `Taberî (ö. 310/923)` and the embedded work note was removed. Footnote 66 contains concrete reading-variation examples, so it was retained immediately after the first replacement sentence about different readings becoming a source of dispute.
- F4-027: malformed duration expression removed without inventing any numerical duration; note 63 and surrounding paragraph content preserved.
- Genuine footnotes/references **469/469**; exact sets unchanged; orphan/dangling/duplicate **0/0/0**.
- `word/footnotes.xml`, styles, numbering, settings and document relationships: exact baseline hashes.
- Word fields **520/520**; Zotero **465+1**.
- ZIP and all XML/rels parse **PASS**.
- QA-only first 100 body paragraphs rendered as **23 pages**. Pages 15–23 inspected; pages 15,16,19 additionally inspected at full resolution. No clipping, overlap, footnote overflow, unintended style/color propagation or edit-caused pagination defect.
- Result: **PASS — F4-023–027 CHECKPOINT VALIDATED**.