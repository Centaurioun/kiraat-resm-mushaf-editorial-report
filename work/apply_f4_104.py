#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys
import apply_f4_053_057 as h
import apply_f4_078 as f78
NS=h.NS
OLD="Bu çerçevede resm-i Osmânî’ye dair görüşlerin günümüzde basılan, kırâat rivâyetlerine göre düzenlenmiş mushaflarda uygulanan yazı sisteminin teorik arka planını oluşturmaktadır."
NEW="Modern mushafların yüksek düzeyde görsel ve metinsel birlik göstermesinde resm-i Osmânî'ye bağlılık önemli bir unsur olmakla birlikte tek etken değildir. Matbaa teknolojisinin gelişmesi, tashih ve denetim kurulları, kırâat ve yazım alanındaki uzmanlık, eğitim kurumları ve resmî neşir politikaları da bu standardizasyon sürecine katkıda bulunmuştur."

def complete(path:Path):
    with ZipFile(path) as z:
        d=etree.fromstring(z.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        texts=[h.norm(h.txt(p)) for p in ps]
        return sum(h.norm(t)==h.norm(NEW) for t in texts)==1 and not any(h.norm(t).startswith(h.norm(OLD)) for t in texts)

def apply(src:Path,out:Path):
    if complete(src):
        f78.validate_structural(src,src); shutil.copyfile(src,out); return [('F4-104','current','ALREADY_SATISFIED')]
    with ZipFile(src,'r') as zin:
        d=etree.fromstring(zin.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        hits=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p)).startswith(h.norm(OLD))]
        if len(hits)!=1: raise RuntimeError(f'F4-104 anchor mismatch {len(hits)}')
        i,p=hits[0]; s=h.spec(p)
        if s['fn'] or s['instr'] or s['fld'] or s['hyper'] or s['rtl'] or s['book']:
            raise RuntimeError(f'F4-104 unsafe target P{i}: {s}')
        h.whole(p,NEW,())
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
    f78.validate_structural(src,out)
    if not complete(out): raise RuntimeError('F4-104 postconditions incomplete')
    return [('F4-104',f'P{i}','APPLIED_MULTICAUSAL_STANDARDIZATION_REFRAME')]

if __name__=='__main__':
    for r in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,r)))
