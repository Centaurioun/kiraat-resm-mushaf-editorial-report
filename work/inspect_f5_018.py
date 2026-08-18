#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import hashlib, shutil, sys

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}
EXPECTED='554f4b806c66681e55fcba093764d25bca9e9926ea0f296e7f0b027391b45437'
TARGET='Yazılı vahiy metinlerinin Hz. Peygamber döneminde bir araya getirilmemiş olmasının, vahyin o dönemde yazıya geçirilmediği anlamına gelmediğini, bilakis yazılan metinlerin dağınık hâlde bulunduğuna ve bir araya toplanmadığına delalet ettiğini özellikle vurgulamamız gerekmektedir.'

def sha256(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def text(el): return ''.join(el.xpath('.//w:t/text()',namespaces=NS))

def main(src,out):
    got=sha256(src)
    if got!=EXPECTED: raise RuntimeError(f'input sha mismatch {got}')
    with ZipFile(src) as z:
        if z.testzip() is not None: raise RuntimeError('zip integrity')
        d=etree.fromstring(z.read('word/document.xml'))
        ps=d.xpath('.//w:body/w:p',namespaces=NS)
        if len(ps)!=674: raise RuntimeError(f'body count {len(ps)}')
        hits=[i for i,p in enumerate(ps) if TARGET in text(p)]
        print(f'SHA256={got}')
        print(f'BODY_PARAGRAPHS={len(ps)}')
        print('TARGET_HITS='+repr(hits))
        for i in range(52,56):
            p=ps[i]
            print(f'P{i}\tFN={p.xpath(".//w:footnoteReference/@w:id",namespaces=NS)}\t{text(p)}')
        p=ps[54]
        print('P54_SEQUENCE_BEGIN')
        for j,n in enumerate(p.xpath('.//*[self::w:t or self::w:footnoteReference]',namespaces=NS)):
            if n.tag==f'{{{W}}}t': print(f'{j:02d}\tTEXT\t{n.text or ""}')
            else: print(f'{j:02d}\tFN\t{n.get(f"{{{W}}}id")}')
        print('P54_SEQUENCE_END')
        fnroot=etree.fromstring(z.read('word/footnotes.xml'))
        fn=fnroot.xpath('//w:footnote[@w:id="27"]',namespaces=NS)
        if len(fn)!=1: raise RuntimeError('FN27 count')
        print('FN27\t'+text(fn[0]))
    shutil.copyfile(src,out)
    if sha256(out)!=got: raise RuntimeError('inspection copy not byte-identical')
    print('BYTE_IDENTICAL_COPY=PASS')

if __name__=='__main__':
    if len(sys.argv)!=3: raise SystemExit('usage: inspect_f5_018.py INPUT OUTPUT')
    main(Path(sys.argv[1]),Path(sys.argv[2]))
