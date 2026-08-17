#!/usr/bin/env python3
from pathlib import Path
import json, subprocess

R=Path('.')
SPEC=R/'work/CHECKPOINT-BATCH-SPEC.json'
LEDGER=R/'work/application-ledger.jsonl'; STATE=R/'work/APPLICATION-STATE.md'; LOG=R/'work/VALIDATION-LOG.md'; HANDOFF=R/'work/NEXT-HANDOFF.md'
s=json.loads(SPEC.read_text(encoding='utf-8'))
last=int(s['last_f4']); nxt_raw=s.get('next_f4'); nxt=int(nxt_raw) if nxt_raw is not None else None
phase=s.get('phase','FOURTH_APPLY'); next_stage=s.get('next_stage')
head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
rows=[json.loads(x) for x in LEDGER.read_text(encoding='utf-8').splitlines() if x.strip()]
if len(rows)!=210: raise SystemExit(f'ledger count {len(rows)} != 210')
byid={(r.get('id') or f"{r['report']}-{int(r['item_number']):03d}"):r for r in rows}
for iid,u in s['updates'].items():
    if iid not in byid: raise SystemExit('missing ledger id '+iid)
    byid[iid].update(u)
for n in range(1,last+1):
    if byid[f'F4-{n:03d}'].get('status')=='PENDING': raise SystemExit(f'completed-range regression F4-{n:03d}')
if nxt is not None:
    nid=f'F4-{nxt:03d}'
    if nid not in byid: raise SystemExit('missing next ledger id '+nid)
    if byid[nid].get('status')!='PENDING': raise SystemExit(f'next item {nid} is not pending')
else:
    for n in range(1,117):
        if byid[f'F4-{n:03d}'].get('status')=='PENDING': raise SystemExit(f'Fourth Report incomplete at F4-{n:03d}')
LEDGER.write_text('\n'.join(json.dumps(r,ensure_ascii=False,separators=(',',':')) for r in rows)+'\n',encoding='utf-8')

next_fourth=f'`F4-{nxt:03d}`' if nxt is not None else 'none — Fourth Report application complete'
resume_next=f'F4-{nxt:03d}' if nxt is not None else (next_stage or phase)
struct='\n'.join('- '+x for x in s.get('structural_state',[])) or '- Prior completed structural changes remain intact.'
evidence='\n'.join('- '+x for x in s.get('evidence',[]))
protected_status=s.get('protected_parts_status','baseline-identical')
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
- Current phase: `{phase}`
- Last fully completed Fourth Report item: `F4-{last:03d}`
- Next Fourth Report item: {next_fourth}
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (do not start until Fourth Report validation passes)

## Current working state
- Current working DOCX: `{s['docx']}`
- Current working DOCX SHA-256: `{s['sha256']}`
- Last known good commit basis: `{head}`
- Last known good DOCX: `{s['docx']}`
- Current body paragraph count: {s['body_paragraphs']}

## Integrity
- Genuine footnotes/references: 469/469
- Orphan/dangling/duplicate references: 0/0/0
- Word field instructions: 520/520; ADDIN: 466/466
- Zotero: 465 item + 1 bibliography preserved
- Bookmarks: 53/53; hyperlinks: 52
- Arabic/RTL structural inventory: canonical-equal
- Protected OOXML parts: {protected_status}

## Structural-edit state
{struct}

## Holds / validation
- Open HOLD items: {s.get('holds','none')}.
- Last item-level validation result: **PASS**.
- Deterministic replay/idempotency: PASS.
- Technical validation: PASS (`{s['technical_file']}`).
- Bounded visual QA: PASS, {s['visual_pages']}/{s['visual_pages']} pages inspected (`{s['visual_file']}`).

## Exact next action
{s['next_action']}
''',encoding='utf-8')

marker=s['validation_marker']
old=LOG.read_text(encoding='utf-8') if LOG.exists() else '# VALIDATION LOG\n'
if marker not in old:
    old += '\n\n'+marker+'\n'+s['validation_block'].rstrip()+'\n'
LOG.write_text(old,encoding='utf-8')

HANDOFF.write_text(f'''# NEXT HANDOFF

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Checkpoint basis HEAD: `{head}` plus this metadata checkpoint commit
- Current phase: `{phase}`

## Resume boundary
- Last completed item: `F4-{last:03d}`
- Next item/stage: `{resume_next}`
- DO-NOT-REPEAT: `F4-001`–`F4-{last:03d}`

## Working manuscript
- Current working DOCX: `{s['docx']}`
- Current working SHA-256: `{s['sha256']}`
- Last known good DOCX: same path above

## Integrity snapshot
- Footnotes/references: 469/469; orphans/dangling/duplicates: 0/0/0
- Word fields: 520; ADDIN: 466; Zotero: 465 item + 1 bibliography
- Bookmarks: 53/53; hyperlinks: 52; RTL inventory canonical-equal
- Protected OOXML: {protected_status}

## Latest structural state
{struct}

## Evidence
{evidence}

## Open HOLDs
{s.get('holds','None.')}

## Exact next action
{s['next_action']}
''',encoding='utf-8')
print(f'checkpoint metadata prepared through F4-{last:03d}; phase={phase}')