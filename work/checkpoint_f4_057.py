#!/usr/bin/env python3
from pathlib import Path
import json, subprocess

ROOT=Path('.')
LEDGER=ROOT/'work/application-ledger.jsonl'; STATE=ROOT/'work/APPLICATION-STATE.md'; LOG=ROOT/'work/VALIDATION-LOG.md'; HANDOFF=ROOT/'work/NEXT-HANDOFF.md'
head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
rows=[json.loads(x) for x in LEDGER.read_text(encoding='utf-8').splitlines() if x.strip()]
if len(rows)!=210: raise SystemExit(f'expected 210 ledger records, got {len(rows)}')
byid={(r.get('id') or f"{r['report']}-{int(r['item_number']):03d}"):r for r in rows}
commit='434304b4b18db2fd7d155becb4a66d25beee7e3b'
updates={
 'F4-053':dict(status='APPLIED',section='2.1→2.2 transition',action_type='PARAGRAPH_REPLACEMENT',resolved_location='current body paragraph 209',affected_footnote_ids=[],commit=commit,verification='TECHNICAL_PASS + IDEMPOTENCY_PASS + 9/9_FINAL_BOUNDED_VISUAL_QA_PASS',notes='Replaced repeated Netice summary with direct transition into rivayet/sened/otorite.'),
 'F4-054':dict(status='APPLIED',section='2.2.1 Rivâyet',action_type='IN_PARAGRAPH_REPLACEMENT',resolved_location='current body paragraph 215',affected_footnote_ids=[204],commit=commit,verification='TECHNICAL_PASS + IDEMPOTENCY_PASS + 9/9_FINAL_BOUNDED_VISUAL_QA_PASS',notes='Oral transmission remains primary while written mushaf record is framed as complementary; FN204 preserved.'),
 'F4-055':dict(status='APPLIED',section='2.2.2 Sened',action_type='IN_PARAGRAPH_REPLACEMENT',resolved_location='current body paragraph 219',affected_footnote_ids=[207],commit=commit,verification='TECHNICAL_PASS + IDEMPOTENCY_PASS + 9/9_FINAL_BOUNDED_VISUAL_QA_PASS',notes='Asim attribution reframed as identification/transmission tradition rather than free production; FN207 preserved.'),
 'F4-056':dict(status='STRUCTURALLY_APPLIED',section='2.2.1–2.2.3',action_type='STRUCTURAL_CONCEPTUAL_REWRITE',resolved_location='2.2 overview plus Rivâyet/Sened/Otorite subsection openings',affected_footnote_ids=[198,199,200,201,206,214],commit=commit,verification='TECHNICAL_PASS + IDEMPOTENCY_PASS + 9/9_FINAL_BOUNDED_VISUAL_QA_PASS',notes='Rivayet, sened and authority differentiated by direct positive definitions; repetitive negative-definition openings removed while source-backed continuations and citations remain.'),
 'F4-057':dict(status='APPLIED',section='2.2.3→2.3 transition',action_type='PARAGRAPH_REPLACEMENT',resolved_location='current body paragraph 228',affected_footnote_ids=[],commit=commit,verification='TECHNICAL_PASS + IDEMPOTENCY_PASS + 9/9_FINAL_BOUNDED_VISUAL_QA_PASS',notes='Replaced repeated authority conclusion with direct transition to seven-harf/Osmânî mushaf question. Final candidate also includes deterministic xml:space preserve repair for inherited F4-052 run-boundary rendering defect.'),
}
for iid,u in updates.items(): byid[iid].update(u)
for n in range(1,58):
    if byid[f'F4-{n:03d}'].get('status')=='PENDING': raise SystemExit(f'regression: F4-{n:03d} pending')
if byid['F4-058'].get('status')!='PENDING': raise SystemExit('F4-058 unexpectedly non-pending')
LEDGER.write_text('\n'.join(json.dumps(r,ensure_ascii=False,separators=(',',':')) for r in rows)+'\n',encoding='utf-8')

STATE.write_text(f'''# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint basis: `{head}` (metadata checkpoint commit follows this basis)

## Source / reports
- Source manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Source SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: `final/fourth-report-v2.md`
- Fourth Report parsed item count: 116
- Fifth Report: `final/fifth-report-locked.md`
- Fifth Report parsed item count: 94

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: `F4-057`
- Next Fourth Report item: `F4-058`
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (do not start until Fourth Report validation passes)

## Current working state
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-057.docx`
- Current working DOCX SHA-256: `b77bc0066b22c9e66b250c53ff456045abde1f5410cb11ad98d77f3fb69d7810`
- Last known good commit basis: `{head}`
- Last known good DOCX: `artifacts/checkpoints/manuscript-working-f4-057.docx`
- Current body paragraph count: 689

## Footnote integrity
- Baseline/current genuine footnotes: 469 / 469
- Baseline/current body references: 469 / 469
- Orphan footnotes: 0
- Dangling references: 0
- Duplicate references: 0
- Genuine footnote ID set and body-reference order/set: preserved

## Word / Zotero / OOXML integrity
- Baseline/current Word field instructions: 520 / 520
- ADDIN fields: 466 / 466
- Zotero item fields: 465 / 465
- Zotero bibliography fields: 1 / 1
- Bookmarks: 53/53 / 53/53
- Hyperlinks: 52 / 52
- Arabic/RTL structural inventory: equal to canonical source in runner validation
- Protected OOXML parts: baseline-identical

## Structural-edit state
- Prior structural changes through F4-052 remain intact.
- F4-056: 2.2 rivâyet/sened/otorite conceptual openings structurally differentiated.
- F4-057: direct transition from authority discussion into seven-harf/Osmânî mushaf issue.
- OOXML whitespace repair: leading-space `w:t` inherited from F4-052 now carries `xml:space="preserve"`; no text/footnote/field content changed by this repair.

## Holds / validation
- Open HOLD items: none.
- Last validation result: **PASS**.
- F4-053–057 replay: byte-identical on second runner execution.
- Technical validation: PASS (`work/runtime/F4-057-TECHNICAL-VALIDATION.txt`).
- Final bounded visual QA: PASS, 9/9 pages inspected after whitespace repair (`work/F4-057-VISUAL-QA.md`).

## Exact next action
Read authoritative `F4-058`, re-locate it against `artifacts/checkpoints/manuscript-working-f4-057.docx`, inventory the current 2.3–2.4 footnotes/fields/RTL and later F4/F5 overlaps, then apply the next safe bounded Fourth Report unit. Do not repeat `F4-001`–`F4-057`.
''',encoding='utf-8')

