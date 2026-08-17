#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys
import apply_f4_053_057 as h
import apply_f4_078 as f78
NS=h.NS
OLD1="Bütün bu veriler birlikte değerlendirildiğinde, çağdaş matbu mushaflarda resm-i Osmânî’nin korunmasının gelişigüzel bir tercih olmadığı açıkça anlaşılmaktadır."
OLD2="Bu çerçevede çağdaş mushaf neşirlerinde resm-i Osmânî’nin korunması üç temel amaca hizmet etmektedir."
HEAD="Kırâat Rivâyetlerine Göre Düzenlenen Basılı Mushafların Yaygınlaşması ve Etkileri"
NEW=("Modern mushaf neşrinde resm-i Osmânî'nin uygulanması, klasik resm literatüründe kaydedilen yazım rivâyetleri ve kurallarının yeniden değerlendirilmesine dayanır. "
     "Dânî ve Ebû Dâvud'un eserleri bu bakımdan temel başvuru kaynakları arasındadır. "
     "Bununla birlikte modern neşir uygulaması yalnız klasik metinlerin aktarımından ibaret değildir; tashih kurulları, kırâat uzmanlığı ve neşir kurumlarının tercihleri de sürece katılmaktadır.")

def complete(path:Path):
  with ZipFile(path) as z:
    d=etree.fromstring(z.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
    nh=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p))==h.norm(NEW)]
    hh=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p))==h.norm(HEAD)]
    stale=[p for p in ps if h.norm(h.txt(p)).startswith(h.norm(OLD1)) or h.norm(h.txt(p)).startswith(h.norm(OLD2))]
    return len(nh)==1 and len(hh)==1 and nh[0][0]+1==hh[0][0] and not stale and h.spec(nh[0][1])['fn']==[] and h.spec(nh[0][1])['rtl']==0 and h.spec(nh[0][1])['book']==0 and h.spec(hh[0][1])['book']==2

def apply(src:Path,out:Path):
  if complete(src):
    f78.validate_structural(src,src); shutil.copyfile(src,out); return [('F4-101','current','ALREADY_SATISFIED')]
  with ZipFile(src,'r') as zin:
    d=etree.fromstring(zin.read('word/document.xml')); body=d.find('.//w:body',namespaces=NS); ps=body.xpath('./w:p',namespaces=NS)
    h1=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p)).startswith(h.norm(OLD1))]
    h2=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p)).startswith(h.norm(OLD2))]
    hh=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p))==h.norm(HEAD)]
    if len(h1)!=1 or len(h2)!=1 or len(hh)!=1: raise RuntimeError(f'F4-101 anchor mismatch {len(h1)}/{len(h2)}/{len(hh)}')
    i1,p1=h1[0]; i2,p2=h2[0]; ih,ph=hh[0]
    if not (i1+1==i2 and i2+1==ih): raise RuntimeError(f'F4-101 boundary not contiguous: {i1},{i2},{ih}')
    for label,p in [('P421',p1),('P422',p2)]:
      s=h.spec(p)
      if s['fn'] or s['instr'] or s['fld'] or s['hyper'] or s['rtl'] or s['book']: raise RuntimeError(f'F4-101 unsafe {label}: {s}')
    if h.spec(ph)['book']!=2: raise RuntimeError('F4-101 heading bookmark mismatch')
    h.whole(p1,NEW,())
    body.remove(p2)
    xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
    with ZipFile(out,'w') as zout:
      for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
  f78.validate_structural(src,out)
  if not complete(out): raise RuntimeError('F4-101 postconditions incomplete')
  return [('F4-101',f'P{i1}','APPLIED_REPEATED_CONCLUSIONS_CONSOLIDATED')]

if __name__=='__main__':
  for r in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,r)))
