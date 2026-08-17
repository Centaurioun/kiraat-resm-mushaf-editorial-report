#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from collections import Counter
import hashlib, json, sys, traceback

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
NS={'w':W}
CANONICAL=Path('source/manuscript/current/redaktorden_gelen.docx')
CANONICAL_SHA='d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54'
EXPECTED_BODY=674
AUTHORIZED_FN={2,28,32,41,50,66,105,271,272,273,274,292,342,344,345,346,377,380,381,407,409,411,414,421,423,424,425,426,427,428,431}
PROTECTED=['word/styles.xml','word/numbering.xml','word/settings.xml','word/_rels/document.xml.rels']

K_BAD='https://doi.org/http://doi.org/1051702/esoguifd.791085'
M_BAD='https://doi.org/https://doi.org/10.56361/usul.173700'
M_GOOD='https://doi.org/10.56361/usul.173700'
DROP_2006="İbn Ebû Dâvud, Ebû Bekir Abdullah b. Süleymân. Kitâbu’l-mesâhif. thk. Selîm b. Îde’l-Hilâlî el-Eserî. Amman: Ğarâs, 2006."
DROP_ASFAR="İbn Kuteybe, Ebû Muhammed Abdullah b. Muslim. Te’vîlu muhtelifi’l-hadîs. thk. Muhammed Muhyiddîn el-Asfar. Beyrut: el-Mektebetü’l-İslâmî, 1999."
KEEP_2002="İbn Ebû Dâvud, Ebû Bekir Abdullah b. Süleymân b. el-Eş’as. Kitâbu’l-mesâhif. thk. Muhibbüddîn Abdussubhân Vâiz. 2 Cilt. Beyrut: Dâru’l-Beşâiri’l-İslâmiyye, 2002."
KEEP_NECCAR="İbn Kuteybe, Ebû Muhammed Abdullah b. Muslim. Te’vîlu muhtelifu’l-hadîs. thk. Muhammed Zuhrî en-Neccâr. Mektebetü’l-Küllîyât el-Ezheriyye, ts."
KEEP_NECAH_2000="Ebû Dâvud, Süleymân b. Necâh. Muhtasaru’t-tebyîn li hecâi’t-tenzîl. thk. Ahmed b. Muhammed b. Muammer Şarşâl. 5 Cilt. Riyad: Mecmeu’l-Melik Fehd li’t-Tibâati’l-Mushafi’ş-Şerîf, 2000."
KEEP_NECAH_1999="Necâh, Ebû Dâvud Süleymân b. Muhtasaru’t-tebyîn li hecâi’t-tenzîl. thk. Ahmed b. Ahmed Muammer Şarşâl. 2 Cilt. Medine: Mecmau’l-Melik Fahd li’t-Tibâati ve’n-Neşr, 1999."
EBU_1975_BAD="Ebû Şâme, Şihâbuddîn Abdurrahmân b. İsmâîl. el-Murşidu’l-vecîz ilâ ulûmin tetaallaku bi’l-kitâbi’l-azîz. thk. Tayyar Altıkulaç. 2 Cilt. Beyrut: Dâr Sadr, 1975."
EBU_1975_GOOD="Ebû Şâme, Şihâbuddîn Abdurrahmân b. İsmâîl. el-Murşidu’l-vecîz ilâ ulûmin tetaallaku bi’l-kitâbi’l-azîz. thk. Tayyar Altıkulaç. Beyrut: Dâr Sadr, 1975."
EBU_1993="Ebû Şâme, Şihâbuddîn Abdurrahmân İsmâîl. el-Murşidu’l-vecîz ilâ ulûmin tetaallaku bi’l-kitâbi’l-Azîz. thk. Velîd Müsâid et-Tabatabâî. Kuveyt: Mektebetü’l-İmâm ez-Zehebî, 1993."
WORK_NOTES=('bu dipnot daha önce geçmiş midir','bu eserin müellifi meçhuldür literatürde bu şekilde geçiyor','bu eser daha önce tam adıyla geçmişmiydi')


