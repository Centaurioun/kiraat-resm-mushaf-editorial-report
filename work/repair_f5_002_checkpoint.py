#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET
import hashlib, json, subprocess

R=Path('.')
INP=R/'artifacts/checkpoints/manuscript-working-f5-001.docx'
CUR=R/'artifacts/checkpoints/manuscript-working-f5-002.docx'
LEDGER=R/'work/application-ledger.jsonl'
STATE=R/'work/APPLICATION-STATE.md'
LOG=R/'work/VALIDATION-LOG.md'
HANDOFF=R/'work/NEXT-HANDOFF.md'
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
OLD='Bu sorular birbirinden bağımsız değildir.'
NEW='Araştırma soruları birbirine bağlıdır.'
REST=' Osmânî mushafların ortak başvuru metni hâline gelme süreci, resm-i Osmânî’nin kabul ölçüsü hâline gelişinden ayrı anlaşılamaz. Kırâatin rivâyet mantığı da yalnız resm üzerinden değerlendirilemez.'

def ptext(p):
    return ''.join((t.text or '') for t in p.iter(W+'t'))

def body_ps(root):
    body=root.find('.//'+W+'body')
    return [x for x in list(body) if x.tag==W+'p']

def xml_sig(el):
    return ET.tostring(el,encoding='utf-8')

def field_inventory(z):
    vals=[]
    for n in z.namelist():
        if n.startswith('word/') and n.endswith('.xml'):
            try:r=ET.fromstring(z.read(n))
            except Exception: continue
            for x in r.iter(W+'instrText'):
                vals.append(''.join(x.itertext()).strip())
    return vals

if not INP.exists() or not CUR.exists():
    raise SystemExit('missing F5-001 input or F5-002 candidate')
sha=hashlib.sha256(CUR.read_bytes()).hexdigest()

with ZipFile(INP) as za, ZipFile(CUR) as zb:
    if za.testzip() is not None or zb.testzip() is not None: raise SystemExit('ZIP CRC failure')
    if za.namelist()!=zb.namelist(): raise SystemExit('ZIP member/order changed')
    for n in za.namelist():
        if n!='word/document.xml' and za.read(n)!=zb.read(n):
            raise SystemExit('unexpected package change: '+n)
    da=ET.fromstring(za.read('word/document.xml')); db=ET.fromstring(zb.read('word/document.xml'))
    pa=body_ps(da); pb=body_ps(db)
    if len(pa)!=674 or len(pb)!=674: raise SystemExit(f'body paragraphs {len(pa)}->{len(pb)} != 674')
    changed=[i for i,(a,b) in enumerate(zip(pa,pb)) if xml_sig(a)!=xml_sig(b)]
    if changed!=[22]: raise SystemExit(f'changed paragraphs {changed} != [22]')
    before=ptext(pa[22]); after=ptext(pb[22])
    if not before.startswith(OLD+REST): raise SystemExit('F5-001 P22 does not match authoritative precondition')
    if not after.startswith(NEW+REST): raise SystemExit('F5-002 P22 does not match authoritative postcondition')
    if OLD in after: raise SystemExit('old F5-002 sentence survives')
    ia=field_inventory(za); ib=field_inventory(zb)
    if ia!=ib or len(ib)!=520: raise SystemExit('field instruction inventory changed')
    addin=sum('ADDIN ' in x for x in ib); item=sum('ZOTERO_ITEM' in x for x in ib); bib=sum('ZOTERO_BIBL' in x for x in ib)
    if (addin,item,bib)!=(466,465,1): raise SystemExit(f'ADDIN/Zotero inventory {(addin,item,bib)}')
    ra=[x.attrib.get(W+'id') for x in da.iter(W+'footnoteReference')]
    rb=[x.attrib.get(W+'id') for x in db.iter(W+'footnoteReference')]
    if ra!=rb or len(rb)!=469 or len(set(rb))!=469: raise SystemExit('footnote reference identity/order changed')
    if len(list(db.iter(W+'bookmarkStart')))!=53 or len(list(db.iter(W+'bookmarkEnd')))!=53: raise SystemExit('bookmark inventory changed')
    if len(list(db.iter(W+'hyperlink')))!=52: raise SystemExit('hyperlink inventory changed')
    if len(list(da.iter(W+'rtl')))!=len(list(db.iter(W+'rtl'))): raise SystemExit('RTL inventory changed')

rows=[json.loads(x) for x in LEDGER.read_text(encoding='utf-8').splitlines() if x.strip()]
if len(rows)!=210: raise SystemExit(f'ledger count {len(rows)} != 210')
byid={(r.get('id') or f"{r['report']}-{int(r['item_number']):03d}"):r for r in rows}
if byid['F5-001'].get('status') in (None,'PENDING','HOLD','FAILED'): raise SystemExit('F5-001 is not durable')
if byid['F5-003'].get('status')!='PENDING': raise SystemExit('F5-003 must remain PENDING')
byid['F5-002'].update({
    'status':'APPLIED',
    'section':'Giriş — araştırma sorularının olumlu ilişkilendirilmesi',
    'action_type':'TARGETED_POSITIVE_SENTENCE_REWRITE_WITH_FOURTH_PRECEDENCE',
    'resolved_location':'word/document.xml P22',
    'affected_body_paragraphs':[22],
    'verification':'ITEM_IDENTITY_PASS + P22_ONLY_CHANGE + STRUCTURAL_PASS + HUMAN_VISUAL_PASS',
    'notes':'Prior F5-002 no-op metadata was misbound to another issue and is superseded by work/F5-002-CORRECTION-NOTE.md. Actual F5-002 changes only the first P22 sentence to a positive formulation while preserving the Fourth-scientific follow-up.'
})
LEDGER.write_text('\n'.join(json.dumps(r,ensure_ascii=False,separators=(',',':')) for r in rows)+'\n',encoding='utf-8')

