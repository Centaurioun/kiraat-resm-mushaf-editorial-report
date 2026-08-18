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


## F4-079 checkpoint — PASS
- Final replay: `work/apply_f4_079_v2.py`; candidate commit `85196bc9947a2b8398017a7c50da4d9d152ad37a`; SHA-256 `6c373c2173180bc54d97baf7264f267fc3d25f56383f795f95d8d37378774e16`.
- F4-079 APPLIED: the Israel/Africa tampered-mushaf narrative is no longer presented as verified historical fact. The report-approved limited attribution and an explicit verification caveat replace the detailed asserted narrative. Unsupported perpetrator-intent attribution was removed.
- Citation-safe mapping preserved FN341–347 as sources for what the relevant resm literature reports, rather than as independent verification of the historical allegations. Footnote identity/multiplicity remains canonical-equal.
- Deterministic second replay is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical; RTL inventory canonical-equal.
- First visual render was rejected because old Arabic-example paragraphs leaked numbering/centering into the new caveat prose. RTL-safe v2 removes only stale paragraph list/alignment/bidi formatting without copying paragraph-mark RTL or changing RTL counts.
- Corrected bounded render: 4/4 pages inspected; PASS. No residual list numbering/centering, no blank RTL artifacts, no footnote overflow, clipping or style propagation.
- Durable boundary: last F4-079; next F4-080.


## F4-080 checkpoint — PASS
- Final replay: `work/apply_f4_080.py`; candidate commit `eacf658a35c4075bf0ac92fed7a7475c60204449`; SHA-256 `26a91412247c513c0c607994547c5fdd56492c67bb0d9bc05ce7107e7f022851`.
- F4-080 APPLIED: the unsupported counterfactual that fully phonetic writing would weaken mushafaha or cause eda forms to disappear was replaced with the report-approved evidentially bounded statement about telakki, mushafaha, isnad and the written framework.
- FN340 is preserved on the replacement paragraph. Deterministic second replay is byte-identical.
- Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical.
- Bounded render: 3/3 pages inspected; PASS. No clipping, overlap, style leakage, footnote overflow or transition damage.
- Durable boundary: last F4-080; next F4-081.


## F4-081 checkpoint — PASS
- Final replay: `work/apply_f4_081.py`; candidate commit `731f245b2a57abb181aa7b1f685ff665d172026c`; SHA-256 `707ca2de808935a2bec9a57dd7a2a335180b5ac76fe4e3eb1dece308658bed63`.
- F4-081 APPLIED: the claim that changing orthography would cause qiraat variants themselves to disappear was replaced with the report-approved distinction between loss/change of graphic visibility within the Uthmanic rasm and the independent transmission basis of readings through telakki, eda and riwaya.
- Target paragraph was citation-free and structurally plain; FN352 remains on the preceding filological paragraph. No footnote remapping was required.
- Deterministic second replay is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical.
- Bounded render: 4/4 pages inspected; PASS. No clipping, overlap, footnote overflow, RTL artifact or style propagation. Final-page whitespace is bounded-slice termination, not a new blank manuscript page.
- Durable boundary: last F4-081; next F4-082.


## F4-082 checkpoint — PASS
- Final replay: `work/apply_f4_082.py`; candidate commit `ed3719283c97f7fff7e00a46803369c9525955af`; SHA-256 `299bed4bcf3fa1b479ec1ff1b6ee1baa0f7aa4210dd47f789cdf1f35cc81bbad`.
- F4-082 APPLIED: the report-approved Third-to-Fourth transition was placed in an existing safe empty paragraph immediately before the Fourth Section boundary; no paragraph was inserted and body count remains 677.
- `DÖRDÜNCÜ BÖLÜM`, the Fourth Section main title and 4.1 heading retain their bookmark structures; citation identity/order is unchanged.
- Deterministic second replay is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical.
- Bounded render: 4/4 pages inspected; PASS. Existing Fourth Section new-page behavior remains intact; no new blank page or section break was introduced.
- Durable boundary: last F4-082; next F4-083.


## F4-083 checkpoint — PASS
- Final replay: `work/apply_f4_083.py`; candidate commit `812d3189861607d4a2822108d77c45fb48b719eb`; SHA-256 `d4adb180cd58a6d74d1557a6c14fe2bc2b1fc42018c7b4bcffaf2029e2993127`.
- F4-083 APPLIED: repeated cem/istinsah history in P351 was reduced to the argument-essential reminder while FN365 was preserved.
- P352 no longer assigns autonomous selecting/producing agency to rasm; mushaf-line compatibility is framed as an evaluative criterion within transmitted qiraat. FN366–367 remain on the source-backed acceptance-criterion discussion.
- F4-084 evidence language in P350 was intentionally left untouched for the next sequential item.
- Deterministic second replay is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical.
- Bounded render: 4/4 pages inspected; PASS. No clipping, overlap, footnote overflow, heading damage or style leakage.
- Durable boundary: last F4-083; next F4-084.


