# F5-013 ADJUDICATION

## Locked Fifth item
- Item: `F5-013`
- Location: `Giriş, kapsam ve katkı paragrafları`
- Locked representative target: `Böylece ana problemden uzaklaştıracak ayrıntılar sınırlandırılırken kitabın dört bölümünü birbirine bağlayan tarihsel ve kavramsal hat korunmuştur.`
- Fifth concern: two nearby Introduction paragraphs each close with a repetitive `Böylece` mini-summary.
- Suggested positive forms:
  1. `Araştırma, sahâbe mushafları, erken yazı tarihi, kırâat tasnifleri ve matbu mushafları yalnız resm-i mushaf ile kırâat rivâyeti arasındaki ilişkiye temas ettikleri ölçüde ele almaktadır. Bu sınır, kitabın tarihsel ve kavramsal hattını ana problem etrafında tutmaktadır.`
  2. `Kitabın katkısı, yazılı birlik, rivâyet sürekliliği ve okuyuş çeşitliliğini aynı aktarım düzeninin birbirini tamamlayan unsurları olarak birlikte incelemesidir.`

## Current durable state and Fourth precedence
The durable F5-012 binary is `artifacts/checkpoints/manuscript-working-f5-012.docx`, SHA-256 `c99826db06c605f5950e682c82af6d5c6f481d0c43a3364d029daadabe51fc19`, 674 body paragraphs.

Existing postflight evidence shows the Fourth-restructured Introduction already uses direct scope/method language rather than the locked `Böylece` mini-summary pattern. In particular, current P28 directly states the study scope (`Bu çalışma, Kur’an tarihinin bütün meselelerini ele almak yerine resm-i Osmânî ile kırâat rivâyeti arasındaki ilişkiye odaklanmaktadır.`), while P29–P32 continue with substantive scope, method, sources and aim rather than nearby `Böylece` closures.

Because the Fifth Report is subordinate to the Fourth Report's scientific and structural reconstruction, the suggested paragraphs must not be inserted merely to recreate material that the current Introduction no longer contains. The correct decision rule is therefore fail-closed:

1. Verify the exact durable input SHA and 674-paragraph structure.
2. Verify P15 is the `Giriş` heading and inspect the complete current Introduction body before the First Chapter boundary.
3. If the locked target or any current `Böylece` mini-summary remains in that bounded Introduction, stop and report the exact current paragraphs; do not guess or edit another location.
4. If no such mini-summary remains, classify F5-013 as `VERIFIED_NO_CHANGE` and preserve the complete DOCX byte-identically.

## Explicit exclusions
- Do not insert either Fifth suggested paragraph if the current Fourth-resolved Introduction no longer contains the targeted mini-summaries.
- Do not alter P28–P34 merely to make them resemble the Fifth report's pre-Fourth wording.
- Do not apply F5-014 or later items.
- Do not alter citations, fields, footnotes, bookmarks, hyperlinks, RTL structures, styles, numbering, or any OOXML package part.
