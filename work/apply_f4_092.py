#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil, sys
import apply_f4_053_057 as h
import apply_f4_078 as f78

NS = h.NS
ANCHOR = "Bu çerçevede mushaf hattına aykırı olan kırâat vecihlerinin tedricen şâz kategorisine sevk edildiği görülmektedir."
OLD_OPEN = "Bu çerçevede mushaf hattına aykırı olan kırâat vecihlerinin tedricen şâz kategorisine sevk edildiği görülmektedir. Rivâyetleri sahih olsa bile, Osmânî mushaf hattına uymayan okuyuşlar fiilî kırâat alanının dışına çıkarılmış ve zamanla “şâz kırâat” adıyla anılmaya başlanmıştır."
NEW_OPEN = "Klasik kaynaklarda müşterek mushaf hattına aykırı kalan okuyuşlar, isnad ve kabul durumlarına göre farklı şekillerde değerlendirilmiştir. Bazı rivâyetler şâz, bazıları âhâd veya tefsirî malzeme, bazıları ise mensuh olduğu ileri sürülen okuyuşlar bağlamında ele alınmıştır. Bu kategoriler aynı değildir. Resme uygunluk önemli bir kabul ölçüsüdür; ancak her okuyuşun statüsü isnad, dil, şöhret ve ilmî kabul gibi diğer unsurlarla birlikte belirlenmelidir."
OLD_CLOSE = "Dolayısıyla bu yaklaşım, mushaf hattının kırâat ilminde pasif bir unsur olmadığını; sahih ile şâz arasındaki çizgiyi belirleyen bağlayıcı bir ölçü hâline geldiğini göstermektedir."
NEW_CLOSE = "Bu açıklamalar, resme uygunluğun kırâatlerin değerlendirilmesinde önemli ölçülerden biri olduğunu; ancak şâzlık veya kabul statüsünün isnad, dil ve ilmî kabul gibi diğer unsurlarla birlikte ele alındığını göstermektedir."
NEXT = "Bu noktada dikkat çekici olan husus, mushaf hattına aykırı kalan bütün vecihlerin baştan beri temelsiz veya uydurma sayılmamasıdır."


def complete(path: Path):
    with ZipFile(path) as z:
        d = etree.fromstring(z.read('word/document.xml'))
        ps = d.xpath('.//w:body/w:p', namespaces=NS)
        hits=[]
        for i,p in enumerate(ps):
            t=h.norm(h.txt(p))
            if h.norm(NEW_OPEN) in t and h.norm(NEW_CLOSE) in t:
                hits.append((i,p))
        if len(hits)!=1:
            return False
        i,p=hits[0]; s=h.spec(p)
        return (s['fn']==['392','393'] and not s['rtl'] and not s['fld'] and not s['book'] and not s['hyper'] and
                i+1 < len(ps) and h.norm(h.txt(ps[i+1])).startswith(h.norm(NEXT)) and
                h.norm(OLD_OPEN) not in h.norm(h.txt(p)) and h.norm(OLD_CLOSE) not in h.norm(h.txt(p)))


def apply(src: Path, out: Path):
    if complete(src):
        f78.validate_structural(src, src); shutil.copyfile(src, out)
        return [('F4-092','current','ALREADY_SATISFIED')]
    with ZipFile(src,'r') as zin:
        d=etree.fromstring(zin.read('word/document.xml')); body=d.find('.//w:body',namespaces=NS); ps=body.xpath('./w:p',namespaces=NS)
        i,p=h.find(ps,ANCHOR)
        s=h.spec(p)
        if s['fn']!=['392','393'] or s['rtl'] or s['fld'] or s['book'] or s['hyper']:
            raise RuntimeError('unexpected protected F4-092 target '+str(s))
        if i+1>=len(ps) or not h.norm(h.txt(ps[i+1])).startswith(h.norm(NEXT)) or h.spec(ps[i+1])['fn']!=['394']:
            raise RuntimeError('F4-092/F4-093 boundary mismatch')
        r1=h.span(p,OLD_OPEN,NEW_OPEN)
        r2=h.span(p,OLD_CLOSE,NEW_CLOSE)
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
    f78.validate_structural(src,out)
    if not complete(out): raise RuntimeError('F4-092 postconditions incomplete')
    return [('F4-092',f'P{i}',f'{r1}+{r2}')]

if __name__=='__main__':
    for row in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,row)))
