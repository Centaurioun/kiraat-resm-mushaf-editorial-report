#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import hashlib, shutil, sys, re
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}
EXPECTED='869aefdec0d5fe046176e09e690d0e7d928ab53566b641fa6ace912bda31160e'
PHRASES=['Sonuç olarak','Netice itibarıyla','Hülasa','Bütün bu veriler','Bütün bunlar birlikte düşünüldüğünde','Bu bağlamda','Bu çerçevede','göstermektedir','ortaya koymaktadır','açıkça ortaya koymaktadır','anlaşılmaktadır','Nitekim','Dolayısıyla','Böylece','Bu noktada','Bu yönüyle','Bununla birlikte','Diğer bir ifadeyle','Başka bir ifadeyle','dikkat çekici','önemlidir','önem arz etmektedir','Vurgulamak gerekir','vurgulamak gerekir','Bu durum','Bu yaklaşım','Bu süreç']
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
def qflag(s,a,b): return any(a>=x and b<=y for x,y in ranges(s))
if len(sys.argv)!=3: raise SystemExit('usage: audit_f5_global_085.py INPUT OUTPUT')
src=Path(sys.argv[1]); out=Path(sys.argv[2]); got=sha(src)
if got!=EXPECTED: raise RuntimeError(got)
with ZipFile(src) as z:
    d=etree.fromstring(z.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
    if len(ps)!=674: raise RuntimeError(len(ps))
    texts=[txt(p) for p in ps]
    print('SHA='+got); print('BODY='+str(len(ps)))
    for ph in PHRASES:
        rec=[]
        for i,s in enumerate(texts[:457]):
            st=0
            while True:
                j=s.find(ph,st)
                if j<0: break
                rec.append((i,qflag(s,j,j+len(ph)))); st=j+len(ph)
        print('PHRASE\t'+ph+'\tCOUNT='+str(len(rec))+'\t'+','.join(str(i)+('Q' if q else '') for i,q in rec))
    for needle in ['değildir','değil']:
        rec=[]
        for i,s in enumerate(texts[:457]):
            st=0
            while True:
                j=s.find(needle,st)
                if j<0: break
                if not qflag(s,j,j+len(needle)): rec.append(i)
                st=j+len(needle)
        print('AUTHOR_NEGATIVE\t'+needle+'\tCOUNT='+str(len(rec))+'\t'+','.join(map(str,rec)))
    print('QUOTE_NEGATIVES')
    for i,s in enumerate(texts[:457]):
        for a,b in ranges(s):
            q=s[a:b]
            if 'değil' in q: print(f'QNEG\tP{i}\t{q}')
shutil.copyfile(src,out)
if sha(out)!=got: raise RuntimeError('copy mismatch')
print('BYTE_IDENTICAL_COPY=PASS')
