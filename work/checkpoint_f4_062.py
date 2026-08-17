#!/usr/bin/env python3
from pathlib import Path
import json, subprocess

ROOT=Path('.')
LEDGER=ROOT/'work/application-ledger.jsonl'; STATE=ROOT/'work/APPLICATION-STATE.md'; LOG=ROOT/'work/VALIDATION-LOG.md'; HANDOFF=ROOT/'work/NEXT-HANDOFF.md'
head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
rows=[json.loads(x) for x in LEDGER.read_text(encoding='utf-8').splitlines() if x.strip()]
if len(rows)!=210: raise SystemExit(f'expected 210 ledger records, got {len(rows)}')
byid={(r.get('id') or f"{r['report']}-{int(r['item_number']):03d}"):r for r in rows}
commit='35141e43b74fbe4b0760c3be19b8fedc7bf9f7dc'
updates={
 'F4-058':dict(status='STRUCTURALLY_APPLIED',section='2.3',action_type='STRUCTURAL_VIEWPOINT_CONSOLIDATION',resolved_location='former current paragraphs 232–235 consolidated to one synthesis',affected_footnote_ids=[219,220,221,222],commit=commit,verification='TECHNICAL_PASS + IDEMPOTENCY_PASS + 9/9_FINAL_BOUNDED_VISUAL_QA_PASS',notes='Competing seven-harf/Osmânî-mushaf views retained as views rather than certainty; notes 219–222 preserved on their source families.'),
 'F4-059':dict(status='STRUCTURALLY_APPLIED',section='2.3',action_type='STRUCTURAL_REPETITION_REDUCTION_AND_TRANSITION',resolved_location='2.3 opening and closing synthesis',affected_footnote_ids=[],commit=commit,verification='TECHNICAL_PASS + IDEMPOTENCY_PASS + 9/9_FINAL_BOUNDED_VISUAL_QA_PASS',notes='Repeated first-chapter history shortened; long mini-conclusion replaced by direct bridge to 2.4.'),
 'F4-060':dict(status='APPLIED',section='2.4',action_type='BALANCED_CAUSALITY_REWRITE',resolved_location='current 2.4 opening and authority paragraphs',affected_footnote_ids=[225,226,227],commit=commit,verification='TECHNICAL_PASS + IDEMPOTENCY_PASS + 9/9_FINAL_BOUNDED_VISUAL_QA_PASS',notes='Resm reframed as shared written reference rather than sole cause of qiraat/tafsir authority. Notes 225–227 preserved. Initial inherited italics were rejected in QA and removed by v2 replay.'),
 'F4-061':dict(status='APPLIED',section='2.4',action_type='COUNTERFACTUAL_REMOVAL',resolved_location='current 2.4 Semîn el-Halebî paragraph',affected_footnote_ids=[237],commit=commit,verification='TECHNICAL_PASS + IDEMPOTENCY_PASS + 9/9_FINAL_BOUNDED_VISUAL_QA_PASS',notes='Counterfactual history removed; current historical application retained with FN237.'),
 'F4-062':dict(status='APPLIED',section='2.4→Third Chapter transition',action_type='PARAGRAPH_REPLACEMENT',resolved_location='current transition immediately before Third Chapter',affected_footnote_ids=[],commit=commit,verification='TECHNICAL_PASS + IDEMPOTENCY_PASS + 9/9_FINAL_BOUNDED_VISUAL_QA_PASS',notes='Direct conceptual bridge into concrete resm examples. Initial inherited italics were rejected in QA and removed by v2 replay.'),
}
for iid,u in updates.items(): byid[iid].update(u)
for n in range(1,63):
    if byid[f'F4-{n:03d}'].get('status')=='PENDING': raise SystemExit(f'regression: F4-{n:03d} pending')
if byid['F4-063'].get('status')!='PENDING': raise SystemExit('F4-063 unexpectedly non-pending')
LEDGER.write_text('\n'.join(json.dumps(r,ensure_ascii=False,separators=(',',':')) for r in rows)+'\n',encoding='utf-8')