## F4-084 checkpoint — PASS
- Final replay: `work/apply_f4_084.py`; candidate commit `7a7f5aa363b5729a86aecf188c21ba7f67747be0`; SHA-256 `459e8be1b0a4d294cb5ac5473d19073d68b879bd5069405eda2da02a8281f86d`.
- F4-084 APPLIED: the `Kırâat sünnettir` / Ebû Amr evidence is retained but its inference is reduced to the report-approved claim that these reports indicate the centrality of rivâyet and telakki in qiraat transmission.
- FN361–364 remain in their original order; Kastallânî and Dânî source-backed continuation remains untouched.
- F4-083 P351/P352 reframe remains intact. Deterministic second replay is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical.
- Bounded render: 3/3 pages inspected; PASS. No clipping, overlap, footnote overflow, or style propagation.
- Durable boundary: last F4-084; next F4-085.


## F4-085 checkpoint — PASS
- Final replay: `work/apply_f4_085.py`; candidate commit `aa3b05436d460bb9d412fcecd488c4609fef407b`; SHA-256 `d48b31281dc7e8ddde3b30856e2ce1d6edcfc4b079de2c87c63d0b54fdac0af1`.
- F4-085 APPLIED: the former 4.1 summary was replaced with the report-approved transition distinguishing the normative common Uthmanic mushaf tradition from the historical evidentiary value of personal Companion codices.
- The transition is citation-free and immediately precedes the bookmark-bearing 4.2 heading; heading/bookmark structures remain unchanged.
- Deterministic second replay is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical.
- Bounded render: 4/4 pages inspected; PASS. FN373–378 and Arabic examples remain stable; visible red editor note belongs to pending F4-087.
- Durable boundary: last F4-085; next F4-086.


## F4-086 checkpoint — PASS
- Final replay: `work/apply_f4_086.py`; candidate commit `0ac7c7dc0c2b6c0e07ceab8987c8aed0e4b23896`; SHA-256 `2d7e6dc15e60c4b85db6de9459cc5bdd24f41da98f77577d17871e68d477826c`.
- F4-086 STRUCTURALLY_APPLIED: a citation-free category frame was inserted after the FN375 general introduction and before the FN376 explanatory/tafsiri example, explicitly distinguishing reading reports, explanatory/tafsiri expressions, word-order/writing differences, and disputed records.
- Source-specific example paragraphs, FN375–383 and Arabic/RTL runs were not relocated or collapsed. The normative criterion is stated as the Uthmanic written framework together with sound transmission.
- F4-087 open editor note and F4-088 active-agent conclusions were intentionally left for their own sequential items.
- Deterministic second replay is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical; RTL inventory canonical-equal.
- Bounded render: 5/5 pages inspected; PASS. No clipping, overlap, footnote overflow, Arabic corruption, heading damage or style propagation.
- Durable boundary: last F4-086; next F4-087.


## F4-087 checkpoint — PASS
- Final replay: `work/apply_f4_087.py`; candidate commit `a49959ebcc7cf55aece1874636838e083da536af`; SHA-256 `cedcc233e5e3ce9150f3ebbd66b199075517dcac4a7d771a455a03db5e16a3ce`.
- F4-087 APPLIED: the explicit parenthetical editor/work note embedded in the FN377–378 paragraph was removed and ordinary spacing before `Bunun en meşhur örneklerinden biri...` was restored.
- FN377–378, the Arabic Bakara 2/238 runs and all surrounding source-backed text remain in the same paragraph; F4-088 active-agent wording remains intentionally untouched.
- Deterministic second replay is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical.
- Bounded render: 4/4 pages inspected; PASS. No clipping, overlap, footnote overflow, Arabic/RTL corruption or F4-087-induced style propagation.
- Durable boundary: last F4-087; next F4-088.


## F4-088 checkpoint — PASS
- Final replay: `work/apply_f4_088.py`; candidate commit `bb9c5bff1d7681a2e9565f2b448d5cab57cc2bba`; SHA-256 `92d3f7222c33e04fe4c737bd6bce3087e811d02e4f11e78755f95c857e4eb362`.
- F4-088 APPLIED: the active-agent sentence assigning selective/curatorial authority to `Osmânî resm` was replaced with the report-approved distinction between the historical Uthmanic recension/common mushaf acceptance process and rasm as a written evaluative criterion.
- The target paragraph remains citation-free and structurally unchanged; neighboring source-backed FN380–387 and RTL material remain intact. F4-089 Ibn Masud intent language remains intentionally pending.
- Deterministic second replay is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical.
- Bounded render: 4/4 pages inspected; PASS. No clipping, overlap, footnote overflow or style propagation.
- Durable boundary: last F4-088; next F4-089.


## F4-089 checkpoint — PASS
- Final replay: `work/apply_f4_089.py`; candidate commit `c63d1d21db9c885b45f28df21cea123996421371`; SHA-256 `740d2d4960e9d6918baf808cba1d290c88e86caaa43f4395f5335b4746e210be`.
- F4-089 APPLIED: the author-level psychological interpretation of Ibn Masud's objection was replaced with the report-approved bounded statement that the transmitted reports indicate objections related to the recension process and his codex without assigning a definite motive.
- FN388 and the following explicitly source-attributed Kurtubi/Ibn Kathir discussion remain in the same paragraph. F4-090 repeated 4.2 conclusions remain intentionally pending.
- Deterministic second replay is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical.
- Bounded render: 4/4 pages inspected; PASS. No clipping, overlap, footnote overflow, run-boundary spacing defect or style propagation.
- Durable boundary: last F4-089; next F4-090.


