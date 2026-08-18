#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import hashlib, shutil, sys

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}
EXPECTED_INPUT_SHA='c99826db06c605f5950e682c82af6d5c6f481d0c43a3364d029daadabe51fc19'
LOCKED_1="Bütün bu veriler bir arada değerlendirildiğinde İslâm öncesi Arap toplumunda yazının hiç bilinmediğini söylemek mümkün değildir."
LOCKED_2="Ancak toplumun geneline yayılmış bir konumda da olmadığı anlaşılmaktadır."
FIFTH_PROPOSAL_ANCHOR="İslâm öncesi Arap toplumunda yazı bilinen ve çeşitli ihtiyaçlarda kullanılan bir araçtı"
FOURTH_1="Bütün bu veriler birlikte değerlendirildiğinde, İslâm öncesi Arabistan'da yazının bütünüyle bilinmeyen bir araç olmadığı, ancak kullanımının toplumun tamamına yayılmış düzenli bir sistem hâline de gelmediği anlaşılmaktadır."
FOURTH_2="Yazı belirli idarî, ticarî ve kültürel çevrelerde kullanılmakta; sözlü aktarım ise toplumsal iletişim ve kültürel hafızada ağırlığını korumaktaydı."
FOURTH_3="Kur’an vahyinin inmeye başlamasıyla yazının vahyin kaydı bakımından daha düzenli bir işlev üstlendiği görülmektedir."

def sha256(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''): h.update(chunk)
    return h.hexdigest()

def text(el): return ''.join(el.xpath('.//w:t/text()',namespaces=NS))

def instrs(z):
    out=[]
    for n in z.namelist():
        if n.startswith('word/') and n.endswith('.xml'):
            try:r=etree.fromstring(z.read(n))
            except Exception:continue
            out += [''.join(x.itertext()).strip() for x in r.xpath('//w:instrText',namespaces=NS)]
    return out

def inspect(path):
    actual=sha256(path)
    if actual!=EXPECTED_INPUT_SHA: raise RuntimeError('input sha mismatch '+actual)
    with ZipFile(path) as z:
        if z.testzip() is not None: raise RuntimeError('zip integrity')
        d=etree.fromstring(z.read('word/document.xml'))
        ps=d.xpath('.//w:body/w:p',namespaces=NS)
        if len(ps)!=674: raise RuntimeError('body count')
        rows=[(i,text(p)) for i,p in enumerate(ps)]
        locked_hits=[(i,t) for i,t in rows if LOCKED_1 in t or LOCKED_2 in t]
        fifth_hits=[(i,t) for i,t in rows if FIFTH_PROPOSAL_ANCHOR in t]
        fourth_hits=[(i,t) for i,t in rows if FOURTH_1 in t and FOURTH_2 in t and FOURTH_3 in t]
        if locked_hits: raise RuntimeError('locked F5-015 negative target still present '+repr(locked_hits))
        if fifth_hits: raise RuntimeError('F5-015 proposal appears pre-applied '+repr(fifth_hits))
        if len(fourth_hits)!=1: raise RuntimeError('accepted F4-011 synthesis not uniquely present '+repr(fourth_hits))
        idx, current=fourth_hits[0]
        ia=instrs(z)
        if len(ia)!=520: raise RuntimeError('fields')
        if (sum('ADDIN ' in x for x in ia),sum('ZOTERO_ITEM' in x for x in ia),sum('ZOTERO_BIBL' in x for x in ia))!=(466,465,1): raise RuntimeError('zotero')
        refs=d.xpath('//w:footnoteReference/@w:id',namespaces=NS)
        if len(refs)!=469 or len(set(refs))!=469: raise RuntimeError('footnotes')
        if len(d.xpath('//w:bookmarkStart',namespaces=NS))!=53 or len(d.xpath('//w:bookmarkEnd',namespaces=NS))!=53 or len(d.xpath('//w:hyperlink',namespaces=NS))!=52: raise RuntimeError('bookmarks/hyperlinks')
        return idx,current

def apply(src,out):
    idx,current=inspect(src)
    shutil.copyfile(src,out)
    if src.read_bytes()!=out.read_bytes(): raise RuntimeError('no-op byte identity failure')
    idx2,current2=inspect(out)
    if (idx,current)!=(idx2,current2): raise RuntimeError('resolved target drift')
    print(f'F5-015\tVERIFIED_NO_CHANGE\tF4_011_SYNTHESIS_ALREADY_RESOLVES_TARGET\tP{idx}')
    print('LOCKED_NEGATIVE_TARGET\tABSENT')
    print('FIFTH_PROPOSAL\tNOT_PREAPPLIED')
    print('FOURTH_F4_011_SYNTHESIS\tPRESERVED')
    print('PACKAGE_AND_RTL\tBYTE_IDENTICAL')

if __name__=='__main__':
    if len(sys.argv)!=3: raise SystemExit('usage: apply_f5_015.py INPUT.docx OUTPUT.docx')
    apply(Path(sys.argv[1]),Path(sys.argv[2]))
