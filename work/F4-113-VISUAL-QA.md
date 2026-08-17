# F4-113 Visual QA — PASS

Candidate: `artifacts/checkpoints/manuscript-working-f4-113.docx`

SHA-256: `e4287570d99f9d3c20f96752497787e6d97f6a07047555ecbe5c05e5c69bdac1`

Scope: Fourth Report F4-113, footnote house-style normalization of Arabic-article/transliteration usage. Author-name variants are normalized conservatively (`ed-Dânî` → `Dânî`, `ez-Zürkânî` → `Zürkânî`, `es-Suyûtî` → `Suyûtî`). Sura names in explicit Qur'anic verse references use an articleless house style, while bibliographic work titles and unrelated article-bearing names remain untouched.

## Deterministic application

- Input durable checkpoint: `artifacts/checkpoints/manuscript-working-f4-112.docx`
- Input durable SHA-256: `58e23edd3cdbffbacaf8a2e14fc2dff5ea5357dd76b15cda30c4d31820e12e9a`
- Replay script: `work/apply_f4_113.py`
- Final candidate SHA-256: `e4287570d99f9d3c20f96752497787e6d97f6a07047555ecbe5c05e5c69bdac1`
- Deterministic replay/idempotency: **PASS**.
- An earlier queued/stale SHA observation was rejected by the fail-closed SHA gate. The stable candidate was re-hashed and all later validation/visual requests were locked to the SHA above.

## Technical gate

`work/runtime/F4-113-TECHNICAL-VALIDATION.txt` = **PASS**.

Verified invariants:

- body paragraphs: 676;
- genuine footnotes: 469;
- body footnote references: 469;
- reference identity multiset: canonical-equal;
- orphan / dangling / duplicate references: 0 / 0 / 0;
- Word field instructions: 520;
- protected OOXML parts: baseline-identical except explicitly authorized footnote text changes;
- target footnote structure: unchanged;
- no unauthorized footnote changes.

Canonical-to-candidate changed-footnote authorization set (31 total, including the three already accepted F4-112 changes):

`2, 28, 32, 41, 50, 66, 105, 271, 272, 273, 274, 292, 342, 344, 345, 346, 377, 380, 381, 407, 409, 411, 414, 421, 423, 424, 425, 426, 427, 428, 431`

The technical gate required the actually changed canonical-to-candidate set to match this authorization set exactly.

## Content/postflight checks

Representative accepted results include:

- FN28: author form `Muhammed Abdülazîm Zürkânî`;
- FN50: author form `Celâleddîn Abdurrahmân Suyûtî`;
- FN2: `Ebû Amr b. Osman Dânî`, while the work title `el-Mukni‘` remains article-bearing;
- FN271–274: `İsrâ 17/11`, `Şûrâ 42/24`, `Kamer 54/6`, `Alak 96/18`;
- FN292: `Zâriyât 51/47`;
- FN342: `Bakara 2/113`;
- FN344: `Mâide 5/38`;
- FN345–346: `Mümtehine 60/8`, `Mümtehine 60/9`;
- bibliographic titles such as `el-İtkân`, `el-Mukni‘` and comparable work-title forms are preserved rather than mechanically stripped.

No F4-114 transliteration work was pre-applied.

## Human visual review

Every rasterized page from every representative visual slice was manually inspected. Human visual verdict: **PASS**.

### Slice A — early author-name normalization and quotation/layout preservation

- Range: P50–P75
- Workflow run: `32079868743`
- Artifact: `application-bounded-qa-pages`, artifact ID `9304743549`
- Rasterized pages: **8/8 inspected**
- Verdict: **PASS**
- Checks: normal paragraph and heading flow; clean footnote zones; no clipping/overlap; no unexpected italic/bold/run corruption; punctuation intact; author forms render naturally; `Dânî`, `Zürkânî`, `Suyûtî` visible in accepted form; bibliographic work-title articles preserved; Mervân quotation context remains intact; no RTL or page-flow regression attributable to F4-113.

### Slice B — middle sura-normalization / RTL-heavy region

- Range: P274–P280
- Workflow run: `32080087101`
- Artifact: `application-bounded-qa-pages`, artifact ID `9304818453`
- Rasterized pages: **4/4 inspected**
- Verdict: **PASS**
- Checks: Arabic/RTL fragments, superscript footnote marks, paragraph flow and footnote area render cleanly; no clipping, overlap, punctuation corruption or run-formatting damage.

### Slice C — later qiraat/resm region with complex formatting

- Range: P389–P401
- Workflow run: `32080209568`
- Artifact: `application-bounded-qa-pages`, artifact ID `9304867454`
- Rasterized pages: **7/7 inspected**
- Verdict: **PASS**
- Checks: Arabic fragments, RTL runs, italics, dense scholarly prose, heading transition and footnote zones render normally; no clipping, overlap, broken footnote placement, unexpected blank-page regression or F4-113-attributable formatting damage.

Total manually inspected rasterized pages: **19/19**.

## Bounded-render footnote-number limitation

The ordinary bounded-slice renderer removes body paragraphs outside the requested range. LibreOffice may therefore remap the displayed low footnote numbers in the rendered slice for high-numbered original footnotes. This renderer is consequently used here for **layout/run/RTL/footnote-zone visual safety**, not as the authority for original high footnote ID identity.

Original footnote identity, exact changed-footnote scope and candidate content are instead established by the structural technical gate and full-candidate postflight evidence, which operate on the unchanged candidate OOXML and require the canonical-to-candidate changed-footnote set to match the authorized set exactly.

## Final adjudication

- deterministic replay/idempotency: **PASS**
- candidate SHA lock: **PASS**
- technical structural validation: **PASS**
- postflight content normalization: **PASS**
- human visual QA: **PASS (19/19 pages)**
- preserved exclusions (work titles / unrelated bibliographic articles / non-target content): **PASS**

**Overall F4-113 verdict: PASS.**