## F4-090 checkpoint — PASS
- Final replay: `work/apply_f4_090.py`, revision 2; candidate commit `8dcd3e9f12ffee82d648d247c0deaa96040d10ae`; SHA-256 `4f6218852a35d1775610e19f199158677540870a4f3ea27974aabbcc7050d5e1`.
- F4-090 STRUCTURALLY_APPLIED: the earlier citation-free repeated 4.2 conclusion was removed, while the final citation-free conclusion immediately before 4.3 was replaced with the report-approved three-sentence synthesis distinguishing historical witness from normative text authority.
- Source-backed FN384–388 paragraphs remain in sequence and the 4.3 heading/bookmark was not moved or rewritten. Body paragraph count changed only as expected, 678 -> 677.
- Revision 1 visual QA exposed an inherited run-whitespace defect from the F4-089 paragraph. Revision 2 was regenerated from the F4-089 input and deterministically fixed the OOXML whitespace-preservation property; the corrected `değerlendirilmelidir. Kurtubî’nin` spacing is visually confirmed. Revision 1 is superseded and must not be used.
- Deterministic second replay is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical.
- Bounded render revision 2: 5/5 pages inspected; PASS. No clipping, overlap, footnote overflow, Arabic/RTL corruption, heading damage, blank-page regression or style propagation.
- Durable boundary: last F4-090; next F4-091.


## F4-091 checkpoint — PASS
- Final replay: `work/apply_f4_091.py`; candidate commit `99a3565ce4b027b8a27dfc94c6197967d081b3b9`; SHA-256 `85fe7159297c0d7ca2c477a871af1655571e14fd7b68f44abe7040b7994bb222`.
- F4-091 APPLIED: the Ibn Shanbudh example is now framed through public recitation, transmission, common mushaf tradition and period acceptance criteria rather than as a one-factor rasm-only causation.
- FN391 remains on the rewritten Ibn Shanbudh paragraph; the following FN392–393 paragraph is untouched and reserved for F4-092.
- Deterministic second replay is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical.
- Bounded render: 4/4 pages inspected; PASS. No clipping, overlap, footnote overflow, heading damage, run-boundary spacing defect or style propagation.
- Durable boundary: last F4-091; next F4-092.


## F4-092 checkpoint — PASS
- Final replay: `work/apply_f4_092.py`; candidate commit `82395162a0958f8340fe36837c00a86db94ca310`; SHA-256 `0c6d7393e9eac0054ef8c9de7e27cc6dc257a741e54587df0f260c4512ce0d6f`.
- F4-092 APPLIED: the FN392–393 paragraph now distinguishes rasm-nonconforming, shadh, ahad/tafsiri and alleged-mansukh categories rather than collapsing them into one historical/usuli line.
- The source-specific Ibn Taymiyya / Ibn al-Jazari middle discussion and FN392–393 are preserved; the concluding claim is narrowed so rasm conformity is one important criterion considered with isnad, language and scholarly acceptance.
- P377/FN394 and later F4-093+ material remain untouched.
- Deterministic second replay is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical.
- Bounded render: 5/5 pages inspected; PASS. No clipping, overlap, footnote overflow, RTL corruption, run-boundary spacing defect or style propagation. The short fifth page is the natural bounded-slice ending, not a blank-page regression.
- Durable boundary: last F4-092; next F4-093.


## F4-093 checkpoint — PASS
- Final replay: `work/apply_f4_093.py`; candidate commit `77c2e6707cdbff9eb9e57b1715f09ec5aeb2de80`; SHA-256 `3a2c3f5b16a889de359ed59c859a2eeff4d9610b76b92c7af023858e8a9a5a06`.
- F4-093 APPLIED: the citation-free 4.3 closing conclusion was replaced with a direct conceptual transition distinguishing acceptance status from preference, linguistic tawjih and waqf explanation.
- The new transition sits immediately before the bookmark-backed 4.4 heading. Source-backed 4.3 material including FN395–399 and the 4.4 opening FN400+ paragraphs remain intact.
- Deterministic second replay is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical.
- Bounded render: 4/4 pages inspected; PASS. No clipping, overlap, footnote overflow, RTL corruption, heading damage, orphaned heading, run-boundary spacing defect or style propagation.
- Durable boundary: last F4-093; next F4-094.


## F4-094 checkpoint — PASS
- Final replay: `work/apply_f4_094.py`; candidate SHA-256 `523fcf36cae029c4761e254a378beda7f378499ed8a0b13bcf0371cd83079894`.
- F4-094 APPLIED: the bookmark-backed 4.4 heading was corrected from the grammatically problematic `Tercîhî, Tevcîhi ... Etkisi` formulation to `Resm-i Osmânî'nin Kırâatlerin Tercihi, Tevcîhi ve Vakıf Uygulamalarıyla İlişkisi`, avoiding one-way causal overstatement.
- The two heading bookmarks remain preserved; the F4-093 transition and FN400+ source-backed opening material remain intact.
- Deterministic second replay is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical.
- Bounded render: 4/4 pages inspected; PASS. The heading wraps cleanly over two lines with no clipping, overlap, orphaning, footnote overflow or style propagation.
- Durable boundary: last F4-094; next F4-095.


