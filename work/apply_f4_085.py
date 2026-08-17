#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys
import apply_f4_053_057 as h
import apply_f4_078 as f78

NS=h.NS
OLD="Bütün bunlar birlikte düşünüldüğünde Osmânî resmin kırâat vecihlerinin rivâyet ve naklinde üç yönlü bir rol üstlendiği söylenebilir."
NEW="Osmânî mushaflar ümmetin müşterek yazılı başvuru zemini hâline gelirken, sahâbeye nispet edilen şahsî mushaflar erken dönemdeki okuyuş, tertip ve yazım çeşitliliğine ilişkin tarihsel veriler sunmaktadır. Bu iki malzemenin işlev ve otorite düzeyi aynı değildir. Bir sonraki başlık bu farkı ele almaktadır."
HEADING="Sahâbe Mushaflarındaki Kırâat Rivâyetlerine Karşı Resm-i Osmânî’nin Konumu"

def complete(path):
    with ZipFile(path) as z:
        d=etree.fromstring(z.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        nh=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p))==h.norm(NEW)]
        hh=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p))==h.norm(HEADING)]
        return len(nh)==1 and len(hh)==1 and nh[0][0]+1==hh[0][0] and h.spec(nh[0][1])['fn']==[] and h.spec(hh[0][1])['book']==2

def apply(src:Path,out:Path):
    if complete(src):
        f78.validate_structural(src,src); shutil.copyfile(src,out); return [('F4-085','current','ALREADY_SATISFIED')]
    with ZipFile(src,'r') as zin:
        d=etree.fromstring(zin.read('word/document.xml')); body=d.find('.//w:body',namespaces=NS); ps=body.xpath('./w:p',namespaces=NS)
        i,p=h.find(ps,OLD)
        if h.spec(p)['fn'] or h.spec(p)['rtl'] or h.spec(p)['book'] or h.spec(p)['fld'] or h.spec(p)['hyper']:
            raise RuntimeError('unexpected protected F4-085 target '+str(h.spec(p)))
        if i+1>=len(ps) or h.norm(h.txt(ps[i+1]))!=h.norm(HEADING) or h.spec(ps[i+1])['book']!=2:
            raise RuntimeError('4.2 heading boundary mismatch')
        h.whole(p,NEW,())
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
    f78.validate_structural(src,out)
    if not complete(out): raise RuntimeError('F4-085 postconditions incomplete')
    return [('F4-085','current','APPLIED_NORMATIVE_STATUS_TRANSITION')]

if __name__=='__main__':
    for row in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,row)))
