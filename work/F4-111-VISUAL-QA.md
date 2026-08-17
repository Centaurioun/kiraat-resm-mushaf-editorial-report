# F4-111 Visual QA — PASS

- Candidate: `artifacts/checkpoints/manuscript-working-f4-111.docx`
- SHA-256: `4c9eba6d4ca9e65dc7148921c8331a21f4768ecc3aed65c9c0deda0ff98166c9`
- Scope: main-text house-style normalization only; bibliography and `word/footnotes.xml` excluded.
- Replay result: 4 nonpreferred `Kur’an` spellings normalized in eligible narrative runs; 6 curated `İmam Mushaf` narrative contexts normalized. Italic bibliographic titles and direct quotations were deliberately preserved.

## Bounded visual QA

- Slice A, P20–29: **4/4 PASS** — conceptual definition area; `İmam Mushaf` definition and `Kur’an` house style render normally.
- Slice B, P62–85: **8/8 PASS** — Mervân quotation remains lower-case/original inside direct quotation while narrative `İmam Mushaf` usage is normalized; no layout regression.
- Slice C, P397–411: **7/7 PASS** — later resm/modern-mushaf prose and specific-name normalization render normally; bibliographic title spellings in notes remain untouched.
- Total inspected: **19/19 pages PASS**.

No clipping, overlap, unintended blank page, indentation regression, or RTL corruption was observed. Existing red direct-formatting/editorial marks visible in some source paragraphs predate F4-111 and were not created or modified by this item.

Technical validation: PASS; 469/469 footnotes/references; 0 orphan/dangling/duplicate; 520 fields; protected OOXML parts baseline-identical.
