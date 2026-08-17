#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys
import apply_f4_053_057 as h
import apply_f4_078 as f78

NS=h.NS
P351_OLD="Bu çerçevede resm-i Osmânî, ihtilafı azaltmak ve sahih olanı muhafaza etmek için en başta sabit rivâyete bağlı kalmayı"
P351_NEW="Birinci Bölümde ayrıntıları verilen cem ve istinsah süreci bakımından burada vurgulanması gereken husus şudur: Osmânî mushafların yazılı çerçevesi, rivâyetle sabit ve müşterek kabul gören okuyuşların kaydedildiği tarihsel zemini oluşturmuştur; yazı bu okuyuşları üretmemiş, rivâyet edilen metni müşterek mushaf biçiminde kayda geçirmiştir."
S1_OLD="Osmânî resmin diğer temel işlevi, tevâtüren sabit olan kırâatlerle âhâd rivâyetleri birbirinden ayıran bağlayıcı bir ölçü oluşturmasıdır."
S1_NEW="Resm-i Osmânî, kırâat rivâyetlerini meydana getiren bağımsız bir kaynak değildir. Bununla birlikte mushaf hattına uygunluk, rivâyetle nakledilen okuyuşların müşterek mushaf yazısıyla bağdaşma durumunu değerlendirmede kullanılan önemli ölçütlerden biridir."
S3_OLD="Bu yaklaşım, Osmânî resmin sadece mevcut rivâyetleri kaydeden edilgen bir kalıp olmadığını; aksine ümmetin ortak mushafında hangi vecihlerin kalacağını belirleyen seçici bir çerçeve olduğunu göstermektedir."
S3_NEW="Bu durum, resmin okuyuşları seçen bağımsız bir özne olduğunu değil, rivâyet edilen okuyuşların müşterek yazılı çerçeveyle uyumunun değerlendirilmesine katkı sağladığını göstermektedir."
S5_OLD="Dolayısıyla resm-i Osmânî, sahih kırâat alanını tahdit eden ve onu ümmetin müşterek rivâyet zemini içinde koruyan kurucu bir unsur hüviyeti kazanmaktadır."
S5_NEW="Okuyuşun varlığı ve edâsı rivâyet yoluyla bilinir; resm ise bu okuyuşun Osmânî mushafların yazılı çerçevesi içindeki konumunu değerlendirmeye katkı sağlar."

def complete(path):
    with ZipFile(path) as z:
        d=etree.fromstring(z.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        text='\n'.join(h.txt(p) for p in ps)
        p351=[p for p in ps if h.norm(h.txt(p))==h.norm(P351_NEW)]
    olds=[P351_OLD,S1_OLD,S3_OLD,S5_OLD]
    news=[P351_NEW,S1_NEW,S3_NEW,S5_NEW]
    return len(p351)==1 and h.spec(p351[0])['fn']==['365'] and all(h.norm(x) not in h.norm(text) for x in olds) and all(h.norm(x) in h.norm(text) for x in news)

def apply(src:Path,out:Path):
    if complete(src):
        f78.validate_structural(src,src); shutil.copyfile(src,out)
        return [('F4-083','current','ALREADY_SATISFIED')]
    with ZipFile(src,'r') as zin:
        d=etree.fromstring(zin.read('word/document.xml')); body=d.find('.//w:body',namespaces=NS); ps=body.xpath('./w:p',namespaces=NS)
        _,p351=h.find(ps,P351_OLD)
        if h.spec(p351)['fn']!=['365'] or h.spec(p351)['rtl'] or h.spec(p351)['book'] or h.spec(p351)['fld'] or h.spec(p351)['hyper']:
            raise RuntimeError('unexpected protected P351 structure '+str(h.spec(p351)))
        h.whole(p351,P351_NEW,(365,))
        ps=body.xpath('./w:p',namespaces=NS)
        _,p352=h.find(ps,S1_OLD)
        if h.spec(p352)['fn']!=['366','367']:
            raise RuntimeError('unexpected P352 footnotes '+str(h.spec(p352)))
        for a,r in [(S1_OLD,S1_NEW),(S3_OLD,S3_NEW),(S5_OLD,S5_NEW)]:
            h.span(p352,a,r)
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
    f78.validate_structural(src,out)
    if not complete(out): raise RuntimeError('F4-083 postconditions incomplete')
    return [('F4-083','current','APPLIED_ACTIVE_AGENT_REFRAME_AND_HISTORY_REDUCTION')]

if __name__=='__main__':
    for row in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,row)))
