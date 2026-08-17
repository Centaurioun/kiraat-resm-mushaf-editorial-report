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
def find(ps,a,starts=True):
 a=norm(a);h=[]
 for i,p in enumerate(ps):
  t=norm(txt(p));ok=t.startswith(a) if starts else a in t
  if ok:h.append((i,p))
 if len(h)!=1:raise RuntimeError(f'{a[:90]} hits={len(h)}')
 return h[0]
def first_rpr(p):
 for r in p.xpath('./w:r',namespaces=NS):
  if r.xpath('.//w:footnoteReference|.//w:rtl|.//w:vertAlign',namespaces=NS):continue
  cols=r.xpath('./w:rPr/w:color/@w:val',namespaces=NS)
  if cols and cols[0].upper() not in ('AUTO','000000'):continue
  rp=r.find(f'{{{W}}}rPr');return deepcopy(rp) if rp is not None else None
 r=p.find(f'{{{W}}}r');return deepcopy(r.find(f'{{{W}}}rPr')) if r is not None and r.find(f'{{{W}}}rPr') is not None else None
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
def chunks(p,parts,expected_fn,expected_rtl=0):
 sp=spec(p)
 if sp['fn']!=list(map(str,expected_fn)) or sp['instr'] or sp['fld'] or sp['hyper'] or sp['rtl']!=expected_rtl or sp['book']:raise RuntimeError('unsafe chunks '+str(sp))
 rp=first_rpr(p);fr=fnruns(p);rtl_runs=[deepcopy(r) for r in p.xpath('./w:r',namespaces=NS) if r.xpath('.//w:rtl',namespaces=NS)];clear(p)
 ri=0
 for k,v in parts:
  if k=='t':add(p,v,rp)
  elif k=='fn':p.append(fr[str(v)])
  elif k=='rtl':p.append(rtl_runs[ri]);ri+=1
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
def remove_if_present(body,prefix,expected_fn=()):
 ps=body.xpath('./w:p',namespaces=NS);a=norm(prefix);hits=[(i,p) for i,p in enumerate(ps) if norm(txt(p)).startswith(a)]
 if not hits:return False
 if len(hits)!=1:raise RuntimeError(f'remove {a[:70]} hits={len(hits)}')
 i,p=hits[0];sp=spec(p)
 if sp['fn']!=list(map(str,expected_fn)) or sp['instr'] or sp['fld'] or sp['hyper'] or sp['rtl'] or sp['book']:raise RuntimeError('unsafe removal '+str(sp))
 body.remove(p);return True
