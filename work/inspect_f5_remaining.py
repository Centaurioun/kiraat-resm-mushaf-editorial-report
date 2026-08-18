#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import hashlib, shutil, sys, re
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}
EXPECTED='ffd4c4e8fabd7bd157cd21251f18da065e5466ecce357b63efe80361a18e4543'
PHRASES=['Sonuç olarak','Netice itibarıyla','Hülasa','Bütün bu veriler','Bütün bunlar birlikte düşünüldüğünde','Bu bağlamda','Bu çerçevede','göstermektedir','ortaya koymaktadır','açıkça ortaya koymaktadır','anlaşılmaktadır','Nitekim','Dolayısıyla','Böylece','Bu noktada','Bu yönüyle','Bununla birlikte','Diğer bir ifadeyle','Başka bir ifadeyle','dikkat çekici','önemlidir','önem arz etmektedir','Vurgulamak gerekir','vurgulamak gerekir','Bu durum','Bu yaklaşım','Bu süreç']
def sha256(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def txt(el): return ''.join(el.xpath('.//w:t/text()',namespaces=NS))
def main(src,out):
    got=sha256(src)
    if got!=EXPECTED: raise RuntimeError(f'input sha mismatch {got}')
    with ZipFile(src) as z:
        if z.testzip() is not None: raise RuntimeError('zip integrity')
        d=etree.fromstring(z.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        if len(ps)!=674: raise RuntimeError(len(ps))
        print('SHA256='+got); print('BODY_PARAGRAPHS='+str(len(ps)))
        print('PARAGRAPHS_BEGIN')
        for i,p in enumerate(ps):
            t=txt(p).replace('\t',' '); fns=p.xpath('.//w:footnoteReference/@w:id',namespaces=NS); books=p.xpath('.//w:bookmarkStart/@w:name',namespaces=NS)
            if i>=56:
                print(f'P{i}\tFN={fns}\tBOOK={books}\t{t}')
        print('PARAGRAPHS_END')
        print('PHRASE_OCCURRENCES_BEGIN')
        for phrase in PHRASES:
            hits=[]
            for i,p in enumerate(ps):
                t=txt(p)
                if phrase in t: hits.append((i,t))
            print(f'PHRASE\t{phrase}\tCOUNT={len(hits)}')
            for i,t in hits: print(f'HIT\tP{i}\t{t}')
        print('PHRASE_OCCURRENCES_END')
        # direct quoted segments containing değil/değildir; purely diagnostic
        print('QUOTED_NEGATIVES_BEGIN')
        qre=re.compile(r'[“\"]([^”\"]*(?:değil|değildir)[^”\"]*)[”\"]')
        for i,p in enumerate(ps):
            t=txt(p)
            for m in qre.finditer(t): print(f'P{i}\t{m.group(0)}')
        print('QUOTED_NEGATIVES_END')
    shutil.copyfile(src,out)
    if sha256(out)!=got: raise RuntimeError('copy mismatch')
    print('BYTE_IDENTICAL_COPY=PASS')
if __name__=='__main__':
    if len(sys.argv)!=3: raise SystemExit('usage: inspect_f5_remaining.py INPUT OUTPUT')
    main(Path(sys.argv[1]),Path(sys.argv[2]))
