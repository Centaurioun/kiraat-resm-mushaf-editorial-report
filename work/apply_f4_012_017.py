#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from copy import deepcopy
import re,sys,shutil
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main';NS={'w':W}
def norm(s):return re.sub(r'\s+',' ',s.replace('’',"'").replace('‘',"'")).strip()
def ptext(p):return ''.join(p.xpath('.//w:t/text()',namespaces=NS))
def special(p):return {'footnotes':p.xpath('.//w:footnoteReference/@w:id',namespaces=NS),'instr':p.xpath('.//w:instrText/text()',namespaces=NS),'fld':len(p.xpath('.//w:fldChar',namespaces=NS)),'hyper':len(p.xpath('.//w:hyperlink',namespaces=NS)),'rtl':len(p.xpath('.//w:rtl',namespaces=NS)),'book':len(p.xpath('.//w:bookmarkStart|.//w:bookmarkEnd',namespaces=NS))}
def find_unique(ps,a,starts=False):
 a=norm(a);h=[]
 for i,p in enumerate(ps):
  t=norm(ptext(p));
  if (t.startswith(a) if starts else a in t):h.append((i,p))
 if len(h)!=1:raise RuntimeError(f'anchor {a[:70]!r}: {len(h)} hits')
 return h[0]
def first_rpr(p):
 r=p.find(f'{{{W}}}r');return deepcopy(r.find(f'{{{W}}}rPr')) if r is not None and r.find(f'{{{W}}}rPr') is not None else None
def clear(p):
 pp=p.find(f'{{{W}}}pPr')
 for c in list(p):
  if c is not pp:p.remove(c)
def add(p,t,rpr=None):
 r=etree.Element(f'{{{W}}}r');
 if rpr is not None:r.append(deepcopy(rpr))
 x=etree.SubElement(r,f'{{{W}}}t');x.text=t
 if t.startswith(' ') or t.endswith(' '):x.set('{http://www.w3.org/XML/1998/namespace}space','preserve')
 p.append(r)
def replace_span(p,a,r):
 before=special(p);nodes=p.xpath('.//w:t',namespaces=NS);vals=[x.text or '' for x in nodes];full=''.join(vals)
 cand=[a,a.replace("'",'’'),a.replace('’',"'")];hits=[(full.find(x),x) for x in cand if full.find(x)>=0]
 if not hits:
  if norm(r) in norm(full):return 'ALREADY_SATISFIED'
  raise RuntimeError('span missing: '+a[:70])
 pos,actual=hits[0];end=pos+len(actual);starts=[];c=0
 for v in vals:starts.append(c);c+=len(v)
 fi=next(i for i,(st,v) in enumerate(zip(starts,vals)) if pos<st+len(v));li=next(i for i,(st,v) in enumerate(zip(starts,vals)) if end<=st+len(v))
 pre=vals[fi][:pos-starts[fi]];suf=vals[li][end-starts[li]:];nodes[fi].text=pre+r+(suf if fi==li else '')
 if fi!=li:
  for j in range(fi+1,li):nodes[j].text=''
  nodes[li].text=suf
 if special(p)!=before:raise RuntimeError('protected structure changed')
 return 'APPLIED'
def whole(p,r):
 s=special(p)
 if s['footnotes'] or s['instr'] or s['fld'] or s['hyper'] or s['rtl'] or s['book']:raise RuntimeError('unsafe whole replacement '+str(s))
 rp=first_rpr(p);clear(p);add(p,r,rp)
def fnruns(*pars):
 d={}
 for p in pars:
  for r in p.xpath('./w:r',namespaces=NS):
   ids=r.xpath('.//w:footnoteReference/@w:id',namespaces=NS)
   if ids:d[ids[0]]=deepcopy(r)
 return d
