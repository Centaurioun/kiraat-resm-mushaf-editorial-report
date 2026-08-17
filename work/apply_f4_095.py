#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys
import apply_f4_053_057 as h
import apply_f4_078 as f78

NS=h.NS
ANCHOR="Bu etkinin ilk ve en belirgin tezahürü, kırâat imamlarının yaptıkları ihtiyarlarda görülmektedir."
OLD1="Bu etkinin ilk ve en belirgin tezahürü, kırâat imamlarının yaptıkları ihtiyarlarda görülmektedir. Sahâbenin okuduğu bütün vecihlerin umum kurrâ tarafından bütünüyle kuşatılması mümkün olmadığından, İslâm beldelerinin her biri tâbiîn döneminde bir kırâat imamına yönelmiş ve o imamın tercih ettiği okuyuşlar etrafında istikrar kazanmıştır. Ancak bu tercihler rastgele yahut keyfî biçimde yapılmamıştır."
NEW1="Kırâat imamlarına nispet edilen okuyuşlar, kendilerine ulaşan rivâyet ve öğretim geleneği içinde aktarılmıştır. Kaynaklarda bazı okuyuşlar arasında tercih ifadeleri bulunabilmekle birlikte bu tercih, imamların rivâyetten bağımsız yeni bir kırâat meydana getirdiği anlamına gelmez. Resm verisi de bu değerlendirmelerde rivâyet ve dil unsurlarıyla birlikte kullanılan ölçülerden biridir."
OLD2="Böylece resm-i Osmânî, kırâat imamlarının ihtiyarında sessiz fakat belirleyici bir ölçü işlevi görmüştür. Burada mushaf hattına uygunluk, yazılı şekle bağlı kalma düşüncesinin ötesinde, ümmetin üzerinde birleştiği kırâat alanının dışına çıkmama hassasiyeti olarak da anlaşılmaktadır."
NEW2="Bu çerçevede mushaf hattına uygunluk, kaynaklarda tercih gerekçeleri arasında anılan ölçülerden biri olarak değerlendirilmelidir; rivâyet, dil ve genel kabul unsurlarından bağımsız tek belirleyici sebep değildir."
HEADING="Resm-i Osmânî'nin Kırâatlerin Tercihi, Tevcîhi ve Vakıf Uygulamalarıyla İlişkisi"
NEXT="İmam Nâfiʿin (ö. 169/785) yetmiş tâbiîden kırâat aldığını,"

def complete(path):
    with ZipFile(path) as z:
        d=etree.fromstring(z.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        hits=[(i,p) for i,p in enumerate(ps) if h.norm(NEW1) in h.norm(h.txt(p)) and h.norm(NEW2) in h.norm(h.txt(p))]
        if len(hits)!=1: return False
        i,p=hits[0]; s=h.spec(p)
        if s['fn']!=['401'] or s['rtl'] or s['fld'] or s['book'] or s['hyper']: return False
        if i==0 or h.norm(h.txt(ps[i-1]))==h.norm(HEADING):
            pass
        # F4-094 heading is two paragraphs above because FN400 opening remains between heading and target.
        if i<2 or h.norm(h.txt(ps[i-2]))!=h.norm(HEADING): return False
        if i+1>=len(ps) or not h.norm(h.txt(ps[i+1])).startswith(h.norm(NEXT)): return False
        return True

def apply(src:Path,out:Path):
    if complete(src):
        f78.validate_structural(src,src); shutil.copyfile(src,out); return [('F4-095','current','ALREADY_SATISFIED')]
    with ZipFile(src,'r') as zin:
        d=etree.fromstring(zin.read('word/document.xml')); body=d.find('.//w:body',namespaces=NS); ps=body.xpath('./w:p',namespaces=NS)
        i,p=h.find(ps,ANCHOR)
        before=h.spec(p)
        if before['fn']!=['401'] or before['rtl'] or before['fld'] or before['book'] or before['hyper']:
            raise RuntimeError('unexpected protected F4-095 target '+str(before))
        if i<2 or h.norm(h.txt(ps[i-2]))!=h.norm(HEADING): raise RuntimeError('F4-095 heading boundary mismatch')
        if i+1>=len(ps) or not h.norm(h.txt(ps[i+1])).startswith(h.norm(NEXT)): raise RuntimeError('F4-095 next paragraph boundary mismatch')
        st1=h.span(p,OLD1,NEW1)
        st2=h.span(p,OLD2,NEW2)
        if h.spec(p)!=before: raise RuntimeError('F4-095 protected structure changed')
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
    f78.validate_structural(src,out)
    if not complete(out): raise RuntimeError('F4-095 postconditions incomplete')
    return [('F4-095',f'P{i}',st1+'+'+st2)]

if __name__=='__main__':
    for row in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,row)))
