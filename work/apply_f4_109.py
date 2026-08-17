#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys
import apply_f4_053_057 as h
import apply_f4_078 as f78
NS=h.NS

ANCHOR="Klasik resm geleneğinin çağdaş mushaf neşirlerinde sürdürülmesi, bu ilmin yalnız erken dönem tarihine ait olmadığını göstermektedir."
OLD="Basılı mushaflar yalnız mevcut okuyuşları yansıtmamış, belirli rivâyetlerin standartlaşması ve geniş coğrafyalarda yaygınlaşması üzerinde de etkili olmuştur. Ana metinde ele alınan Hafs ve Verş örnekleri, mushaf neşri ile kırâatlerin bölgesel ve daha geniş dolaşımı arasındaki ilişkinin birlikte incelenmesi gerektiğini göstermektedir."
NEW="Matbu mushafların yaygınlaşması, belirli kırâat rivâyetlerinin yazılı biçimde daha geniş çevrelere ulaşmasına katkı sağlamıştır. Bununla birlikte modern mushaf standardizasyonu yalnız baskının veya resm-i Osmânî'ye bağlılığın sonucu değildir; öğretim gelenekleri, tashih kurumları, kırâat uzmanlığı, bölgesel tercihler ve resmî neşir süreçleri de bu gelişmede etkili olmuştur."
KEEP="Dânî ile Ebû Dâvud Süleymân b. Necâh’ın eserleri ve bu eserlerde derlenen resm rivâyetleri, modern basılı mushafların yazımında başvurulan klasik zeminin önemli bir bölümünü oluşturmuş; resm ile zaptın birbirinden ayrılması, mushafların belirli kırâat rivâyetlerine göre hazırlanmasına imkân vermiştir."

def complete(path:Path):
    with ZipFile(path) as z:
        d=etree.fromstring(z.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        hits=[p for p in ps if h.norm(h.txt(p)).startswith(h.norm(ANCHOR))]
        return (len(hits)==1 and h.norm(KEEP) in h.norm(h.txt(hits[0])) and h.norm(NEW) in h.norm(h.txt(hits[0])) and h.norm(OLD) not in h.norm(h.txt(hits[0])))

def apply(src:Path,out:Path):
    if complete(src):
        f78.validate_structural(src,src); shutil.copyfile(src,out); return [('F4-109','current','ALREADY_SATISFIED')]
    with ZipFile(src,'r') as zin:
        d=etree.fromstring(zin.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        i,p=h.find(ps,ANCHOR)
        s=h.spec(p)
        if s['fn'] or s['instr'] or s['fld'] or s['hyper'] or s['rtl'] or s['book']:
            raise RuntimeError(f'F4-109 protected structure present P{i}: {s}')
        if h.norm(KEEP) not in h.norm(h.txt(p)): raise RuntimeError('F4-109 unique classical-source/resm-zabt core missing')
        st=h.span(p,OLD,NEW)
        if st!='APPLIED': raise RuntimeError('F4-109 replacement not applied')
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
    f78.validate_structural(src,out)
    if not complete(out): raise RuntimeError('F4-109 postconditions incomplete')
    return [('F4-109',f'P{i}','APPLIED_MULTICAUSAL_PRINT_STANDARDIZATION_REFRAME')]

if __name__=='__main__':
    for r in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,r)))
