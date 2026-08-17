#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys
import apply_f4_053_057 as h
import apply_f4_078 as f78
NS=h.NS
ANCHOR="Osmanlı’nın son döneminde mushaf basımı, serbest bir neşir faaliyeti olarak görülmemiş, onay ve denetim mekanizması içinde gelişmiştir."
OLD=("1889’da kurulan Teftîş-i Mesâhif-i Şerîfe Meclisinin ve devamındaki denetim yapılarının, matbu İslâmî eserlerle birlikte mushaf neşrini de kontrol altına aldığını ortaya koymaktadır. "
     "Bu, Osmanlı’nın mushaf basımında hem metin güvenliğini hem de dinî meşruiyeti korumaya çalıştığını göstermektedir.")
NEW=("1889'da kurulan Teftîş-i Mesâhif-i Şerîfe Meclisi, basılan mushafların tashih ve denetimini kurumsal bir çerçeveye bağlamıştır. "
     "Bu uygulama, Osmanlı döneminde mushaf neşrinin yalnız teknik bir baskı faaliyeti olarak görülmediğini, metnin doğruluğunu korumaya yönelik idarî denetim mekanizmalarının da oluşturulduğunu göstermektedir.")

def complete(path:Path):
    with ZipFile(path) as z:
        d=etree.fromstring(z.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        hits=[p for p in ps if h.norm(h.txt(p)).startswith(h.norm(ANCHOR))]
        return len(hits)==1 and h.norm(NEW) in h.norm(h.txt(hits[0])) and h.spec(hits[0])['fn']==['467'] and h.norm(OLD) not in h.norm(h.txt(hits[0]))

def apply(src:Path,out:Path):
    if complete(src):
        f78.validate_structural(src,src); shutil.copyfile(src,out); return [('F4-106','current','ALREADY_SATISFIED')]
    with ZipFile(src,'r') as zin:
        d=etree.fromstring(zin.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        hits=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p)).startswith(h.norm(ANCHOR))]
        if len(hits)!=1: raise RuntimeError(f'F4-106 anchor mismatch {len(hits)}')
        i,p=hits[0]; s=h.spec(p)
        if s['fn']!=['467'] or s['instr'] or s['fld'] or s['hyper'] or s['rtl'] or s['book']:
            raise RuntimeError(f'F4-106 protected structure mismatch P{i}: {s}')
        h.span(p,OLD,NEW)
        if h.spec(p)!=s: raise RuntimeError('F4-106 protected structure changed')
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
    f78.validate_structural(src,out)
    if not complete(out): raise RuntimeError('F4-106 postconditions incomplete')
    return [('F4-106',f'P{i}','APPLIED_TEFTIS_MECLISI_SUBJECT_AND_SCOPE_REPAIR_FN467_PRESERVED')]

if __name__=='__main__':
    for r in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,r)))
