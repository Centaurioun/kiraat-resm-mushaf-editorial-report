#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import hashlib, shutil, sys

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}
EXPECTED_INPUT_SHA='c99826db06c605f5950e682c82af6d5c6f481d0c43a3364d029daadabe51fc19'
LOCKED='Bu yapı içinde araştırmanın temel sorusu, yazı ile sözlü rivâyetten hangisinin üstün olduğu değildir.'
SUGGESTED='Araştırmanın temel sorusu, rivâyet yoluyla sabit okuyuşlarla bunların ortak mushaf yazımı içindeki kabul ve aktarımı arasındaki ilişkinin nasıl kurulduğudur.'
P32_ANCHOR='rivâyetle sabit okuyuşların müşterek mushaf yazısıyla ilişkisini belirleyen tamamlayıcı bir ölçü olarak nasıl işlev gördüğünü ortaya koymaktır.'
P34_ANCHOR='Birinci bölüm bu zemini incelemektedir.'

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
    got=sha256(path)
    if got!=EXPECTED_INPUT_SHA: raise RuntimeError('input sha mismatch '+got)
    with ZipFile(path) as z:
        if z.testzip() is not None: raise RuntimeError('zip integrity')
        d=etree.fromstring(z.read('word/document.xml'))
        ps=d.xpath('.//w:body/w:p',namespaces=NS)
        if len(ps)!=674: raise RuntimeError('body count')
        if text(ps[15]).strip()!='Giriş': raise RuntimeError('Giriş boundary mismatch at P15: '+repr(text(ps[15])))
        if text(ps[38]).strip()!='BİRİNCİ BÖLÜM': raise RuntimeError('First Chapter boundary mismatch at P38: '+repr(text(ps[38])))
        intro=[(i,text(ps[i])) for i in range(16,38) if text(ps[i]).strip()]
        locked_hits=[(i,t) for i,t in intro if LOCKED in t]
        if locked_hits: raise RuntimeError('F5-014 locked target still present: '+repr(locked_hits))
        # The Fifth generic replacement must not have been silently injected before this item.
        suggested_hits=[(i,t) for i,t in intro if SUGGESTED in t]
        if suggested_hits: raise RuntimeError('F5-014 suggested text already present unexpectedly: '+repr(suggested_hits))
        p32=text(ps[32]); p33=text(ps[33]); p34=text(ps[34])
        if not p32.startswith('Araştırmanın temel amacı,') or P32_ANCHOR not in p32:
            raise RuntimeError('Fourth-approved P32 complementary-measure thesis missing: '+repr(p32))
        if not p33.startswith('Kitap dört bölümden oluşmaktadır.'):
            raise RuntimeError('P33 book-architecture anchor missing: '+repr(p33))
        if P34_ANCHOR not in p34:
            raise RuntimeError('P34 transition anchor missing: '+repr(p34))
        ia=instrs(z)
        if len(ia)!=520: raise RuntimeError('fields')
        if (sum('ADDIN ' in x for x in ia),sum('ZOTERO_ITEM' in x for x in ia),sum('ZOTERO_BIBL' in x for x in ia))!=(466,465,1): raise RuntimeError('zotero')
        refs=d.xpath('//w:footnoteReference/@w:id',namespaces=NS)
        if len(refs)!=469 or len(set(refs))!=469: raise RuntimeError('footnotes')
        if len(d.xpath('//w:bookmarkStart',namespaces=NS))!=53 or len(d.xpath('//w:bookmarkEnd',namespaces=NS))!=53 or len(d.xpath('//w:hyperlink',namespaces=NS))!=52: raise RuntimeError('bookmarks/hyperlinks')
        return p32,p33,p34

def apply(src,out):
    inspect(src)
    shutil.copyfile(src,out)
    if src.read_bytes()!=out.read_bytes(): raise RuntimeError('no-op byte identity failure')
    inspect(out)
    print('F5-014\tVERIFIED_NO_CHANGE\tNEGATIVE_SUPERIORITY_QUESTION_ABSENT')
    print('GIRIS_BOUNDARY\tP15=Giriş; inspected P16-P37; P38=BİRİNCİ BÖLÜM')
    print('P32_FOURTH_THESIS\tPRESERVED')
    print('P33_P34_CLOSING_ARCHITECTURE\tPRESERVED')
    print('PACKAGE_AND_RTL\tBYTE_IDENTICAL')

if __name__=='__main__':
    if len(sys.argv)!=3: raise SystemExit('usage: apply_f5_014.py INPUT.docx OUTPUT.docx')
    apply(Path(sys.argv[1]),Path(sys.argv[2]))
