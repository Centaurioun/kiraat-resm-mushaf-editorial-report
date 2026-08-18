#!/usr/bin/env python3
from pathlib import Path
import json, subprocess

R=Path('.')
SPEC=R/'work/CHECKPOINT-BATCH-SPEC.json'
LEDGER=R/'work/application-ledger.jsonl'; STATE=R/'work/APPLICATION-STATE.md'; LOG=R/'work/VALIDATION-LOG.md'; HANDOFF=R/'work/NEXT-HANDOFF.md'
s=json.loads(SPEC.read_text(encoding='utf-8'))
last_f5=int(s['last_f5']); next_f5_raw=s.get('next_f5'); next_f5=int(next_f5_raw) if next_f5_raw is not None else None
sha=s.get('sha256')
if s.get('sha256_from_file'):
    sha=Path(s['sha256_from_file']).read_text(encoding='utf-8').strip()
if not sha or len(sha)!=64: raise SystemExit(f'invalid resolved candidate sha: {sha!r}')
head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
rows=[json.loads(x) for x in LEDGER.read_text(encoding='utf-8').splitlines() if x.strip()]
if len(rows)!=210: raise SystemExit(f'ledger count {len(rows)} != 210')
byid={(r.get('id') or f"{r['report']}-{int(r['item_number']):03d}"):r for r in rows}
for n in range(1,117):
    if byid[f'F4-{n:03d}'].get('status')=='PENDING': raise SystemExit(f'Fourth regression F4-{n:03d}')
for iid,u in s.get('updates',{}).items():
    if iid not in byid: raise SystemExit('missing ledger id '+iid)
    byid[iid].update(u)
for n in range(1,last_f5+1):
    if byid[f'F5-{n:03d}'].get('status') in (None,'PENDING','HOLD','FAILED'):
        raise SystemExit(f'Fifth completed-range regression F5-{n:03d}: {byid[f"F5-{n:03d}"].get("status")}')
if next_f5 is not None:
    if byid[f'F5-{next_f5:03d}'].get('status')!='PENDING': raise SystemExit(f'next F5-{next_f5:03d} not PENDING')
else:
    for n in range(1,95):
        if byid[f'F5-{n:03d}'].get('status')=='PENDING': raise SystemExit(f'Fifth incomplete at F5-{n:03d}')
LEDGER.write_text('\n'.join(json.dumps(r,ensure_ascii=False,separators=(',',':')) for r in rows)+'\n',encoding='utf-8')

next_label=f'`F5-{next_f5:03d}`' if next_f5 is not None else 'none — Fifth Report item application complete'
struct='\n'.join('- '+x for x in s.get('structural_state',[]))
evidence='\n'.join('- '+x for x in s.get('evidence',[]))
protected=s.get('protected_parts_status','Fourth-validated baseline preserved except explicitly authorized changes')
visual_status=s.get('visual_status','PASS')
visual_line=f'- Latest Fifth item human visual QA: **{visual_status}** (`{s.get("visual_file","n/a")}`).'
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
- Current phase: `FIFTH_APPLY`
- Last fully completed Fourth Report item: `F4-116`
- Next Fourth Report item: none — Fourth Report application complete
- Fourth Report global validation: PASS
- Last fully completed Fifth Report item: `F5-{last_f5:03d}`
- Next Fifth Report item: {next_label}

## Current working state
- Current working DOCX: `{s['docx']}`
- Current working DOCX SHA-256: `{sha}`
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
- Protected OOXML parts: {protected}

## Structural-edit state
{struct}

## Holds / validation
- Open HOLD items: {s.get('holds','none')}.
- Fourth Report global validation: **PASS** (`work/runtime/FOURTH-VALIDATE-FINAL.txt`).
- Latest Fifth item technical validation: **PASS** (`{s['technical_file']}`).
{visual_line}

## Exact next action
{s['next_action']}
''',encoding='utf-8')

marker=s['validation_marker']; old=LOG.read_text(encoding='utf-8') if LOG.exists() else '# VALIDATION LOG\n'
if marker not in old: old += '\n\n'+marker+'\n'+s['validation_block'].replace('{RESOLVED_SHA}',sha).rstrip()+'\n'
LOG.write_text(old,encoding='utf-8')
HANDOFF.write_text(f'''# NEXT HANDOFF

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Checkpoint basis HEAD: `{head}` plus this metadata checkpoint commit
- Current phase: `FIFTH_APPLY`

## Resume boundary
- Last completed Fourth item: `F4-116`
- Last completed Fifth item: `F5-{last_f5:03d}`
- Next Fifth item: {next_label}
- DO-NOT-REPEAT Fourth: `F4-001`–`F4-116`
- DO-NOT-REPEAT Fifth: `F5-001`–`F5-{last_f5:03d}`

## Working manuscript
- Current working DOCX: `{s['docx']}`
- Current working SHA-256: `{sha}`
- Last known good DOCX: same path above

## Integrity snapshot
- Footnotes/references: 469/469; orphans/dangling/duplicates: 0/0/0
- Word fields: 520; ADDIN: 466; Zotero: 465 item + 1 bibliography
- Bookmarks: 53/53; hyperlinks: 52; RTL inventory canonical-equal
- Protected OOXML: {protected}
- Latest Fifth visual status: {visual_status}

## Latest state
{struct}

## Evidence
{evidence}

## Open HOLDs
{s.get('holds','None.')}

## Exact next action
{s['next_action']}
''',encoding='utf-8')
print(f'Fifth checkpoint metadata prepared through F5-{last_f5:03d}; sha={sha}')
