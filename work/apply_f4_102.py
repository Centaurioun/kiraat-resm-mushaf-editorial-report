#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys
import apply_f4_053_057 as h
import apply_f4_078 as f78
NS=h.NS
OLD1="İslâm tarihi boyunca mushaf istinsahı yalnız bir çoğaltma faaliyeti olarak görülmemiş, aynı zamanda güçlü bir hat ve yazı geleneği içinde gelişmiştir."
OLD2="Nitekim İbn Kesîr’in de işaret ettiği üzere, ilk dönemlerde yaygın olan yazı biçimi daha sade ve kapalı bir görünüm arz etmiştir."
HEAD="Kırâat Rivâyetlerine Göre Düzenlenen Basılı Mushafların Yaygınlaşması ve Etkileri"
NEW=("Mushafın matbaa yoluyla çoğaltılması, resm-i Osmânî'nin yeni üretim teknikleri içinde nasıl korunacağı meselesini gündeme getirmiştir. "
     "Erken matbu mushaflardan Osmanlı ve sonraki resmî neşir girişimlerine uzanan süreçte baskı tekniği, tashih mekanizmaları ve resm geleneğine bağlılık birlikte etkili olmuştur. "
     "Belirli kırâat rivâyetlerine göre hazırlanan baskılar ise bu tarihsel sürecin ayrı bir boyutunu oluşturmaktadır.")
BG1="Matbaa öncesinde mushaf istinsahı, hat ve yazı geleneği içinde sürdürülmüştür."
BG2="İbn Kesîr’in aktardığı tarihsel çerçevede, erken yazı biçimi daha sade iken İbn Mukle ve İbnü’l-Bevvâb ile birlikte daha kaideli bir üslup gelişmiştir."

def complete(path:Path):
  with ZipFile(path) as z:
    d=etree.fromstring(z.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
    p1=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p))==h.norm(NEW+' '+BG1)]
    p2=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p))==h.norm(BG2)]
    hh=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p))==h.norm(HEAD)]
    stale=[p for p in ps if h.norm(h.txt(p)).startswith(h.norm(OLD1)) or h.norm(h.txt(p)).startswith(h.norm(OLD2))]
    return (len(p1)==len(p2)==len(hh)==1 and hh[0][0]+1==p1[0][0] and p1[0][0]+1==p2[0][0]
            and h.spec(p1[0][1])['fn']==['454'] and h.spec(p2[0][1])['fn']==['455']
            and h.spec(p1[0][1])['rtl']==1 and not stale)

def apply(src:Path,out:Path):
  if complete(src):
    f78.validate_structural(src,src); shutil.copyfile(src,out); return [('F4-102','current','ALREADY_SATISFIED')]
  with ZipFile(src,'r') as zin:
    d=etree.fromstring(zin.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
    h1=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p)).startswith(h.norm(OLD1))]
    h2=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p)).startswith(h.norm(OLD2))]
    hh=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p))==h.norm(HEAD)]
    if len(h1)!=1 or len(h2)!=1 or len(hh)!=1: raise RuntimeError(f'F4-102 anchors {len(h1)}/{len(h2)}/{len(hh)}')
    i1,p1=h1[0]; i2,p2=h2[0]; ih,ph=hh[0]
    if not (ih+1==i1 and i1+1==i2): raise RuntimeError(f'F4-102 boundary {ih},{i1},{i2}')
    if h.spec(p1)['fn']!=['454'] or h.spec(p2)['fn']!=['455']: raise RuntimeError('F4-102 footnote map mismatch')
    if h.spec(p1)['rtl']!=1: raise RuntimeError('F4-102 expected RTL inventory mismatch on first lead-in')
    for p in (p1,p2):
      s=h.spec(p)
      if s['instr'] or s['fld'] or s['hyper'] or s['book']: raise RuntimeError(f'F4-102 unsafe paragraph {s}')
    # Replace only text nodes; genuine FN454/FN455 and the pre-existing RTL run remain structurally intact.
    h.span(p1,h.txt(p1),NEW+' '+BG1)
    h.span(p2,h.txt(p2),BG2)
    xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
    with ZipFile(out,'w') as zout:
      for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
  f78.validate_structural(src,out)
  if not complete(out): raise RuntimeError('F4-102 postconditions incomplete')
  return [('F4-102',f'P{i1}-P{i2}','APPLIED_PRINT_FOCUSED_OPENING_WITH_CITATION_SAFE_COMPRESSION')]

if __name__=='__main__':
  for r in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,r)))
