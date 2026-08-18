#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import hashlib, shutil, sys

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}
EXPECTED='cc3d906b77ae5325b6bcb9b5e458b1af30ef37191c5ee956455613161bd693da'

def sha256(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def all_text(el): return ''.join(el.xpath('.//w:t/text()',namespaces=NS))

def main(src,out):
    got=sha256(src)
    if got!=EXPECTED: raise RuntimeError(f'input sha mismatch {got}')
    with ZipFile(src) as z:
        if z.testzip() is not None: raise RuntimeError('zip integrity')
        d=etree.fromstring(z.read('word/document.xml'))
        ps=d.xpath('.//w:body/w:p',namespaces=NS)
        if len(ps)!=674: raise RuntimeError(f'body count {len(ps)}')
        p=ps[53]
        print(f'SHA256={got}')
        print('P53_TEXT='+all_text(p))
        print('P53_FNS='+repr(p.xpath('.//w:footnoteReference/@w:id',namespaces=NS)))
        fnroot=etree.fromstring(z.read('word/footnotes.xml'))
        for fid in ('24','25','26'):
            hits=fnroot.xpath(f'//w:footnote[@w:id="{fid}"]',namespaces=NS)
            if len(hits)!=1: raise RuntimeError(f'FN{fid} count {len(hits)}')
            print(f'FN{fid}\t{all_text(hits[0])}')
    shutil.copyfile(src,out)
    if sha256(out)!=got: raise RuntimeError('inspection copy not byte-identical')
    print('BYTE_IDENTICAL_COPY=PASS')

if __name__=='__main__':
    if len(sys.argv)!=3: raise SystemExit('usage: inspect_f5_017.py INPUT OUTPUT')
    main(Path(sys.argv[1]),Path(sys.argv[2]))
