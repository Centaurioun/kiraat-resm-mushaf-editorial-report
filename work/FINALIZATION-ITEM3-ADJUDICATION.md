# FINALIZATION ITEM 3 — Editorial / Red-Font Mark Cleanup Adjudication

## Scope
Current accepted input: `artifacts/finalization/manuscript-field-refreshed.docx`

SHA-256: `a5ee8d96fe870086a54da1b6feb95749e443907b97f8e8bfa5b16cae199814c5`

This item is formatting-only. Fourth/Fifth scientific and editorial text is frozen. No wording, citation, field instruction, bookmark target, RTL content, paragraph order, or footnote identity may change.

## Inventory / classification
A full-package inspection of the accepted field-refreshed candidate found direct red font formatting (`w:color w:val="FF0000"`) only in:

- `word/document.xml`: 296 direct red-color nodes across 126 body paragraphs;
- `word/footnotes.xml`: 27 direct red-color nodes across six genuine footnotes (FN32, FN41, FN75, FN89, FN105, FN216).

No `FF0000` direct color occurs in any other OOXML part. The red formatting appears on heterogeneous prose fragments, isolated punctuation/whitespace, names, source-reporting phrases, and bibliographic fragments rather than on a coherent semantic class. The document contains no tracked insertions/deletions, no Word comments, and no highlight layer that would otherwise encode an unresolved review instruction. The pattern is therefore adjudicated as inherited editorial/revision markup, not intentional publication typography.

Blue hyperlink formatting and other non-red color values are outside this item and must be preserved.

## Authorized transformation
Remove only direct run-color elements whose exact value is `FF0000` from `word/document.xml` and `word/footnotes.xml`. Do not replace text, do not recolor hyperlinks, do not normalize styles, and do not accept/reject any content because no tracked changes are present.

The cleanup must preserve:

- all body text byte-for-byte at text-node level;
- body paragraph count 674;
- 469/469 genuine footnote references and footnote IDs/order;
- Zotero/ADDIN 466;
- TOC/PAGEREF/PAGE field instructions from item 1;
- bookmarks 53/53 and current TOC links;
- Arabic/RTL structural inventory;
- `w:updateFields=true`;
- all non-target OOXML member contents.

## Acceptance criteria

1. Pre-cleanup red nodes exactly 296 + 27.
2. Post-cleanup direct `FF0000` nodes = 0 in the whole package.
3. Accepted narrative/body-text hash unchanged.
4. Footnote text and reference integrity unchanged.
5. Non-target package members byte-identical at uncompressed-content level.
6. Deterministic second replay byte-identical.
7. Full-document render and every-page human visual QA PASS.

If any red run is found to encode a still-unresolved textual instruction rather than mere formatting, stop and create a HOLD instead of silently changing wording.
