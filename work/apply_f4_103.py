#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys
import apply_f4_053_057 as h
import apply_f4_078 as f78
NS=h.NS
OLD="Kur’an’ın İslâm dünyası içindeki matbu serüveni, 1201/1787’de Rusya’nın Saint Petersburg şehrinde Mevlây Osman (?) tarafından gerçekleştirilen baskıyla yeni bir safhaya girmiştir."
NEW="Kur’an'ın matbu serüvenindeki önemli örneklerden biri, II. Katerina'nın emriyle 1201/1787'de Saint Petersburg'da gerçekleştirilen baskıdır."
ANCHOR="Kur’an-ı Kerim’in matbu tarihine bakıldığında, ilk baskı teşebbüslerinin Avrupa’da ortaya çıktığı"

def complete(path:Path):
    with ZipFile(path) as z:
        d=etree.fromstring(z.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        texts=[h.norm(h.txt(p)) for p in ps]
        return sum(h.norm(NEW) in t for t in texts)==1 and not any(h.norm(OLD) in t for t in texts)

def apply(src:Path,out:Path):
    if complete(src):
        f78.validate_structural(src,src); shutil.copyfile(src,out); return [('F4-103','current','ALREADY_SATISFIED')]
    with ZipFile(src,'r') as zin:
        d=etree.fromstring(zin.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        hits=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p)).startswith(h.norm(ANCHOR))]
        if len(hits)!=1: raise RuntimeError(f'F4-103 paragraph anchor mismatch {len(hits)}')
        i,p=hits[0]; s=h.spec(p)
        if s['fn'] or s['instr'] or s['fld'] or s['hyper'] or s['rtl'] or s['book']:
            raise RuntimeError(f'F4-103 unsafe target P{i}: {s}')
        if h.norm(OLD) not in h.norm(h.txt(p)): raise RuntimeError('F4-103 old sentence missing')
        h.span(p,OLD,NEW)
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
    f78.validate_structural(src,out)
    if not complete(out): raise RuntimeError('F4-103 postconditions incomplete')
    return [('F4-103',f'P{i}','APPLIED_SAINT_PETERSBURG_SAFE_CORE')]

if __name__=='__main__':
    for r in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,r)))