def text(el): return ''.join(el.xpath('.//w:t/text()',namespaces=NS))
def c14n(el): return etree.tostring(el,method='c14n')
def sig(el): return tuple((n.tag,tuple(sorted(n.attrib.items()))) for n in el.iter())
def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def instrs(z):
    vals=[]
    for name in z.namelist():
        if name.startswith('word/') and name.endswith('.xml'):
            try:r=etree.fromstring(z.read(name))
            except Exception:continue
            vals += [''.join(x.itertext()).strip() for x in r.xpath('//w:instrText',namespaces=NS)]
    return vals


def main(candidate,outfile):
    fatal=[]; defects=[]; notes=[]; lines=[]
    candidate=Path(candidate); outfile=Path(outfile)
    def check(cond,msg):
        if not cond: fatal.append(msg)
    try:
        check(candidate.exists(),f'candidate missing: {candidate}')
        check(CANONICAL.exists(),f'canonical missing: {CANONICAL}')
        if fatal: raise RuntimeError('; '.join(fatal))
        candidate_sha=sha(candidate); canonical_sha=sha(CANONICAL)
        check(canonical_sha==CANONICAL_SHA,f'canonical SHA mismatch {canonical_sha} != {CANONICAL_SHA}')

        ledger_path=Path('work/application-ledger.jsonl')
        rows=[json.loads(x) for x in ledger_path.read_text(encoding='utf-8').splitlines() if x.strip()]
        check(len(rows)==210,f'ledger row count {len(rows)} != 210')
        byid={(r.get('id') or f"{r['report']}-{int(r['item_number']):03d}"):r for r in rows}
        f4=[byid.get(f'F4-{n:03d}') for n in range(1,117)]
        f5=[byid.get(f'F5-{n:03d}') for n in range(1,95)]
        check(all(r is not None for r in f4),'one or more F4 ids missing')
        check(all(r is not None for r in f5),'one or more F5 ids missing')
        if all(r is not None for r in f4):
            bad=[(r['id'],r.get('status')) for r in f4 if str(r.get('status','')).upper() in {'PENDING','HOLD','FAILED'} or not r.get('status')]
            check(not bad,f'Fourth ledger incomplete statuses: {bad}')
        if all(r is not None for r in f5):
            not_pending=[(r['id'],r.get('status')) for r in f5 if r.get('status')!='PENDING']
            check(not not_pending,f'Fifth Report changed before Fourth validation: {not_pending[:10]}')

        state=Path('work/APPLICATION-STATE.md').read_text(encoding='utf-8')
        check('Current phase: `FOURTH_VALIDATE`' in state,'APPLICATION-STATE phase is not FOURTH_VALIDATE')
        check('Last fully completed Fourth Report item: `F4-116`' in state,'APPLICATION-STATE last F4 is not F4-116')
        check('Next Fourth Report item: none — Fourth Report application complete' in state,'APPLICATION-STATE does not mark Fourth apply complete')

        with ZipFile(CANONICAL) as zs, ZipFile(candidate) as z:
            check(z.testzip() is None,'candidate ZIP CRC failure')
            check(zs.namelist()==z.namelist(),'ZIP member/order differs from canonical')
            for name in z.namelist():
                if name.endswith('.xml') or name.endswith('.rels'):
                    try: etree.fromstring(z.read(name))
                    except Exception as e: fatal.append(f'XML parse failure {name}: {e}')
            ds=etree.fromstring(zs.read('word/document.xml')); d=etree.fromstring(z.read('word/document.xml'))
            fs=etree.fromstring(zs.read('word/footnotes.xml')); f=etree.fromstring(z.read('word/footnotes.xml'))
            ps=d.xpath('.//w:body/w:p',namespaces=NS)
            check(len(ps)==EXPECTED_BODY,f'body paragraph count {len(ps)} != {EXPECTED_BODY}')

            f0=[x for x in fs.xpath('./w:footnote/@w:id',namespaces=NS) if int(x)>0]
            ff=[x for x in f.xpath('./w:footnote/@w:id',namespaces=NS) if int(x)>0]
            r0=ds.xpath('//w:footnoteReference/@w:id',namespaces=NS); rr=d.xpath('//w:footnoteReference/@w:id',namespaces=NS)
            check(ff==f0,'genuine footnote ID/order differs from canonical')
            check(len(ff)==469 and len(rr)==469,f'footnotes/references {len(ff)}/{len(rr)} !=469/469')
            check(set(ff)==set(rr),'footnote/reference identity sets differ')
            check(Counter(rr)==Counter(r0),'body footnote reference identity multiset differs from canonical')
            check(not [k for k,v in Counter(rr).items() if v>1],'duplicate body footnote references present')

            ids_all=fs.xpath('./w:footnote/@w:id',namespaces=NS); ids_cur=f.xpath('./w:footnote/@w:id',namespaces=NS)
            check(ids_all==ids_cur,'all footnote IDs/order differs from canonical')
            changed=[]
            if ids_all==ids_cur:
                for fid in ids_all:
                    a=fs.xpath(f'./w:footnote[@w:id="{fid}"]',namespaces=NS); b=f.xpath(f'./w:footnote[@w:id="{fid}"]',namespaces=NS)
                    if len(a)!=1 or len(b)!=1:
                        fatal.append(f'footnote multiplicity changed for id {fid}'); continue
                    if c14n(a[0])!=c14n(b[0]):
                        if int(fid)>0: changed.append(int(fid))
                        if int(fid) not in AUTHORIZED_FN: fatal.append(f'unauthorized footnote change FN{fid}')
                        elif sig(a[0])!=sig(b[0]): fatal.append(f'authorized FN{fid} structure changed')
            check(set(changed)==AUTHORIZED_FN,f'canonical-to-current changed footnote set {sorted(set(changed))} != authorized {sorted(AUTHORIZED_FN)}')

            i0=instrs(zs); ii=instrs(z)
            check(ii==i0,'Word field instruction sequence differs from canonical')
            check(len(ii)==520,f'field instruction count {len(ii)} !=520')
            addin=sum('ADDIN ' in x for x in ii); item=sum('ZOTERO_ITEM' in x for x in ii); bib=sum('ZOTERO_BIBL' in x for x in ii)
            check((addin,item,bib)==(466,465,1),f'ADDIN/Zotero inventory {(addin,item,bib)} != (466,465,1)')
            check(len(d.xpath('//w:bookmarkStart',namespaces=NS))==53 and len(d.xpath('//w:bookmarkEnd',namespaces=NS))==53,'bookmark count !=53/53')
            check(len(d.xpath('//w:hyperlink',namespaces=NS))==52,'hyperlink count !=52')
            check(len(d.xpath('//w:rtl',namespaces=NS))==len(ds.xpath('//w:rtl',namespaces=NS)),'RTL inventory differs from canonical')
            for name in PROTECTED:
                check(z.read(name)==zs.read(name),f'protected part differs from canonical: {name}')

            texts=[text(p) for p in ps]
            body='\n'.join(texts); foot='\n'.join(text(x) for x in f.xpath('./w:footnote',namespaces=NS))
            # F4-110: bibliography boundary remains explicit and bookmark-backed.
            kh=[(i,p) for i,p in enumerate(ps) if text(p).strip()=='Kaynakça']
            check(len(kh)==1,f'Kaynakça heading count {len(kh)} !=1')
            if len(kh)==1:
                i,p=kh[0]
                check(bool(p.xpath('./w:pPr/w:pageBreakBefore',namespaces=NS)),f'Kaynakça P{i} lost pageBreakBefore')
                check(bool(p.xpath('.//w:bookmarkStart',namespaces=NS)),f'Kaynakça P{i} lost bookmarkStart')

            # F4-112 working notes must stay absent.
            for pat in WORK_NOTES:
                check(pat.casefold() not in foot.casefold(),f'working/editor note survives in footnotes: {pat}')
            # F4-114 DOI repairs.
            check(K_BAD not in body,'malformed Kahraman DOI survives')
            check(M_BAD not in body,'malformed Maşalı double DOI survives')
            check(body.count(M_GOOD)==1,f'correct Maşalı DOI count {body.count(M_GOOD)} !=1')
            # F4-115 edition pruning and retention.
            check(body.count(DROP_2006)==0,'unused İbn Ebû Dâvud 2006 record survives')
            check(body.count(DROP_ASFAR)==0,'unused İbn Kuteybe el-Asfar 1999 record survives')
            for keep in (KEEP_2002,KEEP_NECCAR,KEEP_NECAH_2000,KEEP_NECAH_1999,EBU_1993):
                check(body.count(keep)==1,f'required bibliography record count {body.count(keep)} !=1: {keep[:80]}')
            # F4-116 dual-edition retention; validation defect tracked separately.
            e1975_count=body.count(EBU_1975_BAD)+body.count(EBU_1975_GOOD)
            check(e1975_count==1,f'Ebû Şâme 1975 record total count {e1975_count} !=1')
            if body.count(EBU_1975_BAD)==1:
                idx=texts.index(EBU_1975_BAD)
                defects.append(f'FV-001|P{idx}|Ebû Şâme 1975 bibliography record incorrectly states `2 Cilt`; authoritative edition metadata identifies a single-volume publication. Remove only ` 2 Cilt.` from visible bibliography result text.')
            elif body.count(EBU_1975_GOOD)==1:
                notes.append('FV-001_RESOLVED|Ebû Şâme 1975 bibliography record has no erroneous `2 Cilt` statement.')
            else:
                fatal.append('Ebû Şâme 1975 record is neither expected pre-remediation nor expected corrected form')

        status='PASS' if not fatal and not defects else ('DEFECTS_FOUND' if not fatal else 'FATAL_FAIL')
        lines=[
            f'FOURTH_VALIDATE_READONLY={status}',
            f'CANDIDATE={candidate}',
            f'CANDIDATE_SHA256={candidate_sha}',
            f'CANONICAL_SHA256={canonical_sha}',
            f'BODY_PARAGRAPHS={EXPECTED_BODY}',
            'LEDGER_ROWS=210',
            'F4_ITEMS=116',
            'F5_ITEMS=94',
            'FOOTNOTES=469',
            'REFERENCES=469',
            'ORPHANS_DANGLING_DUPLICATES=0/0/0',
            'FIELDS=520',
            'ADDIN=466',
            'ZOTERO_ITEM=465',
            'ZOTERO_BIBLIOGRAPHY=1',
            'BOOKMARKS=53/53',
            'HYPERLINKS=52',
            'AUTHORIZED_CHANGED_FOOTNOTES='+','.join(map(str,sorted(AUTHORIZED_FN))),
            f'FATAL_COUNT={len(fatal)}',
            f'RESIDUAL_DEFECT_COUNT={len(defects)}',
            'FIFTH_BLOCKED='+('YES' if status!='PASS' else 'NO'),
        ]
        lines += ['FATAL|'+x for x in fatal]
        lines += ['DEFECT|'+x for x in defects]
        lines += ['NOTE|'+x for x in notes]
    except Exception:
        fatal.append('validator exception: '+traceback.format_exc().replace('\n',' | '))
        lines=[
            'FOURTH_VALIDATE_READONLY=FATAL_FAIL',
            f'CANDIDATE={candidate}',
            f'FATAL_COUNT={len(fatal)}',
            'FIFTH_BLOCKED=YES',
        ] + ['FATAL|'+x for x in fatal]

    outfile.parent.mkdir(parents=True,exist_ok=True)
    outfile.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print('\n'.join(lines))
    # Evidence-producing validator: semantic defects are reported in-band.
    # Exit non-zero only if the output file itself could not be written.
    return 0

if __name__=='__main__':
    if len(sys.argv)!=3:
        raise SystemExit('usage: validate_fourth.py CANDIDATE.docx OUTPUT.txt')
    raise SystemExit(main(sys.argv[1],sys.argv[2]))
