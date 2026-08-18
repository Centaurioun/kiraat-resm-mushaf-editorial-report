# F5-009 HUMAN VISUAL QA

- Candidate: `artifacts/checkpoints/manuscript-working-f5-009.docx`
- Candidate SHA-256: `ff35f3803f24f68dff43f2ce9569c39a275c03acfa518614803e48530d696dbd`
- QA export workflow run: `32090746409`
- QA export artifact: `9308227484` (`application-qa-export`)
- Bounded source paragraphs: `25..28`
- Render path: exported `slice.docx` rendered with LibreOffice via the canonical DOCX renderer
- Rendered pages inspected: `3/3`
- Result: **PASS**

## Page-by-page inspection

### Page 1
- Expected bounded-slice TOC-field artifact is visible (`İÇİNDEKİLER`).
- No clipping, overlap, broken glyphs, or rendering corruption observed.
- Treated as the known slice artifact, not as an F5-009 regression.

### Page 2
- P25 and the beginning/majority of P26 render normally.
- F5-008 real/ihtimalî conformity wording remains intact.
- F5-009 first positive sentence renders with normal punctuation and spacing:
  `Sahih, meşhur, âhâd ve şâz nitelemeleri, naklin güvenilirliği, yaygınlığı, kabulü ve genel tilâvet alanındaki konumuyla ilgili farklı değerlendirme boyutlarını ...`
- No run-boundary whitespace defect analogous to the rejected F5-007 R1 candidate is visible.
- Footnote markers and footnote block placement are visually coherent.

### Page 3
- The carried line begins cleanly with `ifade eder. Şâz...`; the sentence boundary has a visible, correct space after the period.
- F5-009 second positive sentence renders cleanly:
  `Şâz bir rivâyetin tefsîrî veya dilsel bilgi değeri ile bağlayıcı kırâat statüsü ayrı ayrı değerlendirilmelidir.`
- P27 and P28 remain visually intact and flow normally after the edited paragraph.
- No clipping, overlap, missing characters, abnormal indentation, or punctuation/spacing regression observed.
- Footnote placement remains normal.

## Acceptance judgment

Human visual QA: **PASS — 3/3 pages inspected**.

The candidate is visually eligible for durable F5-009 checkpointing, subject to the already-passed deterministic replay/integrity evidence. No F5-010+ text was adjudicated or applied in this QA step.
