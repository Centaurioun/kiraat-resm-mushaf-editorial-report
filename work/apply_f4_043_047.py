#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from copy import deepcopy
import shutil,sys
from apply_docx_edits import W,NS,norm,ptext,special,first_rpr,replace_span,replace_whole,add_text_run

def find(ps,a):
 h=[(i,p) for i,p in enumerate(ps) if norm(ptext(p)).startswith(norm(a))]
 if len(h)!=1: raise RuntimeError(f'anchor {a!r}: {len(h)} hits')
 return h[0]

def apply(src,out):
 with ZipFile(src) as zin:
  d=etree.fromstring(zin.read('word/document.xml'));body=d.find('.//w:body',namespaces=NS);changed=False;res=[];ps=body.xpath('./w:p',namespaces=NS)
  i,p=find(ps,'Bu kurallar şunlardır: harf düşmesi (hazf)')
  s=replace_span(p,'Bu tespit Osman mushaflarının hazırlanışında yazı ile okuyuş arasında bilinçli bir uyum gözetildiğini ortaya koymaktadır.',"Bu örnekler, bazı mushaf yazımlarının rivâyet yoluyla sabit birden fazla okuyuşla bağdaşabildiğini göstermektedir. Bununla birlikte her yazım özelliğinin doğrudan kırâat farklılıklarını korumak amacıyla ortaya çıktığı söylenemez; erken Arap yazı geleneği ile kırâatlerin resmle ilişkisi ayrı ayrı değerlendirilmelidir.");changed|=s=='APPLIED';res.append(('F4-043',i,s))
  R44="Hazf, lafızda bulunan bazı harflerin mushaf yazısında gösterilmemesidir. Bu özellik resm-i Osmânî'de düzenli biçimde görülen yazım uygulamalarından biridir. Bununla birlikte bütün hazf örneklerinin aynı sebeple ortaya çıktığı veya doğrudan kırâat farklılığını koruma amacı taşıdığı söylenemez. Bazı örnekler erken yazı geleneğiyle açıklanırken bazı yazımlar rivâyetle sabit birden fazla okuyuşla bağdaşabilmektedir."
  h=[(j,q) for j,q in enumerate(ps) if norm(ptext(q))==norm(R44)]
  if h:i44,p44=h[0];s44='ALREADY_SATISFIED'
  else:i44,p44=find(ps,'Resm-i Osmânî’nin temel yazım özelliklerinden biridir.');replace_whole(p44,R44,[145]);changed=True;s44='APPLIED'
  i2,p2=find(ps,'Med harflerinin hazfi:');old="Sonuç olarak hazf, resm-i Osmânî’nin en yaygın, işlevsel ve kırâatlerle yakından ilişkili kuralıdır. Hazf, doğrudan kırâat amacı taşımasa da, özellikle bazı örneklerde Osmânî yazımın tek metinde çoklu okuyuşu koruma kabiliyeti açık biçimde görülür.";new="Bu örnekler, hazfın resm-i Osmânî'de yaygın bir yazım özelliği olduğunu ve bazı durumlarda farklı kırâatlerle bağdaşabildiğini göstermektedir."
  if norm(new) in norm(ptext(p2)):s2='ALREADY_SATISFIED'
  else:s2=replace_span(p2,old,'');add_text_run(p2,' '+new,first_rpr(p2));changed=True
  res.append(('F4-044',i44,'APPLIED' if s44=='APPLIED' or s2=='APPLIED' else 'ALREADY_SATISFIED'))
  i,p=find(ps,"Resm-i Osmânî'nin temel yazım kurallarından biri olup bir harfin yerine başka bir harfin yazılması demektir.")
  s=replace_span(p,"Ca’berî (ö. 832/1428 ölüm tarihleri tekrar gözden geçirilmeli.), resm kurallarını sıralarken ibdâli müstakil bir başlık altında ele almış ve bunun erken yazı geleneğiyle ilişkili olduğunu belirtmiştir.","Ca‘berî (ö. 732/1332), resm kurallarını sıralarken ibdâli müstakil bir başlık altında ele almış ve bunun erken yazı geleneğiyle ilişkili olduğunu belirtmiştir.");changed|=s=='APPLIED';res.append(('F4-045',i,s))
  i,p=find(ps,'Hemze bazen hiç yazılmamış,')
  s=replace_span(p,"Hemzenin erken dönem mushaflarında sıkça görülmemesi, büyük ölçüde o günkü Arap yazısının yapısından veya yazıyı sade tutma yatkınlığından ya da henüz işaret sisteminin gelişmemiş olmasından kaynaklandığı belirtilmektedir. Bununla birlikte hemzenin kırâat ile ilişkisi zayıf olarak değerlendirilmiştir.","Hemzenin erken mushaflarda bugünkü imlâdaki biçimiyle her zaman ayrı ve düzenli bir işaretle gösterilmemesi, erken Arap yazısının imlâ ve işaretleme uygulamaları çerçevesinde değerlendirilmelidir. Hemze kimi kelimelerde med harfleriyle temsil edilmiş, kimi yerlerde ise yazıda ayrıca gösterilmemiştir. Bu özellik tek başına belirli bir kırâati ortaya çıkarmaz; okuyuşun nasıl icra edildiği rivâyet ve edâ yoluyla bilinmektedir.");changed|=s=='APPLIED';res.append(('F4-046',i,s))
  i,p=find(ps,'Ziyâde,')
  if 'Bakara sûresinin 269. âyetindeki' in ptext(p) and 'fonetik zorunluluktan dolayı' not in ptext(p):s='ALREADY_SATISFIED'
  else:
   sp=special(p)
   if sp['footnotes']!=['169','170','171','172'] or sp['rtl']!=3:raise RuntimeError('F4-047 protected inventory mismatch')
   runs=p.xpath('./w:r',namespaces=NS);m171=next(r for r in runs if r.xpath('.//w:footnoteReference/@w:id',namespaces=NS)==['171']);m172=deepcopy(next(r for r in runs if r.xpath('.//w:footnoteReference/@w:id',namespaces=NS)==['172']));arab={''.join(r.xpath('.//w:t/text()',namespaces=NS)):deepcopy(r) for r in runs if ''.join(r.xpath('.//w:t/text()',namespaces=NS)) in ['أُوْلوُا','سَأُوْرِيكُمْ','بِأَيْيْدٍ']}
   children=list(p);pos=children.index(m171)
   for c in children[pos+1:]:p.remove(c)
   rp=first_rpr(p);add_text_run(p,' Ziyâdeye örnek olarak Bakara sûresinin 269. âyetindeki ',rp);p.append(arab['أُوْلوُا']);add_text_run(p,' lafzında yer alan vav zikredilmiştir. ',rp);p.append(arab['سَأُوْرِيكُمْ']);add_text_run(p,' (el-Enbiyâ 21/37) kelimesindeki bazı harfler ile ',rp);p.append(arab['بِأَيْيْدٍ']);add_text_run(p,' (ez-Zâriyât 51/47) kelimesindeki yâ da resm kaynaklarında ziyâde başlığı altında ele alınan örnekler arasındadır. Bazı kaynaklarda bu tür ziyâdeler anlam merkezli yorumlarla da açıklanmış olmakla birlikte, bu yorumlar yazımın zorunlu tarihsel sebebi olarak sunulmamalıdır.',rp);p.append(m172);changed=True;s='APPLIED'
  res.append(('F4-047',i,s))
  if not changed:shutil.copyfile(src,out);return res
  xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
  with ZipFile(out,'w') as zout:
   for info in zin.infolist():zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
  return res
if __name__=='__main__':
 for r in apply(Path(sys.argv[1]),Path(sys.argv[2])):print('\t'.join(map(str,r)))