def apply(src,out):
 with ZipFile(src) as zin:
  doc=etree.fromstring(zin.read('word/document.xml'));body=doc.find('.//w:body',namespaces=NS);changed=False;res=[]
  R12="Vahyin inişiyle birlikte yazı, sözlü aktarımı tamamlayan daha düzenli bir kayıt aracı hâline gelmiştir. Hz. Peygamber'in vahiy kâtiplerini görevlendirmesi ve inen âyetleri yazdırması, özellikle Medine döneminde yazılı kaydın daha belirgin bir uygulamaya dönüştüğünü göstermektedir. Bununla birlikte Kur’an'ın aktarımında ezber, tilâvet ve yazı birlikte işleyen unsurlar olarak varlığını sürdürmüştür."
  ps=body.xpath('./w:p',namespaces=NS);h=[(i,p) for i,p in enumerate(ps) if norm(ptext(p))==norm(R12)]
  if h:
   i,p=h[0]
   if special(p)['footnotes']!=['19','20','21']:raise RuntimeError('F4-012 note mismatch')
   st='ALREADY_SATISFIED'
  else:
   i,p1=find_unique(ps,'Vahyin inişiyle birlikte yazının pozisyonu belirgin bir şekilde değişmeye başlamıştır.',True);i2,p2=find_unique(ps,'Kur’an vahyinin kitaplaşma serüveni, işte bu tarihsel ve kültürel dönüşüm içinde şekillenmiştir.',True);i3,p3=find_unique(ps,'Bu serüven Kur’an’ın ne salt sözlü ne de baştan itibaren tamamen yazılı bir metin olduğunu göstermektedir.',True)
   if [i,i2,i3]!=[i,i+1,i+2] or [special(p1)['footnotes'],special(p2)['footnotes'],special(p3)['footnotes']]!=[['19'],['20'],['21']]:raise RuntimeError('F4-012 cluster mismatch')
   fr=fnruns(p1,p2,p3);rp=first_rpr(p1);clear(p1);add(p1,"Vahyin inişiyle birlikte yazı, sözlü aktarımı tamamlayan daha düzenli bir kayıt aracı hâline gelmiştir. Hz. Peygamber'in vahiy kâtiplerini görevlendirmesi ve inen âyetleri yazdırması, özellikle Medine döneminde yazılı kaydın daha belirgin bir uygulamaya dönüştüğünü göstermektedir.",rp);p1.append(fr['19']);p1.append(fr['20']);add(p1," Bununla birlikte Kur’an'ın aktarımında ezber, tilâvet ve yazı birlikte işleyen unsurlar olarak varlığını sürdürmüştür.",rp);p1.append(fr['21']);body.remove(p2);body.remove(p3);changed=True;st='STRUCTURALLY_APPLIED'
  res.append(('F4-012',i,st))
  ps=body.xpath('./w:p',namespaces=NS);i,p=find_unique(ps,'Kur’an vahyinin ne zaman kayda geçirilmeye başlandığı hususunda kesin ve tarihsel olarak net bir bilgiye sahip değiliz.',True);a="Bu rivâyetler, Mekkî dönemde de vahyin yazıyla kaydedildiğine işaret etmektedir. Bununla birlikte mevcut bilgiler, bu kayıt faaliyetinin kapsamını, sürekliliğini ve bütün Mekkî vahyi içerip içermediğini kesin biçimde belirlemeye elverişli değildir";st='ALREADY_SATISFIED' if norm(ptext(p)).endswith(norm(a+'.')) else replace_span(p,a,a+'.');changed|=st=='APPLIED';res.append(('F4-013',i,st))
  ps=body.xpath('./w:p',namespaces=NS);i,p=find_unique(ps,'Medine dönemine gelindiğinde ise durum daha farklı bir görünüm arz etmiştir.',True);st16=replace_span(p,'Bu ve bunun gibi rivâyetler, Medine döneminde vahyin yazıyla tespitinin düzenli bir uygulama hâline geldiğini açıkça ortaya koymaktadır.','Bu rivâyetler, Medine döneminde vahyin yazıyla kaydedilmesinin düzenli bir uygulama olarak aktarıldığına işaret etmektedir.');changed|=st16=='APPLIED';old="İkinci olarak vahiy henüz tamamlanmadığından Kur’an metninin nihai şeklini henüz almamış olması ve bazı âyetlerin neshedilme ihtimalinin bulunmasıdır.  Üçüncü olarak sûrelerin tertibinin nüzûl sırasına göre olmaması ve vahyin inişinin devam etmesidir.(bu maddeyi ikinci maddeye yedirecektiniz)";new="İkinci olarak vahyin inişi henüz tamamlanmadığından Kur’an metni nihai şeklini almamış; bazı âyetlerin neshedilmesi ve sûrelerin tertibine ilişkin düzenlemelerin devam etmesi ihtimali bulunmuştur.";st14=replace_span(p,old,new);changed|=st14=='APPLIED'
  if special(p)['footnotes']!=['24','25','26']:raise RuntimeError('F4-014/016 note mismatch')
  res.extend([('F4-014',i,st14),('F4-016',i,st16)])
  R15="Rivâyetlerdeki dağınık bilgiler, yazılı vahiy malzemesinin muhafazası konusunda farklı uygulamaların bulunmuş olabileceğini düşündürmektedir. Bazı nakiller yazılı metinlerin Hz. Peygamber'in yakın çevresinde muhafaza edildiğine, bazıları ise vahiy kâtipleri ve diğer sahâbîlerin ellerinde bulunan malzemelerin sonraki cem sırasında bir araya getirildiğine işaret etmektedir. Mevcut veriler, bütün yazılı malzemenin tek bir merkezde veya tek tip bir usulle muhafaza edildiğini kesin biçimde göstermemektedir."
  ps=body.xpath('./w:p',namespaces=NS);h=[(i,p) for i,p in enumerate(ps) if norm(ptext(p))==norm(R15)]
  if h:
   i,p=h[0]
   if special(p)['footnotes']!=['28','29','30']:raise RuntimeError('F4-015 note mismatch')
   st='ALREADY_SATISFIED'
  else:
   i,p1=find_unique(ps,'Nüzûl döneminde yazıya geçirilen vahiy metinlerinin nasıl muhafaza edildiği meselesi de üzerinde durulması gereken önemli bir konudur.',True);i2,p2=find_unique(ps,'İkinci görüş ise, vahiy metinlerinin, bunları yazan vahiy kâtiplerinin yanında kaldığı yönündedir.',True);i3,p3=find_unique(ps,'Her iki yaklaşım birlikte değerlendirildiğinde',True)
   if [i,i2,i3]!=[i,i+1,i+2] or [special(p1)['footnotes'],special(p2)['footnotes'],special(p3)['footnotes']]!=[['28','29'],['30'],[]]:raise RuntimeError('F4-015 cluster mismatch')
   fr=fnruns(p1,p2);rp=first_rpr(p1);clear(p1);add(p1,"Rivâyetlerdeki dağınık bilgiler, yazılı vahiy malzemesinin muhafazası konusunda farklı uygulamaların bulunmuş olabileceğini düşündürmektedir. Bazı nakiller yazılı metinlerin Hz. Peygamber'in yakın çevresinde muhafaza edildiğine, bazıları ise vahiy kâtipleri ve diğer sahâbîlerin ellerinde bulunan malzemelerin sonraki cem sırasında bir araya getirildiğine işaret etmektedir.",rp);p1.append(fr['28']);p1.append(fr['29']);p1.append(fr['30']);add(p1," Mevcut veriler, bütün yazılı malzemenin tek bir merkezde veya tek tip bir usulle muhafaza edildiğini kesin biçimde göstermemektedir.",rp);body.remove(p2);body.remove(p3);changed=True;st='STRUCTURALLY_APPLIED'
  res.append(('F4-015',i,st))
  R17="Hz. Peygamber'in vefatından sonra ortaya çıkan yeni şartlar, dağınık yazılı malzemenin resmî bir derleme içinde bir araya getirilmesi ihtiyacını gündeme getirmiştir. Hz. Ebû Bekir dönemindeki cem faaliyeti bu tarihsel bağlamda değerlendirilmelidir."
  ps=body.xpath('./w:p',namespaces=NS);h=[(i,p) for i,p in enumerate(ps) if norm(ptext(p))==norm(R17)]
  if h:i,p=h[0];st='ALREADY_SATISFIED'
  else:i,p=find_unique(ps,'Nüzûl döneminde vahyin kayıt altına alındığı açık olmakla birlikte bu kayıtların kitap şeklinde bir araya getirilmediği görülmektedir.',True);whole(p,R17);changed=True;st='APPLIED'
  res.append(('F4-017',i,st))
  if not changed:shutil.copyfile(src,out);return res
  xml=etree.tostring(doc,xml_declaration=True,encoding='UTF-8',standalone='yes')
  with ZipFile(out,'w') as zout:
   for info in zin.infolist():zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
  return res
if __name__=='__main__':
 for x in apply(Path(sys.argv[1]),Path(sys.argv[2])):print('\t'.join(map(str,x)))
