#!/usr/bin/env python3
from copy import deepcopy
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys
import apply_f4_053_057 as h
import apply_f4_078 as f78
NS=h.NS; W=h.W
OLD1="İslâm tarihi boyunca mushaf istinsahı yalnız bir çoğaltma faaliyeti olarak görülmemiş, aynı zamanda güçlü bir hat ve yazı geleneği içinde gelişmiştir."
OLD2="Nitekim İbn Kesîr’in de işaret ettiği üzere, ilk dönemlerde yaygın olan yazı biçimi daha sade ve kapalı bir görünüm arz etmiştir."
HEAD="Kırâat Rivâyetlerine Göre Düzenlenen Basılı Mushafların Yaygınlaşması ve Etkileri"
NEW=("Mushafın matbaa yoluyla çoğaltılması, resm-i Osmânî'nin yeni üretim teknikleri içinde nasıl korunacağı meselesini gündeme getirmiştir. "
     "Erken matbu mushaflardan Osmanlı ve sonraki resmî neşir girişimlerine uzanan süreçte baskı tekniği, tashih mekanizmaları ve resm geleneğine bağlılık birlikte etkili olmuştur. "
     "Belirli kırâat rivâyetlerine göre hazırlanan baskılar ise bu tarihsel sürecin ayrı bir boyutunu oluşturmaktadır.")
BG1="Matbaa öncesinde mushaf istinsahı, hat ve yazı geleneği içinde sürdürülmüştür."
BG2="İbn Kesîr’in aktardığı tarihsel çerçevede, erken yazı biçimi daha sade iken İbn Mukle ve İbnü’l-Bevvâb ile birlikte daha kaideli bir üslup gelişmiştir."

def fn_runs(p):
  out={}
  for r in p.xpath('./w:r',namespaces=NS):
    ids=r.xpath('.//w:footnoteReference/@w:id',namespaces=NS)
    for fid in ids: out[fid]=deepcopy(r)
  return out

def first_rpr(p):
  r=p.find(f'{{{W}}}r')
  return deepcopy(r.find(f'{{{W}}}rPr')) if r is not None and r.find(f'{{{W}}}rPr') is not None else None

def clear(p):
  ppr=p.find(f'{{{W}}}pPr')
  for ch in list(p):
    if ch is not ppr: p.remove(ch)

def add_text(p,text,rpr):
  r=etree.Element(f'{{{W}}}r')
  if rpr is not None:r.append(deepcopy(rpr))
  t=etree.SubElement(r,f'{{{W}}}t'); t.text=text; p.append(r)

def complete(path:Path):
  with ZipFile(path) as z:
    d=etree.fromstring(z.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
    nh=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p))==h.norm(NEW)]
    bg=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p))==h.norm(BG1+' '+BG2)]
    hh=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p))==h.norm(HEAD)]
    stale=[p for p in ps if h.norm(h.txt(p)).startswith(h.norm(OLD1)) or h.norm(h.txt(p)).startswith(h.norm(OLD2))]
    return (len(nh)==len(bg)==len(hh)==1 and hh[0][0]+1==nh[0][0] and nh[0][0]+1==bg[0][0]
            and h.spec(nh[0][1])['fn']==[] and h.spec(bg[0][1])['fn']==['454','455'] and not stale)

def apply(src:Path,out:Path):
  if complete(src):
    f78.validate_structural(src,src); shutil.copyfile(src,out); return [('F4-102','current','ALREADY_SATISFIED')]
  with ZipFile(src,'r') as zin:
    d=etree.fromstring(zin.read('word/document.xml')); body=d.find('.//w:body',namespaces=NS); ps=body.xpath('./w:p',namespaces=NS)
    h1=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p)).startswith(h.norm(OLD1))]
    h2=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p)).startswith(h.norm(OLD2))]
    hh=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p))==h.norm(HEAD)]
    if len(h1)!=1 or len(h2)!=1 or len(hh)!=1: raise RuntimeError(f'F4-102 anchors {len(h1)}/{len(h2)}/{len(hh)}')
    i1,p1=h1[0]; i2,p2=h2[0]; ih,ph=hh[0]
    if not (ih+1==i1 and i1+1==i2): raise RuntimeError(f'F4-102 boundary {ih},{i1},{i2}')
    if h.spec(p1)['fn']!=['454'] or h.spec(p2)['fn']!=['455']: raise RuntimeError('F4-102 footnote map mismatch')
    for p in (p1,p2):
      s=h.spec(p)
      if s['instr'] or s['fld'] or s['hyper'] or s['book']: raise RuntimeError(f'F4-102 unsafe paragraph {s}')
    refs={**fn_runs(p1),**fn_runs(p2)}
    # P423 becomes the report-approved direct opener with no citation parked on it.
    clear(p1); add_text(p1,NEW,first_rpr(p1))
    # P424 becomes a compact, citation-supported historical background sentence pair.
    rpr=first_rpr(p2); clear(p2)
    add_text(p2,BG1,rpr); p2.append(refs['454']); add_text(p2,' '+BG2,rpr); p2.append(refs['455'])
    xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
    with ZipFile(out,'w') as zout:
      for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
  f78.validate_structural(src,out)
  if not complete(out): raise RuntimeError('F4-102 postconditions incomplete')
  return [('F4-102',f'P{i1}-P{i2}','APPLIED_PRINT_FOCUSED_OPENING_WITH_FN454_455_REANCHOR')]

if __name__=='__main__':
  for r in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,r)))
