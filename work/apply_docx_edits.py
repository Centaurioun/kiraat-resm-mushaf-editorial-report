#!/usr/bin/env python3
from __future__ import annotations
from copy import deepcopy
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import re, sys, shutil

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
XML='http://www.w3.org/XML/1998/namespace'
NS={'w':W}

def norm(s:str)->str:
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')
    return re.sub(r'\s+',' ',s).strip()

def ptext(p): return ''.join(p.xpath('.//w:t/text()',namespaces=NS))

def find_unique_para(paras, anchor):
    na=norm(anchor); hits=[(i,p) for i,p in enumerate(paras) if na in norm(ptext(p))]
    if len(hits)!=1: raise RuntimeError(f'Anchor resolution failed: expected 1 hit, got {len(hits)} for {anchor[:80]!r}')
    return hits[0]

def special_summary(p):
    return {'footnotes':p.xpath('.//w:footnoteReference/@w:id',namespaces=NS),'instrText':p.xpath('.//w:instrText/text()',namespaces=NS),'fldChar':len(p.xpath('.//w:fldChar',namespaces=NS)),'hyperlink':len(p.xpath('.//w:hyperlink',namespaces=NS)),'rtl':len(p.xpath('.//w:rtl',namespaces=NS)),'bookmarks':len(p.xpath('.//w:bookmarkStart|.//w:bookmarkEnd',namespaces=NS))}

def replace_whole_paragraph(p,replacement,expected_footnote_ids=()):
    ss=special_summary(p)
    if ss['instrText'] or ss['fldChar'] or ss['hyperlink'] or ss['rtl'] or ss['bookmarks']: raise RuntimeError(f'Unsafe paragraph contains protected structures: {ss}')
    if list(map(str,expected_footnote_ids))!=ss['footnotes']: raise RuntimeError(f'Footnote mismatch expected={expected_footnote_ids} actual={ss["footnotes"]}')
    footnote_runs=[deepcopy(r) for r in p.xpath('./w:r',namespaces=NS) if r.xpath('.//w:footnoteReference',namespaces=NS)]
    first_run=p.find(f'{{{W}}}r'); first_rpr=deepcopy(first_run.find(f'{{{W}}}rPr')) if first_run is not None and first_run.find(f'{{{W}}}rPr') is not None else None
    ppr=p.find(f'{{{W}}}pPr')
    for ch in list(p):
        if ch is not ppr: p.remove(ch)
    r=etree.Element(f'{{{W}}}r');
    if first_rpr is not None: r.append(first_rpr)
    t=etree.SubElement(r,f'{{{W}}}t'); t.text=replacement; p.append(r)
    for fr in footnote_runs: p.append(fr)

def replace_literal_span(p, anchor, replacement):
    # Exact text-span replacement across w:t nodes; does not touch field instruction text or non-text runs.
    nodes=p.xpath('.//w:t',namespaces=NS); vals=[n.text or '' for n in nodes]; full=''.join(vals)
    # try exact, then curly/straight apostrophe variants if necessary
    pos=full.find(anchor)
    if pos<0:
        variants={anchor.replace("'",'’'), anchor.replace('’',"'")}
        hits=[(full.find(v),v) for v in variants if full.find(v)>=0]
        if len(hits)!=1: raise RuntimeError(f'literal span not uniquely found for {anchor[:80]!r}')
        pos,actual=hits[0]; end=pos+len(actual)
    else: end=pos+len(anchor)
    # ensure desired state is not already present in same paragraph
    if replacement in full or replacement.replace("'",'’') in full: return 'ALREADY_SATISFIED'
    cur=0; first_i=last_i=None
    for i,v in enumerate(vals):
        nxt=cur+len(v)
        if first_i is None and pos < nxt: first_i=i
        if end <= nxt and last_i is None: last_i=i; break
        cur=nxt
    if first_i is None or last_i is None: raise RuntimeError('span-node mapping failed')
    starts=[]; c=0
    for v in vals: starts.append(c); c+=len(v)
    fi,li=first_i,last_i
    prefix=vals[fi][:pos-starts[fi]]
    suffix=vals[li][end-starts[li]:]
    nodes[fi].text=prefix+replacement+(suffix if fi==li else '')
    if fi!=li:
        for j in range(fi+1,li): nodes[j].text=''
        nodes[li].text=suffix
    return 'APPLIED'


