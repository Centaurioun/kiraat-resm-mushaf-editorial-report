#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys
import apply_f4_053_057 as h
import apply_f4_078 as f78

NS=h.NS
P397_ANCHOR="Osmânî mushafların yazımına dair rivâyetler, kırâat rivâyetlerinden bağımsız bir alan olarak addedilmeyip"
OLD397="Bu tespit, resm bilgisinin yalnız yazı tarihine ilişkin yardımcı tali bir veri alanı şeklinde görülmemesi gerektiğini; bilakis kırâat farklılıklarının anlaşılması için kurucu bir zemin teşkil ettiğini göstermektedir."
NEW397="Bu tespit, resm rivâyetlerinin mushaf yazım biçimlerini ve okuyuşların yazılı mushaf geleneğiyle ilişkisini değerlendirmede tamamlayıcı bir veri alanı olduğunu göstermektedir."
OLD400="Bu çerçevede denilebilir ki Osmânî mushafların hecâsına dair rivâyetler, yalnız yazı tarihine ilişkin malumat sunan tali veriler değildir. Aksine bunlar, kırâat ihtilaflarının tespiti, sınırlarının belirlenmesi ve yorumlanmasında kurucu işleve sahiptir. Bir taraftan mushaflar arasındaki yazım farklılıklarının sahih rivâyet temelinde anlaşılmasını sağlamakta, diğer taraftan kırâat vecihlerinin hangi maddi zemin üzerinde okunup aktarıldığını göstermektedir. Bu sebeple resm rivâyetleri, kırâat ilminin kenarında duran yardımcı bir alan sayılmamalı; kırâat rivâyetlerinin tarihini, meşruiyetini ve farklılık yapısını açıklayan temel bilgi kaynaklarından biri olarak değerlendirilmelidir."
NEW400="Resm rivâyetleri, mushaf kelimelerinin hangi biçimde yazıldığını ve şehir mushafları arasında nakledilen yazım farklılıklarını belirlemek bakımından önemlidir. Bu veriler kırâatlerin rivâyet kaynağının yerine geçmez; okuyuşların yazılı mushaf geleneğiyle ilişkisini değerlendirmeye imkân veren tamamlayıcı malzeme sunar."
NOTE="el-Mehdevî (ö. 440/1048 daha önce geçmişmi)"
NEXT="Osmânî mushaflar arasındaki yazım rivâyetleriyle kırâatler arasındaki ilişki"

def complete(path):
    with ZipFile(path) as z:
        d=etree.fromstring(z.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        p397=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p)).startswith(h.norm(P397_ANCHOR))]
        p400=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p))==h.norm(NEW400)]
        if len(p397)!=1 or len(p400)!=1:return False
        i397,a=p397[0]; i400,b=p400[0]
        if h.norm(NEW397) not in h.norm(h.txt(a)) or NOTE not in h.txt(a):return False
        if h.spec(a)['fn']!=['417'] or h.spec(b)['fn'] or h.spec(b)['rtl'] or h.spec(b)['book']:return False
        if i400+1>=len(ps) or not h.norm(h.txt(ps[i400+1])).startswith(h.norm(NEXT)):return False
        return True

def apply(src:Path,out:Path):
    if complete(src):
        f78.validate_structural(src,src); shutil.copyfile(src,out); return [('F4-097','current','ALREADY_SATISFIED')]
    with ZipFile(src,'r') as zin:
        d=etree.fromstring(zin.read('word/document.xml')); body=d.find('.//w:body',namespaces=NS); ps=body.xpath('./w:p',namespaces=NS)
        i397,p397=h.find(ps,P397_ANCHOR)
        s397=h.spec(p397)
        if s397['fn']!=['417'] or s397['rtl'] or s397['fld'] or s397['book'] or s397['hyper']:
            raise RuntimeError('unexpected F4-097 P397 structure '+str(s397))
        if NOTE not in h.txt(p397): raise RuntimeError('F4-098 work-note boundary unexpectedly absent')
        st397=h.span(p397,OLD397,NEW397)
        if h.spec(p397)!=s397: raise RuntimeError('F4-097 P397 structure changed')
        ps=body.xpath('./w:p',namespaces=NS)
        i400,p400=h.find(ps,OLD400)
        s400=h.spec(p400)
        if s400['fn'] or s400['rtl'] or s400['fld'] or s400['book'] or s400['hyper']:
            raise RuntimeError('unexpected F4-097 P400 structure '+str(s400))
        if i400+1>=len(ps) or not h.norm(h.txt(ps[i400+1])).startswith(h.norm(NEXT)):
            raise RuntimeError('F4-097 next boundary mismatch')
        h.whole(p400,NEW400,())
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
    f78.validate_structural(src,out)
    if not complete(out): raise RuntimeError('F4-097 postconditions incomplete')
    return [('F4-097',f'P{i397}+P{i400}',st397+'+APPLIED_COMPLEMENTARY_EVIDENCE_SYNTHESIS')]

if __name__=='__main__':
    for row in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,row)))
