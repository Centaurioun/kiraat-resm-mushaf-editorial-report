#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import hashlib, shutil, sys, re
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}
EXPECTED='ffd4c4e8fabd7bd157cd21251f18da065e5466ecce357b63efe80361a18e4543'
PHRASES=['Sonuç olarak','Netice itibarıyla','Hülasa','Bütün bu veriler','Bütün bunlar birlikte düşünüldüğünde','Bu bağlamda','Bu çerçevede','göstermektedir','ortaya koymaktadır','açıkça ortaya koymaktadır','anlaşılmaktadır','Nitekim','Dolayısıyla','Böylece','Bu noktada','Bu yönüyle','Bununla birlikte','Diğer bir ifadeyle','Başka bir ifadeyle','dikkat çekici','önemlidir','önem arz etmektedir','Vurgulamak gerekir','vurgulamak gerekir','Bu durum','Bu yaklaşım','Bu süreç']
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def txt(e): return ''.join(e.xpath('.//w:t/text()',namespaces=NS))
def quoted_ranges(s):
    out=[]
    for op,cl in [('“','”'),('"','"'),('‘','’')]:
        if op==cl:
            pts=[m.start() for m in re.finditer(re.escape(op),s)]
            for a,b in zip(pts[0::2],pts[1::2]): out.append((a,b+1))
        else:
            pos=0
            while True:
                a=s.find(op,pos)
                if a<0: break
                b=s.find(cl,a+1)
                if b<0: break
                out.append((a,b+1)); pos=b+1
    return out
def inside(ranges,a,b): return any(a>=x and b<=y for x,y in ranges)
if len(sys.argv)!=3: raise SystemExit('usage: audit_f5_global_patterns.py INPUT OUTPUT')
src=Path(sys.argv[1]); out=Path(sys.argv[2]); got=sha(src)
if got!=EXPECTED: raise RuntimeError(f'input sha mismatch {got}')
with ZipFile(src) as z:
    d=etree.fromstring(z.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
    if len(ps)!=674: raise RuntimeError(len(ps))
    for phrase in PHRASES:
        hits=[]
        for i,p in enumerate(ps):
            s=txt(p); start=0
            while True:
                j=s.find(phrase,start)
                if j<0: break
                hits.append((i,inside(quoted_ranges(s),j,j+len(phrase)),s)); start=j+len(phrase)
        print(f'PHRASE\t{phrase}\tCOUNT={len(hits)}')
        for i,q,s in hits: print(f'HIT\tP{i}\tQUOTED={q}\t{s}')
    # all author negatives outside obvious quoted spans
    for needle in [' değildir',' değil','değildir','değil']:
        hits=[]
        for i,p in enumerate(ps):
            s=txt(p); ranges=quoted_ranges(s); start=0
            while True:
                j=s.find(needle,start)
                if j<0: break
                if not inside(ranges,j,j+len(needle)): hits.append((i,s))
                start=j+len(needle)
        print(f'NEGATIVE\t{needle}\tCOUNT={len(hits)}')
        for i,s in hits: print(f'NEG_HIT\tP{i}\t{s}')
shutil.copyfile(src,out)
if sha(out)!=got: raise RuntimeError('copy mismatch')
print('BYTE_IDENTICAL_COPY=PASS')
