# F5-002 authoritative human visual QA — PASS

## Candidate identity

- DOCX: `artifacts/checkpoints/manuscript-working-f5-002.docx`
- SHA-256: `94de5908c68755855314954102dd946b6c3b594a200617caecedd9e6c5b7b3be`
- Deterministic replay evidence: `work/runtime/F5-002-AUTH-REBUILD-REPLAY.txt`
- Postflight: `work/runtime/F5-002-AUTH-REBUILD-POSTFLIGHT.txt`

## SHA-locked QA export

- Workflow: `application-qa-export`
- Workflow run: `32085611811`
- Artifact: `application-qa-export`, artifact ID `9306592869`
- Exported bounded range: body paragraphs P20–P24
- Export manifest independently records the same candidate SHA-256 and body paragraph count 674.

The exported `slice.docx` was downloaded from the GitHub Actions artifact, converted locally with LibreOffice, and the resulting PDF was rendered at 180 DPI for manual inspection.

## Human inspection

Rendered pages: **3**.

All **3/3 pages** were inspected individually.

### Page 1

- Preserved Word TOC field renders before the bounded body slice; this is the known bounded-slice/field-context artifact and is not an F5-002 manuscript regression.
- No clipping, overlap, broken glyphs, or abnormal layout was observed.

### Page 2

- P20 and P21 render normally.
- F5-002 P22 begins visibly with `Araştırma soruları birbirine bağlıdır.`.
- The preserved Fourth-scientific continuation follows naturally and retains normal paragraph/run formatting.
- No unexpected bold/italic propagation, punctuation damage, clipping, overlap, or abnormal whitespace.

### Page 3

- The continuation of P22 renders normally across the page break.
- P23 and P24 retain their existing layout and typography.
- The red `değil` in P23 is a pre-existing F5-003 target, not introduced by F5-002; it is deliberately left for the next report item.
- Footnote region renders cleanly; no overflow or collision is visible.

## Verdict

- Candidate identity: **PASS**
- Bounded layout: **PASS**
- P22 new first sentence: **PASS**
- Preserved P22 continuation: **PASS**
- Footnote-zone/layout stability: **PASS**
- Human visual QA: **3/3 PASS**

**F5-002 visual acceptance gate = PASS.**