## F4-095 checkpoint — PASS
- Final replay: `work/apply_f4_095.py`; candidate SHA-256 `00eae3a5b7299a0522979562d73e1d4bbe52ff7c205ee59c37f09ba3b4b817ea`.
- F4-095 APPLIED: the FN401 paragraph now states that qiraat-imam readings are transmitted within received teaching/rivayat traditions and that preference language does not imply independent creation of new readings.
- The source-backed Makki three-factor discussion is retained, while rasm conformity is framed as one criterion alongside rivayat, language and general acceptance rather than an independent single determinant.
- FN401 remains attached to the rewritten paragraph; FN402–403 and later F4-096 material remain untouched.
- Deterministic second replay is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical.
- Bounded render: 4/4 pages inspected; PASS. No clipping, overlap, footnote overflow, RTL corruption, run-boundary spacing defect or style propagation.
- Durable boundary: last F4-095; next F4-096.


## F4-096 checkpoint — PASS
- Final replay: `work/apply_f4_096.py`; candidate SHA-256 `67791838653b64426378747d1fd4f4a304afe7d38e2c13cf0b7da60972117e41`.
- F4-096 APPLIED: the citation-free 4.4 waqf introduction now distinguishes meaning, nahw and rivayat as primary waqf/ibtida considerations while limiting rasm to relevant written cues such as wasl-fasl and word boundaries.
- Source-backed FN413–416 examples, including RTL/Arabic material and Hamza/hemza details, remain intact; the bookmark-backed 4.5 heading remains unchanged.
- Deterministic second replay is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical.
- Bounded render: 4/4 pages inspected; PASS. No clipping, overlap, footnote overflow, RTL corruption, heading damage, blank-page regression or style propagation.
- Durable boundary: last F4-096; next F4-097.


## F4-097 checkpoint — PASS
- Final replay: `work/apply_f4_097.py`; candidate SHA-256 `9f76e4b8a98a70a8af42a73b261945378c5bd423d94903b4ac20a94b2880f5da`.
- F4-097 APPLIED: the FN417 opening claim now frames rasm reports as complementary evidence for written mushaf forms and their relationship to transmitted readings rather than a constitutive source of qiraat.
- The citation-free 4.5 synthesis was replaced with the report-approved statement that rasm reports identify written forms/city-mushaf differences and do not replace the rivayat source of readings.
- FN417 and all later source-backed material remain intact; visible Mehdevi/Ebu Amr/Ibn Muaz/Sehavi/Satibi work notes remain intentionally pending for later editorial correction.
- Deterministic second replay is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical.
- Bounded render: 5/5 pages inspected; PASS. No clipping, overlap, footnote overflow, RTL corruption, blank-page regression or style propagation.
- Durable boundary: last F4-097; next F4-098.


## F4-098 checkpoint — PASS
- Final replay: `work/apply_f4_098.py`; candidate SHA-256 `30c5f9140dfbf9425e860563e9c297e3ba3d6b154a74c8d7f5b7236d1df20bc0`.
- F4-098 APPLIED: first-use biographical dates were normalized according to the report: Sehavi at P195 `(ö. 643/1245)` and Mehdevi at P352 `(ö. 440/1048-49 [?])`; repeat-use dates/work notes were removed in 4.5. Ibn Muaz al-Juhani is corrected to `(ö. 442/1050)` and the Ebu Amr work-note fragment was removed while retaining the existing death date.
- The overgeneralized universal-hikma authorial conclusion in the FN418–419 paragraph was replaced with the report-approved qualified framing that attributes meaning/hikma explanations to sources and avoids assigning one conscious purpose to every rasm feature.
- All affected source structure remains intact, including FN417–437 and dense Arabic/RTL runs. Deterministic second replay is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical.
- Because the item touched three distant regions, bounded visual QA used three renders: P192–198 3/3 PASS; P349–355 4/4 PASS; P396–403 5/5 PASS; aggregate 12/12 pages PASS.
- Pre-existing red editorial material outside the F4-098 target remains pending for later report items and is not a batch regression.
- Durable boundary: last F4-098; next F4-099.


## F4-099 checkpoint — PASS
- Final replay: `work/apply_f4_099.py`; candidate SHA-256 `3c3a18fdd19dff05f2bb7e3a03979bc5eb0769085a36b7b2e1c4a61a81d4f8c0`.
- F4-099 APPLIED: inserted the report-approved two-sentence historical bridge between the existing 4.5 closing synthesis and the bookmark-backed 4.6 heading, linking classical rasm literature to later mushaf copying and print-publication practice.
- Existing 4.5 source-backed content and the 4.6 heading/FN438+ material remain unchanged. The insertion adds exactly one normal body paragraph, increasing body paragraphs from 677 to 678.
- Deterministic second replay is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical.
- Bounded render P403–409: 3/3 pages inspected; PASS.
- Durable boundary: last F4-099; next F4-100.


