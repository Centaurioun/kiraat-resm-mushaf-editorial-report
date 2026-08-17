#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from copy import deepcopy
from collections import Counter
import re, sys, shutil

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}

def norm(s):
    return re.sub(r'\s+',' ',(s or '').replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')).strip()
def txt(p): return ''.join(p.xpath('.//w:t/text()',namespaces=NS))
def spec(p):
    return {'fn':p.xpath('.//w:footnoteReference/@w:id',namespaces=NS),'instr':p.xpath('.//w:instrText/text()',namespaces=NS),'fld':len(p.xpath('.//w:fldChar',namespaces=NS)),'hyper':len(p.xpath('.//w:hyperlink',namespaces=NS)),'rtl':len(p.xpath('.//w:rtl',namespaces=NS)),'book':len(p.xpath('.//w:bookmarkStart|.//w:bookmarkEnd',namespaces=NS))}
def find(ps,a,starts=True):
    a=norm(a); hits=[]
    for i,p in enumerate(ps):
        t=norm(txt(p)); ok=t.startswith(a) if starts else a in t
        if ok: hits.append((i,p))
    if len(hits)!=1: raise RuntimeError(f'anchor {a[:90]!r}: hits={len(hits)}')
    return hits[0]
def first_rpr(p):
    for r in p.xpath('./w:r',namespaces=NS):
        if r.xpath('.//w:footnoteReference|.//w:rtl|.//w:vertAlign',namespaces=NS): continue
        cols=r.xpath('./w:rPr/w:color/@w:val',namespaces=NS)
        if cols and cols[0].upper() not in ('AUTO','000000'): continue
        rp=r.find(f'{{{W}}}rPr'); return deepcopy(rp) if rp is not None else None
    return None
def clear(p):
    ppr=p.find(f'{{{W}}}pPr')
    for c in list(p):
        if c is not ppr: p.remove(c)
def add(p,s,rpr=None):
    r=etree.Element(f'{{{W}}}r')
    if rpr is not None: r.append(deepcopy(rpr))
    t=etree.SubElement(r,f'{{{W}}}t'); t.text=s
    if s.startswith(' ') or s.endswith(' '): t.set('{http://www.w3.org/XML/1998/namespace}space','preserve')
    p.append(r)
def fnruns_many(pars):
    out={}
    for p in pars:
        for r in p.xpath('./w:r',namespaces=NS):
            ids=r.xpath('.//w:footnoteReference/@w:id',namespaces=NS)
            if ids: out[ids[0]]=deepcopy(r)
    return out
def safe_plain(p, allow_fn=True):
    s=spec(p)
    return not (s['instr'] or s['fld'] or s['hyper'] or s['rtl'] or s['book'] or (s['fn'] and not allow_fn))
def whole(p,s,expected_fn=()):
    sp=spec(p)
    if sp['fn']!=list(map(str,expected_fn)) or not safe_plain(p,True): raise RuntimeError('unsafe whole '+str(sp))
    rp=first_rpr(p); fr=fnruns_many([p]); clear(p); add(p,s,rp)
    for f in expected_fn: p.append(fr[str(f)])
def chunks(target,sources,parts,expected_fn):
    ids=[]
    for q in sources:
        if not safe_plain(q,True): raise RuntimeError('unsafe chunk source '+str(spec(q)))
        ids += spec(q)['fn']
    if ids!=list(map(str,expected_fn)): raise RuntimeError(f'chunk notes {ids} != {expected_fn}')
    fr=fnruns_many(sources); rp=first_rpr(target); clear(target)
    for kind,val in parts:
        if kind=='t': add(target,val,rp)
        elif kind=='fn': target.append(deepcopy(fr[str(val)]))
        else: raise ValueError(kind)
def span(p,a,r):
    before=spec(p); nodes=p.xpath('.//w:t',namespaces=NS); vals=[n.text or '' for n in nodes]; full=''.join(vals)
    cands=[a,a.replace("'",'’'),a.replace('’',"'")]; hits=[(full.find(x),x) for x in cands if full.find(x)>=0]
    if not hits:
        if norm(r) in norm(full) or (r=='' and norm(a) not in norm(full)): return 'ALREADY_SATISFIED'
        raise RuntimeError('span missing '+a[:100])
    pos,actual=hits[0]; end=pos+len(actual); starts=[]; c=0
    for v in vals: starts.append(c); c+=len(v)
    fi=next(i for i,(st,v) in enumerate(zip(starts,vals)) if pos < st+len(v))
    li=next(i for i,(st,v) in enumerate(zip(starts,vals)) if end <= st+len(v))
    pre=vals[fi][:pos-starts[fi]]; suf=vals[li][end-starts[li]:]
    nodes[fi].text=pre+r+(suf if fi==li else '')
    if fi!=li:
        for j in range(fi+1,li): nodes[j].text=''
        nodes[li].text=suf
    if spec(p)!=before: raise RuntimeError('protected structure changed during span')
    return 'APPLIED'

def instrs(z):
    out=[]
    for n in z.namelist():
        if n.startswith('word/') and n.endswith('.xml'):
            try:
                root=etree.fromstring(z.read(n)); out += [''.join(x.itertext()).strip() for x in root.xpath('//w:instrText',namespaces=NS)]
            except Exception: pass
    return out

def validate_same_structures(src,out):
    protected=['word/footnotes.xml','word/styles.xml','word/numbering.xml','word/settings.xml','word/_rels/document.xml.rels']
    with ZipFile(src) as zs, ZipFile(out) as z:
        if z.testzip() is not None: raise RuntimeError('DOCX ZIP integrity failure')
        for n in z.namelist():
            if n.endswith('.xml') or n.endswith('.rels'): etree.fromstring(z.read(n))
        ds=etree.fromstring(zs.read('word/document.xml')); d=etree.fromstring(z.read('word/document.xml'))
        fs=etree.fromstring(zs.read('word/footnotes.xml')); f=etree.fromstring(z.read('word/footnotes.xml'))
        fn0=[x for x in fs.xpath('//w:footnote/@w:id',namespaces=NS) if int(x)>0]; fn=[x for x in f.xpath('//w:footnote/@w:id',namespaces=NS) if int(x)>0]
        r0=ds.xpath('//w:footnoteReference/@w:id',namespaces=NS); r=d.xpath('//w:footnoteReference/@w:id',namespaces=NS)
        if fn!=fn0 or r!=r0 or len(fn)!=469 or len(r)!=469: raise RuntimeError('footnote/reference identity or order changed')
        if [k for k,v in Counter(r).items() if v>1] or set(fn)!=set(r): raise RuntimeError('orphan/dangling/duplicate reference')
        if instrs(z)!=instrs(zs): raise RuntimeError('Word/Zotero field instruction changed')
        if len(d.xpath('//w:rtl',namespaces=NS))!=len(ds.xpath('//w:rtl',namespaces=NS)): raise RuntimeError('RTL count changed')
        if len(d.xpath('//w:bookmarkStart',namespaces=NS))!=len(ds.xpath('//w:bookmarkStart',namespaces=NS)) or len(d.xpath('//w:bookmarkEnd',namespaces=NS))!=len(ds.xpath('//w:bookmarkEnd',namespaces=NS)): raise RuntimeError('bookmark count changed')
        if len(d.xpath('//w:hyperlink',namespaces=NS))!=len(ds.xpath('//w:hyperlink',namespaces=NS)): raise RuntimeError('hyperlink count changed')
        for n in protected:
            if zs.read(n)!=z.read(n): raise RuntimeError('protected part changed: '+n)
        body='\n'.join(txt(p) for p in d.xpath('.//w:body/w:p',namespaces=NS))
        required=[
            'Diğer bir örnek Bakara sûresinin 132. âyetindeki',
            'Bu özellikler birlikte değerlendirildiğinde resm-i Osmânî',
            "İbn Mücâhid (ö. 324/936), kırâatleri yedi imam etrafında tasnif ederek",
            'Zerkeşî, İbnü’l-Cezerî’den önce, mushaf yazısına uygunluğu',
            'İkinci bölüm bu sebeple kırâatlerin rivâyet mantığına yönelmektedir.',
            "Kur’an'ın okunmasına ilişkin farklı edâ biçimleri erken dönemden itibaren rivâyet yoluyla aktarılmış"
        ]
        for x in required:
            if norm(x) not in norm(body): raise RuntimeError('required postcondition missing: '+x)
        forbidden=['İbn Mücâhid (ö. 324/936 tekrar gözden geçirilsin)','Vurgulamak gerekir ki, bu altı imlâ özelliği','Kırâat ilmi bağımsız bir disiplin hâline hicrî II. ve III. yüzyıllarda gelmiştir.','Bu yaklaşımı benimseyen âlimlerden biri Zerkeşî’dir.']
        for x in forbidden:
            if norm(x) in norm(body): raise RuntimeError('stale postcondition remains: '+x)

def apply(src,out):
    with ZipFile(src) as zin:
        d=etree.fromstring(zin.read('word/document.xml')); body=d.find('.//w:body',namespaces=NS); changed=False; res=[]
        ps=body.xpath('./w:p',namespaces=NS)
        desired='Diğer bir örnek Bakara sûresinin 132. âyetindeki'
        hits=[(i,p) for i,p in enumerate(ps) if norm(desired) in norm(txt(p))]
        if hits:
            i48,p48=hits[0]; st48='ALREADY_SATISFIED'
        else:
            cand=[(i,p) for i,p in enumerate(ps) if 'وَوَص' in txt(p) and '(Bakara 2/85)' in txt(p)]
            if len(cand)!=1: raise RuntimeError(f'F4-048 target hits={len(cand)}')
            i48,p48=cand[0]
            if spec(p48)['rtl']<1 or spec(p48)['fn']!=['173','174']: raise RuntimeError('F4-048 RTL/note preflight mismatch '+str(spec(p48)))
            s1=span(p48,'Diğer bir örnek ise şöyledir: ','Diğer bir örnek Bakara sûresinin 132. âyetindeki ')
            s2=span(p48,'(Bakara 2/85) ','')
            s3=span(p48,'kelimelerinde mushaf yazısı iki okuyuşa da gelebilecek yapıdadır.','okuyuşlarıdır. İlgili mushaf rivâyetleri ve yazım farklılıkları, bu iki okuyuşun resmle ilişkisini değerlendirmek için kullanılmalıdır.')
            changed |= any(s=='APPLIED' for s in (s1,s2,s3)); st48='APPLIED'
        res.append(('F4-048',i48,st48))

        R49a="Bu özellikler birlikte değerlendirildiğinde resm-i Osmânî'nin bazı yerlerde rivâyetle sabit birden fazla okuyuşla bağdaşabildiği görülmektedir."
        R49b=" Ancak bir yazımın teorik olarak birden fazla okuyuşa imkân vermesi, bu okuyuşların sahihliğini tek başına göstermez. Resm, nakledilmiş okuyuşların yazı bakımından karşılanmasına ve sınırlandırılmasına katkı sağlar; hangi okuyuşun kırâat olarak kabul edileceği ise rivâyet, dil ve resme uygunluk ölçülerinin birlikte değerlendirilmesiyle belirlenir."
        ps=body.xpath('./w:p',namespaces=NS); hits=[(i,p) for i,p in enumerate(ps) if norm(txt(p)).startswith(norm(R49a))]
        if hits:
            i49,p49=hits[0]
            if spec(p49)['fn']!=['175','176']: raise RuntimeError('F4-049 completed note mismatch')
            st49='ALREADY_SATISFIED'
        else:
            i49,p1=find(ps,'Resm-i Osmânî’nin yazım kuralları mushaf yazımının rastgele değil belirli bir gelenek çerçevesinde şekillendiğini göstermektedir.')
            i2,p2=find(ps,'Vurgulamak gerekir ki, bu altı imlâ özelliği birlikte değerlendirildiğinde')
            i3,p3=find(ps,'Nitekim İslâm âlimleri, “İki kırâati bulunan kelime mümkünse her ikisini de taşıyacak şekilde yazılır.”')
            if [i2,i3]!=[i49+1,i49+2]: raise RuntimeError('F4-049 cluster not contiguous')
            chunks(p1,[p1,p2,p3],[('t',R49a),('fn',175),('fn',176),('t',R49b)],[175,176])
            body.remove(p2); body.remove(p3); changed=True; st49='STRUCTURALLY_APPLIED'
        res.append(('F4-049',i49,st49))

        R50="Kırâatlerin değerlendirilmesinde sahih nakil, Arap diline uygunluk ve resm-i Osmânî ile bağdaşma zamanla birlikte anılan temel ölçüler hâline gelmiştir. Bu ölçülerin klasik kaynaklarda ifade ediliş biçimi ve ağırlığı aynı değildir; sonraki usûl literatüründe daha sistematik bir çerçevede formüle edilmiştir. Zerkeşî ve İbnü'l-Cezerî'nin açıklamaları kendi kronolojik ve ilmî bağlamları içinde ayrı ayrı değerlendirilmelidir. Resme uygunluk hiçbir aşamada sahih isnadın yerine geçen tek ölçü olarak görülmemelidir."
        ps=body.xpath('./w:p',namespaces=NS); h=[(i,p) for i,p in enumerate(ps) if norm(txt(p))==norm(R50)]
        if h: i50,p190=h[0]; already50=True
        else:
            i50,p190=find(ps,'Zamanla bu fiilî birlik Kur’an ilimleri çalışmalarında temel ölçü olarak kabul edilmiştir.')
            whole(p190,R50); changed=True; already50=False
        ps=body.xpath('./w:p',namespaces=NS)
        R191="İbn Mücâhid (ö. 324/936), kırâatleri yedi imam etrafında tasnif ederek alanın sonraki gelişiminde etkili olan isimlerden biridir. Onun çalışması, kabul ölçülerinin ilk defa ortaya çıktığı nokta olarak görülmemelidir; sahih nakil, dil ve mushaf hattıyla bağdaşma yönündeki hassasiyetler daha erken kaynaklarda farklı biçimlerde görülmektedir."
        h=[(i,p) for i,p in enumerate(ps) if norm(txt(p))==norm(R191)]
        if not h:
            _,p191=find(ps,'İbn Mücâhid (ö. 324/936 tekrar gözden geçirilsin) kırâatleri yedi imam etrafında toplayarak')
            whole(p191,R191); changed=True; already50=False
        ps=body.xpath('./w:p',namespaces=NS)
        R194="İbn Mücâhid'in Kitâbu's-seb‘a'sı, bu erken hassasiyetlerin tasnif sürecindeki önemli örneklerinden biridir."
        h=[(i,p) for i,p in enumerate(ps) if norm(txt(p)).startswith(norm(R194))]
        if not h:
            i194,p194=find(ps,'İbnü’l-Cezerî’nin daha sonra sistemleştirdiği “üç şart” tespitinden önce')
            i195,p195=find(ps,'Sağlam rivâyet (naklin güvenirliği),')
            i196,p196=find(ps,'Arap diline uygunluk,')
            i197,p197=find(ps,'Mushaf yazısına aykırı olmama.')
            i198,p198=find(ps,'Bu nedenle İslâm âlimleri, İbnü’l-Cezerî’nin ortaya koyduğu ölçülerin köklerinin İbn Mücâhid')
            if [i195,i196,i197,i198]!=[i194+1,i194+2,i194+3,i194+4]: raise RuntimeError('F4-050 list cluster not contiguous')
            chunks(p194,[p194,p195,p196,p197,p198],[('t',R194),('fn',183)],[183])
            for q in [p195,p196,p197,p198]: body.remove(q)
            changed=True; already50=False
        ps=body.xpath('./w:p',namespaces=NS)
        R200a="İbnü’l-Cezerî, daha önce farklı bağlamlarda görülen bu ölçüleri en-Neşr’de daha sistematik biçimde formüle etmiştir. Ona göre sahih kırâat güvenilir nakle dayanmalı, Arap diline uygun olmalı ve Osmânî mushaflardan birinin resmine açık veya ihtimalî biçimde uymalıdır."
        R200b=" Resme uygunluk, sahih isnadın yerine geçen bağımsız bir ölçü değil, diğer şartlarla birlikte işleyen sınırlandırıcı bir kriterdir."
        h=[(i,p) for i,p in enumerate(ps) if norm(txt(p)).startswith(norm(R200a))]
        if not h:
            i200,p200=find(ps,'Kırâat ilminde sahih okuyuşların hangi ölçülere göre kabul edileceği meselesi')
            i201,p201=find(ps,'İbnü’l-Cezerî’nin yaklaşımında resm-i Osmânî, kırâatlerin sınırını belirleyen önemli bir ölçü olarak yer almaktadır.')
            if i201!=i200+1: raise RuntimeError('F4-050 Ibn Jazari pair not contiguous')
            chunks(p200,[p200,p201],[('t',R200a),('fn',185),('t',R200b),('fn',186)],[185,186])
            body.remove(p201); changed=True; already50=False
        ps=body.xpath('./w:p',namespaces=NS)
        R202a="Zerkeşî, İbnü’l-Cezerî’den önce, mushaf yazısına uygunluğu kırâat değerlendirmesinde önemli bir unsur olarak ele almıştır."
        h=[(i,p) for i,p in enumerate(ps) if norm(txt(p)).startswith(norm(R202a))]
        if not h:
            i202,p202=find(ps,'İbnü’l-Cezerî’nin sahih kırâatler için ortaya koyduğu prensipler, sonraki dönem kırâat birikiminde geniş kabul görmüştür.')
            chunks(p202,[p202],[('t',R202a),('fn',187),('t',' Suyûtî de daha sonraki ulûmu’l-Kur’ân literatüründe bu ölçüyü aktarır.'),('fn',188),('t',' Ayrıca Sehâvî ve Ebû Şâme’ye nispet edilen açıklamalar, resmle bağdaşma şartının İbnü’l-Cezerî’den önceki literatürde de tartışıldığını göstermektedir.'),('fn',189),('t',' Dolayısıyla bu isimleri İbnü’l-Cezerî’nin sonradan takipçileri gibi sıralamak yerine, ölçünün farklı dönemlerdeki formülasyonlarını kendi kronolojik bağlamlarında değerlendirmek gerekir.')],[187,188,189]); changed=True; already50=False
        res.append(('F4-050',i50,'ALREADY_SATISFIED' if already50 else 'STRUCTURALLY_APPLIED'))

        R51="Resm-i Osmânî'nin kırâatlerin değerlendirilmesinde yazılı bir ölçü hâline gelmesi, bu ölçünün sözlü rivâyet düzeni içindeki yerini ayrıca açıklamayı gerekli kılar. İkinci bölüm bu sebeple kırâatlerin rivâyet mantığına yönelmektedir."
        ps=body.xpath('./w:p',namespaces=NS); h=[(i,p) for i,p in enumerate(ps) if norm(txt(p))==norm(R51)]
        if h: i51,p51=h[0]; st51='ALREADY_SATISFIED'
        else:
            i203,p203=find(ps,'Sonuç olarak Hz. Osman döneminde gerçekleştirilen istinsah faaliyetleri, yalnızca mushafların çoğaltılmasıyla sınırlı kalmamış')
            if i203+1>=len(ps): raise RuntimeError('F4-051 no following paragraph')
            p51=ps[i203+1]
            if norm(txt(p51)) or any(spec(p51).values()): raise RuntimeError('F4-051 expected safe blank paragraph')
            add(p51,R51,first_rpr(p203)); i51=i203+1; changed=True; st51='APPLIED'
        res.append(('F4-051',i51,st51))

        ps=body.xpath('./w:p',namespaces=NS)
        new52="Kur’an'ın okunmasına ilişkin farklı edâ biçimleri erken dönemden itibaren rivâyet yoluyla aktarılmış; bu malzeme sonraki süreçte müstakil kırâat literatürü ve tasnifleri içinde sistemleştirilmiştir. Bu nedenle kırâat rivâyetinin tarihi ile kırâat ilminin bağımsız bir disiplin hâline gelme süreci birbirinden ayrılmalıdır."
        h=[(i,p) for i,p in enumerate(ps) if norm(new52) in norm(txt(p))]
        if h: i52,p52=h[0]; st52='ALREADY_SATISFIED'
        else:
            i52,p52=find(ps,'Kırâat ilmi bağımsız bir disiplin hâline hicrî II. ve III. yüzyıllarda gelmiştir.')
            st52=span(p52,'Kırâat ilmi bağımsız bir disiplin hâline hicrî II. ve III. yüzyıllarda gelmiştir.',new52); changed |= st52=='APPLIED'
        res.append(('F4-052',i52,st52))

        if not changed:
            shutil.copyfile(src,out); return res
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
    validate_same_structures(src,out)
    return res

if __name__=='__main__':
    for row in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,row)))