def apply_f4_006(doc, paras):
    A = "Bu çalışma, Kur’an tarihinin bütün meselelerini ele almak yerine resm-i Osmânî ile kırâat rivâyeti arasındaki ilişkiye odaklanmaktadır. İnceleme sırasında erken dönem rivâyetleri, klasik âlimlerin değerlendirmeleri ve sonraki yorumlar mümkün olduğunca birbirinden ayrılmış; kaynakların farklı aktarımlar sunduğu konularda kesinlik derecesi korunmuştur."
    B = "Araştırmanın temel amacı, resm-i Osmânî'nin kırâatleri meydana getiren bağımsız bir kaynak olmadığını; buna karşılık rivâyetle sabit okuyuşların müşterek mushaf yazısıyla ilişkisini belirleyen tamamlayıcı bir ölçü olarak nasıl işlev gördüğünü ortaya koymaktır."
    C = "Kitap dört bölümden oluşmaktadır. Birinci bölüm resm-i Osmânî'nin tarihsel ve kavramsal zeminini, ikinci bölüm kırâat rivâyetinin aktarım yapısını, üçüncü bölüm resm ile kırâatlerin bağdaşma biçimlerini, dördüncü bölüm ise bu ilişkinin kırâatlerin değerlendirilmesi ve sonraki mushaf geleneğindeki yansımalarını ele almaktadır."
    # Idempotency: desired three replacements present and stale repeated plan paragraphs absent.
    texts=[ptext(p) for p in paras]
    stale_starts=[
      "Bu sınırlandırma, çalışmanın Kur’an tarihinin bütün meselelerini",
      "Bu sınırlandırma, çalışmanın Kur'an tarihinin bütün meselelerini",
      "Kaynak kullanımında rivâyetin varlığı ile ona yüklenen yorumun aynı düzlemde olmadığı gözetilmiştir.",
      "Kitabın literatüre sağlamayı hedeflediği katkı,",
      "Kitabın dört ana bölümü bu düşünsel ilerleyişe göre düzenlenmiştir.",
      "Birinci bölümde, İslâm öncesi Arap yazısından başlayarak",
      "İkinci bölümde, kırâatlerin rivâyet mantığı açıklanarak",
      "Üçüncü bölümde, ilk iki bölümde kurulan zemin",
      "Dördüncü bölümde ise kitabın ana problemi uygulama alanında incelenmekte;",
    ]
    if sum(norm(t)==norm(A) for t in texts)==1 and sum(norm(t)==norm(B) for t in texts)==1 and sum(norm(t)==norm(C) for t in texts)==1 and not any(any(norm(t).startswith(norm(st)) for st in stale_starts) for t in texts):
        return 'ALREADY_SATISFIED'

    # Locate exact semantic source paragraphs in CURRENT document.
    def start_unique(prefix):
        hits=[(i,p) for i,p in enumerate(paras) if norm(ptext(p)).startswith(norm(prefix))]
        if len(hits)!=1: raise RuntimeError(f'F4-006 expected one paragraph starting {prefix[:70]!r}, got {len(hits)}')
        return hits[0]
    i28,p28=start_unique("Araştırmanın kapsamı bu temel problemle sınırlıdır.")
    i29,p29=start_unique("Bu sınırlandırma, çalışmanın Kur’an tarihinin bütün meselelerini")
    i30,p30=start_unique("Çalışmanın son halkasında resm verilerinin kırâat vecihlerinin tespiti")
    i31,p31=start_unique("Yöntem bakımından kitap, tarihsel rivâyetlerin karşılaştırılması")
    i32,p32=start_unique("Araştırmanın kaynak zemini, mushaf tarihi ve cem-istinsah rivâyetlerini aktaran eserler")
    i33,p33=start_unique("Kaynak kullanımında rivâyetin varlığı ile ona yüklenen yorumun aynı düzlemde olmadığı gözetilmiştir.")
    i34,p34=start_unique("Kitabın literatüre sağlamayı hedeflediği katkı,")
    i35,p35=start_unique("Kitabın dört ana bölümü bu düşünsel ilerleyişe göre düzenlenmiştir.")
    i36,p36=start_unique("Birinci bölümde, İslâm öncesi Arap yazısından başlayarak")
    i37,p37=start_unique("İkinci bölümde, kırâatlerin rivâyet mantığı açıklanarak")
    i38,p38=start_unique("Üçüncü bölümde, ilk iki bölümde kurulan zemin")
    i39,p39=start_unique("Dördüncü bölümde ise kitabın ana problemi uygulama alanında incelenmekte;")
    if [i28,i29,i30,i31,i32,i33,i34,i35,i36,i37,i38,i39] != list(range(i28,i28+12)):
        raise RuntimeError('F4-006 source cluster is not contiguous in expected order')
    # Protected structures may exist only in the preserved unique paragraph p30 (footnote 7).
    for label,p in [('p28',p28),('p29',p29),('p33',p33),('p34',p34),('p35',p35),('p36',p36),('p37',p37),('p38',p38),('p39',p39)]:
        ss=special_summary(p)
        if ss['footnotes'] or ss['instrText'] or ss['fldChar'] or ss['hyperlink'] or ss['rtl'] or ss['bookmarks']:
            raise RuntimeError(f'F4-006 unsafe structural target {label}: {ss}')
    if special_summary(p30)['footnotes'] != ['7']:
        raise RuntimeError(f'F4-006 preserved unique p30 no longer has exactly footnote 7: {special_summary(p30)}')
    # Replace three retained paragraph shells to preserve paragraph properties/styles.
    replace_whole_paragraph(p28,A,[])
    replace_whole_paragraph(p34,B,[])
    replace_whole_paragraph(p35,C,[])
    # Remove only true repetition / superseded detailed plan; preserve p30, p31, p32 unchanged.
    body=doc.find('.//w:body',namespaces=NS)
    for doomed in [p29,p33,p36,p37,p38,p39]:
        body.remove(doomed)
    return 'STRUCTURALLY_APPLIED'

