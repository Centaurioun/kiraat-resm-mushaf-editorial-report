# F4-102 Bounded Visual QA

## Verdict

PASS — 4/4 rendered pages inspected for layout.

## Candidate

- DOCX: `artifacts/checkpoints/manuscript-working-f4-102.docx`
- SHA-256: `38561f498d0abacc3dacea2bb35b92aa1ed4abe67d8b767657ea80e759ff69e8`
- Bounded range: P422–P431

## Visual findings

- The bookmark-backed 4.7 heading renders correctly and is followed immediately by the new print/resm-focused opening.
- The compressed historical-background material is visually integrated without clipping, overlap, blank-page creation, broken heading flow, or visible RTL/layout regression.
- P425+ and the later Saint Petersburg target remain visibly present and unchanged for subsequent Fourth Report items.
- The pre-existing red Huzai editorial note remains visible and is outside F4-102 scope.

## Footnote-render caveat

The bounded QA workflow creates `slice.docx` by removing body paragraphs outside the requested range while copying the full original `word/footnotes.xml` containing all 469 footnotes. LibreOffice renumbers/re-associates the sparse high-ID footnote references in that isolated slice for display, so the footnote *text shown in the slice PDF* is not authoritative for proposition-to-`w:id` mapping.

For F4-102 citation safety, the authoritative evidence is therefore the candidate OOXML/preflight plus the technical invariant gate:

- current P423 contains genuine `w:footnoteReference/@w:id=454`;
- current P424 contains genuine `w:footnoteReference/@w:id=455`;
- preflight resolves FN454 to `Sâlih, Mebâhis, 99.` and FN455 to Ibn Kesîr, `Tefsîru’l-Kur’âni’l-Azîm`, 1/30;
- `word/footnotes.xml` is baseline-identical;
- 469 footnotes / 469 references; no orphan, dangling or duplicate reference; reference identity multiset canonical-equal.

Accordingly, the render is used only for bounded page/layout QA, not for validating footnote-content identity in the isolated slice.
