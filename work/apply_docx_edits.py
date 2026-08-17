#!/usr/bin/env python3
from __future__ import annotations
from copy import deepcopy
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import re, sys

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
XML='http://www.w3.org/XML/1998/namespace'
NS={'w':W}

def norm(s:str)->str:
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')
    return re.sub(r'\s+',' ',s).strip()

def ptext(p):
    return ''.join(p.xpath('.//w:t/text()',namespaces=NS))

def find_unique_para(paras, anchor):
    na=norm(anchor)
    hits=[(i,p) for i,p in enumerate(paras) if na in norm(ptext(p))]
    if len(hits)!=1:
        raise RuntimeError(f'Anchor resolution failed: expected 1 hit, got {len(hits)} for {anchor[:80]!r}')
    return hits[0]

def special_summary(p):
    return {
        'footnotes':p.xpath('.//w:footnoteReference/@w:id',namespaces=NS),
        'instrText':p.xpath('.//w:instrText/text()',namespaces=NS),
        'fldChar':len(p.xpath('.//w:fldChar',namespaces=NS)),
        'hyperlink':len(p.xpath('.//w:hyperlink',namespaces=NS)),
        'rtl':len(p.xpath('.//w:rtl',namespaces=NS)),
        'bookmarks':len(p.xpath('.//w:bookmarkStart|.//w:bookmarkEnd',namespaces=NS)),
    }

def replace_whole_paragraph(p, replacement, expected_footnote_ids=()):
    ss=special_summary(p)
    if ss['instrText'] or ss['fldChar'] or ss['hyperlink'] or ss['rtl'] or ss['bookmarks']:
        raise RuntimeError(f'Unsafe paragraph contains protected structures: {ss}')
    if list(map(str,expected_footnote_ids)) != ss['footnotes']:
        raise RuntimeError(f'Footnote mismatch. expected={expected_footnote_ids} actual={ss["footnotes"]}')
    footnote_runs=[]
    for r in p.xpath('./w:r',namespaces=NS):
        if r.xpath('.//w:footnoteReference',namespaces=NS):
            footnote_runs.append(deepcopy(r))
    first_run=p.find(f'{{{W}}}r')
    first_rpr=deepcopy(first_run.find(f'{{{W}}}rPr')) if first_run is not None and first_run.find(f'{{{W}}}rPr') is not None else None
    ppr=p.find(f'{{{W}}}pPr')
    for ch in list(p):
        if ch is not ppr:
            p.remove(ch)
    r=etree.Element(f'{{{W}}}r')
    if first_rpr is not None:
        r.append(first_rpr)
    t=etree.SubElement(r,f'{{{W}}}t')
    if replacement[:1].isspace() or replacement[-1:].isspace() or '  ' in replacement:
        t.set(f'{{{XML}}}space','preserve')
    t.text=replacement
    p.append(r)
    for fr in footnote_runs:
        p.append(fr)

def apply(source:Path, out:Path):
    with ZipFile(source,'r') as zin:
        doc=etree.fromstring(zin.read('word/document.xml'))
        paras=doc.xpath('.//w:body/w:p',namespaces=NS)
        ops=[
            {'id':'F4-001','anchor':"Resm-i Osmânî'ye uygunluk, klasik kırâat usûlünde temel ölçüler arasında anılmakla birlikte bu ölçünün tarihsel zemini ve uygulamadaki kapsamı çoğu zaman farklı bahisler içinde ele alınmaktadır.",'replacement':"Resm-i Osmânî'ye uygunluk, kırâat usûlünde okuyuşların değerlendirilmesinde dikkate alınan temel ölçülerden biridir. Bununla birlikte kırâatlerin aslî aktarım zemini telakki, müşâfehe, edâ ve isnada dayanan rivâyet geleneğidir. Bu kitap, sözlü aktarım ile mushaf yazısı arasındaki ilişkiyi, resm-i Osmânî'nin kırâatlerin rivâyeti ve kabulündeki işlevi bakımından incelemektedir.",'footnotes':[]},
            {'id':'F4-002','anchor':"Eserin, resm-i mushaf'ı yalnız geçmişte teşekkül etmiş bir imlâ biçimi olarak indirgemeyip, kırâatlerin rivâyeti, mushaf yazımı ve çağdaş neşir geleneğiyle ilişkili bir ilim alanı olarak değerlendirmeye katkı sağlaması hedeflenmektedir.",'replacement':"Eserin, mushaf yazım geleneğini yalnız tarihsel bir imlâ biçimi olarak ele almakla yetinmeyip, resm-i mushaf ilminin kırâat rivâyeti ve çağdaş neşir geleneğiyle ilişkisini göstermeye katkı sağlaması hedeflenmektedir. Kaynaklarda ihtilaf bulunan meselelerde tarihsel veriler ile sonraki yorumlar birbirinden ayrılarak ihtiyatlı bir değerlendirme benimsenmiştir.",'footnotes':[]},
            {'id':'F4-003','anchor':"Problemin tarihsel zemini, İslâm öncesi Arap yazısından nüzûl dönemindeki kayıt faaliyetlerine, oradan Kur'an'ın cem ve istinsah süreçlerine uzanmaktadır.",'replacement':"Problemin tarihsel zemini, İslâm öncesi Arap yazısından nüzûl dönemindeki kayıt faaliyetlerine, oradan cem ve istinsah süreçlerine uzanmaktadır. Vahyin yazıya geçirilmesi sözlü aktarımı tamamlayan bir kayıt işlevi görmüş; Hz. Ebû Bekir dönemindeki cem ile Hz. Osman dönemindeki istinsah farklı tarihsel şartlarda gerçekleştirilen iki ayrı uygulama olarak rivâyet edilmiştir. Kaynaklarda istinsah heyeti, mushafların sayısı ve gönderildikleri merkezler konusunda farklı aktarımlar bulunduğundan, bu sürecin ayrıntıları ihtiyatla değerlendirilmelidir.",'footnotes':['2']},
        ]
        result=[]
        for op in ops:
            repl_hits=[(i,p) for i,p in enumerate(paras) if norm(op['replacement'])==norm(ptext(p))]
            if len(repl_hits)==1:
                result.append((op['id'],repl_hits[0][0],'ALREADY_SATISFIED'))
                continue
            i,p=find_unique_para(paras,op['anchor'])
            replace_whole_paragraph(p,op['replacement'],op['footnotes'])
            result.append((op['id'],i,'APPLIED'))
        new_xml=etree.tostring(doc,xml_declaration=True,encoding='UTF-8',standalone='yes')
        out.parent.mkdir(parents=True,exist_ok=True)
        with ZipFile(out,'w') as zout:
            for info in zin.infolist():
                zout.writestr(info,new_xml if info.filename=='word/document.xml' else zin.read(info.filename))
    return result

if __name__=='__main__':
    for row in apply(Path(sys.argv[1]),Path(sys.argv[2])):
        print('\t'.join(map(str,row)))
