#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys
import apply_f4_053_057 as h
import apply_f4_078 as f78

NS=h.NS
HEADING="DÖRDÜNCÜ BÖLÜM"
NEW="Resm-i Osmânî'ye bağlılığın tarihsel ve normatif gerekçeleri bu şekilde ayrıştırıldıktan sonra, resmin kırâat ilmindeki somut kullanım alanlarına dönmek gerekir. Dördüncü bölüm, resmin kırâat rivâyetlerinin tespiti ve tahdidi, sahâbe mushafları, şâz okuyuşlar, tercih, tevcîh ve sonraki mushaf neşriyle ilişkisini bu açıdan ele almaktadır."

def complete(path):
    with ZipFile(path) as z:
        d=etree.fromstring(z.read('word/document.xml'))
        ps=d.xpath('.//w:body/w:p',namespaces=NS)
        hits=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p))==h.norm(NEW)]
        heads=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p))==h.norm(HEADING)]
    return len(hits)==1 and len(heads)==1 and hits[0][0] < heads[0][0] and heads[0][0]-hits[0][0] <= 3 and h.spec(hits[0][1])=={'fn':[],'instr':[],'fld':0,'hyper':0,'rtl':0,'book':0}

def apply(src:Path,out:Path):
    if complete(src):
        f78.validate_structural(src,src)
        shutil.copyfile(src,out)
        return [('F4-082','current','ALREADY_SATISFIED')]
    with ZipFile(src,'r') as zin:
        d=etree.fromstring(zin.read('word/document.xml'))
        body=d.find('.//w:body',namespaces=NS)
        ps=body.xpath('./w:p',namespaces=NS)
        hi,hp=h.find(ps,HEADING)
        hspec=h.spec(hp)
        if hspec['book'] < 2:
            raise RuntimeError('Fourth Section heading bookmark structure missing: '+str(hspec))
        target=None
        for i in range(hi-1,max(-1,hi-5),-1):
            p=ps[i]
            if h.norm(h.txt(p)):
                continue
            if h.spec(p)=={'fn':[],'instr':[],'fld':0,'hyper':0,'rtl':0,'book':0}:
                target=p
                break
        if target is None:
            raise RuntimeError('no safe empty paragraph immediately before Fourth Section')
        h.whole(target,NEW,())
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist():
                zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
    f78.validate_structural(src,out)
    if not complete(out):
        raise RuntimeError('F4-082 postconditions incomplete')
    return [('F4-082','current','APPLIED_THIRD_TO_FOURTH_TRANSITION_IN_EXISTING_EMPTY_PARAGRAPH')]

if __name__=='__main__':
    for row in apply(Path(sys.argv[1]),Path(sys.argv[2])):
        print('\t'.join(map(str,row)))
