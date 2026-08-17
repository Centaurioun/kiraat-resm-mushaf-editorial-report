#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys
import apply_f4_053_057 as h
import apply_f4_078 as f78

NS=h.NS
OLD="Resm-i Osmânî’nin Kırâatlerin Tercîhî, Tevcîhi ve Vakıf Uygulamalarına Etkisi"
NEW="Resm-i Osmânî'nin Kırâatlerin Tercihi, Tevcîhi ve Vakıf Uygulamalarıyla İlişkisi"
BRIDGE="Bir okuyuşun kırâat alanındaki kabul statüsünü belirlemek ile kabul edilmiş rivâyetler arasında tercih yapmak, bu okuyuşları dil bakımından tevcîh etmek veya vakıf uygulamalarını açıklamak aynı işlem değildir. Resm verisinin bu ikinci gruptaki kullanımları bir sonraki başlıkta ayrı olarak ele alınacaktır."
OPENING="Osmânî mushafların resmi, kırâat ilminde zamanla yalnız metni muhafaza eden bir yazı zemini olarak kalmamış;"

def complete(path):
    with ZipFile(path) as z:
        d=etree.fromstring(z.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        hh=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p))==h.norm(NEW)]
        if len(hh)!=1: return False
        i,p=hh[0]; s=h.spec(p)
        if s['book']!=2 or s['fn'] or s['rtl'] or s['fld'] or s['hyper']: return False
        if i==0 or h.norm(h.txt(ps[i-1]))!=h.norm(BRIDGE): return False
        if i+1>=len(ps) or not h.norm(h.txt(ps[i+1])).startswith(h.norm(OPENING)): return False
        return True

def apply(src:Path,out:Path):
    if complete(src):
        f78.validate_structural(src,src); shutil.copyfile(src,out); return [('F4-094','current','ALREADY_SATISFIED')]
    with ZipFile(src,'r') as zin:
        d=etree.fromstring(zin.read('word/document.xml')); body=d.find('.//w:body',namespaces=NS); ps=body.xpath('./w:p',namespaces=NS)
        i,p=h.find(ps,OLD)
        before=h.spec(p)
        if before['book']!=2 or before['fn'] or before['rtl'] or before['fld'] or before['hyper']:
            raise RuntimeError('unexpected protected F4-094 heading '+str(before))
        if i==0 or h.norm(h.txt(ps[i-1]))!=h.norm(BRIDGE): raise RuntimeError('F4-094 preceding bridge mismatch')
        if i+1>=len(ps) or not h.norm(h.txt(ps[i+1])).startswith(h.norm(OPENING)): raise RuntimeError('F4-094 opening boundary mismatch')
        st=h.span(p,OLD,NEW)
        if h.spec(p)!=before: raise RuntimeError('F4-094 heading structure changed')
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
    f78.validate_structural(src,out)
    if not complete(out): raise RuntimeError('F4-094 postconditions incomplete')
    return [('F4-094',f'P{i}',st)]

if __name__=='__main__':
    for row in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,row)))
