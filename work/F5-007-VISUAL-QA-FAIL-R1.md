# F5-007 visual QA R1 — FAIL

- Candidate SHA-256: `0a019bad3d75933734a29e99bd89028c5ba25d258b6d0322c9bdf28d8f4d17d4`
- QA export workflow run: `32087437758`
- Artifact ID: `9307175266`
- SHA-locked range: P24–P27
- Rendered pages inspected: **3/3**

## Result

**FAIL** — page 2 shows a visible whitespace regression at the F5-007 edit boundary:

`... edâ seçeneğine işaret eder.Telakki, okuyuşun ...`

The intended text contains a space between the sentences, but OOXML inspection shows that the following run stores the text as ` Telakki, ...` without `xml:space="preserve"`. LibreOffice therefore drops the leading run-boundary whitespace during rendering.

Other inspected pages showed no clipping, overlap or footnote-layout failure.

## Required remediation

Do not accept or checkpoint this candidate. Rebuild F5-007 from the durable F5-006 input and explicitly preserve the leading whitespace of the `Telakki...` run (or otherwise encode the separator without pre-applying F5-008+). Re-run deterministic validation and human visual QA before F5-007 can become durable.
