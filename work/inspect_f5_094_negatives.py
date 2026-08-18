#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import hashlib, shutil, sys, re
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}
EXPECTED='81f97403c0cfcf151260ab7018077145ba260c4fe4f30ca5fe2d3b501d093571'
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def txt(e): return ''.join(e.xpath('.//w:t/text()',namespaces=NS))
def ranges(s):
    out=[]; pos=0
    while True:
        a=s.find('“',pos)
        if a<0: break
        b=s.find('”',a+1)
        if b<0: break
        out.append((a,b+1)); pos=b+1
    pts=[m.start() for m in re.finditer('"',s)]
    for a,b in zip(pts[0::2],pts[1::2]): out.append((a,b+1))
    return out
def outside(s,needle):
    qs=ranges(s); st=0
    while True:
        j=s.find(needle,st)
        if j<0: return False
        if not any(j>=a and j+len(needle)<=b for a,b in qs): return True
        st=j+len(needle)
if len(sys.argv)!=3: raise SystemExit('usage: inspect_f5_094_negatives.py INPUT OUTPUT')
src=Path(sys.argv[1]); out=Path(sys.argv[2]); got=sha(src)
if got!=EXPECTED: raise RuntimeError(got)
with ZipFile(src) as z:
    d=etree.fromstring(z.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
    if len(ps)!=674: raise RuntimeError(len(ps))
    for i,p in enumerate(ps[:457]):
        s=txt(p)
        if outside(s,'değil'):
            print(f'P{i}\tFN={p.xpath(".//w:footnoteReference/@w:id",namespaces=NS)}\t{s}')
shutil.copyfile(src,out)
if sha(out)!=got: raise RuntimeError('copy mismatch')
print('BYTE_IDENTICAL_COPY=PASS')
