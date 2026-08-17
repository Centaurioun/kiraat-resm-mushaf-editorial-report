# F4-078 bounded visual QA

- Candidate: `artifacts/checkpoints/manuscript-working-f4-078.docx`
- Candidate SHA-256: `131913a4e602ec88fa0582ebe1cd40cfe8f9c1e9461c5692d12d4c4b36465e6f`
- QA range: current body paragraphs 295–350, spanning the end of 3.6, the complete consolidated 3.7 cluster, and the Fourth Section boundary.
- Rendered pages: 17.
- Technical validation before render: PASS.
- Visual result: PASS after one bounded style repair.

## Inspection record

The first render identified one batch-caused defect: the five former 3.8–3.12 heading paragraphs had been demoted to `Normal` paragraph style but retained direct run-level heading formatting and therefore rendered bold. `work/apply_f4_078_v2.py` removed only direct formatting from those five transition paragraphs while preserving their bookmarks and all protected structures. The repaired candidate was replayed twice with byte-identical output and rerendered.

All 17 pages were adjudicated. In the second render, 9 changed pages were reinspected directly; the remaining 8 pages were pixel-identical to the already inspected first render. The five transition paragraphs now render as normal body prose. The consolidated 3.7 heading renders correctly, Arabic/RTL examples remain intact, footnotes do not overflow, and the Fourth Section boundary remains intact. Existing red editorial text is pre-existing and outside F4-078's scope.

## Derived-field note

The Word table of contents still displays the pre-consolidation 3.7–3.12 headings because the TOC is a derived field and has not been recalculated in this citation-safe replay workflow. Do not rebuild or rewrite TOC field structures during Fourth Report application. A final Word field/TOC refresh is required after editorial application and before final delivery.

**Verdict: PASS.**
