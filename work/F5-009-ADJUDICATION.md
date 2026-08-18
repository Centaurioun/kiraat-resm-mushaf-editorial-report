# F5-009 ADJUDICATION

- Report item: `F5-009`
- Phase: `FIFTH_APPLY`
- Durable input: `artifacts/checkpoints/manuscript-working-f5-008.docx`
- Expected input SHA-256: `99b579b4c1ea369fbf4f27705d42a1f632d06f5e67bc177dd09363c765a07b32`
- Resolved location: `word/document.xml` body paragraph `P26`
- Decision: `APPLY_CANDIDATE_PENDING_VALIDATION`

## Locked Fifth issue

The locked Fifth Report targets the negative opening:

`Sahih, meşhur, âhâd ve şâz nitelemeleri de tek bir ölçünün farklı dereceleri değildir.`

Its proposed positive formulation is:

`Sahih, meşhur, âhâd ve şâz nitelemeleri farklı değerlendirme boyutlarını ifade eder. Şâz bir rivâyetin tefsîrî veya dilsel bilgi değeri ile bağlayıcı kırâat statüsü ayrı ayrı değerlendirilmelidir.`

## Current durable P26 state

The F5-008 postflight shows the targeted material as a three-sentence block:

1. Negative categorical opening about sahih/meşhur/âhâd/şâz not being degrees of a single measure.
2. Existing positive Fourth-approved explanation that the categories concern different dimensions including reliability, prevalence, acceptance, and position in the general tilâvet field.
3. Negative sentence distinguishing a shādh report's exegetical/linguistic value from binding qirāʾāt status.

## Editorial/scientific adjudication

A literal replacement by the Fifth wording would unnecessarily discard the scientifically useful explanatory detail already preserved by the Fourth application. Under Fourth-over-Fifth precedence, that detail should remain.

The smallest scientifically sound intervention is therefore to consolidate the three-sentence negative/positive/negative block into two positive sentences while preserving the existing explanatory dimensions:

`Sahih, meşhur, âhâd ve şâz nitelemeleri, naklin güvenilirliği, yaygınlığı, kabulü ve genel tilâvet alanındaki konumuyla ilgili farklı değerlendirme boyutlarını ifade eder. Şâz bir rivâyetin tefsîrî veya dilsel bilgi değeri ile bağlayıcı kırâat statüsü ayrı ayrı değerlendirilmelidir.`

This preserves the Fourth-approved scientific content, removes both negative-definition constructions targeted by F5-009, and does not touch the preceding F5-008 real/ihtimalî conformity discussion or any F5-010+ target.

## Authorized scope

- Only P26 may change.
- The earlier F5-008 conformity text must remain byte/text-equivalent in content.
- No F5-010+ content may be edited.
- Package parts other than `word/document.xml` must remain byte-identical.
- Footnote/reference identities, field instructions, ADDIN/Zotero inventory, bookmarks, hyperlinks, and RTL structure must remain invariant.
- Candidate acceptance requires deterministic replay plus SHA-locked human visual QA.
