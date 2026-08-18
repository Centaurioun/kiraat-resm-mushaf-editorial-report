# F5-006 human visual QA — PASS

- Candidate: `artifacts/checkpoints/manuscript-working-f5-006.docx`
- SHA-256: `91a36064fdded4aa1ca72302ceb2d690f2a945fb921eb5ddc5f5e3b5efc1f092`
- QA export workflow run: `32087050595`
- Artifact: `application-qa-export`, ID `9307054073`
- SHA-locked range: P24–P27
- Rendered with the canonical DOCX renderer / LibreOffice; rendered pages: 3

All **3/3 pages** were inspected individually.

- Page 1: preserved TOC-field context only; known bounded-slice artifact, not an F5-006 regression.
- Page 2: P25 now begins directly with the source-based İbnü’l-Cezerî definition. Paragraph spacing, line wrapping and footnote placement are normal. The next sentence `Bir kırâat imamına nispet edilen ... aynı düzeyde değildir.` remains visibly intact as the pending F5-007 target.
- Page 3: P26/P27 and their footnotes render cleanly. No clipping, overlap, unexpected run-formatting propagation, footnote overflow, or edit-caused page-flow defect was observed.

Later negative constructions visible in P25–P27 belong to F5-007+ and were intentionally not altered by F5-006.

**Verdict: F5-006 HUMAN VISUAL QA = PASS (3/3).**