## F4-100 checkpoint — PASS
- Final replay: `work/apply_f4_100.py`; candidate SHA-256 `6949b4cf0af1e4fc087bf6d4313e22a445e49ba5341ab596c19a027ae0c5da8a`.
- F4-100 APPLIED: at the 4.7 opening, the claim that early mushafs lacked dots/vowels fundamentally in order to preserve multiple qiraat was replaced with the report-approved historically cautious formulation. Early script is now described as later acquiring dots, vowels and auxiliary signs while the basic rasm structure remained; the initial absence of such signs is attributed to the writing system of the period and is not reduced to a single conscious qiraat-preservation purpose.
- Only the first two causal sentences of current P426 were replaced; the later zapt/rivayat/geographical-distribution discussion in the same paragraph remains intact.
- Deterministic replay is byte-identical after the helper-path repair. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical.
- Bounded render P423–429: 3/3 pages inspected; PASS. The pre-existing later Huzai work note remains outside this item and pending.
- Durable boundary: last F4-100; next F4-101.


## F4-101 checkpoint — PASS
- Final replay: `work/apply_f4_101.py`; candidate SHA-256 `b2acdf0116b7b6efa23ddb1661ab6cc8ecd9528ebfb470b44c7a0c2585b2a3a7`.
- F4-101 APPLIED: preserved the source-backed Dânî/Ebû Dâvud/modern-publication evidence in P416–420, replaced the first citation-free repeated conclusion with the report-approved three-sentence synthesis, and removed the redundant second conclusion.
- The bookmark-backed 4.7 heading now follows the single synthesis directly. Body paragraphs decrease from 678 to 677.
- Deterministic second replay is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical.
- Bounded render P416–425: 5/5 pages inspected; PASS. No clipping, overlap, footnote overflow, heading orphaning, RTL corruption, blank-page regression, abnormal spacing or style propagation.
- Durable boundary: last F4-101; next F4-102.


## F4-102 checkpoint — PASS
- Final replay: `work/apply_f4_102.py`; candidate SHA-256 `38561f498d0abacc3dacea2bb35b92aa1ed4abe67d8b767657ea80e759ff69e8`.
- F4-102 APPLIED: 4.7 now opens directly with the report-approved print/resm focus. The repeated calligraphy/copying lead-in was compressed while preserving unique source-backed historical propositions.
- Genuine FN454 and FN455 were proposition-safely retained on the compact historical-background sentences; preflight resolves them from the candidate OOXML, and `word/footnotes.xml` remains baseline-identical. F4-100 P425 and the later F4-103 Saint Petersburg target remain unchanged.
- Deterministic second replay is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical.
- Bounded render P422–431: 4/4 pages inspected; layout PASS. The isolated QA slice copies all 469 footnotes while retaining sparse high w:id references, so LibreOffice-rendered slice footnote text is not authoritative for footnote-content identity; `work/F4-102-VISUAL-QA.md` records this renderer caveat. Candidate OOXML/preflight and protected-part invariants are authoritative for citation mapping.
- Durable boundary: last F4-102; next F4-103.


## F4-103 checkpoint — PASS
- Final replay: `work/apply_f4_103.py`; candidate SHA-256 `31e7ab7f74f1a3370c102ccd63336bedccda664a0e6674a4dbd30193d2bf58b2`.
- F4-103 APPLIED: only the citation-free 1201/1787 Saint Petersburg sentence in current P429 was replaced with the report-authorized safe core naming II. Katerina's order; the uncertain `Mevlây Osman (?)` attribution was removed.
- Hinkelmann/Marracci chronology before the sentence and P430/FN460, P431/FN461, P432/FN462 after it remain unchanged.
- Deterministic second replay is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical.
- Bounded render P427–432: 3/3 pages inspected; PASS.
- Durable boundary: last F4-103; next F4-104.


## F4-104 checkpoint — PASS
- Final replay: `work/apply_f4_104.py`; candidate SHA-256 `641e964820181acf70d8c7e5af7608e1347e7e4faecb2a1a19bfb7628710ee13`.
- F4-104 APPLIED: after F4-101 had already removed the old `three aims` paragraph, the surviving citation-free over-single-cause synthesis in current P413 was replaced with the report-approved multicausal standardization paragraph.
- Resm-i Osmani adherence is now one important factor among printing technology, tashih/control boards, qiraat/writing expertise, educational institutions and official publication policies. Source-backed P410–412 and P414–416 remain unchanged; F4-105 P437 remains untouched.
- Deterministic second replay is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical.
- Bounded render P410–416: 4/4 pages inspected; PASS.
- Durable boundary: last F4-104; next F4-105.


## F4-105 checkpoint — PASS
- Final replay: `work/apply_f4_105.py`; candidate SHA-256 `640fdbf06ee48de553d7341b88592cff5ead107010ccef15e2278f684f36b118`.
- F4-105 APPLIED: replaced the citation-free 4.7 closure that portrayed printed mushafs as active drivers of qiraat spread/standardization with the report-approved multicausal formulation. Printed mushafs are now said to increase written visibility and use, while regional spread also depends on teaching traditions, regional qiraat preferences, official publication policies and educational institutions.
- Source-backed P434–436 and the Türkiye chronology beginning at P438 remain unchanged.
- Deterministic second replay is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical.
- Bounded render P434–440: 3/3 pages inspected; PASS. Existing stale TOC display in the isolated slice is expected and final field refresh remains deferred.
- Durable boundary: last F4-105; next F4-106.