def apply(src,out):
 with ZipFile(src) as zin:
  d=etree.fromstring(zin.read('word/document.xml'));body=d.find('.//w:body',namespaces=NS);changed=False;res=[]
  R28='İstinsah kararının nasıl uygulandığını değerlendirebilmek için, çoğaltılan mushafların sayısı ve gönderildikleri merkezler üzerinde ayrıca durmak gerekir.'
  ps=body.xpath('./w:p',namespaces=NS);h=[(i,p) for i,p in enumerate(ps) if norm(txt(p))==norm(R28)]
  if h:i,p=h[0];st='ALREADY_SATISFIED'
  else:i,p=find(ps,'Hülasa, istinsah kararı, vahyin aslını değiştirme veya yeni bir metin oluşturma girişimi değildir.');whole(p,R28);changed=True;st='APPLIED'
  res.append(('F4-028',i,st))
  R29=("Hz. Osman döneminde çoğaltılan mushafların sayısı konusunda kaynaklarda farklı rivâyetler bulunmaktadır. Dânî, âlimlerin çoğunluğuna göre dört nüsha yazıldığını; bunlardan Kûfe, Basra ve Şam'a birer nüsha gönderildiğini, bir nüshanın da halifenin yanında kaldığını nakleder. Bunun yanında yedi nüsha görüşünü de aktarır. Diğer kaynaklarda beş, sekiz veya dokuz nüshadan söz eden farklı sayımlar da bulunmaktadır. Kevserî ise bir mushafın halifenin yanında bırakıldığını, beş mushafın da emsâr bölgelerine gönderildiğini belirtmektedir. Bu nedenle rivâyetlerden hareketle tek bir toplam sayıyı tartışmasız biçimde kesinleştirmek yerine, farklı nakilleri kendi bağlamları içinde değerlendirmek daha isabetlidir.")
  ps=body.xpath('./w:p',namespaces=NS);h=[(i,p) for i,p in enumerate(ps) if norm(txt(p))==norm(R29)]
  if h:
   i,p=h[0]
   if spec(p)['fn']!=['88']:raise RuntimeError('F4-029 note mismatch after prior application')
   st29='ALREADY_SATISFIED'
  else:
   i,p=find(ps,'Mevcut rivâyetler ışığında, Osmânî mushafları en kuvvetli ihtimalle şu şekilde tasnif etmek mümkündür:')
   chunks(p,[('t',"Hz. Osman döneminde çoğaltılan mushafların sayısı konusunda kaynaklarda farklı rivâyetler bulunmaktadır. Dânî, âlimlerin çoğunluğuna göre dört nüsha yazıldığını; bunlardan Kûfe, Basra ve Şam'a birer nüsha gönderildiğini, bir nüshanın da halifenin yanında kaldığını nakleder. Bunun yanında yedi nüsha görüşünü de aktarır. Diğer kaynaklarda beş, sekiz veya dokuz nüshadan söz eden farklı sayımlar da bulunmaktadır. Kevserî ise bir mushafın halifenin yanında bırakıldığını, beş mushafın da emsâr bölgelerine gönderildiğini belirtmektedir."),('fn',88),('rtl',None),('t',"Bu nedenle rivâyetlerden hareketle tek bir toplam sayıyı tartışmasız biçimde kesinleştirmek yerine, farklı nakilleri kendi bağlamları içinde değerlendirmek daha isabetlidir.")],[88],expected_rtl=1);changed=True;st29='STRUCTURALLY_APPLIED'
  removed=[]
  for pref in [
   'Günümüz araştırmacılarının önemli bir kısmı da bu altı mushaf görüşünü daha makul bulmaktadırlar.',
   'İstinsah edilen mushafların sayısı konusunda klasik kaynaklarda farklı rivâyetler yer almakla birlikte, rivâyetlerin mukayeseli değerlendirilmesi',
   'Kaynaklarda adı geçen muallimler, yukarıda adı geçen beş şehirle ilişkili görünmektedir.'
  ]:
   if remove_if_present(body,pref):removed.append(pref[:30]);changed=True
  if removed:st29='STRUCTURALLY_APPLIED'
  res.append(('F4-029',i,st29))
  ps=body.xpath('./w:p',namespaces=NS);i,p=find(ps,'Mushafların sayıları arasındaki farkları konu edinen rivâyetlere bakıldığında genellikle Mekke, Medine, Basra, Kûfe ve Şam mushafları')
  old30="Ebû Şâme (ö. 665/1276), Ebû Ali el-Ahvâzî’nin (ö. 446/1055) Yemen ve Bahreyn mushafları hakkında “Ne bunlara dair bir haber işittik ne de izlerine rastladık.” dediğini nakleder."
  new30="Ebû Şâme (ö. 665/1267), Ebû Ali el-Ahvâzî'nin Yemen ve Bahreyn mushafları hakkında “Ne bunlara dair bir haber işittik ne de izlerine rastladık.” dediğini nakleder."
  st=span(p,old30,new30);changed|=st=='APPLIED';res.append(('F4-030',i,st))
  ps=body.xpath('./w:p',namespaces=NS);i,p=find(ps,'Öte yandan istinsah edilen mushafların yalnız başına gönderilmediği, her biriyle birlikte bir kırâat mualliminin gönderildiği bilinmektedir.')
  st=span(p,"Amr b. Kays (ö. ?) ise Basra’ya gönderilmiştir.","Amr b. Kays ise Basra'ya gönderilmiştir.");changed|=st=='APPLIED';res.append(('F4-031',i,st))
  R32=("Çağdaş araştırmacılar da mushafların sayısı ve gönderildikleri merkezler konusunda klasik rivâyetleri farklı ölçütlerle değerlendirmişlerdir. Zürkânî, Subhî es-Sâlih, Mustafa el-A‘zamî, Muhammed Hamîdullah (ö. 2002), Muhsin Demirci, Suat Yıldırım ve Mehmet Dağ'ın değerlendirmelerinde özellikle erken rivâyetler, şehir mushaflarına nispet edilen yazım farklılıkları ve dağıtım merkezleri üzerinde durulmaktadır. Bununla birlikte bu çalışmaların tamamının tek bir sayı veya aynı gerekçelendirme üzerinde birleştiği söylenmemelidir.")
  ps=body.xpath('./w:p',namespaces=NS);h=[(i,p) for i,p in enumerate(ps) if norm(txt(p))==norm(R32)]
  if h:i,p=h[0];st32='ALREADY_SATISFIED'
  else:i,p=find(ps,'Osmânî mushafların sayısı hususunda çağdaş araştırmacıların vardığı sonuçlar bireysel kanaatlerin ötesine geçerek');whole(p,R32);changed=True;st32='APPLIED'
  ps=body.xpath('./w:p',namespaces=NS);i2,p2=find(ps,'Suat Yıldırım da mushaf sayısı meselesini kırâat farklılıkları bağlamında ele alır')
  oldend='Böylece altı mushaf görüşü, farklı disipliner yaklaşımların kesişiminde ortak bir kanaat hâline gelmektedir.'
  newend='Bu çalışmaların değerlendirme ölçütleri ve vardıkları sonuçlar farklılaştığından, çağdaş literatürü tek bir mushaf sayısı etrafında birleşen ortak bir görüş olarak sunmak isabetli değildir.'
  stend=span(p2,oldend,newend);changed|=stend=='APPLIED'
  if stend=='APPLIED':st32='APPLIED'
  res.append(('F4-032',i,st32))
  if not changed:shutil.copyfile(src,out);return res
  xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
  with ZipFile(out,'w') as zout:
   for info in zin.infolist():zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
  return res
if __name__=='__main__':
 for r in apply(Path(sys.argv[1]),Path(sys.argv[2])):print('\t'.join(map(str,r)))
