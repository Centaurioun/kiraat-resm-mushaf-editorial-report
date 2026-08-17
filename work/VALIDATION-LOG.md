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


## F4-058–062 checkpoint — PASS
- Final replay: `work/apply_f4_058_062_v2.py` over durable F4-057 input.
- Candidate: `artifacts/checkpoints/manuscript-working-f4-062.docx`.
- SHA-256: `200f55000bf5dbe6e350466c79b4ffa15973bf06d92cb4a66ea91848252b77f3`.
- F4-058 STRUCTURALLY_APPLIED; F4-059 STRUCTURALLY_APPLIED; F4-060 APPLIED; F4-061 APPLIED; F4-062 APPLIED.
- Corrected second replay: all five report items and style repair already satisfied; byte-identical.
- ZIP/XML PASS; footnotes/references 469/469; orphan/dangling/duplicate 0/0/0.
- Word fields 520; Zotero 465+1; RTL/bookmark/hyperlink inventories canonical-equal; protected OOXML baseline-identical.
- Initial visual QA rejected inherited italics on F4-060 and F4-062 new paragraphs. v2 replay removed only direct italic run properties from those two targets.
- Corrected bounded render: 9 pages, 9/9 visually inspected, PASS. No clipping, overlap, footnote overflow, heading damage, Arabic/RTL damage or batch-induced style propagation remains.
- Pre-existing red editorial/Fifth targets remain for their designated later items.
- Durable boundary: last F4-062; next F4-063.


## F4-063–067 checkpoint — PASS
- Replay: `work/apply_f4_063_067.py`; candidate commit `185d2358cb5d1e4a4ccc38a485f0e63f5c065cf8`.
- Candidate SHA-256: `83ce4b2a4d1291d3d2defc47052230d634438e5e1d8a000231fcca9c1d138171`.
- First replay: F4-063–067 APPLIED; second replay: all already satisfied; byte-identical.
- Technical gate: ZIP/XML PASS; 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; Zotero 465+1; canonical-equal RTL/bookmarks/hyperlinks; protected OOXML baseline-identical.
- Long F4-065 Arabic/city-mushaf paragraph retained 70 RTL runs and FNs241–245; Arabic text was not regenerated.
- Bounded render: 7 pages; 7/7 visually inspected; PASS. No clipping, overlap, footnote overflow, heading damage, RTL defect, or batch-induced style propagation.
- Durable boundary: last F4-067; next F4-068.


## F4-068–072 checkpoint — PASS
- Replay: `work/apply_f4_068_072_v2.py`; candidate commit `6537a6fa4c678ef39f1b4fe67be5aa56db4751fc`.
- Candidate SHA-256: `5c77048b0fc6b6fd91b06c1e37c48098f5ef99d66e8b8285cd3c56e4c614876a`.
- First replay: F4-068–072 APPLIED; second replay: all already satisfied; byte-identical.
- Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical; canonical structural invariants preserved.
- F4-070 heading bookmark preserved by targeted span replacement; Arabic P275–277 was not regenerated.
- Bounded render: 7 pages; 7/7 visually inspected; PASS.
- Intermediate QA TOC display retained the pre-edit 3.4 heading because LibreOffice did not recalculate the preserved Word TOC field; actual body heading is correct and field recalculation remains a final acceptance task.
- Durable boundary: last F4-072; next F4-073.


## F4-073–077 checkpoint — PASS
- Final replay: `work/apply_f4_073_077_v3.py`; final candidate commit `b07eda97513611171eb74de05452bbfd48792605`.
- Candidate SHA-256: `9b8eea35a108e9cefe160e5d7f4975f9adbc278d2a6883cd016a3b67fa46a56c`.
- F4-073 STRUCTURALLY_APPLIED; F4-074 STRUCTURALLY_APPLIED; F4-075 STRUCTURALLY_APPLIED; F4-076 APPLIED; F4-077 STRUCTURALLY_APPLIED.
- Second replay: all accepted changes and whitespace-preserve repair already satisfied; byte-identical.
- Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; reference identity/multiplicity canonical-equal; body reference order changed only because accepted source-backed paragraphs were moved; 520 fields; protected OOXML baseline-identical.
- Initial 14-page visual QA was rejected for two missing rendered spaces across run boundaries. v3 adds only `xml:space=preserve` to affected whitespace-bearing text nodes.
- Corrected 14-page render: 14/14 visually inspected; PASS. Both spacing defects are resolved. No clipping, overlap, footnote overflow, heading damage, RTL defect, or batch-induced style propagation remains.
- Durable boundary: last F4-077; next F4-078.


## F4-078 checkpoint — PASS
- Final replay: `work/apply_f4_078_v2.py`; candidate SHA-256 `131913a4e602ec88fa0582ebe1cd40cfe8f9c1e9461c5692d12d4c4b36465e6f`.
- F4-078 STRUCTURALLY_APPLIED: current 3.7–3.12 consolidated under `Resm-i Osmânî’ye Bağlılığın Gerekçeleri ve Sınırları`; five former subsection headings demoted to bookmark-preserving transition prose; unique sourced material retained.
- Eight citation-free repetitive/defensive conclusion paragraphs removed. F4-079/F4-080/F4-081 target claims intentionally remain for their own report items.
- Second replay: byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical; bookmarks 53/53; hyperlinks 52; RTL canonical-equal.
- Initial 17-page visual QA rejected because five demoted headings retained direct run-level bold formatting. v2 removes only direct run formatting from those five transition paragraphs. Repaired render adjudicated across all 17 pages (9 changed pages reinspected directly; 8 pages pixel-identical to already inspected first render): PASS.
- Word TOC remains a stale derived field and must be refreshed in final Word field-refresh phase; field structures were not rewritten during citation-safe application.
- Durable boundary: last F4-078; next F4-079.
