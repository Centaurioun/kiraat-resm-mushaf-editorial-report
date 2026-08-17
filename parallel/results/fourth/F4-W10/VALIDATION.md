# F4-W10 Validation Record

## Frozen input evidence

Repository baseline authority (`parallel/baselines/F4-047-BASELINE.json`) identifies F4-047 logical SHA-256:

`6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7`

Repository validation for that checkpoint records: 469 footnotes / 469 references, 520 fields, 465 Zotero item fields + 1 bibliography field, 53/53 bookmark start/end IDs, 52 hyperlinks, 365 RTL markers, 10 sections, no comments/revisions, no orphan/dangling/duplicate footnote-reference problems, and valid ZIP/XML structure.

## Replay static validation

- `python -m py_compile replay_f4_w10.py` — **PASS**.
- Replay has an exact F4-047 SHA gate for worker-proof execution.
- Replay has deterministic unique-anchor checks and hard failures on 0/2+ hits where a unique target is required.
- Genuine footnote 32/41/105 structure is checked before/after excluding text content; IDs/reference sets are globally checked unchanged.
- All `w:instrText` values are protected exact before/after; target DOI inside an instruction field causes failure.
- All ZIP members outside `document.xml`, `footnotes.xml`, and `document.xml.rels` are required byte-identical.

## Synthetic OOXML replay test

A task-specific synthetic `.docx` fixture was created locally with:

- genuine footnotes 32, 41, 105, 86 and 131;
- exact stale work-note strings;
- Kahraman and Maşalı DOI hyperlink relationships;
- the two remove-edition entries;
- all six required keep-edition anchors;
- a protected `ZOTERO_BIBL` instruction field.

Results:

1. First replay — **PASS**. Only `word/footnotes.xml`, `word/document.xml`, and `word/_rels/document.xml.rels` changed. Footnote work notes were removed; Kahraman malformed DOI was removed; Maşalı DOI was corrected; only the two authorized unused editions were removed; required keep entries remained; field instruction and protected structures remained exact.
2. Second replay — **PASS**. All edit targets reported already satisfied; keep-records remained verified; `changed_parts=[]`.
3. First and second output DOCX files were **byte-identical** (`cmp` success), demonstrating replay idempotency for the implemented transformations.

## Real F4-047 execution boundary

The source DOCX exists in GitHub (`source/manuscript/current/redaktorden_gelen.docx`, 406,091 bytes) and the repository supplies its frozen logical F4-047 SHA/validation evidence. In this ChatGPT runtime, GitHub exposed the binary only through connector/base64 responses while the local execution container could not retrieve the raw GitHub binary. Consequently:

- **Not claimed:** that W10's replay has been executed on the real F4-047 binary in this worker runtime.
- **Claimed:** repository evidence resolves all four task decisions; the replay compiles; deterministic and preservation behavior passes a purpose-built OOXML fixture; the exact-baseline gate and integration-time self-validation are encoded.

This limitation is transport/runtime-specific, not a bibliographic ambiguity. Integration acceptance must run the worker-proof baseline command where the F4-047 binary is locally available, then replay on the cumulative lineage, inspect the JSON validation report, and complete visual QA.

## Disposition

`READY_FOR_INTEGRATION`, subject to the mandatory real-binary replay and visual-QA gates above. No canonical acceptance is asserted by this worker.
