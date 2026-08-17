#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys,re

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}
STALE={
 '32':"(bu dipnot daha önce geçmiş midir.yoksa kitabın ilk adı bu şekilde mi) buna bakılması.",
 '41':"(bu eserin müellifi meçhuldür literatürde bu şekilde geçiyor.",
 '105':"(bu eser daha önce tam adıyla geçmişmiydi)",
}

def text(el): return ''.join(el.xpath('.//w:t/text()',namespaces=NS))
def sig(el): return tuple((n.tag,tuple(sorted(n.attrib.items()))) for n in el.iter())
def c14n(el): return etree.tostring(el,method='c14n')

def replace_span(el,old,new):
    nodes=el.xpath('.//w:t',namespaces=NS); vals=[n.text or '' for n in nodes]; full=''.join(vals)
    hits=[m.start() for m in re.finditer(re.escape(old),full)]
    if not hits:
        if old not in full:return 'ALREADY_SATISFIED'
        raise RuntimeError('unreachable')
    if len(hits)!=1: raise RuntimeError(f'non-unique stale span {old!r}: {len(hits)}')
    pos=hits[0]; end=pos+len(old); starts=[]; cur=0
    for v in vals: starts.append(cur); cur+=len(v)
    fi=next(i for i,(st,v) in enumerate(zip(starts,vals)) if pos < st+len(v))
    li=next(i for i,(st,v) in enumerate(zip(starts,vals)) if end <= st+len(v))
    prefix=vals[fi][:pos-starts[fi]]; suffix=vals[li][end-starts[li]:]
    nodes[fi].text=prefix+new+(suffix if fi==li else '')
    if fi!=li:
        for j in range(fi+1,li): nodes[j].text=''
        nodes[li].text=suffix
    return 'APPLIED'

def validate(src,out):
    with ZipFile(src) as za, ZipFile(out) as zb:
        if za.namelist()!=zb.namelist(): raise RuntimeError('ZIP member/order changed')
        for n in za.namelist():
            if n!='word/footnotes.xml' and za.read(n)!=zb.read(n): raise RuntimeError(f'unexpected OOXML/package change: {n}')
        da=etree.fromstring(za.read('word/document.xml')); db=etree.fromstring(zb.read('word/document.xml'))
        fa=etree.fromstring(za.read('word/footnotes.xml')); fb=etree.fromstring(zb.read('word/footnotes.xml'))
        ids_a=fa.xpath('./w:footnote/@w:id',namespaces=NS); ids_b=fb.xpath('./w:footnote/@w:id',namespaces=NS)
        refs_a=da.xpath('.//w:footnoteReference/@w:id',namespaces=NS); refs_b=db.xpath('.//w:footnoteReference/@w:id',namespaces=NS)
        if ids_a!=ids_b or refs_a!=refs_b: raise RuntimeError('footnote identity/reference order changed')
        if len(refs_b)!=469 or len(set(refs_b))!=469:
            raise RuntimeError(f'body footnote reference inventory {len(refs_b)} refs / {len(set(refs_b))} unique != 469/469')
        if len(ids_b)!=len(ids_a): raise RuntimeError(f'raw footnote element count changed {len(ids_a)}->{len(ids_b)}')
        idset=set(ids_b)
        missing=[x for x in refs_b if x not in idset]
        if missing: raise RuntimeError(f'body references missing from footnotes.xml: {missing[:10]}')
        for fid in ids_a:
            aa=fa.xpath(f'./w:footnote[@w:id="{fid}"]',namespaces=NS); bb=fb.xpath(f'./w:footnote[@w:id="{fid}"]',namespaces=NS)
            if len(aa)!=1 or len(bb)!=1: raise RuntimeError(f'footnote {fid} multiplicity changed')
            if fid not in STALE and c14n(aa[0])!=c14n(bb[0]): raise RuntimeError(f'non-target footnote changed: {fid}')
        for fid,stale in STALE.items():
            aa=fa.xpath(f'./w:footnote[@w:id="{fid}"]',namespaces=NS)[0]; bb=fb.xpath(f'./w:footnote[@w:id="{fid}"]',namespaces=NS)[0]
            if sig(aa)!=sig(bb): raise RuntimeError(f'target footnote structural drift: {fid}')
            if stale in text(bb): raise RuntimeError(f'stale work note remains: FN{fid}')
            if len(text(bb).strip())<20: raise RuntimeError(f'FN{fid} citation unexpectedly truncated')
        # document.xml is required byte-identical above; assert field/bookmark inventories pre/post rather than assuming a fixed fldChar count.
        if da.xpath('.//w:fldChar/@w:fldCharType',namespaces=NS) != db.xpath('.//w:fldChar/@w:fldCharType',namespaces=NS):
            raise RuntimeError('field-character inventory changed')
        if da.xpath('.//w:instrText/text()',namespaces=NS) != db.xpath('.//w:instrText/text()',namespaces=NS):
            raise RuntimeError('field-instruction inventory changed')
        if da.xpath('.//w:bookmarkStart/@w:id',namespaces=NS) != db.xpath('.//w:bookmarkStart/@w:id',namespaces=NS):
            raise RuntimeError('bookmark-start inventory changed')
        if da.xpath('.//w:bookmarkEnd/@w:id',namespaces=NS) != db.xpath('.//w:bookmarkEnd/@w:id',namespaces=NS):
            raise RuntimeError('bookmark-end inventory changed')
        for n in zb.namelist():
            if n.endswith('.xml') or n.endswith('.rels'): etree.fromstring(zb.read(n))

def complete(path):
    with ZipFile(path) as z:
        f=etree.fromstring(z.read('word/footnotes.xml'))
        return all(len(f.xpath(f'./w:footnote[@w:id="{fid}"]',namespaces=NS))==1 and stale not in text(f.xpath(f'./w:footnote[@w:id="{fid}"]',namespaces=NS)[0]) for fid,stale in STALE.items())

def apply(src,out):
    if complete(src): validate(src,src); shutil.copyfile(src,out); return [('F4-112','FN32,41,105','ALREADY_SATISFIED')]
    with ZipFile(src,'r') as zin:
        original={i.filename:zin.read(i.filename) for i in zin.infolist()}; f=etree.fromstring(original['word/footnotes.xml'])
        rows=[]
        for fid,stale in STALE.items():
            hits=f.xpath(f'./w:footnote[@w:id="{fid}"]',namespaces=NS)
            if len(hits)!=1: raise RuntimeError(f'FN{fid} multiplicity={len(hits)}')
            fn=hits[0]; before=sig(fn); full=text(fn)
            if stale in full:
                candidate=(' '+stale) if (' '+stale) in full else stale
                status=replace_span(fn,candidate,'')
            else: status='ALREADY_SATISFIED'
            if stale in text(fn): raise RuntimeError(f'FN{fid} stale tail remains')
            if sig(fn)!=before: raise RuntimeError(f'FN{fid} structure changed during text cleanup')
            rows.append(('F4-112',f'FN{fid}',status))
        repl=etree.tostring(f,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,repl if info.filename=='word/footnotes.xml' else original[info.filename])
    validate(src,out)
    return rows

if __name__=='__main__':
    for r in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,r)))
