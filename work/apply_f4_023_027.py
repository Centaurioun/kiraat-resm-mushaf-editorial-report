#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from copy import deepcopy
import re,sys,shutil
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main';NS={'w':W}
def norm(s): return re.sub(r'\s+',' ',s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')).strip()
def txt(p): return ''.join(p.xpath('.//w:t/text()',namespaces=NS))
def spec(p): return {'fn':p.xpath('.//w:footnoteReference/@w:id',namespaces=NS),'instr':p.xpath('.//w:instrText/text()',namespaces=NS),'fld':len(p.xpath('.//w:fldChar',namespaces=NS)),'hyper':len(p.xpath('.//w:hyperlink',namespaces=NS)),'rtl':len(p.xpath('.//w:rtl',namespaces=NS)),'book':len(p.xpath('.//w:bookmarkStart|.//w:bookmarkEnd',namespaces=NS))}
def find(ps,a):
 a=norm(a); h=[(i,p) for i,p in enumerate(ps) if norm(txt(p)).startswith(a)]
 if len(h)!=1: raise RuntimeError(f'{a[:80]} hits={len(h)}')
 return h[0]
def first_rpr(p):
 r=p.find(f'{{{W}}}r'); return deepcopy(r.find(f'{{{W}}}rPr')) if r is not None and r.find(f'{{{W}}}rPr') is not None else None
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
def chunks(p, parts, expected_fn):
 sp=spec(p)
 if sp['fn']!=list(map(str,expected_fn)) or sp['instr'] or sp['fld'] or sp['hyper'] or sp['rtl'] or sp['book']:raise RuntimeError('unsafe chunks '+str(sp))
 rp=first_rpr(p);fr=fnruns(p);clear(p)
 for k,v in parts:
  if k=='t':add(p,v,rp)
  else:p.append(fr[str(v)])
def span(p,a,r):
 before=spec(p);nodes=p.xpath('.//w:t',namespaces=NS);vals=[x.text or '' for x in nodes];full=''.join(vals)
 cand=[a,a.replace("'",'’'),a.replace('’',"'")];hits=[(full.find(x),x) for x in cand if full.find(x)>=0]
 if not hits:
  if norm(r) in norm(full):return 'ALREADY_SATISFIED'
  raise RuntimeError('span missing '+a[:80])
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
  R23="Mervân b. Hakem'e nispet edilen açıklamada, sahifelerde yer alan Kur’an metninin Osmânî mushaflara geçirildiği ve ilerleyen dönemlerde bu sahifeler üzerinden eksiklik veya farklılık iddialarının ortaya çıkmasından endişe edildiği belirtilmektedir. Yedi harf ve arza-i âhire ile kurulan bağlantılar ise bu rivayetin doğrudan ifadesi değil, meselenin sonraki kaynaklarda açıklanma biçimleri çerçevesinde ayrıca değerlendirilmelidir."
  ps=body.xpath('./w:p',namespaces=NS);h=[(i,p) for i,p in enumerate(ps) if norm(txt(p))==norm(R23)]
  if h:i,p=h[0];st='ALREADY_SATISFIED'
  else:i,p=find(ps,'Görünen o ki, Mervân b. Hakem’i söz konusu sahifeleri imha etmeye sevk eden temel endişe');whole(p,R23);changed=True;st='APPLIED'
  res.append(('F4-023',i,st))
  R24="Yedi harf ile Osmânî istinsah arasındaki ilişkiyi açıklayan görüşlerden bir kısmı arza-i âhireye özel önem vermiştir. Bu yaklaşıma göre Hz. Peygamber'in Cebrâil ile yaptığı son mukabele, sonraki cem ve istinsah faaliyetlerinin değerlendirilmesinde başvurulan temel referanslardan biridir. Bununla birlikte Hz. Osman dönemindeki istinsahın arza-i âhire ile hangi ayrıntılar üzerinden ilişkilendirildiği konusunda sonraki açıklamalar ile erken tarihsel rivâyetler aynı kanıt düzeyinde değerlendirilmemelidir."
  ps=body.xpath('./w:p',namespaces=NS);h=[(i,p) for i,p in enumerate(ps) if norm(txt(p))==norm(R24)]
  if h:
   i,p=h[0]
   if spec(p)['fn']!=['49']:raise RuntimeError('F4-024 note mismatch')
   st='ALREADY_SATISFIED'
  else:
   i,p=find(ps,'Bu durumda “arza-i âhira” kavramı belirleyici bir referans olarak devreye girmiştir.')
   chunks(p,[('t',"Yedi harf ile Osmânî istinsah arasındaki ilişkiyi açıklayan görüşlerden bir kısmı arza-i âhireye özel önem vermiştir. Bu yaklaşıma göre Hz. Peygamber'in Cebrâil ile yaptığı son mukabele, sonraki cem ve istinsah faaliyetlerinin değerlendirilmesinde başvurulan temel referanslardan biridir."),('fn',49),('t'," Bununla birlikte Hz. Osman dönemindeki istinsahın arza-i âhire ile hangi ayrıntılar üzerinden ilişkilendirildiği konusunda sonraki açıklamalar ile erken tarihsel rivâyetler aynı kanıt düzeyinde değerlendirilmemelidir.")],[49]);changed=True;st='APPLIED'
  res.append(('F4-024',i,st))
  R25="Hz. Ebû Bekir dönemindeki cem faaliyeti, vahyin yazılı kayıtları ile sahâbenin hafızasındaki aktarımın güvenilir bir derleme içinde bir araya getirilmesine yönelik bir tedbir olarak rivâyet edilmektedir. Hz. Ömer döneminde ise yeni bir istinsah faaliyetini gerektirecek ölçüde yaygın bir kırâat ihtilafının gündeme geldiğine dair aynı yoğunlukta rivâyet bulunmamaktadır."
  ps=body.xpath('./w:p',namespaces=NS);h=[(i,p) for i,p in enumerate(ps) if norm(txt(p))==norm(R25)]
  if h:i,p=h[0];st='ALREADY_SATISFIED'
  else:i,p=find(ps,'Hz. Ebû Bekir döneminde gerçekleştirilen ilk cem faaliyetiyle birlikte Kur’an vahyinin tamamı yazılı malzeme üzerinden güvence altına alınmıştır.');whole(p,R25);changed=True;st='APPLIED'
  res.append(('F4-025',i,st))
  ps=body.xpath('./w:p',namespaces=NS);i72,p72=find(ps,'Kaynaklarda hem Medine’de hem de Medine dışında birtakım kırâat ihtilaflarının zuhur etmeye başladığı belirtilmektedir.')
  oldtab="Taberî’nin (ö. 310/922) (Tâberî’nin ölüm tarihi daha önce geçti mi bakılabilir mi)  rivâyetinde ise";newtab="Taberî'nin (ö. 310/923) rivâyetinde ise"
  sttab=span(p72,oldtab,newtab);changed|=sttab=='APPLIED'
  R26="Rivâyetler, farklı okuyuşların özellikle yeni fethedilen bölgelerde ihtilaf konusu hâline gelmesinin ciddi bir endişe doğurduğunu aktarmaktadır. Buradaki mesele, Kur’an metninin varlığından ziyade okuyuş farklılıklarının nasıl anlaşılacağı ve müşterek bir mushaf çerçevesi içinde nasıl sınırlandırılacağıyla ilgilidir. Bu sebeple istinsah faaliyetine götüren şartlar, rivâyetlerin açıkça aktardığı ihtilaf örnekleri üzerinden değerlendirilmelidir."
  ps=body.xpath('./w:p',namespaces=NS);h=[(i,p) for i,p in enumerate(ps) if norm(txt(p))==norm(R26)]
  if h:
   i,p=h[0]
   if spec(p)['fn']!=['66']:raise RuntimeError('F4-026 note mismatch')
   stbody='ALREADY_SATISFIED'
  else:
   i,p=find(ps,'Bu rivâyetler, o dönemde Müslümanlar arasında kırâate yönelik ihtilafların çok vahim bir noktaya geldiği')
   chunks(p,[('t','Rivâyetler, farklı okuyuşların özellikle yeni fethedilen bölgelerde ihtilaf konusu hâline gelmesinin ciddi bir endişe doğurduğunu aktarmaktadır.'),('fn',66),('t',' Buradaki mesele, Kur’an metninin varlığından ziyade okuyuş farklılıklarının nasıl anlaşılacağı ve müşterek bir mushaf çerçevesi içinde nasıl sınırlandırılacağıyla ilgilidir. Bu sebeple istinsah faaliyetine götüren şartlar, rivâyetlerin açıkça aktardığı ihtilaf örnekleri üzerinden değerlendirilmelidir.')],[66]);changed=True;stbody='APPLIED'
  res.append(('F4-026',i,'APPLIED' if sttab=='APPLIED' or stbody=='APPLIED' else 'ALREADY_SATISFIED'))
  ps=body.xpath('./w:p',namespaces=NS);desired27="Zeyd b. Sâbit'in başkanlığında oluşturulan istinsah heyeti, Kur’an'ın çoğaltılmasıyla ilgili çalışmasını tamamlamıştır."
  dh=[(j,x) for j,x in enumerate(ps) if norm(txt(x)).startswith(norm(desired27))]
  if dh:i,p=dh[0]
  else:i,p=find(ps,'Zeyd b. Sâbit’in başkanlığında oluşturulan istinsah heyeti, Kur’an’ın çoğaltılmasıyla ilgili faaliyetlerini tam baş senede tamamlamıştır.')
  st=span(p,"Zeyd b. Sâbit’in başkanlığında oluşturulan istinsah heyeti, Kur’an’ın çoğaltılmasıyla ilgili faaliyetlerini tam baş senede tamamlamıştır.",desired27);changed|=st=='APPLIED';res.append(('F4-027',i,st))
  if not changed:shutil.copyfile(src,out);return res
  xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
  with ZipFile(out,'w') as zout:
   for info in zin.infolist():zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
  return res
if __name__=='__main__':
 for r in apply(Path(sys.argv[1]),Path(sys.argv[2])):print('\t'.join(map(str,r)))
