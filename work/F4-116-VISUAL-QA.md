# F4-116 Visual QA — PASS / VERIFIED_NO_CHANGE

Candidate: `artifacts/checkpoints/manuscript-working-f4-116.docx`

SHA-256: `73ccdd0b5e0c63450cf611d175e5fcf547ac0b9a9aaaf11bf09a4e5db5c996bf`

The candidate is **byte-identical** to durable F4-115. F4-116 is an edition-use adjudication and requires no manuscript change because both Ebû Şâme editions are genuinely used.

## Edition-use adjudication

See `work/F4-116-EDITION-ADJUDICATION.md`.

- 1993 Velîd Müsâid et-Tabatabâî edition: **KEEP** — FN86 is a full edition-specific 1993 citation at p. 212.
- 1975 Tayyar Altıkulaç edition: **KEEP** — FN394 cites p. 144, and printed p. 144 of the 1975 scan was independently inspected and directly matches the distinctive P377 claim carried by FN394.
- The short `1/x` forms were not treated as edition identifiers because independent catalogue metadata describes both relevant editions as single-volume publications.
- No bibliography record was removed under F4-116.

A separate metadata discrepancy was discovered: the current 1975 bibliography record says `2 Cilt`, whereas independent catalogue records describe the Altıkulaç 1975 edition as one volume. This is intentionally **not silently folded into F4-116** and is carried forward to FOURTH_VALIDATE.

## Deterministic no-op validation

Replay: `work/apply_f4_116.py`

- input: durable F4-115;
- output: `manuscript-working-f4-116.docx`;
- input/output SHA-256: identical `73ccdd0b5e0c63450cf611d175e5fcf547ac0b9a9aaaf11bf09a4e5db5c996bf`;
- body paragraphs: 674;
- output bytes: **identical**;
- both bibliography records: present once at current P504/P505;
- FN86: explicit 1993 full citation preserved;
- FN394: p. 144 short citation preserved and still referenced by P377;
- footnotes/references: 469/469;
- fields: 520; ADDIN 466; Zotero ITEM 465; Zotero bibliography 1;
- bookmarks 53/53; hyperlinks 52.

Second replay is byte-identical/idempotent.

## Technical validation

`work/runtime/F4-116-TECHNICAL-VALIDATION.txt` = **PASS**.

- candidate SHA locked to the byte-identical F4-115/F4-116 SHA;
- genuine footnotes/references 469/469;
- reference identity multiset canonical-equal;
- orphan/dangling/duplicate 0/0/0;
- field instructions 520;
- inherited authorized F4-112/F4-113 footnote text differences remain the only authorized footnote changes.

## Human visual review

- Range: P500–P507
- Workflow run: `32082193276`
- Artifact: `application-bounded-qa-pages`, artifact ID `9305471951`
- Rasterized pages: **2/2 manually inspected**
- Verdict: **PASS**

Observed:

- both Ebû Şâme bibliography records are visibly present and distinct;
- the 1975 Altıkulaç and 1993 Tabatabâî records render normally;
- hanging-indent behavior, italics, punctuation and adjacent bibliography records remain intact;
- no clipping, overlap, style propagation or F4-116-attributable layout change exists;
- the first rendered TOC page is the known bounded-render field-context artefact, not a manuscript regression.

## Final adjudication

- report criterion resolved: **PASS**
- 1975 use proven: **PASS**
- 1993 use proven: **PASS**
- manuscript change required: **NO**
- deterministic byte-identical carry-forward: **PASS**
- technical validation: **PASS**
- human visual QA: **PASS (2/2 pages)**

**Overall F4-116 verdict: VERIFIED_NO_CHANGE / PASS.**

After durable checkpointing, the state machine must enter **FOURTH_VALIDATE**. Do not start Fifth Report application before Fourth Report global validation passes.