## F4-106 checkpoint — PASS
- Final replay: `work/apply_f4_106.py`; candidate SHA-256 `cace4c42e6f82b75c31b6533fb732892aa2d916baf8ec7abf6168730d6e15f38`.
- F4-106 APPLIED: repaired the 1889 Teftîş-i Mesâhif-i Şerîfe Meclisi grammar and narrowed the claim to institutional tashih/idarî denetim. Genuine FN467 remains on the same paragraph and proposition.
- P438, P440 and P441 remain unchanged for F4-107.
- Deterministic second replay is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical.
- Bounded render P437–441: 3/3 pages inspected; PASS.
- Durable boundary: last F4-106; next F4-107.


## F4-107 checkpoint — PASS
- Final replay: `work/apply_f4_107.py`; candidate SHA-256 `a9edfb112efc69f95d99f400197d0f66ad47e977142dee8555d83cdc93233186`.
- F4-107 APPLIED: removed the citation-free pre-Türkiye intermediate conclusion so 4.7 now proceeds directly from printed-mushaf chronology into the Ottoman/Türkiye control and publication experience.
- Replaced only the repeated `Özetle...` Türkiye ending inside the FN469-bearing final paragraph with the report-approved single multicausal final conclusion. The source-backed Diyanet/imlâ propositions and FN469 remain in place.
- The 1873 decision/permission versus 1874 actual-printing distinction remains unchanged. Body paragraphs 677→676 solely because the former citation-free intermediate conclusion paragraph was removed.
- Deterministic second replay is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical.
- Bounded render P430–442: 6/6 pages inspected; PASS. The final 4.7 conclusion ends normally and `Sonuç` begins on the following page using the pre-existing page/section break.
- Durable boundary: last F4-107; next F4-108.


## F4-108 checkpoint — PASS
- Final replay: `work/apply_f4_108.py`; candidate SHA-256 `38926bbf6e31f5b1d74ca5a883d1867bae35fa06ef89187d0d35d2860edf6bfa`.
- F4-108 APPLIED: consolidated repeated main-thesis blocks in Sonuç into the report-approved two-focus framing. P443 now states the oral/riwayah transmission thesis plus rasm as complementary compatibility criterion; P445 states the joint oral/written framework and combined acceptance criteria.
- The unique sahih/meşhur/âhâd/şâz distinction was retained in compact form at P446; unique historical/result paragraphs P444 and P447–454 remain unchanged. The former final repetition was removed.
- Body paragraphs 676→675 solely because the final citation-free repetition paragraph was removed. Deterministic second replay is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical.
- Bounded render P442–456: 5/5 pages inspected; PASS. `Kaynakça` begins on the following page with the pre-existing break. P444 contains a pre-existing red directly formatted sentence not introduced or altered by F4-108.
- Durable boundary: last F4-108; next F4-109.


## F4-109 checkpoint — PASS
- Final replay: `work/apply_f4_109.py`; candidate SHA-256 `8e9000db5b0574d5203689eb70786babe01d59665dd51d09241f38f1f5c0cbc1`.
- F4-109 APPLIED: retained the unique Dânî/Ebû Dâvud classical-source and resm-zapt core in current P453 while replacing only the one-way print-causes-standardization/spread conclusion with the report-approved multicausal formulation.
- Printed mushafs are now framed as contributing to wider written reach, while teaching traditions, tashih institutions, qiraat expertise, regional preferences and official publication processes are also named. P454 remains unchanged for F4-110.
- Deterministic second replay is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical.
- Bounded render P450–456: 4/4 pages inspected; PASS.
- Durable boundary: last F4-109; next F4-110.


## F4-110 checkpoint — PASS
- Accepted replay: `work/apply_f4_110.py`, revision 4; candidate SHA-256 `fcdca872a3efc36b96e9f9d600fd23ba73b45a4fec4857ea5434df2b6dd1c807`. Revisions 1–3 were explicitly rejected from durable state because bounded rendering placed the future-research paragraph with the bibliography.
- F4-110 APPLIED: retained the unique ilmî-contribution core, separated the report-approved final judgment and future-research recommendation into distinct paragraphs, and kept `Kaynakça` as the bibliography boundary.
- Layout repair: existing bookmark-backed `Kaynakça` heading now carries explicit `pageBreakBefore` so the future-research paragraph remains part of Sonuç and bibliography begins on the following page. Heading text/bookmarks remain intact.
- Body paragraphs 675→676 because one additional future-research paragraph was created.
- Deterministic second replay is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical.
- Bounded render P452–458: 5/5 pages inspected; PASS.
- Durable boundary: last F4-110; next F4-111.


