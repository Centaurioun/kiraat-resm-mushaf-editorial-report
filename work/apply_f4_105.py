#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys
import apply_f4_053_057 as h
import apply_f4_078 as f78
NS=h.NS
OLD="Bütün bu veriler, matbu mushafların sadece mevcut okuyuşları pasif biçimde yansıtan araçlar olmadığını göstermektedir."
NEW="Belirli kırâat rivâyetlerine göre hazırlanan matbu mushaflar, bu rivâyetlerin yazılı görünürlüğünü ve kullanım alanını artırmıştır. Bununla birlikte bir rivâyetin belirli bölgelerde yaygınlaşması yalnız baskı faaliyetiyle açıklanamaz; öğretim gelenekleri, bölgesel kırâat tercihleri, resmî neşir politikaları ve eğitim kurumları da bu süreçte etkili olmuştur."

def complete(path:Path):
    with ZipFile(path) as z:
        d=etree.fromstring(z.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        texts=[h.norm(h.txt(p)) for p in ps]
        return sum(h.norm(t)==h.norm(NEW) for t in texts)==1 and not any(h.norm(t).startswith(h.norm(OLD)) for t in texts)

def apply(src:Path,out:Path):
    if complete(src):
        f78.validate_structural(src,src); shutil.copyfile(src,out); return [('F4-105','current','ALREADY_SATISFIED')]
    with ZipFile(src,'r') as zin:
        d=etree.fromstring(zin.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        hits=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p)).startswith(h.norm(OLD))]
        if len(hits)!=1: raise RuntimeError(f'F4-105 anchor mismatch {len(hits)}')
        i,p=hits[0]; s=h.spec(p)
        if s['fn'] or s['instr'] or s['fld'] or s['hyper'] or s['rtl'] or s['book']:
            raise RuntimeError(f'F4-105 unsafe target P{i}: {s}')
        h.whole(p,NEW,())
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
    f78.validate_structural(src,out)
    if not complete(out): raise RuntimeError('F4-105 postconditions incomplete')
    return [('F4-105',f'P{i}','APPLIED_MULTICAUSAL_QIRAAT_SPREAD_CLOSURE')]

if __name__=='__main__':
    for r in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,r)))
