# F5-007 human visual QA R2 — PASS

## Candidate
- DOCX: `artifacts/checkpoints/manuscript-working-f5-007.docx`
- SHA-256: `81ea83b68eb3ee24061c522aad07f96507e4b0ff00847a5f140a8dbe66d60c80`
- Replay: `work/runtime/F5-007-REPLAY.txt`

## Prior failed candidate
The first F5-007 candidate (`0a019bad3d75933734a29e99bd89028c5ba25d258b6d0322c9bdf28d8f4d17d4`) failed human visual QA because LibreOffice dropped a run-boundary leading space, rendering `işaret eder.Telakki`. That failure is preserved in `work/F5-007-VISUAL-QA-FAIL-R1.md` and is not accepted.

## R2 remediation
The replay now explicitly sets `xml:space="preserve"` on the ` Telakki...` run and validates that this is the only allowed structural attribute difference beyond the P25 text edit.

- QA export workflow run: `32087726229`
- Artifact ID: `9307270173`
- SHA-locked range: P24–P27
- Canonical DOCX render produced 3 pages.

All **3/3 pages** were inspected individually.

- Page 1: expected bounded-slice TOC-field context only.
- Page 2: the positive kırâat/rivâyet/tarîk/vecih hierarchy renders naturally. The previously broken boundary now correctly displays `... edâ seçeneğine işaret eder. Telakki, okuyuşun ...`. No clipping, overlap, abnormal spacing, run-formatting propagation or footnote-zone defect.
- Page 3: P26/P27 and footnotes remain layout-stable; later negative constructions are future Fifth targets and remain untouched.

**Verdict: F5-007 R2 HUMAN VISUAL QA = PASS (3/3).**