## F4-111 checkpoint — PASS
- Final replay: `work/apply_f4_111.py`; candidate SHA-256 `4c9eba6d4ca9e65dc7148921c8331a21f4768ecc3aed65c9c0deda0ff98166c9`.
- F4-111 APPLIED: normalized 4 eligible main-text `Kur’ân`/`Kur'an` occurrences to house-style `Kur’an` and 6 curated specific-name contexts to `İmam Mushaf`; bibliography and footnotes were excluded.
- Direct quotations and italic bibliographic work titles retain their original spelling. In particular Mervân’s quotation at P64 retains lower-case `imam mushafa`, while narrative specific-name usages are normalized.
- Deterministic second replay reports ALREADY_SATISFIED and is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML baseline-identical.
- Three bounded representative visual slices: P20–29 4/4 PASS; P62–85 8/8 PASS; P397–411 7/7 PASS; total 19/19 pages PASS.
- Durable boundary: last F4-111; next F4-112.


## F4-112 checkpoint — PASS
- Final replay: `work/apply_f4_112.py`; candidate SHA-256 `58e23edd3cdbffbacaf8a2e14fc2dff5ea5357dd76b15cda30c4d31820e12e9a`.
- F4-112 APPLIED: removed only the surviving editorial/work-note tails from genuine footnotes 32, 41 and 105; bibliographic citation content and all footnote IDs/body references are preserved.
- Deterministic second replay is byte-identical. Footnote-aware technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; only authorized target footnote text differs, target footnote OOXML structure unchanged.
- Visual QA used a P0–P118 prefix render to preserve the true footnote-reference sequence after bounded-slice rendering was found unsuitable for high-numbered footnotes. Real pages carrying FN32, FN41 and FN105 were inspected; all 3/3 target pages PASS.
- Durable boundary: last F4-112; next F4-113.


## F4-113 checkpoint — PASS
- Final replay: `work/apply_f4_113.py`; candidate SHA-256 `e4287570d99f9d3c20f96752497787e6d97f6a07047555ecbe5c05e5c69bdac1`.
- F4-113 APPLIED: normalized author-name article variants conservatively (`ed-Dânî` → `Dânî`, `ez-Zürkânî` → `Zürkânî`, `es-Suyûtî` → `Suyûtî`) and adopted articleless sura names only in explicit verified Qur'anic verse-reference contexts. Bibliographic work titles such as `el-Mukni‘` and `el-İtkân` remain untouched.
- Deterministic second replay is byte-identical. Technical gate: 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; canonical-to-candidate changed-footnote set exactly equals the authorized 31-ID set (including inherited F4-112 FN32/FN41/FN105); target footnote OOXML structure unchanged.
- Human visual QA: three representative slices (P50–75, P274–280, P389–401), workflow runs 32079868743 / 32080087101 / 32080209568; all 19/19 rasterized pages manually inspected and PASS. Bounded-render high-footnote renumbering limitation is explicitly documented; original footnote identity is established by the structural gate and full-candidate postflight.
- Durable boundary: last F4-113; next F4-114.


## F4-114 checkpoint — PASS
- Final replay: `work/apply_f4_114.py`; candidate SHA-256 `419bc27be6a259d03f42ed7da7f7bbf0b1f64c9af3ab6ed78393f6aa9a96ca56`.
- F4-114 APPLIED: removed the malformed Kahraman DOI URL from P578 and repaired Maşalı P599 to `https://doi.org/10.56361/usul.173700`. The DOI text was not inside `w:hyperlink`, so hyperlink objects/relationships remained unchanged.
- Deterministic second replay is ALREADY_SATISFIED and byte-identical. Application validator permits only P578/P599 changes from durable F4-113; all non-document package parts are byte-identical, 520 fields and Zotero/ADDIN inventory remain intact.
- Human visual QA P570–P605: workflow run 32080808433 / artifact 9305055721; 4/4 rasterized pages manually inspected and PASS. Bibliography line flow, italics and adjacent records remain clean.
- Durable boundary: last F4-114; next F4-115.


## F4-115 checkpoint — PASS
- Final replay: `work/apply_f4_115.py`; candidate SHA-256 `73ccdd0b5e0c63450cf611d175e5fcf547ac0b9a9aaaf11bf09a4e5db5c996bf`; body paragraphs 676→674.
- F4-115 APPLIED after full manuscript-use matching: FN2 confirms İbn Ebû Dâvud Vâiz 2002; FN8 confirms İbn Kuteybe en-Neccâr; FN109 confirms Süleymân b. Necâh Riyad 2000; FN373 confirms Süleymân b. Necâh Medine 1999.
- Removed only the demonstrably unused bibliography-result paragraphs: original P548 İbn Ebû Dâvud / Selîm b. Îde’l-Hilâlî / Amman 2006 and original P557 İbn Kuteybe / Muhammed Muhyiddîn el-Asfar / Beyrut 1999. Both Necâh editions and the cited Vâiz/en-Neccâr records remain.
- Deterministic second replay is ALREADY_SATISFIED and byte-identical. All non-document package parts are byte-identical to durable F4-114; 520 field instructions, ADDIN/Zotero field inventory, 469 footnote references, bookmarks, hyperlinks and RTL inventory are preserved.
- Human visual QA P495–P615: workflow run 32081290071 / artifact 9305200072; 9/9 rasterized pages manually inspected and PASS.
- Durable boundary: last F4-115; next F4-116.


