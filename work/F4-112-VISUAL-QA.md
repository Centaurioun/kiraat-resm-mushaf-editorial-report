# F4-112 Visual QA — PASS

Candidate: `artifacts/checkpoints/manuscript-working-f4-112.docx`

SHA-256: `58e23edd3cdbffbacaf8a2e14fc2dff5ea5357dd76b15cda30c4d31820e12e9a`

Scope: remove surviving editorial/work notes from genuine footnotes 32, 41 and 105 while preserving their bibliographic citation content, IDs and body references.

## Technical gate

- 469/469 genuine footnotes/references preserved.
- 0 orphan / dangling / duplicate references.
- 520 field instructions preserved.
- Only `word/footnotes.xml` is authorized to differ, and only FN32/FN41/FN105 text differs; target footnote structure remains unchanged.
- `protected_parts=targeted-footnote-text-authorized` with `allowed_footnote_text_ids=32,41,105`.

## Human visual review

The ordinary bounded-slice renderer was found unsuitable as sole evidence for high-numbered footnotes because deleting preceding body paragraphs can make LibreOffice remap displayed footnote text. A prefix render retaining P0–P118 was therefore used so every preceding footnote reference remains in its original sequence.

- Prefix render: 25 pages generated; all page-flow/footnote identity behavior retained.
- Real page carrying FN32: inspected — citation renders as `İbn Sa’d, et-Tabakâtü’l-kübrâ, 3/355.`; work note absent; PASS.
- Real page carrying FN41: inspected — `Mukaddimetân fî ulûmi’l-Kur’ân, thk. Arthur Jeffery (Mektebetü’l-Hâncî, 1954), 25.`; unfinished work note absent; PASS.
- Real page carrying FN105: inspected — Kastallânî citation ends at `1/84.`; work note absent; PASS.
- No clipping, overlap, footnote-number mismatch, unexpected blank page, heading regression or RTL corruption observed on the three target pages.

Verdict: **PASS**.
