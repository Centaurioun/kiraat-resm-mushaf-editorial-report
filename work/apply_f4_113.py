#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil, sys, re

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}

AUTHOR_REPL={
    'ed-Dânî':'Dânî',
    'ez-Zürkânî':'Zürkânî',
    'es-Suyûtî':'Suyûtî',
}

# F4-113 uses an articleless house style for sura names in footnote verse references.
# Match only a known sura name immediately followed by its correct sura number / verse,
# so bibliographic work titles such as el-İtkân 4/… and el-Mukni’ 1/… cannot match.
SURA_NUMBERS={
    'Cum’â':62,
    'İsrâ':17,
    'Şûrâ':42,
    'Kamer':54,
    'Alak':96,
    'Zâriyât':51,
    'Bakara':2,
    'Mâide':5,
    'Mümtehine':60,
    'Nûr':24,
    'Şuarâ’':26,
    'Mutaffifîn':83,
    'Zuhruf':43,
    'Kehf':18,
    'Kasas':28,
    'Mü’min':40,
}
ARTICLE_FORMS=('el','er','es','ez','et','ed','en','eş')
SURA_RE=re.compile(
    r'(?<![\w’ʼʿʻ-])(?P<article>'+ '|'.join(ARTICLE_FORMS) + r')-'
    r'(?P<name>' + '|'.join(sorted((re.escape(x) for x in SURA_NUMBERS), key=len, reverse=True)) + r')'
    r'(?P<gap>\s+)(?P<chapter>\d{1,3})/(?P<verse>\d{1,3}(?:[-–]\d{1,3})?)'
)

def text(el): return ''.join(el.xpath('.//w:t/text()',namespaces=NS))
def sig(el): return tuple((n.tag,tuple(sorted(n.attrib.items()))) for n in el.iter())
def c14n(el): return etree.tostring(el,method='c14n')

def replace_range(el,start,end,new):
    nodes=el.xpath('.//w:t',namespaces=NS); vals=[n.text or '' for n in nodes]
    if start<0 or end<start or end>sum(map(len,vals)): raise RuntimeError('invalid replacement span')
    if start==end: raise RuntimeError('zero-length replacement span unsupported')
    starts=[]; cur=0
    for v in vals: starts.append(cur); cur+=len(v)
    fi=next(i for i,(st,v) in enumerate(zip(starts,vals)) if start < st+len(v))
    li=next(i for i,(st,v) in enumerate(zip(starts,vals)) if end <= st+len(v))
    prefix=vals[fi][:start-starts[fi]]; suffix=vals[li][end-starts[li]:]
    nodes[fi].text=prefix+new+(suffix if fi==li else '')
    if fi!=li:
        for j in range(fi+1,li): nodes[j].text=''
        nodes[li].text=suffix

def normalized_string(s):
    out=s
    for old,new in AUTHOR_REPL.items(): out=out.replace(old,new)
    # Context-sensitive sura normalization. Validate sura name against chapter number.
    pos=0
    while True:
        m=SURA_RE.search(out,pos)
        if not m: break
        name=m.group('name'); chapter=int(m.group('chapter'))
        if SURA_NUMBERS[name]==chapter:
            out=out[:m.start('article')] + out[m.end('article')+1:]
            pos=max(0,m.start('article')+len(name))
        else:
            pos=m.end()
    return out