## F4-116 checkpoint — VERIFIED_NO_CHANGE / PASS
- Final replay: `work/apply_f4_116.py`; output `manuscript-working-f4-116.docx` is byte-identical to durable F4-115 with SHA-256 `73ccdd0b5e0c63450cf611d175e5fcf547ac0b9a9aaaf11bf09a4e5db5c996bf`; body paragraphs remain 674.
- F4-116 VERIFIED_NO_CHANGE: FN86 explicitly proves use of the 1993 Velîd Müsâid et-Tabatabâî edition. FN394 cites p. 144; independent inspection of printed p. 144 of the Tayyar Altıkulaç 1975 scan directly matches the distinctive P377 claim, proving genuine use of the 1975 edition. Therefore both Ebû Şâme bibliography records are retained.
- Edition adjudication evidence: `work/F4-116-EDITION-ADJUDICATION.md`. The manuscript's `1/x` short forms were not treated as edition identifiers.
- Technical workflow PASS: 469/469 footnotes/references, 0 orphan/dangling/duplicate, 520 fields, inherited authorized footnote-text change set only.
- Human visual QA P500–P507: workflow run 32082193276 / artifact 9305471951; 2/2 rasterized pages manually inspected and PASS; both retained Ebû Şâme records are visible and layout-stable.
- A separate metadata discrepancy discovered during adjudication is carried into FOURTH_VALIDATE: the 1975 bibliography record currently says `2 Cilt`, while independent catalogue records describe the Altıkulaç 1975 edition as one volume. This was not silently expanded into F4-116.
- Fourth Report application boundary: F4-001–F4-116 complete. Next phase: FOURTH_VALIDATE; Fifth Report application remains blocked until validation passes.


## FOURTH_VALIDATE — PASS
- Durable Fourth input before global validation: `manuscript-working-f4-116.docx`, SHA `73ccdd0b5e0c63450cf611d175e5fcf547ac0b9a9aaaf11bf09a4e5db5c996bf`, body 674.
- Read-only global gate `work/runtime/FOURTH-VALIDATE-READONLY.txt`: 210 ledger rows; F4 items 116 complete; all 94 F5 items still PENDING; 469/469 footnotes/references; 520 fields; ADDIN 466; Zotero ITEM 465 + bibliography 1; bookmarks 53/53; hyperlinks 52; fatal errors 0. Exactly one residual defect was identified: FV-001 at P504, where the Ebû Şâme 1975 / Tayyar Altıkulaç bibliography record incorrectly stated `2 Cilt`.
- Independent catalogue evidence consistently identifies the 1975 Dâr Sadr / Tayyar Altıkulaç edition as a single-volume publication. FV-001 was remediated conservatively by removing only the visible result-text token ` 2 Cilt.`; F4-116's evidence-backed decision to retain both the 1975 and 1993 Ebû Şâme editions remains unchanged.
- Remediation replay `work/apply_fourth_validate_fv001.py`: first replay changes P504 only; second replay `ALREADY_SATISFIED`; byte-identical idempotency PASS. Final candidate SHA `c2ca1ee19360cb7d6176f26b1ff894160ebb9b4ecd0492fbaf38ce5b15531a95`; body remains 674.
- Final global validator `work/runtime/FOURTH-VALIDATE-FINAL.txt`: PASS; fatal 0; residual defects 0; all F4/F5 ledger and OOXML invariants PASS.
- Final technical gate `work/runtime/FOURTH-VALIDATE-FINAL-TECHNICAL.txt`: PASS on the final SHA.
- Final human visual QA P500–P507: workflow run 32082945226 / artifact 9305697542; 2/2 rasterized pages manually inspected and PASS. The corrected 1975 record and retained 1993 record render naturally with no bibliography layout regression.
- FOURTH_VALIDATE overall PASS. Fifth Report application is now authorized from the final validated Fourth binary; next item F5-001.


## F5-001 checkpoint — VERIFIED_NO_CHANGE / PASS
- Fifth target: replace a negative cem/istinsah contrast in the Giriş with a positive distinction.
- Current P19 after Fourth Report + FOURTH_VALIDATE already states that the Hz. Ebû Bekir cem and Hz. Osman istinsah were `farklı tarihsel şartlarda gerçekleştirilen iki ayrı uygulama olarak rivâyet edilmiştir`, followed by an explicit source-plurality/caution sentence. The Fifth literal negative target is absent.
- Fourth scientific/structural precedence therefore controls: replacing the accepted wording with the Fifth suggestion would add no correction and could weaken the historiographic safeguard carried by `rivâyet edilmiştir`.
- `work/apply_f5_001.py` verified the resolved P19 state and absence of the old target, then carried the binary forward byte-identically twice. Output SHA remains `c2ca1ee19360cb7d6176f26b1ff894160ebb9b4ecd0492fbaf38ce5b15531a95`.
- Structural inventory remains 674 body paragraphs, 469/469 genuine footnotes/references, 520 fields, ADDIN 466, Zotero ITEM 465 + bibliography 1, bookmarks 53/53, hyperlinks 52.
- Human visual QA: NOT_REQUIRED_NO_BYTE_CHANGE because the F5-001 output is byte-for-byte the already globally validated Fourth binary.
- Durable boundary: last F5-001; next F5-002.
