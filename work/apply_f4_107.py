#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys
import apply_f4_053_057 as h
import apply_f4_078 as f78
NS=h.NS
EARLY="Belirli kırâat rivâyetlerine göre hazırlanan matbu mushaflar, bu rivâyetlerin yazılı görünürlüğünü ve kullanım alanını artırmıştır. Bununla birlikte bir rivâyetin belirli bölgelerde yaygınlaşması yalnız baskı faaliyetiyle açıklanamaz; öğretim gelenekleri, bölgesel kırâat tercihleri, resmî neşir politikaları ve eğitim kurumları da bu süreçte etkili olmuştur."
OLD_END="Özetle, Türkiye’de mushaf basımının tarihî seyri üç temel nitelikle öne çıkmaktadır: geç başlaması, sıkı biçimde denetlenmesi ve nihayet Diyanet İşleri Başkanlığı bünyesinde kurumsal bir standarda bağlanması. Bu durum, mushafın Türkiye’de tarih boyunca hem metin güvenliği hem de dinî otorite açısından özel bir konuma sahip olduğunu teyit etmektedir."
FINAL="Matbu mushafların yaygınlaşması, resm-i Osmânî'nin yeni üretim teknikleri içinde uygulanmasını ve belirli kırâat rivâyetlerinin yazılı neşir yoluyla daha görünür hâle gelmesini sağlamıştır. Bu süreç, klasik resm kaynakları, kırâat öğretimi, tashih kurumları, baskı teknolojisi ve resmî neşir politikalarının birlikte etkisiyle şekillenmiştir."
TURKEY_ANCHOR="Bugün Türkiye’de mushaf basımı, Diyanet denetimine bağlı kurumsal bir süreç olarak devam etmektedir."
CHRONOLOGY="1873 yılında alınan kararın ardından 1874’te Maarif Nezâreti'nin denetiminde ilk resmî Osmanlı mushafı basılmıştır."

def state(path:Path):
    with ZipFile(path) as z:
        d=etree.fromstring(z.read('word/document.xml')); body=d.find('.//w:body',namespaces=NS); ps=body.xpath('./w:p',namespaces=NS)
        texts=[h.norm(h.txt(p)) for p in ps]
        return d,body,ps,texts

def complete(path:Path):
    d,body,ps,texts=state(path)
    th=[p for p in ps if h.norm(h.txt(p)).startswith(h.norm(TURKEY_ANCHOR))]
    return (not any(h.norm(t)==h.norm(EARLY) for t in texts)
            and len(th)==1 and h.norm(FINAL) in h.norm(h.txt(th[0]))
            and h.spec(th[0])['fn']==['469']
            and not any(h.norm(OLD_END) in t for t in texts)
            and sum(h.norm(CHRONOLOGY) in t for t in texts)==1)

def apply(src:Path,out:Path):
    if complete(src):
        f78.validate_structural(src,src); shutil.copyfile(src,out); return [('F4-107','current','ALREADY_SATISFIED')]
    with ZipFile(src,'r') as zin:
        d=etree.fromstring(zin.read('word/document.xml')); body=d.find('.//w:body',namespaces=NS); ps=body.xpath('./w:p',namespaces=NS)
        early=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p))==h.norm(EARLY)]
        turkey=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p)).startswith(h.norm(TURKEY_ANCHOR))]
        chrono=[(i,p) for i,p in enumerate(ps) if h.norm(CHRONOLOGY) in h.norm(h.txt(p))]
        if len(early)!=1 or len(turkey)!=1 or len(chrono)!=1: raise RuntimeError(f'F4-107 anchors early/turkey/chrono={len(early)}/{len(turkey)}/{len(chrono)}')
        ie,pe=early[0]; it,pt=turkey[0]
        se=h.spec(pe); st=h.spec(pt)
        if se['fn'] or se['instr'] or se['fld'] or se['hyper'] or se['rtl'] or se['book']:
            raise RuntimeError(f'F4-107 unsafe early conclusion P{ie}: {se}')
        if st['fn']!=['469'] or st['instr'] or st['fld'] or st['hyper'] or st['rtl'] or st['book']:
            raise RuntimeError(f'F4-107 Turkey paragraph protection mismatch P{it}: {st}')
        if h.norm(OLD_END) not in h.norm(h.txt(pt)): raise RuntimeError('F4-107 old Turkey ending missing')
        h.span(pt,OLD_END,FINAL)
        if h.spec(pt)!=st: raise RuntimeError('F4-107 FN469/protected structure changed')
        body.remove(pe)
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
    f78.validate_structural(src,out)
    if not complete(out): raise RuntimeError('F4-107 postconditions incomplete')
    return [('F4-107',f'P{ie}_REMOVED_AND_TURKEY_END_REPLACED','APPLIED_SINGLE_FINAL_CONCLUSION_ORDER_REPAIR_FN469_PRESERVED')]

if __name__=='__main__':
    for r in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,r)))
