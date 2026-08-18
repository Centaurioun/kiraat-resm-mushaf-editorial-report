#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import hashlib, shutil, sys

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}
EXPECTED_INPUT_SHA='c99826db06c605f5950e682c82af6d5c6f481d0c43a3364d029daadabe51fc19'
LOCKED='Böylece ana problemden uzaklaştıracak ayrıntılar sınırlandırılırken kitabın dört bölümünü birbirine bağlayan tarihsel ve kavramsal hat korunmuştur.'

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
    if sha256(path)!=EXPECTED_INPUT_SHA: raise RuntimeError('input sha mismatch '+sha256(path))
    with ZipFile(path) as z:
        if z.testzip() is not None: raise RuntimeError('zip integrity')
        d=etree.fromstring(z.read('word/document.xml'))
        ps=d.xpath('.//w:body/w:p',namespaces=NS)
        if len(ps)!=674: raise RuntimeError('body count')
        if text(ps[15]).strip()!='Giriş': raise RuntimeError('Giriş boundary mismatch at P15: '+repr(text(ps[15])))
        if text(ps[38]).strip()!='BİRİNCİ BÖLÜM': raise RuntimeError('First Chapter boundary mismatch at P38: '+repr(text(ps[38])))
        intro=[(i,text(ps[i])) for i in range(16,38) if text(ps[i]).strip()]
        locked_hits=[(i,t) for i,t in intro if LOCKED in t]
        boylece_hits=[(i,t) for i,t in intro if 'Böylece' in t or 'böylece' in t]
        if locked_hits or boylece_hits:
            raise RuntimeError('F5-013 current Introduction target remains; locked_hits='+repr(locked_hits)+'; boylece_hits='+repr(boylece_hits))
        # Current Fourth-resolved scope paragraph must remain present.
        p28=text(ps[28])
        if 'Bu çalışma, Kur’an tarihinin bütün meselelerini ele almak yerine resm-i Osmânî ile kırâat rivâyeti arasındaki ilişkiye odaklanmaktadır.' not in p28:
            raise RuntimeError('Fourth-resolved P28 scope anchor missing')
        ia=instrs(z)
        if len(ia)!=520: raise RuntimeError('fields')
        if (sum('ADDIN ' in x for x in ia),sum('ZOTERO_ITEM' in x for x in ia),sum('ZOTERO_BIBL' in x for x in ia))!=(466,465,1): raise RuntimeError('zotero')
        refs=d.xpath('//w:footnoteReference/@w:id',namespaces=NS)
        if len(refs)!=469 or len(set(refs))!=469: raise RuntimeError('footnotes')
        if len(d.xpath('//w:bookmarkStart',namespaces=NS))!=53 or len(d.xpath('//w:bookmarkEnd',namespaces=NS))!=53 or len(d.xpath('//w:hyperlink',namespaces=NS))!=52: raise RuntimeError('bookmarks/hyperlinks')
        return intro

def apply(src,out):
    intro=inspect(src)
    shutil.copyfile(src,out)
    if src.read_bytes()!=out.read_bytes(): raise RuntimeError('no-op byte identity failure')
    inspect(out)
    print('F5-013\tVERIFIED_NO_CHANGE\tGIRIS_BOYLECE_MINI_SUMMARIES_ABSENT')
    print('GIRIS_BOUNDARY\tP15=Giriş; inspected P16-P37; P38=BİRİNCİ BÖLÜM')
    print('P28_SCOPE_ANCHOR\tPRESERVED')
    print('PACKAGE_AND_RTL\tBYTE_IDENTICAL')

if __name__=='__main__':
    if len(sys.argv)!=3: raise SystemExit('usage: apply_f5_013.py INPUT.docx OUTPUT.docx')
    apply(Path(sys.argv[1]),Path(sys.argv[2]))
