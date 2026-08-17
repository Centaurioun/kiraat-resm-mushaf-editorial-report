#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from copy import deepcopy
import re,sys,shutil
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main';NS={'w':W}
def norm(s):return re.sub(r'\s+',' ',s.replace('’',"'").replace('‘',"'")).strip()
def txt(p):return ''.join(p.xpath('.//w:t/text()',namespaces=NS))
def spec(p):return {'fn':p.xpath('.//w:footnoteReference/@w:id',namespaces=NS),'instr':p.xpath('.//w:instrText/text()',namespaces=NS),'fld':len(p.xpath('.//w:fldChar',namespaces=NS)),'hyper':len(p.xpath('.//w:hyperlink',namespaces=NS)),'rtl':len(p.xpath('.//w:rtl',namespaces=NS)),'book':len(p.xpath('.//w:bookmarkStart|.//w:bookmarkEnd',namespaces=NS))}
def find(ps,a):
 a=norm(a);h=[(i,p) for i,p in enumerate(ps) if norm(txt(p)).startswith(a)]
 if len(h)!=1:raise RuntimeError(f'{a[:60]} hits={len(h)}')
 return h[0]
def first_rpr(p):
 r=p.find(f'{{{W}}}r');return deepcopy(r.find(f'{{{W}}}rPr')) if r is not None and r.find(f'{{{W}}}rPr') is not None else None
def clear(p):
 pp=p.find(f'{{{W}}}pPr')
 for c in list(p):
  if c is not pp:p.remove(c)
def add(p,s,rpr=None):
 r=etree.Element(f'{{{W}}}r');
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
def span(p,a,r):
 before=spec(p);nodes=p.xpath('.//w:t',namespaces=NS);vals=[x.text or '' for x in nodes];full=''.join(vals);cand=[a,a.replace("'",'’'),a.replace('’',"'")];hits=[(full.find(x),x) for x in cand if full.find(x)>=0]
 if not hits:
  if norm(r) in norm(full):return 'ALREADY_SATISFIED'
  raise RuntimeError('span missing '+a[:70])
 pos,act=hits[0];end=pos+len(act);starts=[];c=0
 for v in vals:starts.append(c);c+=len(v)
 fi=next(i for i,(st,v) in enumerate(zip(starts,vals)) if pos<st+len(v));li=next(i for i,(st,v) in enumerate(zip(starts,vals)) if end<=st+len(v));pre=vals[fi][:pos-starts[fi]];suf=vals[li][end-starts[li]:]
 nodes[fi].text=pre+r+(suf if fi==li else '')
 if fi!=li:
  for j in range(fi+1,li):nodes[j].text=''
  nodes[li].text=suf
 if spec(p)!=before:raise RuntimeError('protected structure changed')
 return 'APPLIED'
