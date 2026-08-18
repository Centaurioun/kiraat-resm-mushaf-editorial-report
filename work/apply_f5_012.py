#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import hashlib, shutil, sys

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}
EXPECTED_INPUT_SHA='c99826db06c605f5950e682c82af6d5c6f481d0c43a3364d029daadabe51fc19'
LOCKED_OLD='Kitabın literatüre sağlamayı hedeflediği katkı, resm ilmi ile kırâat ilmini bütünüyle yeni kavramlarla açıklamak değil, çoğu zaman ayrı başlıklar altında incelenen meseleleri ortak bir problem etrafında buluşturmaktır.'
LOCKED_NEW='Kitabın literatüre hedeflediği katkı, çoğu zaman ayrı başlıklar altında incelenen resm ve kırâat meselelerini ortak bir problem etrafında birlikte değerlendirmektir.'
PROTECTED_F4_110='Kitabın ilmî katkısı, resm ve kırâat alanlarına yeni bir kaynak veya sahihlik ölçüsü eklemekten ziyade, tarihsel oluşumdan çağdaş mushaf neşrine kadar uzanan farklı meseleleri aynı ilişki içinde değerlendirmesidir.'

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
        d=etree.fromstring(z.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        if len(ps)!=674: raise RuntimeError('body count')
        if text(ps[15])!='Giriş': raise RuntimeError('Giriş boundary mismatch at P15')
        intro='\n'.join(text(ps[i]) for i in range(16,35))
        if LOCKED_OLD in intro: raise RuntimeError('locked F5-012 negative target still present in Giriş')
        if LOCKED_NEW in intro: raise RuntimeError('locked F5-012 replacement unexpectedly present; no-op adjudication requires absence')
        if any(LOCKED_OLD in text(p) for p in ps): raise RuntimeError('locked F5-012 target unexpectedly present elsewhere')
        if PROTECTED_F4_110 not in text(ps[454]): raise RuntimeError('protected F4-110 conclusion mismatch at P454')
        ins=instrs(z)
        if len(ins)!=520: raise RuntimeError('field count')
        if (sum('ADDIN ' in x for x in ins),sum('ZOTERO_ITEM' in x for x in ins),sum('ZOTERO_BIBL' in x for x in ins))!=(466,465,1): raise RuntimeError('zotero/ADDIN inventory')
        refs=d.xpath('//w:footnoteReference/@w:id',namespaces=NS)
        if len(refs)!=469 or len(set(refs))!=469: raise RuntimeError('footnote references')
        if len(d.xpath('//w:bookmarkStart',namespaces=NS))!=53 or len(d.xpath('//w:bookmarkEnd',namespaces=NS))!=53: raise RuntimeError('bookmarks')
        if len(d.xpath('//w:hyperlink',namespaces=NS))!=52: raise RuntimeError('hyperlinks')
        if len(d.xpath('//w:rtl',namespaces=NS))!=365: raise RuntimeError('rtl inventory')

def apply(src,out):
    inspect(src)
    shutil.copyfile(src,out)
    if src.read_bytes()!=out.read_bytes(): raise RuntimeError('no-op byte identity failure')
    inspect(out)
    print('F5-012\tVERIFIED_NO_CHANGE\tGIRIS_TARGET_ABSENT')
    print('GIRIS_BOUNDARY\tP15=Giriş; inspected P16-P34')
    print('PROTECTED_F4_110\tP454_UNCHANGED')

if __name__=='__main__':
    if len(sys.argv)!=3: raise SystemExit('usage: apply_f5_012.py INPUT.docx OUTPUT.docx')
    apply(Path(sys.argv[1]),Path(sys.argv[2]))
