#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys
import apply_f4_053_057 as h
import apply_f4_078 as f78

NS=h.NS
OLD="Resm-i Osmânî’nin kırâat ilmindeki tesiri, yalnız kırâat vecihlerinin kabulü ve tercihiyle sınırlı kalmamış; vakıf uygulamalarına ve edâ tercihlerine kadar uzanan daha geniş bir alanda da belirginleşmiştir. Nitekim kırâat geleneğinde vakıf, ilk bakışta sadece ses icrasıyla ilgili bir mesele gibi görünse de, gerçekte mushaf hattıyla doğrudan irtibatlandırılmıştır. Çünkü kelimenin son harfinin nasıl değerlendirileceği, hazif ve isbatın nasıl uygulanacağı, ayrıca iki kelimenin bitişik yahut ayrı yazılmış olmasının vakfa nasıl yansıyacağı gibi hususlar, çoğu zaman mushaf resmine göre tayin edilmiştir. Bu sebeple resm-i Mushaf, okuyuşun fiilî icrasına yön veren bağlayıcı bir ölçü olarak karşımıza çıkmaktadır."
NEW="Vakıf ve ibtidâda mana, nahiv ve rivâyet temel ölçüler arasında yer alır. Mushaf yazımı ise özellikle vasl-fasl ve kelime sınırlarının yazıda nasıl gösterildiği gibi bazı durumlarda değerlendirmeye katkı sağlayabilir. Bu nedenle resm, bütün vakıf uygulamalarını doğrudan belirleyen tek ölçü olarak değil, belirli örneklerde başvurulan yazılı verilerden biri olarak ele alınmalıdır."
PREV="İbn Hâleveyh’in, (ö. 370/980) bir lafzın bazı yerlerde ittifakla, başka yerlerde ise ihtilafla okunmasını mushaftaki yazım biçimine bağlaması"
NEXT="Dânî’nin, Nâfiʿ, Ebû Amr (ö. 154/771) ve Kûfeli imamların vakıfta mushaf resmine göre durduklarını nakletmesi"

def complete(path):
    with ZipFile(path) as z:
        d=etree.fromstring(z.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        hits=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p))==h.norm(NEW)]
        if len(hits)!=1:return False
        i,p=hits[0]; s=h.spec(p)
        return (not s['fn'] and not s['rtl'] and not s['fld'] and not s['book'] and not s['hyper']
                and i>0 and h.norm(h.txt(ps[i-1])).startswith(h.norm(PREV))
                and i+1<len(ps) and h.norm(h.txt(ps[i+1])).startswith(h.norm(NEXT))
                and h.spec(ps[i+1])['fn']==['413'])

def apply(src:Path,out:Path):
    if complete(src):
        f78.validate_structural(src,src); shutil.copyfile(src,out); return [('F4-096','current','ALREADY_SATISFIED')]
    with ZipFile(src,'r') as zin:
        d=etree.fromstring(zin.read('word/document.xml')); body=d.find('.//w:body',namespaces=NS); ps=body.xpath('./w:p',namespaces=NS)
        i,p=h.find(ps,OLD)
        s=h.spec(p)
        if s['fn'] or s['rtl'] or s['fld'] or s['book'] or s['hyper']: raise RuntimeError('unexpected protected F4-096 target '+str(s))
        if i==0 or not h.norm(h.txt(ps[i-1])).startswith(h.norm(PREV)): raise RuntimeError('F4-096 previous boundary mismatch')
        if i+1>=len(ps) or not h.norm(h.txt(ps[i+1])).startswith(h.norm(NEXT)) or h.spec(ps[i+1])['fn']!=['413']:
            raise RuntimeError('F4-096 next boundary mismatch')
        h.whole(p,NEW,())
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
    f78.validate_structural(src,out)
    if not complete(out): raise RuntimeError('F4-096 postconditions incomplete')
    return [('F4-096',f'P{i}','APPLIED_WAQF_SCOPE_CORRECTION')]

if __name__=='__main__':
    for row in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,row)))
