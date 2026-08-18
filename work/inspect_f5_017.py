#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import hashlib, shutil, sys

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}
EXPECTED='cc3d906b77ae5325b6bcb9b5e458b1af30ef37191c5ee956455613161bd693da'
TARGET='Bu döneme ilişkin rivâyetler, vahyin yazıya geçirilmesi hususunda çok daha sistemli ve titiz bir uygulamanın bulunduğunu göstermektedir.'

def sha256(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def text(p): return ''.join(p.xpath('.//w:t/text()',namespaces=NS))

def main(src,out):
    got=sha256(src)
    if got!=EXPECTED: raise RuntimeError(f'input sha mismatch {got}')
    with ZipFile(src) as z:
        if z.testzip() is not None: raise RuntimeError('zip integrity')
        d=etree.fromstring(z.read('word/document.xml'))
        ps=d.xpath('.//w:body/w:p',namespaces=NS)
        if len(ps)!=674: raise RuntimeError(f'body count {len(ps)}')
        print(f'SHA256={got}')
        print(f'BODY_PARAGRAPHS={len(ps)}')
        hits=[]
        for i in range(50,56):
            t=text(ps[i])
            if TARGET in t: hits.append(i)
            fns=ps[i].xpath('.//w:footnoteReference/@w:id',namespaces=NS)
            print(f'P{i}\tFN={fns}\t{t}')
        print('TARGET_HITS='+repr(hits))
        p=ps[53]
        print('P53_SEQUENCE_BEGIN')
        for j,n in enumerate(p.xpath('.//*[self::w:t or self::w:footnoteReference]',namespaces=NS)):
            if n.tag==f'{{{W}}}t': print(f'{j:02d}\tTEXT\t{n.text or ""}')
            else: print(f'{j:02d}\tFN\t{n.get(f"{{{W}}}id")}')
        print('P53_SEQUENCE_END')
    shutil.copyfile(src,out)
    if sha256(out)!=got: raise RuntimeError('inspection copy not byte-identical')
    print('BYTE_IDENTICAL_COPY=PASS')

if __name__=='__main__':
    if len(sys.argv)!=3: raise SystemExit('usage: inspect_f5_017.py INPUT OUTPUT')
    main(Path(sys.argv[1]),Path(sys.argv[2]))
