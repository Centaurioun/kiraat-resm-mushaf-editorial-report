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
- F4-033–037: replay `58d891d493331863b9f8fdfb0436267a97d33f4e`; checkpoint PASS.
- F4-038–042: replay `89f8263a3fb90454727660654d103e6e2c132c16`; output SHA `e23e7c57a52b5ef6f95c3f36ea2ab614274464bff6e65803198c5c868cb1181c`; 35-page bounded QA PASS.

## F4-043–047 checkpoint — 2026-08-17
- Input: validated F4-042 logical state.
- Durable replay runner: `work/apply_f4_043_047.py`; exact transformation/recovery specification: `work/F4-043-047-REPLAY-SPEC.md`.
- Durable ledger commit: `86ebf507741218a7b2f38c3008f2eac97c825c53`.
- Output SHA-256: `6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7`.
- Second local replay returns F4-043–047 all already satisfied and produces exactly the same SHA. **BYTE IDEMPOTENCY PASS**.
- Body paragraphs remain **696**.
- F4-043: replaced the direct `bilinçli uyum` inference with a compatibility-vs-causation distinction; genuine footnote 142 unchanged.
- F4-044: hazf opening corrected with genuine footnote 145 preserved. The repeated `Sonuç olarak hazf...` conclusion was shortened; footnote 151 deliberately remains before the new synthesis, attached to the preceding source-specific examples.
- F4-045: Ca‘berî sentence corrected to `(ö. 732/1332)`; paragraph notes 158–163 preserved, including note 161 immediately after the Ca‘berî proposition.
- F4-046: overdetermined hemze-history explanation replaced with the report-approved early-writing/edâ framing; notes 166/167 remain with examples and 168 remains at the end.
- F4-047: opening through note 171 preserved. Existing RTL runs for `أُوْلوُا`, `سَأُوْرِيكُمْ`, `بِأَيْيْدٍ` were reused; Bakara corrected to 2/269. Unsupported `fonetik zorunluluktan dolayı` reasoning removed. Note 172's own source supports only a limited meaning-centred interpretation, so note 172 now follows that limited caution sentence rather than the corrected examples.
- Genuine footnotes/references: **469/469**; exact ID/reference sets baseline-identical; orphan/dangling/duplicate **0/0/0**.
- Word fields: **520/520**; type inventory exact baseline match. Zotero **465 item + 1 bibliography**.
- RTL **365/365**; bookmarks 53/53; hyperlinks 52; sections 10.
- Protected `word/footnotes.xml`, `word/styles.xml`, `word/numbering.xml`, `word/settings.xml`, `word/_rels/document.xml.rels`: exact baseline hashes.
- ZIP/package integrity PASS; all XML/rels parse PASS.
- QA-only first 190 body paragraphs rendered as **38 pages**. All 38 reviewed in contact-sheet form; pages 32–38 inspected at full resolution.
- Page 34 confirms note 151 remains before the new hazf synthesis; page 36 confirms corrected Arabic/RTL ziyâde examples and note 172 placement render cleanly.
- No clipping, overlap, footnote overflow, abnormal whitespace, unintended style propagation or edit-caused pagination defect.
- Full-document direct render again exceeded the bounded execution window; this matches the pre-existing renderer limitation and does not waive final all-page acceptance.
- Result: **PASS — F4-043–047 CHECKPOINT VALIDATED**.

## F4-048–052 checkpoint — PASS
- Application replay: `work/apply_f4_048_052.py` (commit `38d21ce2e2e83828e395d7d1c75048d7b1f9e483`).
- First runner execution: F4-048 APPLIED; F4-049 STRUCTURALLY_APPLIED; F4-050 STRUCTURALLY_APPLIED; F4-051 APPLIED; F4-052 APPLIED.
- Second runner execution: all five `ALREADY_SATISFIED`; candidate byte-identical.
- Candidate DOCX: `artifacts/checkpoints/manuscript-working-f4-052.docx`.
- Candidate SHA-256: `f94870a3b0b8a06acdb39cf104e78c3715f0c734068ee6dfc312795c863eabe4`.
- ZIP/XML integrity: PASS.
- Genuine footnotes/references: 469/469; orphan=0; dangling=0; duplicate=0; ID/reference order preserved.
- Word fields: 520; Zotero 465 item + 1 bibliography; field instructions baseline-identical.
- Bookmarks 53/53; hyperlinks 52; protected OOXML parts baseline-identical.
- Arabic/RTL: structural inventory equal to canonical source; F4-048 Arabic runs preserved rather than regenerated.
- Bounded render: `work/runtime/F4-052-QA.pdf`, 12 pages.
- Visual QA: 12/12 pages inspected; PASS. No clipping, overlap, footnote overflow, heading damage, Arabic-direction defect, or batch-induced style propagation.
- Visible pre-existing red editorial/style markings are deferred to their later Fourth/Fifth items; not introduced by F4-048–052.
- Evidence: `work/runtime/F4-052-TECHNICAL-VALIDATION.txt`, `work/runtime/F4-052-POSTFLIGHT.txt`, `work/F4-052-VISUAL-QA.md`.
- Durable boundary after this checkpoint: last `F4-052`; next `F4-053`.


## F4-053–057 checkpoint — PASS
- Replay: `work/apply_f4_053_057_v3.py` over durable F4-052 input.
- Candidate DOCX: `artifacts/checkpoints/manuscript-working-f4-057.docx`.
- Candidate SHA-256: `b77bc0066b22c9e66b250c53ff456045abde1f5410cb11ad98d77f3fb69d7810`.
- First final replay: F4-053 APPLIED; F4-054 APPLIED; F4-055 APPLIED; F4-056 STRUCTURALLY_APPLIED; F4-057 APPLIED; OOXML whitespace-preserve repair APPLIED.
- Second replay: all five items and whitespace repair ALREADY_SATISFIED; candidate byte-identical.
- ZIP/XML: PASS; footnotes/references 469/469; orphan=0; dangling=0; duplicate=0.
- Word fields 520; Zotero 465 item + 1 bibliography; protected OOXML parts baseline-identical.
- Arabic/RTL, bookmarks and hyperlinks equal to canonical-source structural inventory.
- Initial visual QA found one inherited run-boundary rendering defect (`ayrılmalıdır.İlk`); root cause was missing `xml:space="preserve"` despite a raw leading-space character.
- `work/apply_f4_053_057_v3.py` repaired only the whitespace-preservation property. Final 9-page bounded render was inspected page-by-page; the defect is resolved and visual QA is PASS.
- No new clipping, overlap, footnote overflow, blank page, heading damage, RTL damage or style propagation.
- Pre-existing red Fifth-style targets and the later red footnote editorial note remain for their designated report items.
- Durable boundary: last F4-057; next F4-058.
