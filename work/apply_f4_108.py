#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys
import apply_f4_053_057 as h
import apply_f4_078 as f78
NS=h.NS

OLD443="Bu araştırmanın ortaya koyduğu temel sonuç, resm-i mushaf ile kırâat rivâyeti arasındaki ilişkinin yazı ile söz karşıtlığı üzerinden açıklanamayacağıdır."
OLD445="Osmânî istinsahın önemli sonuçlarından biri, okuyuş farklılıklarını ortadan kaldırmadan kabul edilebilir çeşitliliği ortak bir yazım çerçevesi içinde korumasıdır."
OLD446="Bu nedenle resm-i Osmânî’ye uygunluk, kırâatlerin kabulünde tek başına yeterli veya diğer şartlara indirgenebilecek bir ölçü değildir."
OLD455="Sonuç olarak resm-i Osmânî, kırâati doğuran bağımsız kaynak değil, rivâyet yoluyla nakledilen kırâatlerin ortak yazılı sınırıdır."

NEW1="Bu çalışmada ulaşılan temel sonuç, resm-i Osmânî'nin kırâatleri meydana getiren bağımsız bir kaynak olmadığı; kırâatlerin aslî aktarımının telakki, müşâfehe, edâ, isnad ve rivâyet yoluyla gerçekleştiğidir. Resm-i Osmânî ise rivâyetle sabit okuyuşların müşterek mushaf yazısıyla bağdaşma durumunu belirleyen tamamlayıcı bir ölçü olarak işlev görmüştür. Bazı okuyuşlar yazıda açık karşılık bulurken bazıları harf iskeletinin ihtimali içinde yer almış; ancak grafik ihtimal hiçbir durumda okuyuşun sahihliğini tek başına belirlememiştir."
NEW2="Bu çerçeve, Kur’an metninin korunmasını yalnız yazıya veya yalnız sözlü aktarım zincirine indirgemeden açıklamayı mümkün kılmaktadır. Sözlü rivâyet okuyuşun nasıl edâ edileceğini ve hangi nakil hattına dayandığını korurken, müşterek mushaf yazısı bu rivâyetlerin yazılı metinle ilişkisini denetleyen bir çerçeve sağlamıştır. Kırâatlerin kabulünde isnad, Arap diline uygunluk ve resm-i Osmânî'ye uygunluk bu nedenle birbirinin alternatifi değil, birlikte değerlendirilen ölçülerdir."
UNIQUE446="Sahih, meşhur, âhâd ve şâz okuyuşlara ilişkin değerlendirmeler bu çoklu ölçü düzeni içinde anlam kazanmaktadır. Şâz rivâyetlerin tefsîr ve dil bakımından bilgi değeri taşımasıyla bağlayıcı kırâat kabul edilmesi birbirinden ayrılmalıdır."
HIST="Bu birlikteliğin tarihsel zemini, nüzûl dönemindeki kayıt faaliyetleri ile Hz. Ebû Bekir ve Hz. Osman dönemlerinde yürütülen farklı işlemlerde görülmektedir."


def state(path:Path):
    with ZipFile(path) as z:
        d=etree.fromstring(z.read('word/document.xml')); body=d.find('.//w:body',namespaces=NS); ps=body.xpath('./w:p',namespaces=NS)
        return d,body,ps,[h.norm(h.txt(p)) for p in ps]

def complete(path:Path):
    d,body,ps,texts=state(path)
    return (sum(h.norm(t)==h.norm(NEW1) for t in texts)==1
            and sum(h.norm(t)==h.norm(NEW2) for t in texts)==1
            and sum(h.norm(t)==h.norm(UNIQUE446) for t in texts)==1
            and sum(h.norm(HIST) in t for t in texts)==1
            and not any(t.startswith(h.norm(OLD443)) for t in texts)
            and not any(t.startswith(h.norm(OLD445)) for t in texts)
            and not any(t.startswith(h.norm(OLD446)) for t in texts)
            and not any(t.startswith(h.norm(OLD455)) for t in texts))

def safe_no_protected(p,label):
    s=h.spec(p)
    if s['fn'] or s['instr'] or s['fld'] or s['hyper'] or s['rtl'] or s['book']:
        raise RuntimeError(f'{label} protected structure present: {s}')

def apply(src:Path,out:Path):
    if complete(src):
        f78.validate_structural(src,src); shutil.copyfile(src,out); return [('F4-108','current','ALREADY_SATISFIED')]
    with ZipFile(src,'r') as zin:
        d=etree.fromstring(zin.read('word/document.xml')); body=d.find('.//w:body',namespaces=NS); ps=body.xpath('./w:p',namespaces=NS)
        i443,p443=h.find(ps,OLD443)
        i445,p445=h.find(ps,OLD445)
        i446,p446=h.find(ps,OLD446)
        i455,p455=h.find(ps,OLD455)
        for lab,p in [('P443',p443),('P445',p445),('P446',p446),('P455',p455)]: safe_no_protected(p,lab)
        # Ensure unique historical/result material outside the repeated blocks remains available before modification.
        ih,ph=h.find(ps,HIST)
        h.whole(p443,NEW1)
        h.whole(p445,NEW2)
        h.whole(p446,UNIQUE446)
        body.remove(p455)
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
    f78.validate_structural(src,out)
    if not complete(out): raise RuntimeError('F4-108 postconditions incomplete')
    return [('F4-108',f'P{i443}/P{i445}/P{i446}_CONSOLIDATED_P{i455}_REMOVED','APPLIED_TWO_FOCUS_CONCLUSION_CONSOLIDATION')]

if __name__=='__main__':
    for r in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,r)))