def apply_normalization(fn):
    rows=[]
    # Literal author-name variants.
    for old,new in AUTHOR_REPL.items():
        count=0
        while True:
            full=text(fn); p=full.find(old)
            if p<0: break
            replace_range(fn,p,p+len(old),new); count+=1
        if count: rows.append(('AUTHOR',old,new,count))
    # Sura articles, only when paired with the correct Qur'anic chapter number.
    count=0
    while True:
        full=text(fn); m=SURA_RE.search(full)
        if not m: break
        name=m.group('name'); chapter=int(m.group('chapter'))
        if SURA_NUMBERS[name]!=chapter:
            # Keep a non-Qur'anic or mismatched numeric context untouched and continue.
            tail_start=m.end(); rest=SURA_RE.search(full,tail_start)
            if not rest: break
            # The current inventory contains no mismatched known-sura hits; fail closed if one appears.
            raise RuntimeError(f'ambiguous/mismatched sura numeric context in FN: {m.group(0)!r}')
        old=m.group('article')+'-';
        replace_range(fn,m.start('article'),m.end('article')+1,''); count+=1
    if count: rows.append(('SURA','articleless','verified-name+chapter',count))
    return rows

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
        idset=set(ids_b); missing=[x for x in refs_b if x not in idset]
        if missing: raise RuntimeError(f'body references missing from footnotes.xml: {missing[:10]}')
        changed=[]
        for fid in ids_a:
            aa=fa.xpath(f'./w:footnote[@w:id="{fid}"]',namespaces=NS); bb=fb.xpath(f'./w:footnote[@w:id="{fid}"]',namespaces=NS)
            if len(aa)!=1 or len(bb)!=1: raise RuntimeError(f'footnote {fid} multiplicity changed')
            before=text(aa[0]); after=text(bb[0]); expected=normalized_string(before)
            if after!=expected: raise RuntimeError(f'FN{fid} text differs from sanctioned F4-113 normalization')
            if sig(aa[0])!=sig(bb[0]): raise RuntimeError(f'FN{fid} structural drift')
            if before==expected:
                if c14n(aa[0])!=c14n(bb[0]): raise RuntimeError(f'non-target FN{fid} changed')
            else: changed.append(fid)
        # document.xml is byte-identical above; explicitly protect structural inventories too.
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
        return changed

def complete(path):
    with ZipFile(path) as z:
        f=etree.fromstring(z.read('word/footnotes.xml'))
        return all(normalized_string(text(fn))==text(fn) for fn in f.xpath('./w:footnote',namespaces=NS))

def body_map(src,ids):
    ids=set(str(x) for x in ids); found={x:[] for x in ids}
    with ZipFile(src) as z:
        d=etree.fromstring(z.read('word/document.xml'))
        paras=d.xpath('.//w:body/w:p',namespaces=NS)
        for i,p in enumerate(paras):
            for fid in p.xpath('.//w:footnoteReference/@w:id',namespaces=NS):
                if fid in found: found[fid].append(i)
    return found

def apply(src,out):
    if complete(src):
        validate(src,src); shutil.copyfile(src,out)
        return [('F4-113','ALL_TARGETS','ALREADY_SATISFIED')]
    with ZipFile(src,'r') as zin:
        original={i.filename:zin.read(i.filename) for i in zin.infolist()}; f=etree.fromstring(original['word/footnotes.xml'])
        rows=[]; touched=[]; author_count=0; sura_count=0
        for fn in f.xpath('./w:footnote',namespaces=NS):
            fid=fn.get('{'+W+'}id'); before=text(fn); before_sig=sig(fn)
            ops=apply_normalization(fn); after=text(fn)
            if sig(fn)!=before_sig: raise RuntimeError(f'FN{fid} structure changed during normalization')
            if before!=after:
                touched.append(fid)
                for kind,a,b,count in ops:
                    if kind=='AUTHOR': author_count+=count
                    elif kind=='SURA': sura_count+=count
                rows.append(('F4-113',f'FN{fid}',before,'=>',after))
        repl=etree.tostring(f,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,repl if info.filename=='word/footnotes.xml' else original[info.filename])
    changed=validate(src,out)
    if set(changed)!=set(touched): raise RuntimeError(f'changed-footnote mismatch validator={changed} apply={touched}')
    bm=body_map(src,touched)
    rows.insert(0,('APPLIED_MAIN_FOOTNOTE_HOUSE_STYLE',f'AUTHOR={author_count}',f'SURA={sura_count}',f'FN={len(touched)}'))
    rows.append(('CHANGED_FN_IDS',','.join(touched)))
    rows.append(('BODY_PARAGRAPH_MAP',','.join(f'FN{k}:P{"/P".join(map(str,v))}' for k,v in sorted(bm.items(),key=lambda kv:int(kv[0])))))
    return rows

if __name__=='__main__':
    for r in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,r)))
