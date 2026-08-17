#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys
import apply_f4_053_057 as h
import apply_f4_078 as f78
NS=h.NS
E=[
("el-Mehdevî’nin mushaf hattına muhalif rivâyetlerin kabul edilmeyeceğini","el-Mehdevî’nin (ö. 440/1048-49 [?]) mushaf hattına muhalif rivâyetlerin kabul edilmeyeceğini"),
("el-Mehdevî (ö. 440/1048 daha önce geçmişmi)","el-Mehdevî"),
("Ayrıca Sehâvî ve Ebû Şâme’ye nispet edilen açıklamalar","Ayrıca Sehâvî (ö. 643/1245) ve Ebû Şâme’ye nispet edilen açıklamalar"),
("Sehâvî (ö. 642/1244 daha önce geçti mi)","Sehâvî"),
("Ebû Amr’ın (ö. 154/771 daha önce geçti mi) Zuhruf sûresinde geçen","Ebû Amr’ın (ö. 154/771) Zuhruf sûresinde geçen"),
("İbn Muʿâz el-Cühenî (ö. 442/10509 daha önce geçti mi)","İbn Muʿâz el-Cühenî (ö. 442/1050)"),
("Nitekim bir grup imamın, kurrânın, âlimin, kâtibin ve edibin mushaf hattındaki bu resmi bilmeleri, ona uymaları ve onu aşmamaları gerektiğini vurgulaması da aynı anlayışın devamıdır. Çünkü onlara göre bu yazı, vahiy kâtibi ve Rasûlullah’ın emini olan Zeyd b. Sâbit’in resmidir; onun yazdığı hiçbir şey hikmetsiz ve ince bir illetten yoksun değildir. Böylece resm-i mushaf, korunmuş bir yazı biçiminin ötesinde, güvenilir naklin maddi zemini olarak değerlendirilmektedir.","Resm kaynaklarında bazı yazım biçimlerine hikmet veya anlam ilişkisi yükleyen açıklamalar bulunmaktadır. Bu görüşler ilgili müelliflere nispet edilerek aktarılmalı; bütün resm özelliklerinin aynı bilinçli amaçla meydana geldiği yönünde genelleme yapılmamalıdır. Bazı yazım biçimleri kırâat farklılığıyla doğrudan ilişkiliyken bazıları erken imlâ teamülleri veya mushaf rivâyetleri çerçevesinde açıklanabilir.")]
def done(path):
  with ZipFile(path) as z:
    d=etree.fromstring(z.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS); T='\n'.join(h.txt(p) for p in ps)
    return all(new in T and old not in T for old,new in E) and [i for i,p in enumerate(ps) if 'Mehdevî' in h.txt(p)][0]==352 and [i for i,p in enumerate(ps) if 'Sehâvî' in h.txt(p)][0]==195
def apply(src,out):
  if done(src): f78.validate_structural(src,src); shutil.copyfile(src,out); return [('F4-098','current','ALREADY_SATISFIED')]
  with ZipFile(src,'r') as zin:
    d=etree.fromstring(zin.read('word/document.xml')); body=d.find('.//w:body',namespaces=NS); ps=body.xpath('./w:p',namespaces=NS)
    if [i for i,p in enumerate(ps) if 'Mehdevî' in h.txt(p)][0]!=352 or [i for i,p in enumerate(ps) if 'Sehâvî' in h.txt(p)][0]!=195: raise RuntimeError('first-use map mismatch')
    hits=[]
    for old,new in E:
      ps=body.xpath('./w:p',namespaces=NS); m=[(i,p) for i,p in enumerate(ps) if h.norm(old) in h.norm(h.txt(p))]
      if len(m)!=1: raise RuntimeError('target count '+old+' '+str(len(m)))
      i,p=m[0]; s=h.spec(p); h.span(p,old,new)
      if h.spec(p)!=s: raise RuntimeError('structure changed P'+str(i))
      hits.append(i)
    xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
    with ZipFile(out,'w') as zout:
      for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
  f78.validate_structural(src,out)
  if not done(out): raise RuntimeError('postconditions incomplete')
  return [('F4-098',','.join('P'+str(i) for i in hits),'APPLIED')]
if __name__=='__main__':
  for r in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,r)))
