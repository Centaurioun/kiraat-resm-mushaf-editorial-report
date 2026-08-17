#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil, sys
import apply_f4_053_057 as h
import apply_f4_078 as f78
NS=h.NS
OLD=("Bununla birlikte Osmânî mushaflarının ilk şeklinde nokta ve hareke bulunmamaktadır. "
     "Bunun temel sebebi, mushaf resminin farklı kırâat vecihlerini ihtimal dâhilinde taşıyabilecek bir esnekliğe sahip olmasıdır.")
NEW=("Erken mushafların yazı iskeleti zamanla nokta, hareke ve diğer yardımcı işaretlerin gelişmesiyle daha ayrıntılı bir görsel sisteme kavuşmuştur. "
     "Bu gelişme, resm-i Osmânî'nin temel harf yapısının sonraki mushaflarda korunmasıyla birlikte ilerlemiştir. "
     "Nokta ve harekenin ilk mushaflarda bugünkü biçimiyle bulunmaması dönemin yazı sistemiyle ilgilidir; bunu yalnız farklı kırâatleri açık tutmak amacıyla yapılmış bilinçli bir tercih olarak açıklamak ihtiyat gerektirir.")
TAIL="Ancak zamanla hareke ve diğer zapt işaretleri kullanılmaya başlanınca, müstensihler mushaflarını"

def complete(path:Path):
  with ZipFile(path) as z:
    d=etree.fromstring(z.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
    texts=[h.norm(h.txt(p)) for p in ps]
    return sum(h.norm(NEW) in t and h.norm(TAIL) in t for t in texts)==1 and not any(h.norm(OLD) in t for t in texts)

def apply(src:Path,out:Path):
  if complete(src):
    f78.validate_structural(src,src); shutil.copyfile(src,out); return [('F4-100','current','ALREADY_SATISFIED')]
  with ZipFile(src,'r') as zin:
    d=etree.fromstring(zin.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
    hits=[(i,p) for i,p in enumerate(ps) if h.norm(OLD) in h.norm(h.txt(p))]
    if len(hits)!=1: raise RuntimeError(f'F4-100 anchor mismatch: {len(hits)}')
    i,p=hits[0]; s=h.spec(p)
    if s['fn'] or s['instr'] or s['fld'] or s['hyper'] or s['rtl'] or s['book']:
      raise RuntimeError(f'F4-100 unsafe target P{i}: {s}')
    if h.norm(TAIL) not in h.norm(h.txt(p)): raise RuntimeError('F4-100 untouched continuation missing')
    h.span(p,OLD,NEW)
    xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
    with ZipFile(out,'w') as zout:
      for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
  f78.validate_structural(src,out)
  if not complete(out): raise RuntimeError('F4-100 postconditions incomplete')
  return [('F4-100',f'P{i}','APPLIED_EARLY_SCRIPT_CAUSAL_SCOPE_REFRAME')]

if __name__=='__main__':
  for r in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,r)))
