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
def first_rpr(p):
 for r in p.xpath('./w:r',namespaces=NS):
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
def chunks(p,parts,expected_fn):
 sp=spec(p)
 if sp['fn']!=list(map(str,expected_fn)) or sp['instr'] or sp['fld'] or sp['hyper'] or sp['rtl'] or sp['book']:raise RuntimeError('unsafe chunks '+str(sp))
 rp=first_rpr(p);fr=fnruns(p);clear(p)
 for k,v in parts:
  if k=='t':add(p,v,rp)
  elif k=='fn':p.append(fr[str(v)])
  else:raise ValueError(k)
def new_para_like(template,text):
 p=etree.Element(f'{{{W}}}p');ppr=template.find(f'{{{W}}}pPr')
 if ppr is not None:p.append(deepcopy(ppr))
 add(p,text,first_rpr(template));return p
def apply(src,out):
 with ZipFile(src) as zin:
  d=etree.fromstring(zin.read('word/document.xml'));body=d.find('.//w:body',namespaces=NS);changed=False;res=[]
  R38="İlk dönem âlimlerinden Ebû Ubeyde el-Kâsım b. Sellâm (ö. 224/838), resm-i Osmânî'yi daha sonraki literatürdeki teknik çerçevesiyle müstakil bir başlık altında tanımlamamıştır. Bununla birlikte Kur’an ilimlerine dair eserlerinde Osman mushaflarının yazımını sahâbe nakline dayanan bir metin geleneği içinde değerlendirmesi, resm düşüncesinin erken safhası bakımından önemlidir. Bu yaklaşım, daha sonra sistemleşecek resm literatüründeki bazı temel kabullerin erken dönemdeki görünümünü yansıtmaktadır."
  ps=body.xpath('./w:p',namespaces=NS);h=[(i,p) for i,p in enumerate(ps) if norm(txt(p))==norm(R38)]
  if h:i,p=h[0];st='ALREADY_SATISFIED'
  else:i,p=find(ps,'İlk dönem âlimlerinden Ebû Ubeyde el-Kâsım b. Sellâm (ö. 224/838), resm-i Osmânî terimini');chunks(p,[('t',R38),('fn',108)],[108]);changed=True;st='APPLIED'
  if spec(p)['fn']!=['108']:raise RuntimeError('F4-038 note mismatch');res.append(('F4-038',i,st))
  R39a="Resm-i Osmânî'nin müstakil bir inceleme alanı hâline gelmesinde Dânî'nin çalışmaları önemli bir yer tutmaktadır. Dânî, Osman mushaflarının yazım özelliklerini ve şehir mushafları arasında nakledilen farklılıkları sistematik biçimde kaydetmiştir. Böylece resm, belirli kuralları, örnekleri ve tasnif biçimleri bulunan teknik bir alan hâline gelmiştir. Dânî'nin yaklaşımı, farklı merkezlere nispet edilen yazım rivâyetlerini karşılaştırmalı biçimde ele alması bakımından özellikle önemlidir."
  ps=body.xpath('./w:p',namespaces=NS);h=[(i,p) for i,p in enumerate(ps) if norm(txt(p))==norm(R39a)]
  if h:i39a,p39a=h[0];stA='ALREADY_SATISFIED'
  else:i39a,p39a=find(ps,'Resm-i Osmânî’nin müstakil bir ilim hâline gelmesinde Dânî’nin çalışmaları belirleyici bir dönüm noktası');chunks(p39a,[('t',"Resm-i Osmânî'nin müstakil bir inceleme alanı hâline gelmesinde Dânî'nin çalışmaları önemli bir yer tutmaktadır. Dânî, Osman mushaflarının yazım özelliklerini ve şehir mushafları arasında nakledilen farklılıkları sistematik biçimde kaydetmiştir."),('fn',110),('t'," Böylece resm, belirli kuralları, örnekleri ve tasnif biçimleri bulunan teknik bir alan hâline gelmiştir. Dânî'nin yaklaşımı, farklı merkezlere nispet edilen yazım rivâyetlerini karşılaştırmalı biçimde ele alması bakımından özellikle önemlidir."),('fn',111)],[110,111]);changed=True;stA='APPLIED'
  R39b="Dânî'nin talebesi Ebû Dâvud Süleymân b. Necâh ise bu çerçeveyi ayrıntılı kurallar, örnekler ve uygulamalarla geliştiren önemli resm âlimlerinden biridir. Onun çalışmalarında mushaf yazımının temel başvuru zemini, güvenilir nakille aktarılan Osman mushaflarının yazım geleneğidir."
  ps=body.xpath('./w:p',namespaces=NS);h=[(i,p) for i,p in enumerate(ps) if norm(txt(p))==norm(R39b)]
  if h:i39b,p39b=h[0];stB='ALREADY_SATISFIED'
  else:i39b,p39b=find(ps,'Dânî’nin talebesi olarak bilinen Ebû Dâvud Süleymân b. Necâh, resm-i Osmânî ilminin gelişiminde');chunks(p39b,[('t',R39b),('fn',112)],[112]);changed=True;stB='APPLIED'
  if spec(p39a)['fn']!=['110','111'] or spec(p39b)['fn']!=['112']:raise RuntimeError('F4-039 note mismatch')
  res.append(('F4-039',i39a,'APPLIED' if 'APPLIED' in (stA,stB) else 'ALREADY_SATISFIED'))
  R40="Zerkeşî, Osman mushaflarında benimsenen yazım biçiminin dilcilerin kıyas yoluyla belirlediği standart imlâ kurallarıyla her zaman örtüşmediğine dikkat çeker. Onun aktardığı çerçevede mushaf hattının ölçüsü, sonraki kıyasî imlâdan ziyade sahâbe döneminden nakledilen yazım uygulamasıdır. Elif hazifleri, harf ziyadeleri ve vasl-fasl örneklerinin sonraki mushaflarda korunması da bu tarihsel aktarımın devamı olarak değerlendirilmiştir. Bu sebeple resm-i Osmânî'nin normatif değeri açıklanırken kıyasî imlâ ile nakledilmiş mushaf yazımı arasındaki farkın korunması yeterlidir; her yazım farklılığına ayrıca özel ve bilinçli bir amaç yüklenmemelidir."
  ps=body.xpath('./w:p',namespaces=NS);h=[(i,p) for i,p in enumerate(ps) if norm(txt(p))==norm(R40)]
  if h:i,p=h[0];st='ALREADY_SATISFIED'
  else:i,p=find(ps,'Zerkeşî ise, mushaf yazımını ele alırken önemli bir ilkeye dikkat çeker.');chunks(p,[('t','Zerkeşî, Osman mushaflarında benimsenen yazım biçiminin dilcilerin kıyas yoluyla belirlediği standart imlâ kurallarıyla her zaman örtüşmediğine dikkat çeker.'),('fn',113),('t',' Onun aktardığı çerçevede mushaf hattının ölçüsü, sonraki kıyasî imlâdan ziyade sahâbe döneminden nakledilen yazım uygulamasıdır.'),('fn',114),('t',' Elif hazifleri, harf ziyadeleri ve vasl-fasl örneklerinin sonraki mushaflarda korunması da bu tarihsel aktarımın devamı olarak değerlendirilmiştir.'),('fn',115),('t'," Bu sebeple resm-i Osmânî'nin normatif değeri açıklanırken kıyasî imlâ ile nakledilmiş mushaf yazımı arasındaki farkın korunması yeterlidir; her yazım farklılığına ayrıca özel ve bilinçli bir amaç yüklenmemelidir.")],[113,114,115]);changed=True;st='APPLIED'
  if spec(p)['fn']!=['113','114','115']:raise RuntimeError('F4-040 note mismatch');res.append(('F4-040',i,st))
  R41="Günümüz Kur’an tarihi çalışmalarında sözlü aktarım ile yazılı kayıtların erken dönemde birlikte işleyen unsurlar olduğu üzerinde durulmaktadır. Harald Motzki ve Nicolai Sinai gibi araştırmacıların değerlendirmeleri, erken İslâm toplumunda sözlü aktarım güçlü konumunu korurken yazılı kayıtların da giderek belirginleştiğine işaret etmektedir. Bu bulgular, resm-i Osmânî'nin kırâatleri meydana getirdiğini değil, yazılı ve sözlü aktarım kanallarının tarihsel olarak birlikte değerlendirilmesi gerektiğini göstermesi bakımından kullanılmalıdır."
  ps=body.xpath('./w:p',namespaces=NS);h=[(i,p) for i,p in enumerate(ps) if norm(txt(p))==norm(R41)]
  if h:i,p=h[0];st='ALREADY_SATISFIED'
  else:i,p=find(ps,'Benzer şekilde Harald Motzki ve Nicolai Sinai gibi modern batılı araştırmacılar');chunks(p,[('t',R41),('fn',119)],[119]);changed=True;st='APPLIED'
  if spec(p)['fn']!=['119']:raise RuntimeError('F4-041 note mismatch');res.append(('F4-041',i,st))
  R42="Resm-i Osmânî'nin tevkîfî veya ictihâdî oluşu ile sonraki mushaf geleneğinde bağlayıcı kabul edilmesi aynı soru değildir. İlk mesele, bu yazım biçiminin tarihsel kökeni ve Hz. Peygamber dönemine nispetiyle; ikinci mesele ise Osmânî mushafların ümmetin müşterek yazılı geleneği hâline gelmesinden sonra bu resme bağlılığın nasıl gerekçelendirildiğiyle ilgilidir. Aşağıdaki görüşler bu iki düzey birbirine karıştırılmadan ele alınmalıdır."
  ps=body.xpath('./w:p',namespaces=NS);h=[(i,p) for i,p in enumerate(ps) if norm(txt(p))==norm(R42)]
  if h:i,p=h[0];st='ALREADY_SATISFIED'
  else:
   ih,heading=find(ps,'Resm-i Osmânî Tevkîfî mi İctihâdi mi?')
   if spec(heading)['book']!=2:raise RuntimeError('F4-042 heading bookmarks changed')
   template=ps[ih+1]
   if spec(template)['fn']!=['121']:raise RuntimeError('unexpected first 1.8 paragraph')
   p=new_para_like(template,R42);heading.addnext(p);i=ih+1;changed=True;st='APPLIED'
  res.append(('F4-042',i,st))
  if not changed:shutil.copyfile(src,out);return res
  xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
  with ZipFile(out,'w') as zout:
   for info in zin.infolist():zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
  return res
if __name__=='__main__':
 for r in apply(Path(sys.argv[1]),Path(sys.argv[2])):print('\t'.join(map(str,r)))
