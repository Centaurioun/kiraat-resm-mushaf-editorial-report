#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from copy import deepcopy
import shutil,sys
import apply_f4_053_057 as base

W=base.W; NS=base.NS

def collect_fn_runs(pars):
    out={}
    for p in pars:
        if not base.safe_plain(p): raise RuntimeError('protected structure in structural cluster '+str(base.spec(p)))
        for r in p.xpath('./w:r',namespaces=NS):
            ids=r.xpath('.//w:footnoteReference/@w:id',namespaces=NS)
            if ids: out[ids[0]]=deepcopy(r)
    return out

def replace_parts(target,sources,parts,expected_ids):
    ids=[]
    for p in sources: ids += base.spec(p)['fn']
    if ids!=list(map(str,expected_ids)): raise RuntimeError(f'footnote order mismatch {ids} != {expected_ids}')
    fr=collect_fn_runs(sources); rp=base.first_rpr(target); base.clear(target)
    for kind,val in parts:
        if kind=='t': base.add(target,val,rp)
        elif kind=='fn': target.append(deepcopy(fr[str(val)]))
        else: raise ValueError(kind)

def apply(src:Path,out:Path):
    with ZipFile(src,'r') as zin:
        d=etree.fromstring(zin.read('word/document.xml')); body=d.find('.//w:body',namespaces=NS); changed=False; rows=[]

        # F4-058: consolidate the competing views without selecting one as historically certain.
        R58a="Osmânî mushaflarla yedi harf arasındaki ilişkinin nasıl anlaşılacağı konusunda klasik kaynaklarda farklı görüşler bulunmaktadır. "
        R58b="Bir kısım âlimler Hz. Osman'ın ümmeti belirli bir harf üzerinde topladığını, "
        R58c="bir kısmı ise mushaf resminin taşıdığı ölçüde birden fazla vechin korunduğunu ifade etmiştir. "
        R58d="Bu görüşlerin her biri kendi kaynak ve yorum bağlamı içinde değerlendirilmelidir. Bununla birlikte bu tartışma, sahih kırâatlerin mushaf yazısından üretildiği anlamına gelmez. Kırâatlerin aktarımında telakki ve rivâyet belirleyici olmaya devam etmiş; resm ise nakledilen okuyuşların ortak mushaf yazısıyla bağdaşma sınırını göstermiştir."
        ps=body.xpath('./w:p',namespaces=NS); h=[(i,p) for i,p in enumerate(ps) if base.norm(base.txt(p)).startswith(base.norm(R58a))]
        if h:
            i58,p58=h[0]
            if base.spec(p58)['fn']!=['219','220','221','222']: raise RuntimeError('F4-058 completed note mismatch')
            st58='ALREADY_SATISFIED'
        else:
            i58,p232=base.find(ps,'Osmânî mushaf ile yedi harf arasındaki ilişki meselesi tam burada başlar.')
            i233,p233=base.find(ps,'Klasik literatürde bu konuda öne çıkan ilk görüş')
            i234,p234=base.find(ps,'Buna karşılık ikinci ve daha mutedil görünen görüş')
            i235,p235=base.find(ps,'Âlimlerin bir kısmı daha ileri giderek Osmânî mushafın yedi harfin tamamını')
            if [i233,i234,i235]!=[i58+1,i58+2,i58+3]: raise RuntimeError('F4-058 source cluster not contiguous')
            replace_parts(p232,[p232,p233,p234,p235],[('t',R58a),('t',R58b),('fn',219),('fn',220),('t',R58c),('fn',221),('fn',222),('t',R58d)],[219,220,221,222])
            for q in [p233,p234,p235]: body.remove(q)
            changed=True; st58='STRUCTURALLY_APPLIED'
        rows.append(('F4-058',i58,st58))

        # F4-059: shorten repeated historical setup and replace the long mini-conclusion with a bridge to 2.4.
        R59open='Osmânî mushaflarla yedi harf arasındaki ilişki, klasik kaynaklarda farklı biçimlerde açıklanmış tartışmalı bir meseledir. Bu başlıkta amaç cem ve istinsah tarihini yeniden kurmak değil, yedi harf açıklamalarının müşterek mushaf yazısıyla nasıl ilişkilendirildiğini göstermektir.'
        ps=body.xpath('./w:p',namespaces=NS); h=[(i,p) for i,p in enumerate(ps) if base.norm(base.txt(p))==base.norm(R59open)]
        if h: i59a,p=h[0]; already_open=True
        else:
            i59a,p=base.find(ps,'Kur’an tarihi içinde en çok tartışılan meselelerden biri, Hz. Osman döneminde çoğaltılan mushaflarla “yedi harf” ruhsatı')
            base.whole(p,R59open); changed=True; already_open=False
        R59='Yedi harf ile Osmânî mushaf arasındaki ilişkiye dair bu farklı açıklamalar, resm-i Osmânî’nin sonraki kırâat değerlendirmelerinde nasıl ortak bir yazılı başvuru zemini hâline geldiği sorusunu gündeme getirmektedir. Bir sonraki başlık bu tarihsel sonucun kırâat ve tefsîr alanındaki yansımalarını ele almaktadır.'
        ps=body.xpath('./w:p',namespaces=NS); h=[(i,p) for i,p in enumerate(ps) if base.norm(base.txt(p))==base.norm(R59)]
        if h: i59,p=h[0]; already_end=True
        else:
            i59,p=base.find(ps,'Sonuç olarak Osmânî mushaf ile yedi harf meselesi')
            base.whole(p,R59); changed=True; already_end=False
        rows.append(('F4-059',i59,'ALREADY_SATISFIED' if already_open and already_end else 'STRUCTURALLY_APPLIED'))

        # F4-060: balance resm with transmission networks, teaching environments and scholarly acceptance.
        R60p240='Osmânî mushafların ortak başvuru metni hâline gelmesi, kırâatlerin sonraki değerlendirilmesinde resme uygunluk ölçüsünün daha belirgin hâle gelmesine zemin hazırlamıştır. Tefsîr geleneğinde ise müşterek mushaf metni ortak bir yazılı zemin sağlamış, farklı kırâatlerin yorumdaki kullanımı rivâyet ve dil verileriyle birlikte sürmüştür.'
        ps=body.xpath('./w:p',namespaces=NS); h=[(i,p) for i,p in enumerate(ps) if base.norm(base.txt(p)).startswith(base.norm(R60p240))]
        if h:
            i60,p240=h[0]
            if base.spec(p240)['fn']!=['225']: raise RuntimeError('F4-060 P240 note mismatch')
            a60=True
        else:
            i60,p240=base.find(ps,'Kur’an metninin yazı bakımından ortak bir biçime kavuşması, yani resm-i Osmânî’nin yerleşmesi')
            replace_parts(p240,[p240],[('t',R60p240),('fn',225)],[225]); changed=True; a60=False
        R60p241='Bununla birlikte kırâat imamlarının otoritesi ve öğretim geleneklerinin yerleşmesi yalnız mushaf yazısıyla açıklanamaz; rivâyet zincirleri, bölgesel öğretim çevreleri ve ilmî kabul de bu sürecin temel unsurlarıdır. Ebû Şâme, bir okuyuşun yalnız bir imama nispet edilmesini yeterli görmeyip sahih nakil ile mushaf hattına uygunluğun birlikte aranması gerektiğini vurgular. İbn Mücâhid’in yedi imam tasnifi de bölgesel öğretim ve rivâyet çevrelerinin tarihsel gelişimi içinde değerlendirilmelidir.'
        ps=body.xpath('./w:p',namespaces=NS); h=[(i,p) for i,p in enumerate(ps) if base.norm(base.txt(p)).startswith(base.norm(R60p241))]
        if h:
            _,p241=h[0]
            if base.spec(p241)['fn']!=['226','227']: raise RuntimeError('F4-060 P241 note mismatch')
            b60=True
        else:
            _,p241=base.find(ps,'Resmin ortak hale gelmesinin kırâat ilmine etkisi')
            replace_parts(p241,[p241],[('t','Bununla birlikte kırâat imamlarının otoritesi ve öğretim geleneklerinin yerleşmesi yalnız mushaf yazısıyla açıklanamaz; rivâyet zincirleri, bölgesel öğretim çevreleri ve ilmî kabul de bu sürecin temel unsurlarıdır. Ebû Şâme, bir okuyuşun yalnız bir imama nispet edilmesini yeterli görmeyip sahih nakil ile mushaf hattına uygunluğun birlikte aranması gerektiğini vurgular.'),('fn',226),('t',' İbn Mücâhid’in yedi imam tasnifi de bölgesel öğretim ve rivâyet çevrelerinin tarihsel gelişimi içinde değerlendirilmelidir.'),('fn',227)],[226,227]); changed=True; b60=False
        rows.append(('F4-060',i60,'ALREADY_SATISFIED' if a60 and b60 else 'APPLIED'))

        # F4-061: replace counterfactual history with source-bound historical description.
        R61a='Osmânî mushafların ortak başvuru metni hâline gelmesi, farklı merkezlerdeki kırâat rivâyetlerinin müşterek bir yazılı çerçeveyle ilişkilendirilmesine imkân vermiştir. Bunun sonraki kırâat ve tefsîr literatüründeki sonuçları, mevcut tarihsel uygulamalar ve kaynakların aktardığı değerlendirmeler üzerinden açıklanmalıdır. Semîn el-Halebî’nin çalışması da farklı bir ilmî çevrede müşterek mushaf hattı üzerinde yürütülen tefsîr faaliyetinin örneklerinden biridir.'
        ps=body.xpath('./w:p',namespaces=NS); h=[(i,p) for i,p in enumerate(ps) if base.norm(base.txt(p)).startswith(base.norm(R61a))]
        if h:
            i61,p249=h[0]
            if base.spec(p249)['fn']!=['237']: raise RuntimeError('F4-061 note mismatch')
            st61='ALREADY_SATISFIED'
        else:
            i61,p249=base.find(ps,'Mushaf metni, tefsîrin ümmet nezdinde ortak metne dayanmasını sağlamıştır.')
            replace_parts(p249,[p249],[('t',R61a),('fn',237)],[237]);changed=True;st61='APPLIED'
        rows.append(('F4-061',i61,st61))

        # F4-062: direct conceptual bridge into the concrete examples of Chapter Three.
        R62='Resm-i Osmânî’nin kırâat rivâyetiyle ilişkisi genel ilkeler düzeyinde bu şekilde belirlendikten sonra, bu ilişkinin somut yazım örneklerinde nasıl göründüğünü incelemek gerekir. Üçüncü bölüm hazf, ziyâde, ibdâl, vasl-fasl ve benzeri resm özelliklerinin kırâat, lafız ve mana ile ilişkisini bu açıdan ele almaktadır.'
        ps=body.xpath('./w:p',namespaces=NS); h=[(i,p) for i,p in enumerate(ps) if base.norm(base.txt(p))==base.norm(R62)]
        if h: i62,p=h[0];st62='ALREADY_SATISFIED'
        else:
            i62,p=base.find(ps,'Sonuç olarak resmin standartlaşması tefsîr ilmini sadece teknik olarak etkilememiş')
            base.whole(p,R62);changed=True;st62='APPLIED'
        rows.append(('F4-062',i62,st62))

        if not changed:
            shutil.copyfile(src,out); return rows
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist():zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
    base.validate(src,out)
    # Batch-specific postconditions.
    with ZipFile(out) as z:
        doc=etree.fromstring(z.read('word/document.xml')); body_text='\n'.join(base.txt(p) for p in doc.xpath('.//w:body/w:p',namespaces=NS))
    required=[R58a.strip(),R59,R60p240,R60p241,R61a,R62]
    for x in required:
        if base.norm(x) not in base.norm(body_text): raise RuntimeError('missing F4-058-062 postcondition: '+x[:80])
    stale=['Buna karşılık ikinci ve daha mutedil görünen görüş','Doğruya yakın olan, mushafın ihtilafa yol açan fazlalıkları','Sonuç olarak Osmânî mushaf ile yedi harf meselesi','Bu gelişme doğrudan doğruya kırâat ve tefsîr alanını şekillendiren','Resmin ortaklaşması, dolaylı olarak kırâat imamlarının otoritesini','Şayet mushaf yazısı ortak olmasaydı','Böylece tefsîr ilmi, hem ortak mushaf metnini esas alan']
    for x in stale:
        if base.norm(x) in base.norm(body_text): raise RuntimeError('stale F4-058-062 text remains: '+x)
    return rows

if __name__=='__main__':
    for row in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,row)))
