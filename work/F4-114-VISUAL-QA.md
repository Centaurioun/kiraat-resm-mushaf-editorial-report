# F4-114 Visual QA — PASS

Candidate: `artifacts/checkpoints/manuscript-working-f4-114.docx`

SHA-256: `419bc27be6a259d03f42ed7da7f7bbf0b1f64c9af3ab6ed78393f6aa9a96ca56`

## Application

- Replay script: `work/apply_f4_114.py`
- Durable input: F4-113 SHA `e4287570d99f9d3c20f96752497787e6d97f6a07047555ecbe5c05e5c69bdac1`
- Kahraman P578: malformed DOI URL removed entirely; record now ends `11-36.`
- Maşalı P599: duplicated DOI prefix repaired to `https://doi.org/10.56361/usul.173700`.
- Target DOI text was confirmed not to be inside `w:hyperlink`; hyperlink objects/relationships therefore required no modification.
- Deterministic second replay: **ALREADY_SATISFIED / byte-identical PASS**.
- Application validator permits only P578 and P599 to differ from durable F4-113 on first replay and requires zero differences on second replay.

## Technical validation

`work/runtime/F4-114-TECHNICAL-VALIDATION.txt` = **PASS**.

- body paragraphs: 676;
- footnotes/references: 469/469;
- orphan/dangling/duplicate: 0/0/0;
- field instructions: 520;
- Zotero/ADDIN inventory preserved by deterministic application validator;
- hyperlinks: 52, unchanged by deterministic application validator;
- inherited authorized F4-112/F4-113 footnote text differences remain structurally unchanged;
- all non-`word/document.xml` package parts are byte-identical to durable F4-113 in the F4-114 application validator.

## Human visual review

- Range: P570–P605
- Workflow run: `32080808433`
- Artifact: `application-bounded-qa-pages`, artifact ID `9305055721`
- Rasterized pages: **4/4 manually inspected**
- Verdict: **PASS**

Observed:

- Kahraman bibliography record renders cleanly without a dangling URL, spacing gap, or punctuation defect.
- Maşalı DOI renders once as `https://doi.org/10.56361/usul.173700` with normal line flow.
- Bibliography hanging-indent/paragraph flow, italics and adjacent records remain visually intact.
- No clipping, overlap, style propagation, blank-page regression or field-result corruption is visible.
- The leading TOC page is a known bounded-render field-context artefact and is not a manuscript regression.

## Final adjudication

- deterministic replay/idempotency: **PASS**
- technical validation: **PASS**
- postflight DOI content: **PASS**
- human visual QA: **PASS (4/4 pages)**

**Overall F4-114 verdict: PASS.**