head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
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
- Last fully completed Fifth Report item: `F5-002`
- Next Fifth Report item: `F5-003`

## Current working state
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f5-002.docx`
- Current working DOCX SHA-256: `{sha}`
- Last known good commit basis: `{head}`
- Last known good DOCX: `artifacts/checkpoints/manuscript-working-f5-002.docx`
- Current body paragraph count: 674

## Integrity
- Genuine footnotes/references: 469/469; identity/order preserved
- Orphan/dangling/duplicate references: 0/0/0
- Word field instructions: 520/520; ADDIN: 466/466
- Zotero: 465 item + 1 bibliography preserved
- Bookmarks: 53/53; hyperlinks: 52
- Arabic/RTL structural inventory: unchanged from durable F5-001 input
- Package scope: only `word/document.xml` changed; only body P22 differs from F5-001

## Structural-edit state
- Fourth Report F4-001–116 and FOURTH_VALIDATE remain fully accepted.
- F5-001 remains durable VERIFIED_NO_CHANGE.
- F5-002 is APPLIED / PASS at P22: `Araştırma soruları birbirine bağlıdır.`
- The accepted Fourth-scientific follow-up in P22 is preserved unchanged.
- The earlier misbound F5-002 no-op metadata is superseded by `work/F5-002-CORRECTION-NOTE.md` and `work/F5-002-ACTUAL-ADJUDICATION.md`.
- F5-003 remains PENDING and has not been pre-applied.

## Holds / validation
- Open HOLD items: none.
- Fourth Report global validation: PASS.
- F5-002 deterministic/structural adjudication: PASS (`work/F5-002-ACTUAL-ADJUDICATION.md`).
- F5-002 candidate SHA-256 independently recomputed by repair checkpoint: `{sha}`.
- F5-002 human visual QA: PASS (bounded P20–P24 review recorded in `work/F5-002-ACTUAL-ADJUDICATION.md`).

## Exact next action
Fetch the exact F5-003 item from `final/fifth-report-locked.md`, resolve it against the durable F5-002 binary, and apply only F5-003 if unambiguous. Preserve Fourth scientific meaning and do not pre-apply F5-004+.
''',encoding='utf-8')

marker='## F5-002 authoritative metadata reconciliation — APPLIED / PASS'
old=LOG.read_text(encoding='utf-8') if LOG.exists() else '# VALIDATION LOG\n'
if marker not in old:
    old += f'''\n\n{marker}
- Prior F5-002 no-op metadata was found to be bound to the wrong Fifth Report issue; the no-op caused no manuscript byte corruption.
- Actual F5-002 item identity: Giriş P22, `Bu sorular birbirinden bağımsız değildir.`
- Accepted correction: `Araştırma soruları birbirine bağlıdır.`; accepted Fourth-scientific follow-up preserved.
- F5-001 → F5-002 package comparison: only `word/document.xml` differs; only body P22 differs; all other package parts byte-identical.
- Structural invariants: body 674; footnote refs 469/469 identity/order preserved; fields 520; ADDIN 466; Zotero ITEM 465 + bibliography 1; bookmarks 53/53; hyperlinks 52; RTL count unchanged.
- Candidate SHA-256 recomputed inside checkpoint: `{sha}`.
- Human visual QA: PASS per `work/F5-002-ACTUAL-ADJUDICATION.md`.
- Durable boundary: last F5-002; next F5-003.
'''
LOG.write_text(old,encoding='utf-8')

HANDOFF.write_text(f'''# NEXT HANDOFF

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Checkpoint basis HEAD: `{head}` plus this metadata checkpoint commit
- Current phase: `FIFTH_APPLY`

## Resume boundary
- Last completed Fourth item: `F4-116`
- Last completed Fifth item: `F5-002`
- Next Fifth item: `F5-003`
- DO-NOT-REPEAT Fourth: `F4-001`–`F4-116`
- DO-NOT-REPEAT Fifth: `F5-001`–`F5-002`

## Working manuscript
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f5-002.docx`
- Current working SHA-256: `{sha}`
- Body paragraphs: 674

## Integrity snapshot
- Footnotes/references: 469/469; identity/order preserved
- Word fields: 520; ADDIN: 466; Zotero: 465 item + 1 bibliography
- Bookmarks: 53/53; hyperlinks: 52; RTL inventory unchanged
- F5-002 package scope: only `word/document.xml` / P22 differs from F5-001

## Latest state
- F5-002 actual item was corrected after an item-number metadata misbinding audit.
- Accepted P22 opening: `Araştırma soruları birbirine bağlıdır.`
- Earlier F5-002 no-op metadata is superseded; no manuscript corruption resulted from it.
- F5-003 remains PENDING.

## Evidence
- `work/F5-002-CORRECTION-NOTE.md`
- `work/F5-002-ACTUAL-ADJUDICATION.md`
- `work/apply_f5_002.py`
- Recomputed candidate SHA-256: `{sha}`

## Open HOLDs
None.

## Exact next action
Fetch and adjudicate only F5-003 from `final/fifth-report-locked.md` against `artifacts/checkpoints/manuscript-working-f5-002.docx`. Do not pre-apply F5-004+.
''',encoding='utf-8')
print('F5-002 authoritative metadata reconciliation PASS; sha256='+sha)