def apply(source:Path,out:Path):
    with ZipFile(source,'r') as zin:
        doc=etree.fromstring(zin.read('word/document.xml')); paras=doc.xpath('.//w:body/w:p',namespaces=NS); result=[]; changed=False
        whole_ops=[
          ('F4-001',"Resm-i Osmânî'ye uygunluk, klasik kırâat usûlünde temel ölçüler arasında anılmakla birlikte bu ölçünün tarihsel zemini ve uygulamadaki kapsamı çoğu zaman farklı bahisler içinde ele alınmaktadır.","Resm-i Osmânî'ye uygunluk, kırâat usûlünde okuyuşların değerlendirilmesinde dikkate alınan temel ölçülerden biridir. Bununla birlikte kırâatlerin aslî aktarım zemini telakki, müşâfehe, edâ ve isnada dayanan rivâyet geleneğidir. Bu kitap, sözlü aktarım ile mushaf yazısı arasındaki ilişkiyi, resm-i Osmânî'nin kırâatlerin rivâyeti ve kabulündeki işlevi bakımından incelemektedir.",[]),
          ('F4-002',"Eserin, resm-i mushaf'ı yalnız geçmişte teşekkül etmiş bir imlâ biçimi olarak indirgemeyip, kırâatlerin rivâyeti, mushaf yazımı ve çağdaş neşir geleneğiyle ilişkili bir ilim alanı olarak değerlendirmeye katkı sağlaması hedeflenmektedir.","Eserin, mushaf yazım geleneğini yalnız tarihsel bir imlâ biçimi olarak ele almakla yetinmeyip, resm-i mushaf ilminin kırâat rivâyeti ve çağdaş neşir geleneğiyle ilişkisini göstermeye katkı sağlaması hedeflenmektedir. Kaynaklarda ihtilaf bulunan meselelerde tarihsel veriler ile sonraki yorumlar birbirinden ayrılarak ihtiyatlı bir değerlendirme benimsenmiştir.",[]),
          ('F4-003',"Problemin tarihsel zemini, İslâm öncesi Arap yazısından nüzûl dönemindeki kayıt faaliyetlerine, oradan Kur'an'ın cem ve istinsah süreçlerine uzanmaktadır.","Problemin tarihsel zemini, İslâm öncesi Arap yazısından nüzûl dönemindeki kayıt faaliyetlerine, oradan cem ve istinsah süreçlerine uzanmaktadır. Vahyin yazıya geçirilmesi sözlü aktarımı tamamlayan bir kayıt işlevi görmüş; Hz. Ebû Bekir dönemindeki cem ile Hz. Osman dönemindeki istinsah farklı tarihsel şartlarda gerçekleştirilen iki ayrı uygulama olarak rivâyet edilmiştir. Kaynaklarda istinsah heyeti, mushafların sayısı ve gönderildikleri merkezler konusunda farklı aktarımlar bulunduğundan, bu sürecin ayrıntıları ihtiyatla değerlendirilmelidir.",['2']),
        ]
        for iid,a,rp,fids in whole_ops:
            repl_hits=[(i,p) for i,p in enumerate(paras) if norm(rp)==norm(ptext(p))]
            if len(repl_hits)==1: result.append((iid,repl_hits[0][0],'ALREADY_SATISFIED')); continue
            i,p=find_unique_para(paras,a); replace_whole_paragraph(p,rp,fids); result.append((iid,i,'APPLIED')); changed=True
        span_ops=[
          ('F4-004',"Çalışmada kırâatin aslî dayanağı, telakki ve müşâfehe yoluyla sürdürülen, okuyuş ve isnadla denetlenen rivâyet geleneği olarak kabul edilmektedir.","Çalışmada kırâatin aslî dayanağı, telakki ve müşâfehe yoluyla sürdürülen, edâ ve isnadla denetlenen rivâyet geleneği olarak kabul edilmektedir. Resm-i Osmânî ise bu sözlü aktarımın yerine geçen bağımsız bir kaynak değil, rivâyetle sabit okuyuşların müşterek mushaf yazısıyla ilişkisini gösteren tamamlayıcı bir ölçüdür."),
          ('F4-005',"Şehir mushafları arasında nakledilen sınırlı yazım farklılıkları, ortak mushaf otoritesinin bulunmadığını değil, aynı istinsah geleneği içinde bazı yazım farklılıklarının rivâyet edildiğini göstermektedir.","Şehir mushafları arasında nakledilen sınırlı yazım farklılıkları, müşterek mushaf otoritesi içinde farklı yazım rivâyetlerinin bulunabildiğini göstermektedir."),
        ]
        for iid,a,rp in span_ops:
            repl_hits=[(i,p) for i,p in enumerate(paras) if rp in ptext(p)]
            if len(repl_hits)==1: result.append((iid,repl_hits[0][0],'ALREADY_SATISFIED')); continue
            i,p=find_unique_para(paras,a)
            before_ss=special_summary(p)
            st=replace_literal_span(p,a,rp)
            after_ss=special_summary(p)
            if before_ss!=after_ss: raise RuntimeError(f'{iid}: protected structure changed {before_ss} -> {after_ss}')
            result.append((iid,i,st)); changed = changed or st=='APPLIED'
        # High-risk structural item F4-006. Recompute current body paragraphs after earlier edits.
        paras=doc.xpath('.//w:body/w:p',namespaces=NS)
        st6=apply_f4_006(doc,paras)
        # Locate the retained replacement A for stable logging after potential deletions.
        paras_after=doc.xpath('.//w:body/w:p',namespaces=NS)
        a6="Bu çalışma, Kur’an tarihinin bütün meselelerini ele almak yerine resm-i Osmânî ile kırâat rivâyeti arasındaki ilişkiye odaklanmaktadır. İnceleme sırasında erken dönem rivâyetleri, klasik âlimlerin değerlendirmeleri ve sonraki yorumlar mümkün olduğunca birbirinden ayrılmış; kaynakların farklı aktarımlar sunduğu konularda kesinlik derecesi korunmuştur."
        loc6=[i for i,p in enumerate(paras_after) if norm(ptext(p))==norm(a6)]
        if len(loc6)!=1: raise RuntimeError(f'F4-006 replacement location expected 1, got {loc6}')
        result.append(('F4-006',loc6[0],st6)); changed = changed or st6=='STRUCTURALLY_APPLIED'
        if not changed:
            shutil.copyfile(source,out)
            return result
        new_xml=etree.tostring(doc,xml_declaration=True,encoding='UTF-8',standalone='yes')
        out.parent.mkdir(parents=True,exist_ok=True)
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,new_xml if info.filename=='word/document.xml' else zin.read(info.filename))
    return result
if __name__=='__main__':
  for row in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,row)))
