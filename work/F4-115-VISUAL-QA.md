# F4-115 Visual QA — PASS

Candidate: `artifacts/checkpoints/manuscript-working-f4-115.docx`

SHA-256: `73ccdd0b5e0c63450cf611d175e5fcf547ac0b9a9aaaf11bf09a4e5db5c996bf`

## Evidence-based edition decisions

Current-manuscript footnote evidence reconfirmed the Fourth Report decisions before any deletion:

- FN2 cites İbn Ebû Dâvud, `Kitâbu’l-mesâhif`, Muhibbüddîn Abdüssübhân Vâiz, Beyrut 2002 → **keep 2002**.
- No current footnote use of the Selîm b. Îde’l-Hilâlî el-Eserî, Amman 2006 record was found → **remove unused 2006 bibliography record**.
- FN8 cites İbn Kuteybe, `Te’vîlu muhtelifu’l-hadîs`, Muhammed Zuhrî en-Neccâr, ts. → **keep en-Neccâr**.
- No current footnote use of the Muhammed Muhyiddîn el-Asfar, Beyrut 1999 record was found → **remove unused el-Asfar bibliography record**.
- FN109 cites Ebû Dâvud Süleymân b. Necâh, `Muhtasaru’t-tebyîn`, Riyad 2000 → **keep 2000**.
- FN373 cites the same work, Medine 1999 → **keep 1999**.

Thus only the original bibliography-result paragraphs P548 (İbn Ebû Dâvud 2006) and P557 (İbn Kuteybe el-Asfar 1999) were removed.

## Deterministic application

- Durable input: `artifacts/checkpoints/manuscript-working-f4-114.docx`
- Input SHA-256: `419bc27be6a259d03f42ed7da7f7bbf0b1f64c9af3ab6ed78393f6aa9a96ca56`
- Replay: `work/apply_f4_115.py`
- Candidate SHA-256: `73ccdd0b5e0c63450cf611d175e5fcf547ac0b9a9aaaf11bf09a4e5db5c996bf`
- Body paragraph count: **676 → 674**
- First replay: output paragraph sequence equals input sequence with exactly original P548 and P557 removed.
- Second replay: **ALREADY_SATISFIED / byte-identical PASS**.
- All non-`word/document.xml` package parts are byte-identical to durable F4-114.
- Word/Zotero field instructions are preserved; bibliography field is not flattened or rebuilt.

## Postflight

Confirmed on the F4-115 candidate:

- unused İbn Ebû Dâvud 2006 record: **absent**;
- unused İbn Kuteybe el-Asfar 1999 record: **absent**;
- İbn Ebû Dâvud Vâiz 2002 record: **present once**;
- İbn Kuteybe en-Neccâr record: **present once**;
- Süleymân b. Necâh Riyad 2000 record: **present once**;
- Süleymân b. Necâh Medine 1999 record: **present once**.

## Technical validation

`work/runtime/F4-115-TECHNICAL-VALIDATION.txt` = **PASS**.

- footnotes/references: 469/469;
- reference identity multiset: canonical-equal;
- orphan/dangling/duplicate: 0/0/0;
- field instructions: 520;
- inherited authorized F4-112/F4-113 footnote text changes remain structurally authorized;
- deterministic application validator additionally verifies ADDIN 466, Zotero ITEM 465, Zotero bibliography 1, bookmarks 53/53, hyperlinks 52, RTL inventory unchanged, and all non-document package parts byte-identical to F4-114.

## Human visual review

- Range: P495–P615 of the 674-paragraph candidate
- Workflow run: `32081290071`
- Artifact: `application-bounded-qa-pages`, artifact ID `9305200072`
- Rasterized pages: **9/9 manually inspected**
- Verdict: **PASS**

Observed across every rendered page:

- bibliography paragraph flow and hanging-indent behavior remain normal;
- italics and mixed transliteration typography remain intact;
- no clipping, overlap, orphaned partial entry, doubled blank line, or style propagation appears at either deletion point;
- Vâiz 2002 and en-Neccâr retained records render normally in their new adjacency;
- both Necâh editions (Riyad 2000 and Medine 1999) render normally and remain distinct;
- no F4-115-attributable page-break or field-result corruption is visible.

The leading TOC page and the large trailing blank area on the final bounded page are expected consequences of the bounded rendering context, not candidate-manuscript regressions.

## Final adjudication

- evidence-to-edition matching: **PASS**
- deterministic replay/idempotency: **PASS**
- postflight target/remnant checks: **PASS**
- technical validation: **PASS**
- human visual QA: **PASS (9/9 pages)**

**Overall F4-115 verdict: PASS.**
