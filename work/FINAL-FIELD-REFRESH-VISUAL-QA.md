# Final Field Refresh — Focused Visual QA

- Candidate: `artifacts/finalization/manuscript-field-refreshed.docx`
- SHA-256: `a5ee8d96fe870086a54da1b6feb95749e443907b97f8e8bfa5b16cae199814c5`
- SHA-locked full candidate QA export: workflow run `32189159596`, artifact `9343561312`
- QA export range: P0–P673 (complete body exported for verification)
- Visual scope for finalization item 1: generated TOC/front matter and immediate body transition only. Full all-page manuscript acceptance is intentionally deferred to finalization item 2.

A render-only focused DOCX was built locally from the SHA-locked QA export by retaining the TOC SDT and the first 24 direct body paragraphs. The accepted candidate bytes were not modified by this rendering-only slice. It was rendered with `/home/oai/skills/docx/render_docx.py` and produced 6 pages.

## Page-by-page inspection

1. Title page: clean; no clipping, overlap, missing glyphs, or field-refresh artefact.
2. TOC page i: refreshed headings and cached page numbers render cleanly. Demoted/stale former headings are absent. The long 1.9.2 entry wraps naturally and retains page number 32.
3. TOC page ii: Fourth Chapter entries, `Sonuç` (94), and `Kaynakça` (98) render cleanly. Long entries wrap without overlap; no stale 2.4 or former 3.8–3.12 generated entries appear.
4. Önsöz page 1: clean transition from refreshed front matter into body; accepted prose unchanged.
5. Giriş page 2: clean body/footnote rendering; no field-refresh-induced style or pagination defect observed.
6. Giriş continuation page 3: clean body/footnote rendering. The visible red `değil` is a pre-existing editorial-format mark and was not introduced by field refresh.

## Independent field cross-check

LibreOffice was used only in memory as an independent ContentIndex/pagination engine; the document was not saved from LibreOffice. Updating the generated content index returned exactly the same page cache for all 46 retained TOC entries as the surgical candidate. See `work/runtime/FINAL-FIELD-REFRESH-LO-CROSSCHECK.txt`.

The previously tested LibreOffice DOCX round-trip was not accepted because saving through LibreOffice rewrote protected OOXML structures. The durable candidate therefore remains the surgical OOXML refresh, which changes only `word/document.xml` and `word/settings.xml` and instructs Microsoft Word to update fields on open.

**Result: PASS — 6/6 focused field/front-matter pages inspected; 46/46 TOC page-cache values independently cross-checked.**

This closes finalization item 1 only. Full-document all-page acceptance/layout QA remains the next separate finalization task.
