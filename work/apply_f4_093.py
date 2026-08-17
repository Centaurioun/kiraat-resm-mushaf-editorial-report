#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys
import apply_f4_053_057 as h
import apply_f4_078 as f78

NS=h.NS
OLD="Bütün bu veriler ışığında, resm-i Osmânî’ye aykırı kırâat vecihlerinin mensuh ve şâz sayılması meselesinin, mushaf hattının kırâat ilmindeki merkezî konumunu gösterdiği anlaşılmaktadır."
NEW="Bir okuyuşun kırâat alanındaki kabul statüsünü belirlemek ile kabul edilmiş rivâyetler arasında tercih yapmak, bu okuyuşları dil bakımından tevcîh etmek veya vakıf uygulamalarını açıklamak aynı işlem değildir. Resm verisinin bu ikinci gruptaki kullanımları bir sonraki başlıkta ayrı olarak ele alınacaktır."
HEADING="Resm-i Osmânî’nin Kırâatlerin Tercîhî, Tevcîhi ve Vakıf Uygulamalarına Etkisi"

def complete(path):
    with ZipFile(path) as z:
        d=etree.fromstring(z.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        nh=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p))==h.norm(NEW)]
        hh=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p))==h.norm(HEADING)]
        return len(nh)==1 and len(hh)==1 and nh[0][0]+1==hh[0][0] and h.spec(nh[0][1])['fn']==[] and h.spec(nh[0][1])['rtl']==0 and h.spec(nh[0][1])['book']==0 and h.spec(hh[0][1])['book']==2

def apply(src:Path,out:Path):
    if complete(src):
        f78.validate_structural(src,src); shutil.copyfile(src,out); return [('F4-093','current','ALREADY_SATISFIED')]
    with ZipFile(src,'r') as zin:
        d=etree.fromstring(zin.read('word/document.xml')); body=d.find('.//w:body',namespaces=NS); ps=body.xpath('./w:p',namespaces=NS)
        i,p=h.find(ps,OLD)
        s=h.spec(p)
        if s['fn'] or s['rtl'] or s['fld'] or s['book'] or s['hyper']:
            raise RuntimeError('unexpected protected F4-093 target '+str(s))
        if i+1>=len(ps) or h.norm(h.txt(ps[i+1]))!=h.norm(HEADING) or h.spec(ps[i+1])['book']!=2:
            raise RuntimeError('F4-093 4.4 heading boundary mismatch')
        h.whole(p,NEW,())
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
    f78.validate_structural(src,out)
    if not complete(out): raise RuntimeError('F4-093 postconditions incomplete')
    return [('F4-093',f'P{i}','APPLIED_CONCEPTUAL_TRANSITION')]

if __name__=='__main__':
    for row in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,row)))
