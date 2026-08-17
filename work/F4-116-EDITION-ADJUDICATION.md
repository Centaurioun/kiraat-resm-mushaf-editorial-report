# F4-116 — Ebû Şâme edition-use adjudication

## Fourth Report criterion

F4-116 does not authorize mechanical deduplication. It requires the 1993 Velîd Müsâid et-Tabatabâî edition to remain and directs the 1975 Tayyar Altıkulaç edition to remain **if a genuine current short citation can be tied to it**; only an actually unused 1975 record may be removed.

## Current-manuscript evidence

Durable input: `artifacts/checkpoints/manuscript-working-f4-115.docx`

SHA-256: `73ccdd0b5e0c63450cf611d175e5fcf547ac0b9a9aaaf11bf09a4e5db5c996bf`

### 1993 edition — proven use

FN86 contains a full edition-specific citation:

> Şihâbuddîn Abdurrahmân İsmâîl Ebû Şâme, *el-Murşidu’l-vecîz ilâ ulûmin tetaallaku bi’l-kitâbi’l-Azîz*, thk. Velîd Müsâid et-Tabatabâî (Kuveyt: Mektebetü’l-İmâm ez-Zehebî, 1993), 212.

Therefore the 1993 bibliography record is unquestionably used and must remain.

### 1975 edition — proven use

FN394 is the short citation:

> Ebû Şâme, *el-Murşidu’l-vecîz*, 144.

FN394 belongs to current body P377. P377 explains that after the community united on the Uthmanic muṣḥaf and nonconforming material was excluded, material outside the agreed written text could be treated analogously to what had been abrogated/removed, while the text between the two covers became the preserved common muṣḥaf / imām for the community.

The Tayyar Altıkulaç / Dâr Sâdır 1975 scan was independently inspected at **printed page 144**. That page contains this same distinctive argument: the community's choice of one muṣḥaf, Uthman's copying and destruction of alternatives to end disagreement, treatment of what conflicts with the agreed written text in the category of what was abrogated/removed by agreement of the Companions, and the written text between the two covers as the preserved common text and imām for the community.

This is a direct page-and-content match, not an inference from `1/x` formatting. It proves that at least FN394 genuinely uses the 1975 Altıkulaç edition.

## Why `1/x` is not used as the decision rule

Several current short references are written `1/173`, `1/262`, or `1/324`. Independent bibliographic metadata describes both the 1975 Altıkulaç and 1993 Tabatabâî editions as single-volume editions. Therefore the manuscript's `1/` prefix is not reliable evidence for choosing one of these two editions.

For example, printed page 212 of the 1975 scan discusses recitation/tajwīd matters and does **not** contain the Yemen/Bahrain muṣḥaf passage for which FN86 explicitly cites the 1993 edition at p. 212. The editions therefore have materially different pagination.

## External bibliographic cross-check

Public bibliographic/catalogue checks used only to distinguish edition structure and support the adjudication:

- al-Maktaba al-Waqfiyya, Tayyar Altıkulaç edition: Dâr Sâdır, 1975, one volume; scanned record reports 342 pages.
- al-Maktaba al-Waqfiyya, Velîd Müsâid et-Tabatabâî edition: Maktabat al-Imâm al-Dhahabî, 1993, one volume; scanned record reports 512 pages.
- TDV İslâm Ansiklopedisi separately records the Beirut 1975 Altıkulaç publication and the Kuwait 1414/1993 Tabatabâî publication.

The current bibliography's `2 Cilt` wording for the 1975 record is therefore a **separate metadata discrepancy** discovered during adjudication. It is not silently folded into F4-116 because F4-116's stated decision is edition use/retention. The discrepancy is carried forward for FOURTH_VALIDATE.

## F4-116 adjudication

- 1993 Tabatabâî record: **KEEP — USED (FN86 explicit full citation)**
- 1975 Altıkulaç record: **KEEP — USED (FN394 p. 144 direct page/content match)**
- bibliography record deletion under F4-116: **NONE**
- manuscript text change under F4-116: **NONE**
- status: **VERIFIED_NO_CHANGE**

F4-116 may be durably closed only after a deterministic byte-identical replay/validation confirms that the F4-115 binary is carried forward unchanged and all structural invariants remain intact.
