# F4-W10 Deterministic Replay Specification

Replay artifact: `parallel/results/fourth/F4-W10/replay_f4_w10.py`

## Scope

The replay implements only F4-112, F4-114, F4-115 and F4-116. It does not implement or alter F4-111/F4-113, any other Fourth item, any Fifth item, the ledger, canonical branch selection, or integrator-owned state.

## Worker-proof invocation on the frozen F4-047 baseline

```bash
python parallel/results/fourth/F4-W10/replay_f4_w10.py \
  /path/to/F4-047.docx /tmp/F4-W10.docx \
  --require-f4-047-sha \
  --report-json /tmp/F4-W10-report.json
```

`--require-f4-047-sha` rejects any input whose SHA-256 is not exactly:

`6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7`

It also requires the frozen F4-047 inventory (469 footnote IDs/references, 520 fields, 465 Zotero item markers, one Zotero bibliography marker, 365 RTL markers, 10 sections).

## Integrator invocation on the cumulative lineage

Because W10 is replayed after earlier Fourth workers, cumulative input bytes will no longer equal F4-047. The integrator must therefore omit the baseline-SHA switch while retaining all fail-closed anchors/invariants:

```bash
python parallel/results/fourth/F4-W10/replay_f4_w10.py \
  /path/to/cumulative-before-W10.docx /tmp/cumulative-after-W10.docx \
  --report-json /tmp/F4-W10-integrator-report.json
```

## Authorized transformations

1. **F4-112:** locate genuine `word/footnotes.xml` footnotes `w:id=32`, `41`, `105`; remove only the three exact stale work-note strings. Preserve all element/attribute structure inside each footnote.
2. **F4-114 Kahraman:** locate the unique malformed DOI. Remove it, with no invented replacement. If it is a standalone safe paragraph, remove that paragraph; otherwise remove only the exact DOI text. Remove only an associated hyperlink relationship that has become unreferenced.
3. **F4-114 Maşalı:** replace the unique duplicated DOI resolver with the single correct resolver. If the DOI is in a hyperlink, update only that relationship target.
4. **F4-115:** remove exactly two unused edition paragraphs: İbn Ebû Dâvud 2006 (Selîm b. Îde'l-Hilâlî) and İbn Kuteybe 1999 (Muhammed Muhyiddîn el-Asfar). A paragraph containing field codes, bookmarks, footnote references, comments, section properties, drawings or objects is rejected as unsafe.
5. **F4-115/116 preservation:** fail if any of the required retained edition anchors is absent. Preserve both `Muhtasaru't-tebyîn` editions and both Ebû Şâme editions.
6. **F4-116 citation anchors:** require genuine footnote 86 to retain the 1993 full-citation anchor/page 212 and genuine footnote 131 to retain the `el-Murşidu'l-vecîz, 1/173` short-citation anchor.

## Protected invariants

The replay requires exact before/after equality for:

- complete `w:footnote/@w:id` sequence;
- complete body `w:footnoteReference/@w:id` sequence;
- `w:fldChar` count;
- every `w:instrText` value (therefore all Zotero field instructions);
- Zotero item and bibliography marker counts;
- bookmark start/end IDs;
- RTL marker count;
- section count;
- comment markers;
- tracked revision markers.

The ZIP member set must remain exact. Every XML/RELS part must parse. All OOXML members outside these three explicitly permitted parts must remain byte-identical:

- `word/document.xml`
- `word/footnotes.xml`
- `word/_rels/document.xml.rels`

A target DOI detected inside `w:instrText` causes a hard failure; the replay never rewrites a Zotero/Word field instruction.

## Idempotency

Run the replay a second time on its own output without the baseline-SHA switch:

```bash
python parallel/results/fourth/F4-W10/replay_f4_w10.py \
  /tmp/F4-W10.docx /tmp/F4-W10-second.docx \
  --report-json /tmp/F4-W10-second.json
cmp /tmp/F4-W10.docx /tmp/F4-W10-second.docx
```

Expected second-run statuses are `ALREADY_SATISFIED` for edits and `VERIFIED_PRESENT` for required retained entries, with `changed_parts=[]`; `cmp` must return zero.

## Fail-closed conditions

Replay aborts on SHA mismatch when the baseline gate is requested, missing or duplicate genuine footnote IDs, non-unique bibliography/DOI anchors, target DOI inside field instructions, unsafe bibliography paragraph structure, missing keep-records, missing F4-116 citation anchors, protected-invariant drift, unexpected ZIP member changes, protected-part byte drift, or malformed XML.