STATE.write_text(f'''# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint basis: `{head}` (metadata checkpoint commit follows this basis)

## Source / reports
- Source manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: `final/fourth-report-v2.md` — 116 items
- Fifth Report: `final/fifth-report-locked.md` — 94 items

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: `F4-062`
- Next Fourth Report item: `F4-063`
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (do not start until Fourth Report validation passes)

## Current working state
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-062.docx`
- Current working DOCX SHA-256: `200f55000bf5dbe6e350466c79b4ffa15973bf06d92cb4a66ea91848252b77f3`
- Last known good commit basis: `{head}`
- Last known good DOCX: `artifacts/checkpoints/manuscript-working-f4-062.docx`
- Current body paragraph count: 686

## Integrity
- Genuine footnotes/references: 469/469
- Orphan/dangling/duplicate references: 0/0/0
- Word field instructions: 520/520; ADDIN: 466/466
- Zotero: 465 item + 1 bibliography preserved
- Bookmarks: 53/53; hyperlinks: 52
- Arabic/RTL structural inventory: canonical-equal
- Protected OOXML parts: baseline-identical

## Structural state / validation
- F4-058: competing-viewpoint cluster consolidated with FNs 219–222 preserved.
- F4-059: repeated 2.3 setup/conclusion reduced and direct transition added.
- F4-060: resm/qiraat/tafsir causality balanced; FNs 225–227 preserved.
- F4-061: counterfactual history removed; FN237 preserved.
- F4-062: direct Third Chapter transition applied.
- Initial F4-062 visual QA found inherited italics on two new paragraphs; rejected and repaired deterministically by `work/apply_f4_058_062_v2.py`.
- Final corrected replay: byte-identical on second execution.
- Technical validation: PASS (`work/runtime/F4-062-TECHNICAL-VALIDATION.txt`).
- Final bounded visual QA: PASS, 9/9 pages inspected (`work/F4-062-VISUAL-QA.md`).
- Open HOLD items: none.

## Exact next action
Read authoritative `F4-063`, re-locate it against the current F4-062 checkpoint, inventory current 3.1 footnotes/fields/Arabic/RTL and downstream F4/F5 overlaps, then apply the next safe bounded Fourth Report unit. Do not repeat `F4-001`–`F4-062`.
''',encoding='utf-8')

old=LOG.read_text(encoding='utf-8') if LOG.exists() else '# VALIDATION LOG\n'
marker='## F4-058–062 checkpoint — PASS'
if marker not in old:
    old += f'''\n\n{marker}
- Final replay: `work/apply_f4_058_062_v2.py` over durable F4-057 input.
- Candidate: `artifacts/checkpoints/manuscript-working-f4-062.docx`.
- SHA-256: `200f55000bf5dbe6e350466c79b4ffa15973bf06d92cb4a66ea91848252b77f3`.
- F4-058 STRUCTURALLY_APPLIED; F4-059 STRUCTURALLY_APPLIED; F4-060 APPLIED; F4-061 APPLIED; F4-062 APPLIED.
- Corrected second replay: all five report items and style repair already satisfied; byte-identical.
- ZIP/XML PASS; footnotes/references 469/469; orphan/dangling/duplicate 0/0/0.
- Word fields 520; Zotero 465+1; RTL/bookmark/hyperlink inventories canonical-equal; protected OOXML baseline-identical.
- Initial visual QA rejected inherited italics on F4-060 and F4-062 new paragraphs. v2 replay removed only direct italic run properties from those two targets.
- Corrected bounded render: 9 pages, 9/9 visually inspected, PASS. No clipping, overlap, footnote overflow, heading damage, Arabic/RTL damage or batch-induced style propagation remains.
- Pre-existing red editorial/Fifth targets remain for their designated later items.
- Durable boundary: last F4-062; next F4-063.
'''
LOG.write_text(old,encoding='utf-8')

HANDOFF.write_text(f'''# NEXT HANDOFF

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Checkpoint basis HEAD: `{head}` plus this metadata checkpoint commit
- Current phase: `FOURTH_APPLY`

## Resume boundary
- Last completed item: `F4-062`
- Next item: `F4-063`
- DO-NOT-REPEAT: `F4-001`–`F4-062`

## Working manuscript
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-062.docx`
- Current working SHA-256: `200f55000bf5dbe6e350466c79b4ffa15973bf06d92cb4a66ea91848252b77f3`
- Last known good DOCX: same path above

## Integrity snapshot
- Footnotes/references: 469/469; orphans/dangling/duplicates: 0/0/0
- Word fields: 520; ADDIN: 466; Zotero: 465 item + 1 bibliography
- Bookmarks: 53/53; hyperlinks: 52; RTL inventory canonical-equal
- Protected OOXML: baseline-identical

## Latest evidence
- Replay: `work/apply_f4_058_062_v2.py`
- Candidate: `artifacts/checkpoints/manuscript-working-f4-062.docx`
- Technical: `work/runtime/F4-062-TECHNICAL-VALIDATION.txt`
- Postflight: `work/runtime/F4-062-POSTFLIGHT.txt`
- QA PDF: `work/runtime/F4-062-QA.pdf`
- Human QA: `work/F4-062-VISUAL-QA.md` — corrected render 9/9 PASS

## Open HOLDs
None.

## Exact next action
Read and apply `F4-063` against the current F4-062 binary. Re-locate 3.1 from current structure; inspect citations, Arabic/RTL and later Fourth/Fifth overlaps before editing. Do not restore stale pre-F4-062 prose.
''',encoding='utf-8')
print('F4-062 durable metadata prepared')
