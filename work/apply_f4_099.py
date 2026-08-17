#!/usr/bin/env python3
from copy import deepcopy
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys
import apply_f4_053_057 as h
import apply_f4_078 as f78
NS=h.NS
OLD="Bütün bu tasnifler bir arada değerlendirildiğinde, Osmânî mushaflar arasındaki yazım farklılıklarının kırâat rivâyetleriyle ilişkisinin son derece bilinçli ve işlevsel bir yapıya sahip olduğu anlaşılmaktadır."
HEAD="Çağdaş Basılı Mushaflarda Resm-i Osmânî’nin Korunması ve Klasik Kaynaklara Dayalı Yazım Geleneği"
NEW="Klasik resm literatüründe kaydedilen bu yazım özellikleri, sonraki mushaf istinsah ve neşir geleneğinde başvuru kaynağı olmayı sürdürmüştür. Bu devamlılığın nasıl korunduğunu anlayabilmek için resmin sonraki mushaflarda uygulanma biçimine ayrıca bakmak gerekir."
def complete(path):
  with ZipFile(path) as z:
    d=etree.fromstring(z.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
    nh=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p))==h.norm(NEW)]
    hh=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p))==h.norm(HEAD)]
    return len(nh)==1 and len(hh)==1 and nh[0][0]+1==hh[0][0] and h.spec(nh[0][1])['fn']==[] and h.spec(nh[0][1])['rtl']==0 and h.spec(nh[0][1])['book']==0 and h.spec(hh[0][1])['book']==2
def apply(src:Path,out:Path):
  if complete(src): f78.validate_structural(src,src); shutil.copyfile(src,out); return [('F4-099','current','ALREADY_SATISFIED')]
  with ZipFile(src,'r') as zin:
    d=etree.fromstring(zin.read('word/document.xml')); body=d.find('.//w:body',namespaces=NS); ps=body.xpath('./w:p',namespaces=NS)
    hits=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p)).startswith(h.norm(OLD))]
    if len(hits)!=1: raise RuntimeError('F4-099 closing anchor mismatch')
    i,p=hits[0]
    if h.spec(p)['fn'] or h.spec(p)['rtl'] or h.spec(p)['fld'] or h.spec(p)['book']: raise RuntimeError('unsafe F4-099 source paragraph')
    if i+1>=len(ps) or h.norm(h.txt(ps[i+1]))!=h.norm(HEAD) or h.spec(ps[i+1])['book']!=2: raise RuntimeError('F4-099 heading boundary mismatch')
    q=deepcopy(p); h.whole(q,NEW,()); body.insert(body.index(p)+1,q)
    xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
    with ZipFile(out,'w') as zout:
      for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
  f78.validate_structural(src,out)
  if not complete(out): raise RuntimeError('F4-099 postconditions incomplete')
  return [('F4-099',f'P{i+1}','APPLIED_HISTORICAL_TRANSITION_INSERTION')]
if __name__=='__main__':
  for r in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,r)))