def apply(src,out):
 with ZipFile(src) as zin:
  d=etree.fromstring(zin.read('word/document.xml'));body=d.find('.//w:body',namespaces=NS);changed=False;res=[];ps=body.xpath('./w:p',namespaces=NS)
  i,p=find(ps,'Genel kabul, vahyin toplu hâlde derlenmesinin Hz. Ebû Bekir’in halifeliği döneminde gerçekleştiği yönündedir.')
  desired="Genel kabul, vahyin toplu hâlde derlenmesinin Hz. Ebû Bekir’in halifeliği döneminde gerçekleştiği yönündedir. Sahâbeden bazılarının Hz. Peygamber döneminde Kur’an’ı topladıkları yönündeki rivâyetler, bu kabul ile çelişmemektedir. Hz. Peygamber döneminde cem ifadesi bazı rivâyetlerde Kur’an'ın ezberlenmesi anlamında kullanılmakla birlikte vahyin çeşitli yazı malzemelerine kaydedildiği de bilinmektedir. Hz. Ebû Bekir dönemindeki cem faaliyetinin ayırt edici yönü, dağınık yazılı malzemenin ve hafızadaki aktarımın resmî bir derleme süreci içinde bir araya getirilmesidir."
  if norm(txt(p))==norm(desired):
   if spec(p)['fn']!=['31','32']:raise RuntimeError('F4-018 note mismatch')
   st='ALREADY_SATISFIED'
  else:
   if spec(p)['fn']!=['31','32'] or any([spec(p)['instr'],spec(p)['fld'],spec(p)['hyper'],spec(p)['rtl'],spec(p)['book']]):raise RuntimeError('unsafe F4-018')
   fr=fnruns(p);rp=first_rpr(p);clear(p);add(p,"Genel kabul, vahyin toplu hâlde derlenmesinin Hz. Ebû Bekir’in halifeliği döneminde gerçekleştiği yönündedir. Sahâbeden bazılarının Hz. Peygamber döneminde Kur’an’ı topladıkları yönündeki rivâyetler, bu kabul ile çelişmemektedir. Hz. Peygamber döneminde cem ifadesi bazı rivâyetlerde Kur’an'ın ezberlenmesi anlamında kullanılmakla birlikte vahyin çeşitli yazı malzemelerine kaydedildiği de bilinmektedir.",rp);p.append(fr['31']);add(p," Hz. Ebû Bekir dönemindeki cem faaliyetinin ayırt edici yönü, dağınık yazılı malzemenin ve hafızadaki aktarımın resmî bir derleme süreci içinde bir araya getirilmesidir.",rp);p.append(fr['32']);changed=True;st='APPLIED'
  res.append(('F4-018',i,st))
  ps=body.xpath('./w:p',namespaces=NS);i,p=find(ps,'Rivâyetlerin çoğuna göre bu önemli görev, vahiy kâtiplerinden Zeyd b. Sâbit’e verilmiş;')
  old19="Ayrıca Zeyd b. Sâbit’in kızı Hârice’den (ö. 100/718) gelen aktarıma göre Hz. Ebû Bekir’in Saîd b. el-Âs’ı Zeyd b. Sâbit’e yardımcı olarak atadığından da bahsedilmektedir."
  new19="Ayrıca Zeyd b. Sâbit'in oğlu Hârice b. Zeyd'den (ö. 100/718-19) gelen aktarıma göre, Hz. Ebû Bekir'in Saîd b. el-Âs'ı Zeyd b. Sâbit'e yardımcı olarak görevlendirdiğinden de bahsedilmektedir."
  st19=span(p,old19,new19);changed|=st19=='APPLIED'
  old21="Öte yandan derlemeyle ilgili rivâyetlerde geçmese de Hz. Osman döneminde yapılan istinsah faaliyetlerini dile getiren kimi rivâyette Zeyd’in, “en iyi yazı yazan sahâbî” olduğu yönündeki bilgiler de onun gerek derleme, gerekse istinsah faaliyetinde aktif rol almasının nedeninin yazı noktasındaki maharetli olduğunu gösterir."
  new21="Zeyd b. Sâbit'in görevlendirilmesinde, vahiy kâtipliği tecrübesinin yanı sıra yazı konusundaki yetkinliğinin de etkili olduğu anlaşılmaktadır."
  st21=span(p,old21,new21);changed|=st21=='APPLIED'
  if spec(p)['fn']!=['34','35','36','37']:raise RuntimeError('F4-019/021 note inventory changed')
  res.extend([('F4-019',i,st19),('F4-021',i,st21)])
  ps=body.xpath('./w:p',namespaces=NS);i,p=find(ps,'Genel kabule göre bu şekilde derlenen sahifeler (suhuf), Hz. Ebû Bekir’in yanında muhafaza edilmiş')
  old20="Daha sonraki dönemlerde bu sahifelerin akıbeti ile ilgili farklı rivâyetler bulunmaktadır. Hz. Osman zamanında mushafın çoğaltılması meselesi gündeme geldiğinde, mushaf Hz. Hafsa’dan ödünç alınarak istinsahın ardından kendisine iade edilmiştir."
  new20="Daha sonraki dönemlerde bu suhufun akıbetiyle ilgili farklı rivâyetler bulunmaktadır. Hz. Osman döneminde mushafların çoğaltılması gündeme geldiğinde, Hz. Hafsa'nın yanında bulunan bu suhuf istinsah amacıyla alınmış, işlem tamamlandıktan sonra kendisine iade edilmiştir."
  st20=span(p,old20,new20);changed|=st20=='APPLIED'
  old22="Kaynakların belirttiğine göre bu mushaf Hz. Hafsa’nın vefatından sonra Medine Valisi Mervân b. Hakem (ö. 132/749) tarafından Abdullah b. Ömer’den alınmış, bu ilk nüsha ile Hz. Osman’ın istinsah ettirdiği mushaflar arasında ihtilaf bulunduğu iddiasına kalkışılmaması için yaktırılmıştır."
  new22="Kaynakların belirttiğine göre bu sahifeler, Hz. Hafsa'nın vefatından sonra Medine Valisi Mervân b. Hakem (ö. 65/685) tarafından Abdullah b. Ömer'den alınmış ve imha ettirilmiştir."
  st22=span(p,old22,new22);changed|=st22=='APPLIED'
  if spec(p)['fn']!=['43','44','45']:raise RuntimeError('F4-020/022 note inventory changed')
  res.extend([('F4-020',i,st20),('F4-022',i,st22)])
  if not changed:shutil.copyfile(src,out);return res
  xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
  with ZipFile(out,'w') as zout:
   for info in zin.infolist():zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
  return res
if __name__=='__main__':
 for r in apply(Path(sys.argv[1]),Path(sys.argv[2])):print('\t'.join(map(str,r)))
