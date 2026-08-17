# F4-W10 Citation and Bibliography Map

## Certification status

`PROVISIONAL_PROJECT-EVIDENCE_MAP — DEPENDENCY_BLOCKED`

The mappings below are useful preparatory evidence, but they are **not certified against a reconstructed F4-047 DOCX** because the mandatory baseline binary could not be materialized in this runtime. They must be rechecked on the genuine reconstructed F4-047 before any edit is accepted.

This map is repository-evidence-only. It deliberately does not infer missing bibliographic facts from the web.

## F4-112 — genuine Word footnotes

| Word footnote ID | Current citation-bearing text | Authorized edit | Citation semantics after edit | Repository cross-check |
|---|---|---|---|---|
| 32 | `İbn Sa'd, et-Tabakâtü'l-kübrâ, 3/355.` followed by an editorial/work note | Delete only `(bu dipnot daha önce geçmiş midir.yoksa kitabın ilk adı bu şekilde mi) buna bakılması.` | Keep `İbn Sa'd, et-Tabakâtü'l-kübrâ, 3/355.` unchanged | Earlier full Ibn Sa'd identification already exists in footnote 17; no citation-text normalization is authorized here. |
| 41 | `Mukaddimetân fî ulûmi'l-Kur'ân, thk. Arthur Jeffery (Mektebetü'l-Hâncî, 1954), 25.` followed by an unfinished work note | Delete only `(bu eserin müellifi meçhuldür literatürde bu şekilde geçiyor.` | Keep the citation unchanged | This is the full citation used before later short citation(s); only the work note is removed. |
| 105 | `Ebu'l-Abbâs Ahmed b. Muhammed b. Ebû Bekir Kastallânî, Letâifu'l-işârât li fünûni'l-kırâât ... 1/84.` followed by a work note | Delete only `(bu eser daha önce tam adıyla geçmişmiydi)` | Keep the citation unchanged | This is the full citation used before later short citation(s); only the work note is removed. |

Replay invariant: `w:footnote/@w:id` and matching `w:footnoteReference/@w:id` sets must remain identical before/after. Only `w:t` text in footnotes 32/41/105 is authorized to change.

## F4-114 — DOI decisions

| Record | Current malformed value | Decision | Authorized resulting value |
|---|---|---|---|
| Kahraman | `https://doi.org/http://doi.org/1051702/esoguifd.791085` | REMOVE malformed DOI; repository evidence does not resolve a valid DOI, so no replacement may be invented | DOI text absent |
| Maşalı | `https://doi.org/https://doi.org/10.56361/usul.173700` | Correct duplicated resolver prefix | `https://doi.org/10.56361/usul.173700` |

If either malformed DOI occurs inside protected `w:instrText`, replay must fail closed rather than edit a Zotero/Word field instruction.

## F4-115 — edition retain/remove matrix

| Work / edition | Decision | Repository evidence |
|---|---|---|
| İbn Ebû Dâvud, `Kitâbu'l-mesâhif`, thk. Muhibbüddîn Abdussubhân Vâiz, Beyrut 2002 | KEEP | Used in body/footnote citation chain; current footnote 2 supplies the full 2002 citation. |
| İbn Ebû Dâvud, `Kitâbu'l-mesâhif`, thk. Selîm b. Îde'l-Hilâlî el-Eserî, Amman 2006 | REMOVE | No genuine body/footnote use found in the current project evidence; duplicate unused bibliography edition. |
| Ebû Dâvud Süleymân b. Necâh, `Muhtasaru't-tebyîn`, Riyad 2000, 5 cilt | KEEP | Genuine citation chain; current footnote 109 represents this edition. |
| Ebû Dâvud Süleymân b. Necâh, `Muhtasaru't-tebyîn`, Medine 1999, 2 cilt | KEEP | Genuine citation chain; current footnote 373 represents this edition. Both editions are intentionally retained. |
| İbn Kuteybe, `Te'vîlu muhtelifi'l-hadîs`, thk. Muhammed Zuhrî en-Neccâr, ts. | KEEP | Genuine citation chain; current footnote 8 uses this edition. |
| İbn Kuteybe, `Te'vîlu muhtelifi'l-hadîs`, thk. Muhammed Muhyiddîn el-Asfar, Beyrut 1999 | REMOVE | Bibliography-only duplicate edition in project evidence; no genuine cited use found. |

## F4-116 — Ebû Şâme edition adjudication

**Provisional content decision: KEEP BOTH the 1975 and 1993 editions.**

- 1993 is directly supported in the current extracted manuscript evidence: genuine footnote 86 contains the full 1993 citation and page 212.
- 1975 is directly resolved by project-internal continuity: `source/manuscript/archive/earlier_manuscript.md` contains genuine footnote 131 with the full Tayyar Altıkulaç / Beyrût / Dâru's-Sadır / 1975 citation at `1/173`; the current extracted manuscript's genuine footnote 131 is the corresponding short citation `Ebû Şâme, el-Murşidu'l-vecîz, 1/173.`

This removes the bibliographic ambiguity at the project-evidence level, but the W10 application remains blocked until the genuine reconstructed F4-047 is verified.