old=LOG.read_text(encoding='utf-8') if LOG.exists() else '# VALIDATION LOG\n'
marker='## F4-053–057 checkpoint — PASS'
if marker not in old:
    old += f'''\n\n{marker}
- Replay: `work/apply_f4_053_057_v3.py` over durable F4-052 input.
- Candidate DOCX: `artifacts/checkpoints/manuscript-working-f4-057.docx`.
- Candidate SHA-256: `b77bc0066b22c9e66b250c53ff456045abde1f5410cb11ad98d77f3fb69d7810`.
- First final replay: F4-053 APPLIED; F4-054 APPLIED; F4-055 APPLIED; F4-056 STRUCTURALLY_APPLIED; F4-057 APPLIED; OOXML whitespace-preserve repair APPLIED.
- Second replay: all five items and whitespace repair ALREADY_SATISFIED; candidate byte-identical.
- ZIP/XML: PASS; footnotes/references 469/469; orphan=0; dangling=0; duplicate=0.
- Word fields 520; Zotero 465 item + 1 bibliography; protected OOXML parts baseline-identical.
- Arabic/RTL, bookmarks and hyperlinks equal to canonical-source structural inventory.
- Initial visual QA found one inherited run-boundary rendering defect (`ayrılmalıdır.İlk`); root cause was missing `xml:space="preserve"` despite a raw leading-space character.
- `work/apply_f4_053_057_v3.py` repaired only the whitespace-preservation property. Final 9-page bounded render was inspected page-by-page; the defect is resolved and visual QA is PASS.
- No new clipping, overlap, footnote overflow, blank page, heading damage, RTL damage or style propagation.
- Pre-existing red Fifth-style targets and the later red footnote editorial note remain for their designated report items.
- Durable boundary: last F4-057; next F4-058.
'''
LOG.write_text(old,encoding='utf-8')

HANDOFF.write_text(f'''# NEXT HANDOFF

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Checkpoint basis HEAD: `{head}` plus this metadata checkpoint commit
- Current phase: `FOURTH_APPLY`

## Resume boundary
- Last completed item: `F4-057`
- Next item: `F4-058`
- DO-NOT-REPEAT: `F4-001`–`F4-057`

## Working manuscript
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-057.docx`
- Current working SHA-256: `b77bc0066b22c9e66b250c53ff456045abde1f5410cb11ad98d77f3fb69d7810`
- Last known good commit basis: `{head}`
- Last known good DOCX: `artifacts/checkpoints/manuscript-working-f4-057.docx`

## Integrity snapshot
- Footnotes: 469/469
- Body references: 469/469
- Orphans/dangling/duplicates: 0/0/0
- Word fields: 520/520; ADDIN 466/466
- Zotero: 465 item + 1 bibliography preserved
- Bookmarks: 53/53; hyperlinks: 52
- RTL inventory: canonical-equal
- Protected OOXML parts: baseline-identical

## Latest completed work
- F4-053: direct 2.1→2.2 transition.
- F4-054: oral transmission remains primary; written mushaf record framed as complementary; FN204 preserved.
- F4-055: Âsım attribution corrected to a transmission/identification formulation; FN207 preserved.
- F4-056: rivâyet, sened and authority structurally differentiated; source-backed continuations and FNs 198–201/206/214 preserved.
- F4-057: direct transition into seven-harf/Osmânî mushaf issue.
- Rendering repair: inherited F4-052 leading-space run now has `xml:space="preserve"`; final 9/9 bounded visual QA PASS.

## Evidence
- Replay: `work/apply_f4_053_057_v3.py`
- Candidate: `artifacts/checkpoints/manuscript-working-f4-057.docx`
- SHA: `work/runtime/F4-057-SHA256.txt`
- Postflight: `work/runtime/F4-057-POSTFLIGHT.txt`
- Technical validation: `work/runtime/F4-057-TECHNICAL-VALIDATION.txt`
- QA PDF: `work/runtime/F4-057-QA.pdf`
- Human visual record: `work/F4-057-VISUAL-QA.md` (9/9 PASS after repair)

## Open HOLDs
None.

## Exact next action
Read and apply `F4-058` against the current F4-057 checkpoint. Re-locate current 2.3–2.4 targets; do not restore stale pre-F4-057 prose. Inventory footnotes/fields/RTL and Fourth/Fifth overlaps before modifying them.
''',encoding='utf-8')
print('F4-057 durable metadata prepared')
