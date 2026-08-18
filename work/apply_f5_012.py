#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import hashlib, shutil, sys

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}
EXPECTED_INPUT_SHA='c99826db06c605f5950e682c82af6d5c6f481d0c43a3364d029daadabe51fc19'
OLD='Kitabın literatüre sağlamayı hedeflediği katkı, resm ilmi ile kırâat ilmini bütünüyle yeni kavramlarla açıklamak değil, çoğu zaman ayrı başlıklar altında incelenen meseleleri ortak bir problem etrafında buluşturmaktır.'
NEW='Kitabın literatüre hedeflediği katkı, çoğu zaman ayrı başlıklar altında incelenen resm ve kırâat meselelerini ortak bir problem etrafında birlikte değerlendirmektir.'

def sha256(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''): h.update(chunk)
    return h.hexdigest()

def text(el): return ''.join(el.xpath('.//w:t/text()',namespaces=NS))
def c14n(el): return etree.tostring(el,method='c14n')
def sig(el): return tuple((n.tag,tuple(sorted(n.attrib.items()))) for n in el.iter())
def instrs(z):
    out=[]
    for n in z.namelist():
        if n.startswith('word/') and n.endswith('.xml'):
            try:r=etree.fromstring(z.read(n))
            except Exception:continue
            out += [''.join(x.itertext()).strip() for x in r.xpath('//w:instrText',namespaces=NS)]
    return out

def replace_range(p,start,end,new):
    nodes=p.xpath('.//w:t',namespaces=NS); vals=[n.text or '' for n in nodes]; starts=[];cur=0
    for v in vals: starts.append(cur);cur+=len(v)
    fi=next(i for i,(st,v) in enumerate(zip(starts,vals)) if start<st+len(v))
    li=next(i for i,(st,v) in enumerate(zip(starts,vals)) if end<=st+len(v))
    prefix=vals[fi][:start-starts[fi]]; suffix=vals[li][end-starts[li]:]
    nodes[fi].text=prefix+new+(suffix if fi==li else '')
    if fi!=li:
        for j in range(fi+1,li): nodes[j].text=''
        nodes[li].text=suffix

def locate(ps,needle):
    hits=[i for i,p in enumerate(ps) if needle in text(p)]
    if len(hits)!=1:
        candidates=[(i,text(p)) for i,p in enumerate(ps) if ('literatür' in text(p).lower() or 'katkı' in text(p).lower())]
        raise RuntimeError(f'unique target failure for {needle!r}: {hits}; candidates={candidates!r}')
    return hits[0]

def satisfied(d):
    ps=d.xpath('.//w:body/w:p',namespaces=NS)
    if len(ps)!=674: return False
    old_hits=[i for i,p in enumerate(ps) if OLD in text(p)]
    new_hits=[i for i,p in enumerate(ps) if NEW in text(p)]
    return old_hits==[] and len(new_hits)==1

def apply(src,out):
    actual_sha=sha256(src)
    with ZipFile(src,'r') as zin:
        original={i.filename:zin.read(i.filename) for i in zin.infolist()}
        d=etree.fromstring(original['word/document.xml']); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        if len(ps)!=674: raise RuntimeError('body count')
        if satisfied(d):
            idx=locate(ps,NEW)
            shutil.copyfile(src,out); validate(src,out,False,idx)
            print(f'F5-012\tALREADY_SATISFIED\tP{idx}'); return
        if actual_sha!=EXPECTED_INPUT_SHA:
            raise RuntimeError('input sha mismatch '+actual_sha)
        idx=locate(ps,OLD); p=ps[idx]; before=text(p)
        if before.count(OLD)!=1 or NEW in before: raise RuntimeError('target paragraph precondition')
        expected=before.replace(OLD,NEW,1); bs=sig(p)
        start=before.index(OLD); end=start+len(OLD)
        replace_range(p,start,end,NEW)
        after=text(p)
        if after!=expected or sig(p)!=bs: raise RuntimeError('F5-012 postcondition/structure failure')
        if not satisfied(d): raise RuntimeError('F5-012 document satisfaction failure')
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else original[info.filename])
    validate(src,out,True,idx)
    print(f'F5-012\tAPPLIED\tP{idx}'); print('BEFORE\t'+before); print('AFTER\t'+after)

def validate(src,out,chg,idx):
    with ZipFile(src) as a,ZipFile(out) as b:
        if a.namelist()!=b.namelist() or b.testzip() is not None: raise RuntimeError('zip invariant')
        for n in a.namelist():
            if n!='word/document.xml' and a.read(n)!=b.read(n): raise RuntimeError('unexpected package change '+n)
        da=etree.fromstring(a.read('word/document.xml')); db=etree.fromstring(b.read('word/document.xml'))
        pa=da.xpath('.//w:body/w:p',namespaces=NS); pb=db.xpath('.//w:body/w:p',namespaces=NS)
        if len(pa)!=674 or len(pb)!=674: raise RuntimeError('body count invariant')
        changed=[i for i,(x,y) in enumerate(zip(pa,pb)) if c14n(x)!=c14n(y)]
        if changed!=([idx] if chg else []): raise RuntimeError('paragraph change set '+repr(changed))
        if sig(pa[idx])!=sig(pb[idx]) or not satisfied(db): raise RuntimeError('target paragraph/document invariant')
        ia=instrs(a); ib=instrs(b)
        if ia!=ib or len(ib)!=520: raise RuntimeError('fields')
        if (sum('ADDIN ' in x for x in ib),sum('ZOTERO_ITEM' in x for x in ib),sum('ZOTERO_BIBL' in x for x in ib))!=(466,465,1): raise RuntimeError('zotero')
        ra=da.xpath('//w:footnoteReference/@w:id',namespaces=NS); rb=db.xpath('//w:footnoteReference/@w:id',namespaces=NS)
        if ra!=rb or len(rb)!=469 or len(set(rb))!=469: raise RuntimeError('footnotes')
        if len(db.xpath('//w:bookmarkStart',namespaces=NS))!=53 or len(db.xpath('//w:bookmarkEnd',namespaces=NS))!=53 or len(db.xpath('//w:hyperlink',namespaces=NS))!=52: raise RuntimeError('bookmarks/hyperlinks')
        if len(da.xpath('//w:rtl',namespaces=NS))!=len(db.xpath('//w:rtl',namespaces=NS)): raise RuntimeError('rtl')

if __name__=='__main__':
    if len(sys.argv)!=3: raise SystemExit('usage: apply_f5_012.py INPUT.docx OUTPUT.docx')
    apply(Path(sys.argv[1]),Path(sys.argv[2]))
