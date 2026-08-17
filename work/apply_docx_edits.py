#!/usr/bin/env python3
from __future__ import annotations
from copy import deepcopy
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from lxml import etree
import re, sys, shutil

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}

def norm(s:str)->str:
    return re.sub(r'\s+',' ',s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')).strip()
def ptext(p): return ''.join(p.xpath('.//w:t/text()',namespaces=NS))
def special(p): return {'footnotes':p.xpath('.//w:footnoteReference/@w:id',namespaces=NS),'instr':p.xpath('.//w:instrText/text()',namespaces=NS),'fld':len(p.xpath('.//w:fldChar',namespaces=NS)),'hyper':len(p.xpath('.//w:hyperlink',namespaces=NS)),'rtl':len(p.xpath('.//w:rtl',namespaces=NS)),'book':len(p.xpath('.//w:bookmarkStart|.//w:bookmarkEnd',namespaces=NS))}
def find_unique(paras, anchor, starts=False):
    a=norm(anchor); hits=[]
    for i,p in enumerate(paras):
        t=norm(ptext(p)); ok=t.startswith(a) if starts else a in t
        if ok:hits.append((i,p))
    if len(hits)!=1: raise RuntimeError(f'expected unique anchor {anchor[:90]!r}, got {len(hits)}')
    return hits[0]
def first_rpr(p):
    r=p.find(f'{{{W}}}r'); return deepcopy(r.find(f'{{{W}}}rPr')) if r is not None and r.find(f'{{{W}}}rPr') is not None else None
def clear_runs(p):
    ppr=p.find(f'{{{W}}}pPr')
    for ch in list(p):
        if ch is not ppr: p.remove(ch)
def add_text_run(p, text, rpr=None):
    r=etree.Element(f'{{{W}}}r');
    if rpr is not None:r.append(deepcopy(rpr))
    t=etree.SubElement(r,f'{{{W}}}t')
    if text.startswith(' ') or text.endswith(' '): t.set('{http://www.w3.org/XML/1998/namespace}space','preserve')
    t.text=text; p.append(r)
def make_fn_run(fid):
    r=etree.Element(f'{{{W}}}r'); rpr=etree.SubElement(r,f'{{{W}}}rPr')
    rs=etree.SubElement(rpr,f'{{{W}}}rStyle'); rs.set(f'{{{W}}}val','FootnoteReference')
    ref=etree.SubElement(r,f'{{{W}}}footnoteReference'); ref.set(f'{{{W}}}id',str(fid)); return r
def replace_whole(p,repl, expected_footnotes=(), prefer_plain=False):
    s=special(p)
    if s['instr'] or s['fld'] or s['hyper'] or s['rtl'] or s['book']: raise RuntimeError(f'unsafe whole target {s}')
    if list(map(str,expected_footnotes)) != s['footnotes']: raise RuntimeError(f'footnote mismatch expected {expected_footnotes} got {s["footnotes"]}')
    old_fn={fid:deepcopy(r) for r in p.xpath('./w:r',namespaces=NS) for fid in r.xpath('.//w:footnoteReference/@w:id',namespaces=NS)}
    if prefer_plain:
        chosen=None
        for rr in p.xpath('./w:r',namespaces=NS):
            cols=rr.xpath('./w:rPr/w:color/@w:val',namespaces=NS)
            if not cols or cols[0].upper() in ('AUTO','000000'):
                rp=rr.find(f'{{{W}}}rPr'); chosen=deepcopy(rp) if rp is not None else None; break
        rpr=chosen
    else:
        rpr=first_rpr(p)
    clear_runs(p); add_text_run(p,repl,rpr)
    for fid in expected_footnotes:p.append(old_fn[str(fid)])
def replace_with_chunks_and_footnotes(p, chunks, expected_footnotes):
    s=special(p)
    if s['instr'] or s['fld'] or s['hyper'] or s['rtl'] or s['book']: raise RuntimeError(f'unsafe chunk target {s}')
    if s['footnotes'] != list(map(str,expected_footnotes)): raise RuntimeError(f'footnote mismatch {s["footnotes"]}')
    old_fn={fid:deepcopy(r) for r in p.xpath('./w:r',namespaces=NS) for fid in r.xpath('.//w:footnoteReference/@w:id',namespaces=NS)}
    rpr=first_rpr(p); clear_runs(p)
    for kind,val in chunks:
        if kind=='t':add_text_run(p,val,rpr)
        elif kind=='fn':p.append(old_fn.get(str(val),make_fn_run(val)))
        else:raise ValueError(kind)
def replace_span(p, anchor, repl):
    before=special(p); nodes=p.xpath('.//w:t',namespaces=NS); vals=[n.text or '' for n in nodes]; full=''.join(vals)
    candidates=[anchor,anchor.replace("'",'’'),anchor.replace('’',"'")]
    hits=[(full.find(c),c) for c in candidates if full.find(c)>=0]
    if not hits:
        if repl in full or repl.replace("'",'’') in full:return 'ALREADY_SATISFIED'
        raise RuntimeError(f'span not found: {anchor[:90]!r}')
    pos,actual=hits[0]; end=pos+len(actual)
    starts=[]; c=0
    for v in vals:starts.append(c); c+=len(v)
    fi=next(i for i,(st,v) in enumerate(zip(starts,vals)) if pos < st+len(v))
    li=next(i for i,(st,v) in enumerate(zip(starts,vals)) if end <= st+len(v))
    prefix=vals[fi][:pos-starts[fi]]; suffix=vals[li][end-starts[li]:]
    nodes[fi].text=prefix+repl+(suffix if fi==li else '')
    if fi!=li:
        for j in range(fi+1,li):nodes[j].text=''
        nodes[li].text=suffix
    if special(p)!=before: raise RuntimeError('protected structure changed in span replacement')
    return 'APPLIED'

def apply_f4_006(doc,paras):
    A="Bu çalışma, Kur’an tarihinin bütün meselelerini ele almak yerine resm-i Osmânî ile kırâat rivâyeti arasındaki ilişkiye odaklanmaktadır. İnceleme sırasında erken dönem rivâyetleri, klasik âlimlerin değerlendirmeleri ve sonraki yorumlar mümkün olduğunca birbirinden ayrılmış; kaynakların farklı aktarımlar sunduğu konularda kesinlik derecesi korunmuştur."
    B="Araştırmanın temel amacı, resm-i Osmânî'nin kırâatleri meydana getiren bağımsız bir kaynak olmadığını; buna karşılık rivâyetle sabit okuyuşların müşterek mushaf yazısıyla ilişkisini belirleyen tamamlayıcı bir ölçü olarak nasıl işlev gördüğünü ortaya koymaktır."
    C="Kitap dört bölümden oluşmaktadır. Birinci bölüm resm-i Osmânî'nin tarihsel ve kavramsal zeminini, ikinci bölüm kırâat rivâyetinin aktarım yapısını, üçüncü bölüm resm ile kırâatlerin bağdaşma biçimlerini, dördüncü bölüm ise bu ilişkinin kırâatlerin değerlendirilmesi ve sonraki mushaf geleneğindeki yansımalarını ele almaktadır."
    texts=[norm(ptext(p)) for p in paras]
    stale=["Bu sınırlandırma, çalışmanın Kur’an tarihinin bütün meselelerini","Kaynak kullanımında rivâyetin varlığı ile ona yüklenen yorumun aynı düzlemde olmadığı gözetilmiştir.","Kitabın literatüre sağlamayı hedeflediği katkı,","Kitabın dört ana bölümü bu düşünsel ilerleyişe göre düzenlenmiştir.","Birinci bölümde, İslâm öncesi Arap yazısından başlayarak","İkinci bölümde, kırâatlerin rivâyet mantığı açıklanarak","Üçüncü bölümde, ilk iki bölümde kurulan zemin","Dördüncü bölümde ise kitabın ana problemi uygulama alanında incelenmekte;"]
    if all(sum(t==norm(x) for t in texts)==1 for x in [A,B,C]) and not any(any(t.startswith(norm(s)) for s in stale) for t in texts):return 'ALREADY_SATISFIED'
    prefixes=["Araştırmanın kapsamı bu temel problemle sınırlıdır.","Bu sınırlandırma, çalışmanın Kur’an tarihinin bütün meselelerini","Çalışmanın son halkasında resm verilerinin kırâat vecihlerinin tespiti","Yöntem bakımından kitap, tarihsel rivâyetlerin karşılaştırılması","Araştırmanın kaynak zemini, mushaf tarihi ve cem-istinsah rivâyetlerini aktaran eserler","Kaynak kullanımında rivâyetin varlığı ile ona yüklenen yorumun aynı düzlemde olmadığı gözetilmiştir.","Kitabın literatüre sağlamayı hedeflediği katkı,","Kitabın dört ana bölümü bu düşünsel ilerleyişe göre düzenlenmiştir.","Birinci bölümde, İslâm öncesi Arap yazısından başlayarak","İkinci bölümde, kırâatlerin rivâyet mantığı açıklanarak","Üçüncü bölümde, ilk iki bölümde kurulan zemin","Dördüncü bölümde ise kitabın ana problemi uygulama alanında incelenmekte;"]
    hits=[find_unique(paras,x,starts=True) for x in prefixes]; inds=[i for i,_ in hits]
    if inds!=list(range(inds[0],inds[0]+12)):raise RuntimeError('F4-006 cluster no longer contiguous')
    ps=[p for _,p in hits]
    if special(ps[2])['footnotes']!=['7']:raise RuntimeError('F4-006 preserved footnote 7 mismatch')
    for j in [0,1,5,6,7,8,9,10,11]:
        s=special(ps[j]);
        if any([s['footnotes'],s['instr'],s['fld'],s['hyper'],s['rtl'],s['book']]):raise RuntimeError(f'unsafe F4-006 target {j} {s}')
    replace_whole(ps[0],A); replace_whole(ps[6],B); replace_whole(ps[7],C)
    body=doc.find('.//w:body',namespaces=NS)
    for j in [1,5,8,9,10,11]:body.remove(ps[j])
    return 'STRUCTURALLY_APPLIED'

def apply(src:Path,out:Path):
  with ZipFile(src) as zin:
    doc=etree.fromstring(zin.read('word/document.xml')); result=[]; changed=False
    paras=doc.xpath('.//w:body/w:p',namespaces=NS)
    whole=[
      ('F4-001',"Resm-i Osmânî'ye uygunluk, klasik kırâat usûlünde temel ölçüler arasında anılmakla birlikte bu ölçünün tarihsel zemini ve uygulamadaki kapsamı çoğu zaman farklı bahisler içinde ele alınmaktadır.","Resm-i Osmânî'ye uygunluk, kırâat usûlünde okuyuşların değerlendirilmesinde dikkate alınan temel ölçülerden biridir. Bununla birlikte kırâatlerin aslî aktarım zemini telakki, müşâfehe, edâ ve isnada dayanan rivâyet geleneğidir. Bu kitap, sözlü aktarım ile mushaf yazısı arasındaki ilişkiyi, resm-i Osmânî'nin kırâatlerin rivâyeti ve kabulündeki işlevi bakımından incelemektedir.",[]),
      ('F4-002',"Eserin, resm-i mushaf'ı yalnız geçmişte teşekkül etmiş bir imlâ biçimi olarak indirgemeyip, kırâatlerin rivâyeti, mushaf yazımı ve çağdaş neşir geleneğiyle ilişkili bir ilim alanı olarak değerlendirmeye katkı sağlaması hedeflenmektedir.","Eserin, mushaf yazım geleneğini yalnız tarihsel bir imlâ biçimi olarak ele almakla yetinmeyip, resm-i mushaf ilminin kırâat rivâyeti ve çağdaş neşir geleneğiyle ilişkisini göstermeye katkı sağlaması hedeflenmektedir. Kaynaklarda ihtilaf bulunan meselelerde tarihsel veriler ile sonraki yorumlar birbirinden ayrılarak ihtiyatlı bir değerlendirme benimsenmiştir.",[]),
      ('F4-003',"Problemin tarihsel zemini, İslâm öncesi Arap yazısından nüzûl dönemindeki kayıt faaliyetlerine, oradan Kur'an'ın cem ve istinsah süreçlerine uzanmaktadır.","Problemin tarihsel zemini, İslâm öncesi Arap yazısından nüzûl dönemindeki kayıt faaliyetlerine, oradan cem ve istinsah süreçlerine uzanmaktadır. Vahyin yazıya geçirilmesi sözlü aktarımı tamamlayan bir kayıt işlevi görmüş; Hz. Ebû Bekir dönemindeki cem ile Hz. Osman dönemindeki istinsah farklı tarihsel şartlarda gerçekleştirilen iki ayrı uygulama olarak rivâyet edilmiştir. Kaynaklarda istinsah heyeti, mushafların sayısı ve gönderildikleri merkezler konusunda farklı aktarımlar bulunduğundan, bu sürecin ayrıntıları ihtiyatla değerlendirilmelidir.",['2'])]
    for iid,a,r,fns in whole:
      ps=doc.xpath('.//w:body/w:p',namespaces=NS); exact=[(i,p) for i,p in enumerate(ps) if norm(ptext(p))==norm(r)]
      if len(exact)==1:result.append((iid,exact[0][0],'ALREADY_SATISFIED'));continue
      i,p=find_unique(ps,a);replace_whole(p,r,fns);result.append((iid,i,'APPLIED'));changed=True
    spans=[
      ('F4-004',"Çalışmada kırâatin aslî dayanağı, telakki ve müşâfehe yoluyla sürdürülen, okuyuş ve isnadla denetlenen rivâyet geleneği olarak kabul edilmektedir.","Çalışmada kırâatin aslî dayanağı, telakki ve müşâfehe yoluyla sürdürülen, edâ ve isnadla denetlenen rivâyet geleneği olarak kabul edilmektedir. Resm-i Osmânî ise bu sözlü aktarımın yerine geçen bağımsız bir kaynak değil, rivâyetle sabit okuyuşların müşterek mushaf yazısıyla ilişkisini gösteren tamamlayıcı bir ölçüdür."),
      ('F4-005',"Şehir mushafları arasında nakledilen sınırlı yazım farklılıkları, ortak mushaf otoritesinin bulunmadığını değil, aynı istinsah geleneği içinde bazı yazım farklılıklarının rivâyet edildiğini göstermektedir.","Şehir mushafları arasında nakledilen sınırlı yazım farklılıkları, müşterek mushaf otoritesi içinde farklı yazım rivâyetlerinin bulunabildiğini göstermektedir.")]
    for iid,a,r in spans:
      ps=doc.xpath('.//w:body/w:p',namespaces=NS); rh=[(i,p) for i,p in enumerate(ps) if norm(r) in norm(ptext(p))]
      if len(rh)==1:result.append((iid,rh[0][0],'ALREADY_SATISFIED'));continue
      i,p=find_unique(ps,a);st=replace_span(p,a,r);result.append((iid,i,st));changed|=st=='APPLIED'
    ps=doc.xpath('.//w:body/w:p',namespaces=NS);st=apply_f4_006(doc,ps);changed|=st=='STRUCTURALLY_APPLIED';result.append(('F4-006',None,st))

    R7="Bu ilişkinin nasıl kurulduğunu açıklayabilmek için önce resm-i Osmânî'nin ortaya çıktığı tarihsel ve kavramsal zemini belirlemek gerekir. Birinci bölüm bu zemini incelemektedir."
    ps=doc.xpath('.//w:body/w:p',namespaces=NS);rh=[(i,p) for i,p in enumerate(ps) if norm(ptext(p))==norm(R7)]
    if len(rh)==1:result.append(('F4-007',rh[0][0],'ALREADY_SATISFIED'))
    else:
      i,p=find_unique(ps,"Bu yapı içinde araştırmanın temel sorusu, yazı ile sözlü rivâyetten hangisinin üstün olduğu değildir.",starts=True);replace_whole(p,R7);result.append(('F4-007',i,'APPLIED'));changed=True

    R8_full=("İslâm öncesi Arap toplumunda yazının kullanımına ilişkin bilgiler aynı kesinlik düzeyinde değildir. Şiirlerin Kâbe'ye asıldığına dair aktarımlar edebî gelenekte yer almakla birlikte tarihsel değeri konusunda ihtiyat gerektirir. Buna karşılık bazı kişilerin yazıyı bildiğine ve yazının pratik ihtiyaçlarda kullanıldığına ilişkin veriler, yazının tamamen bilinmeyen bir araç olmadığını göstermektedir. Hz. Peygamber’in dedesi Abdülmuttalib’e ait olduğu söylenen ve bir alacak kaydı içeren deri parçasının daha sonra Abbâsî halifesi Me’mûn’un özel mülkü arasında bulunduğuna dair rivâyet bu tür örneklerden biridir. İslâm öncesi Arapların yazıya “bismikellâhümme” ifadesiyle başladıklarına dair nakil de yazıya ilişkin belirli kalıp ve geleneklerin aktarıldığını göstermektedir. Bu nedenle dönem, yazının toplumun tamamına yayılmadığı fakat belirli çevrelerde işlevsel biçimde kullanıldığı bir safha olarak değerlendirilmelidir.")
    ps=doc.xpath('.//w:body/w:p',namespaces=NS); rh=[(i,p) for i,p in enumerate(ps) if norm(ptext(p))==norm(R8_full)]
    if len(rh)==1:result.append(('F4-008',rh[0][0],'ALREADY_SATISFIED'))
    else:
      i,p=find_unique(ps,"Cahiliye döneminde panayırlarda okunan ve büyük beğeni toplayan şiirlerin Kâbe duvarlarına asıldığına dair gelen rivâyetler",starts=True)
      chunks=[('t',"İslâm öncesi Arap toplumunda yazının kullanımına ilişkin bilgiler aynı kesinlik düzeyinde değildir. Şiirlerin Kâbe'ye asıldığına dair aktarımlar edebî gelenekte yer almakla birlikte tarihsel değeri konusunda ihtiyat gerektirir. Buna karşılık bazı kişilerin yazıyı bildiğine ve yazının pratik ihtiyaçlarda kullanıldığına ilişkin veriler, yazının tamamen bilinmeyen bir araç olmadığını göstermektedir. Hz. Peygamber’in dedesi Abdülmuttalib’e ait olduğu söylenen ve bir alacak kaydı içeren deri parçasının daha sonra Abbâsî halifesi Me’mûn’un özel mülkü arasında bulunduğuna dair rivâyet bu tür örneklerden biridir."),('fn',15),('t'," İslâm öncesi Arapların yazıya “bismikellâhümme” ifadesiyle başladıklarına dair nakil de yazıya ilişkin belirli kalıp ve geleneklerin aktarıldığını göstermektedir."),('fn',16),('t'," Bu nedenle dönem, yazının toplumun tamamına yayılmadığı fakat belirli çevrelerde işlevsel biçimde kullanıldığı bir safha olarak değerlendirilmelidir.")]
      replace_with_chunks_and_footnotes(p,chunks,[15,16]);result.append(('F4-008',i,'APPLIED_WITH_CITATION_PRESERVATION'));changed=True

    ps=doc.xpath('.//w:body/w:p',namespaces=NS); i45,p45=find_unique(ps,"Kaynaklar İslâm öncesi dönemde Araplar arasında yazının sınırlı da olsa kullanıldığını",starts=True)
    st9=replace_span(p45,"otaya koymaktadır","ortaya koymaktadır");changed|=st9=='APPLIED'
    old10="Bu duruma dair en dikkat çekici örneklerden biri, ilk vahiy hadisesinden sonra yaşananların hakikatini anlamak üzere Hz. Hatice’nin Hz. Peygamber’i götürdüğü Varaka b. Nevfel’dir [(ö. 610 (?)]."
    new10="Bu duruma dair dikkat çekici örneklerden biri Varaka b. Nevfel'dir (ö. 610 [?])."
    st10=replace_span(p45,old10,new10);changed|=st10=='APPLIED';result.append(('F4-010',i45,st10))

    R11="Bütün bu veriler birlikte değerlendirildiğinde, İslâm öncesi Arabistan'da yazının bütünüyle bilinmeyen bir araç olmadığı, ancak kullanımının toplumun tamamına yayılmış düzenli bir sistem hâline de gelmediği anlaşılmaktadır. Yazı belirli idarî, ticarî ve kültürel çevrelerde kullanılmakta; sözlü aktarım ise toplumsal iletişim ve kültürel hafızada ağırlığını korumaktaydı. Kur’an vahyinin inmeye başlamasıyla yazının vahyin kaydı bakımından daha düzenli bir işlev üstlendiği görülmektedir."
    ps=doc.xpath('.//w:body/w:p',namespaces=NS)
    first_hits=[(i,p) for i,p in enumerate(ps) if norm(ptext(p)).startswith(norm("Bu farklı görüşler birlikte değerlendirildiğinde ortaya daha şu mutedil tablo çıkmaktadır:"))]
    if first_hits:
      if len(first_hits)!=1:raise RuntimeError('F4-011 first synthesis ambiguous')
      if any(special(first_hits[0][1]).values()):raise RuntimeError('F4-011 first synthesis unexpectedly protected')
      doc.find('.//w:body',namespaces=NS).remove(first_hits[0][1]);changed=True
    ps=doc.xpath('.//w:body/w:p',namespaces=NS); r11hits=[(i,p) for i,p in enumerate(ps) if norm(ptext(p))==norm(R11)]
    if len(r11hits)==1:st11='ALREADY_SATISFIED' if not first_hits else 'STRUCTURALLY_APPLIED'
    else:
      i50,p50=find_unique(ps,"Bütün bu veriler bir arada değerlendirildiğinde İslâm öncesi Arap toplumunda yazının hiç bilinmediğini söylemek mümkün değildir.",starts=True);replace_whole(p50,R11,prefer_plain=True);changed=True;st11='STRUCTURALLY_APPLIED';r11hits=[(i50,p50)]
    result.append(('F4-011',r11hits[0][0] if r11hits else None,st11))
    result.append(('F4-009',i45,'APPLIED_WITH_F4_011_MERGE' if st9=='APPLIED' or first_hits else 'ALREADY_SATISFIED'))

    if not changed:
      shutil.copyfile(src,out);return result
    xml=etree.tostring(doc,xml_declaration=True,encoding='UTF-8',standalone='yes')
    out.parent.mkdir(parents=True,exist_ok=True)
    with ZipFile(out,'w') as zout:
      for info in zin.infolist():zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
  return result

if __name__=='__main__':
  for row in apply(Path(sys.argv[1]),Path(sys.argv[2])):print('\t'.join(map(str,row)))
