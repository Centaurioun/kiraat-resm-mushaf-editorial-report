# F4-077 Bounded Visual QA

- Candidate: `artifacts/checkpoints/manuscript-working-f4-077.docx`
- SHA-256: `9b8eea35a108e9cefe160e5d7f4975f9adbc278d2a6883cd016a3b67fa46a56c`
- QA range: current paragraphs 278–315
- Rendered pages: 14
- Final pages visually inspected: 14/14
- Final result: **PASS**

## Findings

1. F4-073 new 3.5 heading renders correctly. The P282 Arabic `أم` runs remain RTL and visually intact; FN281 and following source notes remain readable. The duplicate second 3.5 mini-conclusion is absent.
2. F4-074 structural reordering of 3.6 renders coherently: normativity, historical-origin/tevkîf debate, language/nahw material, hikmet interpretations, Ibn Haldun criticism/response, and the later binding-status views occur in the intended conceptual order.
3. F4-075 Ibn Haldun/response synthesis renders normally. The semantic citation placement is preserved: the Ibn Haldun source and later-response source appear with their corresponding propositions.
4. F4-076 balanced three-level conclusion renders normally and does not create an orphan heading or abnormal page break.
5. F4-077 moved the three-view modern/general-orthography classification into 3.6. The moved block renders across pages 7–9 without clipping or duplication; FNs319–324 move with their supported source material. The stale old 3.7 classification synthesis is absent.
6. Initial visual QA was rejected because two run-boundary spaces rendered as `değerlendirilmemelidir.Bu` and `aramıştır.Bu`. Raw text contained spaces, but the leading-space `w:t` nodes lacked `xml:space="preserve"`.
7. `work/apply_f4_073_077_v3.py` adds whitespace-preservation only to the affected structural paragraphs. The v3 candidate is byte-idempotent on its second replay.
8. Final full-resolution review confirms both boundaries now render correctly as `değerlendirilmemelidir. Bu` and `aramıştır. Bu`.
9. No clipping, overlap, footnote overflow, unexpected blank page, broken heading, RTL corruption, or new batch-induced font/style propagation was observed on any of the 14 pages.
10. Pre-existing red Fifth-style targets and red footnote-internal/editorial work notes visible later in the slice were not introduced by F4-073–077 and remain for their designated later Fourth/Fifth items.

## Paired technical gate

`work/runtime/F4-077-TECHNICAL-VALIDATION.txt` records PASS: 469 genuine footnotes, 469 references, canonical-equal reference identity/multiplicity, zero orphan/dangling/duplicate references, 520 field instructions, and baseline-identical protected OOXML parts. The body-reference order changed because F4-077 intentionally moved source-backed paragraphs; this accepted structural change is tracked explicitly while footnote identities and semantic attachments are preserved.

This is bounded checkpoint QA. Final acceptance still requires full-document all-page rendering after both reports are fully applied.
