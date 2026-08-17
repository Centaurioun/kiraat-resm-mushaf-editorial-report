#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from copy import deepcopy
import re,sys,shutil
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main';NS={'w':W}
def norm(s):return re.sub(r'\s+',' ',s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')).strip()
def txt(p):return ''.join(p.xpath('.//w:t/text()',namespaces=NS))
def spec(p):return {'fn':p.xpath('.//w:footnoteReference/@w:id',namespaces=NS),'instr':p.xpath('.//w:instrText/text()',namespaces=NS),'fld':len(p.xpath('.//w:fldChar',namespaces=NS)),'hyper':len(p.xpath('.//w:hyperlink',namespaces=NS)),'rtl':len(p.xpath('.//w:rtl',namespaces=NS)),'book':len(p.xpath('.//w:bookmarkStart|.//w:bookmarkEnd',namespaces=NS))}
def find(ps,a,starts=True):
 a=norm(a);h=[]
 for i,p in enumerate(ps):
  t=norm(txt(p));ok=t.startswith(a) if starts else a in t
  if ok:h.append((i,p))
 if len(h)!=1:raise RuntimeError(f'{a[:90]} hits={len(h)}')
 return h[0]
def first_rpr(p, fallback=None):
 for q in [p,fallback] if fallback is not None else [p]:
  if q is None:continue
  for r in q.xpath('./w:r',namespaces=NS):
   if r.xpath('.//w:footnoteReference|.//w:rtl|.//w:vertAlign|./w:rPr/w:i|./w:rPr/w:b',namespaces=NS):continue
   cols=r.xpath('./w:rPr/w:color/@w:val',namespaces=NS)
   if cols and cols[0].upper() not in ('AUTO','000000'):continue
   rp=r.find(f'{{{W}}}rPr');return deepcopy(rp) if rp is not None else None
 return None
def clear(p):
 ppr=p.find(f'{{{W}}}pPr')
 for c in list(p):
  if c is not ppr:p.remove(c)
def add(p,s,rpr=None):
 r=etree.Element(f'{{{W}}}r')
 if rpr is not None:r.append(deepcopy(rpr))
 t=etree.SubElement(r,f'{{{W}}}t');t.text=s
 if s.startswith(' ') or s.endswith(' '):t.set('{http://www.w3.org/XML/1998/namespace}space','preserve')
 p.append(r)
def fnruns(p):
 d={}
 for r in p.xpath('./w:r',namespaces=NS):
  ids=r.xpath('.//w:footnoteReference/@w:id',namespaces=NS)
  if ids:d[ids[0]]=deepcopy(r)
 return d
def whole(p,s,expected_fn=()):
 sp=spec(p)
 if sp['fn']!=list(map(str,expected_fn)) or sp['instr'] or sp['fld'] or sp['hyper'] or sp['rtl'] or sp['book']:raise RuntimeError('unsafe whole '+str(sp))
 rp=first_rpr(p);fr=fnruns(p);clear(p);add(p,s,rp)
 for f in expected_fn:p.append(fr[str(f)])
def chunks(p,parts,expected_fn):
 sp=spec(p)
 if sp['fn']!=list(map(str,expected_fn)) or sp['instr'] or sp['fld'] or sp['hyper'] or sp['rtl'] or sp['book']:raise RuntimeError('unsafe chunks '+str(sp))
 rp=first_rpr(p);fr=fnruns(p);clear(p)
 for k,v in parts:
  if k=='t':add(p,v,rp)
  elif k=='fn':p.append(fr[str(v)])
  else:raise ValueError(k)
def span(p,a,r):
 before=spec(p);nodes=p.xpath('.//w:t',namespaces=NS);vals=[x.text or '' for x in nodes];full=''.join(vals)
 cand=[a,a.replace("'",'’'),a.replace('’',"'")];hits=[(full.find(x),x) for x in cand if full.find(x)>=0]
 if not hits:
  if norm(r) in norm(full):return 'ALREADY_SATISFIED'
  raise RuntimeError('span missing '+a[:100])
 pos,act=hits[0];end=pos+len(act);starts=[];c=0
 for v in vals:starts.append(c);c+=len(v)
 fi=next(i for i,(st,v) in enumerate(zip(starts,vals)) if pos<st+len(v));li=next(i for i,(st,v) in enumerate(zip(starts,vals)) if end<=st+len(v));pre=vals[fi][:pos-starts[fi]];suf=vals[li][end-starts[li]:]
 nodes[fi].text=pre+r+(suf if fi==li else '')
 if fi!=li:
  for j in range(fi+1,li):nodes[j].text=''
  nodes[li].text=suf
 if spec(p)!=before:raise RuntimeError('protected changed')
 return 'APPLIED'
def apply(src,out):
 with ZipFile(src) as zin:
  d=etree.fromstring(zin.read('word/document.xml'));body=d.find('.//w:body',namespaces=NS);changed=False;res=[]
  R33="Mushafların sayısı ve dağıtıldığı merkezler hakkındaki rivâyetler, Osmânî istinsahın tarihsel uygulama boyutunu göstermektedir. Bu uygulamanın sonraki ilim geleneğinde nasıl kavramsallaştırıldığını anlayabilmek için şimdi resm ve resm-i Osmânî terimlerinin anlam çerçevesine geçmek gerekir."
  ps=body.xpath('./w:p',namespaces=NS);h=[(i,p) for i,p in enumerate(ps) if norm(txt(p))==norm(R33)]
  if h:i,p=h[0];st='ALREADY_SATISFIED'
  else:
   hi,hp=find(ps,'Resm-i Osmânî’nin Kavramsal Çerçevesi ve Tarihsel Oluşumu')
   if hi==0:raise RuntimeError('missing separator before 1.6')
   p=ps[hi-1]
   if norm(txt(p)) or any(spec(p).values()):raise RuntimeError('F4-033 separator not blank/safe')
   rp=first_rpr(ps[hi-2]);add(p,R33,rp);i=hi-1;changed=True;st='APPLIED'
  res.append(('F4-033',i,st))
  R34="Resm-i Osmânî'nin kırâatlerle ilişkisini değerlendirebilmek için önce resm kelimesinin lügavî ve ıstılahî anlamını, ardından bu terimin mushaf yazımı bağlamındaki kullanımını açıklamak gerekir. Böylece tarihsel yazım biçimi ile bu yazım biçimini inceleyen resm ilmi birbirinden ayrılabilir."
  ps=body.xpath('./w:p',namespaces=NS);h=[(i,p) for i,p in enumerate(ps) if norm(txt(p))==norm(R34)]
  if h:i,p=h[0];st34='ALREADY_SATISFIED'
  else:
   i,p=find(ps,'Resm-i Osmânî, Kur’an ilimleri içerisinde hem yazı tarihi hem de metnin korunması açısından merkezî bir kavramdır.')
   i2,p2=find(ps,'Bu çerçevede konuyu iki ana eksen üzerinde ele almak gerekmektedir.')
   i3,p3=find(ps,'Resm-i Osmânî’nin kavramsal boyutunu anlamak için öncelikle “resm” kelimesinin lügavî anlam alanı tespit edilmelidir.')
   if [i2,i3]!=[i+1,i+2]:raise RuntimeError('F4-034 opening cluster not contiguous')
   for q in [p,p2,p3]:
    if any(spec(q).values()):raise RuntimeError('F4-034 protected structure')
   whole(p,R34);body.remove(p2);body.remove(p3);changed=True;st34='STRUCTURALLY_APPLIED'
  res.append(('F4-034',i,st34))
  R36="Mushaf ilimleri bağlamında resm, Osman mushaflarının kelime ve harf yazımlarını, bu yazımlarda görülen hazf, ziyâde, ibdâl, vasl ve fasl gibi özellikleri ve şehir mushaflarına nispet edilen yazım farklılıklarını konu edinen teknik bir kullanıma kavuşmuştur. Bu ıstılahî çerçeve, özellikle Dânî ve Ebû Dâvud'un eserlerinde sistemli biçimde görünür hâle gelmiştir."
  ps=body.xpath('./w:p',namespaces=NS);h=[(i,p) for i,p in enumerate(ps) if norm(txt(p))==norm(R36)]
  if h:
   i36,p36=h[0]
   if spec(p36)['fn']!=['100']:raise RuntimeError('F4-036 note mismatch')
   st36='ALREADY_SATISFIED'
  else:
   i36,p36=find(ps,'Daha önce de ifade edildiği üzere “resm” kelimesi lügavî olarak “iz” “kalıntı” ve “belirginleşmiş” işaret kavramları etrafında şekillenmiştir.')
   chunks(p36,[('t','Mushaf ilimleri bağlamında resm, Osman mushaflarının kelime ve harf yazımlarını, bu yazımlarda görülen hazf, ziyâde, ibdâl, vasl ve fasl gibi özellikleri ve şehir mushaflarına nispet edilen yazım farklılıklarını konu edinen teknik bir kullanıma kavuşmuştur.'),('fn',100),('t'," Bu ıstılahî çerçeve, özellikle Dânî ve Ebû Dâvud'un eserlerinde sistemli biçimde görünür hâle gelmiştir.")],[100]);changed=True;st36='APPLIED'
  res.append(('F4-036',i36,st36))
  R35=("Bu aşamada resm, yalnızca yazı anlamına gelmemiş, belirli bir yazım düzenine işaret etmeye başlamıştır. Cevherî'nin sözlük açıklamaları, resm kelimesinin iz ve yazı ile ilişkili lügavî anlam alanını göstermektedir. Kelimenin Kur’an yazımına özgü teknik bir terim hâline gelmesi ise mushaf yazımına dair birikimin zamanla müstakil bir inceleme alanına dönüşmesiyle belirginleşmiştir. Özellikle Dânî ve onu takip eden resm âlimlerinin eserlerinde resm, Osman mushaflarının yazım özelliklerini ve şehir mushafları arasında nakledilen farklılıkları inceleyen teknik bir alan olarak sistemleşmiştir.")
  ps=body.xpath('./w:p',namespaces=NS);h=[(i,p) for i,p in enumerate(ps) if norm(txt(p))==norm(R35)]
  if h:
   i35,p35=h[0]
   if spec(p35)['fn']!=['101','102','103']:raise RuntimeError('F4-035 note mismatch')
   st35='ALREADY_SATISFIED'
  else:
   i35,p35=find(ps,'Resmin “iz” anlamı yazının lafzı temsil eden kalıcı bir yapı oluşuyla örtüşmektedir.')
   chunks(p35,[('t','Bu aşamada resm, yalnızca yazı anlamına gelmemiş, belirli bir yazım düzenine işaret etmeye başlamıştır.'),('fn',101),('t'," Cevherî'nin sözlük açıklamaları, resm kelimesinin iz ve yazı ile ilişkili lügavî anlam alanını göstermektedir."),('fn',102),('t',' Kelimenin Kur’an yazımına özgü teknik bir terim hâline gelmesi ise mushaf yazımına dair birikimin zamanla müstakil bir inceleme alanına dönüşmesiyle belirginleşmiştir. Özellikle Dânî ve onu takip eden resm âlimlerinin eserlerinde resm, Osman mushaflarının yazım özelliklerini ve şehir mushafları arasında nakledilen farklılıkları inceleyen teknik bir alan olarak sistemleşmiştir.'),('fn',103)],[101,102,103]);changed=True;st35='APPLIED'
  res.append(('F4-035',i35,st35))
  ps=body.xpath('./w:p',namespaces=NS);iK,pK=find(ps,'Kastallânî (ö. 923/1517 bu tarih daha önce geçtiyse silinsin) ise,') if any(norm(txt(x)).startswith(norm('Kastallânî (ö. 923/1517 bu tarih daha önce geçtiyse silinsin) ise,')) for x in ps) else find(ps,'Kastallânî (ö. 923/1517) ise,')
  oldK='Kastallânî (ö. 923/1517 bu tarih daha önce geçtiyse silinsin) ise, meseleyi bir adım daha ileri götürerek teknik bir düzleme taşır ve resmi, “yazının lafza uygunluğu” şeklinde tanımlar.'
  newK="Kastallânî (ö. 923/1517) ise, meseleyi bir adım daha ileri götürerek teknik bir düzleme taşır ve resm'i “yazının lafza uygunluğu” şeklinde tanımlar."
  stK=span(pK,oldK,newK);changed|=stK=='APPLIED'
  ps=body.xpath('./w:p',namespaces=NS);iB,pB=find(ps,'Ancak bu konuda İslâm âlimleri farklı görüşler ortaya koymuşlardır.')
  oldB='Bâkıllânî (ö. 403/10113 daha önce geçtiyse silinsin) ise şöyle demiştir:';newB='Bâkıllânî ise şöyle demiştir:'
  stB=span(pB,oldB,newB);changed|=stB=='APPLIED'
  res.append(('F4-037',iK,'APPLIED' if stK=='APPLIED' or stB=='APPLIED' else 'ALREADY_SATISFIED'))
  if not changed:shutil.copyfile(src,out);return res
  xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
  with ZipFile(out,'w') as zout:
   for info in zin.infolist():zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
  return res
if __name__=='__main__':
 for r in apply(Path(sys.argv[1]),Path(sys.argv[2])):print('\t'.join(map(str,r)))
