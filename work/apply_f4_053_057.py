#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from copy import deepcopy
from collections import Counter
import re,sys,shutil
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}

def norm(s): return re.sub(r'\s+',' ',(s or '').replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')).strip()
def txt(p): return ''.join(p.xpath('.//w:t/text()',namespaces=NS))
def spec(p): return {'fn':p.xpath('.//w:footnoteReference/@w:id',namespaces=NS),'instr':p.xpath('.//w:instrText/text()',namespaces=NS),'fld':len(p.xpath('.//w:fldChar',namespaces=NS)),'hyper':len(p.xpath('.//w:hyperlink',namespaces=NS)),'rtl':len(p.xpath('.//w:rtl',namespaces=NS)),'book':len(p.xpath('.//w:bookmarkStart|.//w:bookmarkEnd',namespaces=NS))}
def find(ps,a,starts=True):
    a=norm(a); h=[]
    for i,p in enumerate(ps):
        t=norm(txt(p)); ok=t.startswith(a) if starts else a in t
        if ok:h.append((i,p))
    if len(h)!=1: raise RuntimeError(f'anchor {a[:90]!r}: hits={len(h)}')
    return h[0]
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
        if c is not ppr:p.remove(c)
def add(p,s,rpr=None):
    r=etree.Element(f'{{{W}}}r')
    if rpr is not None:r.append(deepcopy(rpr))
    t=etree.SubElement(r,f'{{{W}}}t');t.text=s
    if s.startswith(' ') or s.endswith(' '):t.set('{http://www.w3.org/XML/1998/namespace}space','preserve')
    p.append(r)
def safe_plain(p):
    s=spec(p); return not (s['instr'] or s['fld'] or s['hyper'] or s['rtl'] or s['book'])
def whole(p,s,expected_fn=()):
    sp=spec(p)
    if sp['fn']!=list(map(str,expected_fn)) or not safe_plain(p): raise RuntimeError('unsafe whole '+str(sp))
    fr={}
    for r in p.xpath('./w:r',namespaces=NS):
        ids=r.xpath('.//w:footnoteReference/@w:id',namespaces=NS)
        if ids:fr[ids[0]]=deepcopy(r)
    rp=first_rpr(p); clear(p); add(p,s,rp)
    for f in expected_fn:p.append(fr[str(f)])
def span(p,a,r):
    before=spec(p); nodes=p.xpath('.//w:t',namespaces=NS); vals=[x.text or '' for x in nodes]; full=''.join(vals)
    cands=[a,a.replace("'",'’'),a.replace('’',"'")]; hits=[(full.find(x),x) for x in cands if full.find(x)>=0]
    if not hits:
        if norm(r) in norm(full): return 'ALREADY_SATISFIED'
        raise RuntimeError('span missing '+a[:100])
    pos,act=hits[0]; end=pos+len(act); starts=[]; c=0
    for v in vals:starts.append(c);c+=len(v)
    fi=next(i for i,(st,v) in enumerate(zip(starts,vals)) if pos<st+len(v)); li=next(i for i,(st,v) in enumerate(zip(starts,vals)) if end<=st+len(v))
    pre=vals[fi][:pos-starts[fi]];suf=vals[li][end-starts[li]:];nodes[fi].text=pre+r+(suf if fi==li else '')
    if fi!=li:
        for j in range(fi+1,li):nodes[j].text=''
        nodes[li].text=suf
    if spec(p)!=before:raise RuntimeError('protected structure changed')
    return 'APPLIED'
def instrs(z):
    out=[]
    for n in z.namelist():
        if n.startswith('word/') and n.endswith('.xml'):
            try:r=etree.fromstring(z.read(n));out += [''.join(x.itertext()).strip() for x in r.xpath('//w:instrText',namespaces=NS)]
            except:pass
    return out
def validate(src,out):
    prot=['word/footnotes.xml','word/styles.xml','word/numbering.xml','word/settings.xml','word/_rels/document.xml.rels']
    with ZipFile(src) as zs,ZipFile(out) as z:
        assert z.testzip() is None
        for n in z.namelist():
            if n.endswith('.xml') or n.endswith('.rels'):etree.fromstring(z.read(n))
        ds=etree.fromstring(zs.read('word/document.xml'));d=etree.fromstring(z.read('word/document.xml'));fs=etree.fromstring(zs.read('word/footnotes.xml'));f=etree.fromstring(z.read('word/footnotes.xml'))
        f0=[x for x in fs.xpath('//w:footnote/@w:id',namespaces=NS) if int(x)>0];ff=[x for x in f.xpath('//w:footnote/@w:id',namespaces=NS) if int(x)>0];r0=ds.xpath('//w:footnoteReference/@w:id',namespaces=NS);rr=d.xpath('//w:footnoteReference/@w:id',namespaces=NS)
        assert ff==f0 and rr==r0 and len(ff)==len(rr)==469 and set(ff)==set(rr) and not [k for k,v in Counter(rr).items() if v>1]
        assert instrs(z)==instrs(zs) and len(instrs(z))==520
        assert len(d.xpath('//w:rtl',namespaces=NS))==len(ds.xpath('//w:rtl',namespaces=NS))
        assert len(d.xpath('//w:bookmarkStart',namespaces=NS))==len(ds.xpath('//w:bookmarkStart',namespaces=NS)) and len(d.xpath('//w:bookmarkEnd',namespaces=NS))==len(ds.xpath('//w:bookmarkEnd',namespaces=NS))
        assert len(d.xpath('//w:hyperlink',namespaces=NS))==len(ds.xpath('//w:hyperlink',namespaces=NS))
        for n in prot:assert zs.read(n)==z.read(n),n
        body='\n'.join(txt(p) for p in d.xpath('.//w:body/w:p',namespaces=NS))
        req=[
          'Kırâatin rivâyet temelli bu yapısı, okuyuşların hangi aktarım zincirleri ve ilmî otoriteler üzerinden nakledildiği sorusunu öne çıkarmaktadır.',
          'Kırâatlerin aktarımında aslî zemin telakki, müşâfehe ve edâya dayanan sözlü rivâyettir.',
          'Mesela “Âsım kırâati” denildiğinde yalnız Âsım’a nispet edilen okuyuş bütünü değil',
          'Rivâyet, bir okuyuşun belirli râviler aracılığıyla nakledilen aktarım hattını ifade eder.',
          'Sened, bu naklin kimlerden kimlere ulaştığını gösteren râvi zinciridir.',
          'Otorite ise okuyuşun öğretim ve aktarım geleneği içinde tanınan imam, râvi ve tarîklerle ilişkilendirilmesini ifade eder.',
          'Kırâatlerde otoritenin bu çok katmanlı yapısı, sözlü aktarımın müşterek mushaf yazısıyla nasıl ilişkilendiği sorusunu gündeme getirir.'
        ]
        for x in req:
            if norm(x) not in norm(body):raise RuntimeError('missing postcondition '+x)
        stale=['Netice itibarıyla kırâat kavramı','Bu durum kırâat ilminin baştan itibaren yazılı değil','Âsım’ın tercih ettiği okuyuş biçimi','Kırâat ilmini anlamanın en sağlam yollarından biri, onu sadece','Kırâat ilmini ayakta tutan en temel unsurlardan biri seneddir. Çünkü kırâat sadece','Kırâat ilmini yalnızca “Kur’an’ın farklı okuma biçimleri” olarak görmek','Sonuç olarak kırâatlerde otorite ekseni']
        for x in stale:
            if norm(x) in norm(body):raise RuntimeError('stale postcondition '+x)

def apply(src,out):
    with ZipFile(src) as zin:
        d=etree.fromstring(zin.read('word/document.xml'));body=d.find('.//w:body',namespaces=NS);changed=False;res=[]
        R53='Kırâatin rivâyet temelli bu yapısı, okuyuşların hangi aktarım zincirleri ve ilmî otoriteler üzerinden nakledildiği sorusunu öne çıkarmaktadır. Bu sebeple bir sonraki başlıkta rivâyet, sened ve otorite ekseni ayrı ayrı ele alınacaktır.'
        ps=body.xpath('./w:p',namespaces=NS);h=[(i,p) for i,p in enumerate(ps) if norm(txt(p))==norm(R53)]
        if h:i53,p=h[0];st='ALREADY_SATISFIED'
        else:i53,p=find(ps,'Netice itibarıyla kırâat kavramı');whole(p,R53);changed=True;st='APPLIED'
        res.append(('F4-053',i53,st))

        new54="Kırâatlerin aktarımında aslî zemin telakki, müşâfehe ve edâya dayanan sözlü rivâyettir. Bununla birlikte Kur’an'ın yazılı kaydı ve mushaf geleneği bu aktarımın dışında değildir; yazı, rivâyet edilen okuyuşların müşterek metinle ilişkisini gösteren tamamlayıcı bir çerçeve sağlamıştır."
        ps=body.xpath('./w:p',namespaces=NS);hits=[(i,p) for i,p in enumerate(ps) if norm(new54) in norm(txt(p))]
        if hits:i54,p=hits[0];st='ALREADY_SATISFIED'
        else:
            i54,p=find(ps,'İlk dönemden itibaren Kur’an Hz. Peygamber tarafından ashâba okunarak öğretilmiş')
            if spec(p)['fn']!=['204']:raise RuntimeError('F4-054 note mismatch '+str(spec(p)))
            old='İlk dönemden itibaren Kur’an Hz. Peygamber tarafından ashâba okunarak öğretilmiş; ashâb da Kur’an’ı hem ezberleyerek hem de okuyarak sonraki nesillere aktarmıştır. Bu durum kırâat ilminin baştan itibaren yazılı değil, birebir öğretim geleneği içinde geliştiğini göstermektedir.'
            st=span(p,old,new54);changed|=st=='APPLIED'
        res.append(('F4-054',i54,st))

        new55='Mesela “Âsım kırâati” denildiğinde yalnız Âsım’a nispet edilen okuyuş bütünü değil, bu okuyuşun Hafs ve Şu‘be gibi râviler vasıtasıyla sonraki nesillere nasıl aktarıldığı da anlaşılır. Bu nispet, imamın okuyuşu serbest biçimde meydana getirdiği anlamına değil, ilgili rivâyet ve öğretim geleneğinin onun adı etrafında tanınıp nakledildiğine işaret eder.'
        ps=body.xpath('./w:p',namespaces=NS);hits=[(i,p) for i,p in enumerate(ps) if norm(new55) in norm(txt(p))]
        if hits:i55,p=hits[0];st='ALREADY_SATISFIED'
        else:
            i55,p=find(ps,'Diğer bir anlatımla sened, bir okuyuş biçiminin hangi hocadan hangi talebeye geçtiğini gösteren rivâyet zinciridir.')
            if spec(p)['fn']!=['207']:raise RuntimeError('F4-055 note mismatch '+str(spec(p)))
            old='Mesela “Âsım (ö. 127/745) kırâati” denildiğinde burada sadece Âsım’ın tercih ettiği okuyuş biçimi değil, bu okuyuşun ondan Hafs (ö. 180/796) ve Şu’be (ö. 193/809) gibi râviler vasıtasıyla nasıl aktarıldığı da anlatılmış olur.'
            st=span(p,old,new55);changed|=st=='APPLIED'
        res.append(('F4-055',i55,st))

        R56='Rivâyet, bir okuyuşun belirli râviler aracılığıyla nakledilen aktarım hattını ifade eder. Sened, bu naklin kimlerden kimlere ulaştığını gösteren râvi zinciridir. Otorite ise okuyuşun öğretim ve aktarım geleneği içinde tanınan imam, râvi ve tarîklerle ilişkilendirilmesini ifade eder. Bu üç unsur birbirine bağlı olmakla birlikte aynı kavram değildir.'
        ps=body.xpath('./w:p',namespaces=NS);h=[(i,p) for i,p in enumerate(ps) if norm(txt(p))==norm(R56)]
        if h:i56,p=h[0];st56='ALREADY_SATISFIED'
        else:i56,p=find(ps,'Kırâat ilmini anlamanın en sağlam yollarından biri');whole(p,R56);changed=True;st56='STRUCTURALLY_APPLIED'
        # Direct subsection openings: remove the repeated negative-definition formula while preserving source-backed continuations and notes.
        ps=body.xpath('./w:p',namespaces=NS);iR,pR=find(ps,'Kırâat ilminde “rivâyet” meselesi işin bel kemiğini teşkil eder.') if any(norm(txt(q)).startswith(norm('Kırâat ilminde “rivâyet” meselesi işin bel kemiğini teşkil eder.')) for q in ps) else find(ps,'Rivâyet, bir okuyuşun belirli râviler aracılığıyla nakledilen aktarım hattını ifade eder;')
        if not norm(txt(pR)).startswith(norm('Rivâyet, bir okuyuşun belirli râviler aracılığıyla nakledilen aktarım hattını ifade eder;')):
            old='Kırâat ilminde “rivâyet” meselesi işin bel kemiğini teşkil eder. Çünkü kırâat yalnızca Kur’an kelimelerinin farklı okunma biçimlerini sıralayan bir alan değildir; asıl olarak bu okuyuş biçimlerinin kimden alındığını, nasıl aktarıldığını ve hangi yollarla güven kazandığını konu edinir.'
            span(pR,old,'Rivâyet, bir okuyuşun belirli râviler aracılığıyla nakledilen aktarım hattını ifade eder; bu başlık okuyuş biçimlerinin kimden alındığını, nasıl aktarıldığını ve hangi yollarla güven kazandığını konu edinir.');changed=True;st56='STRUCTURALLY_APPLIED'
        ps=body.xpath('./w:p',namespaces=NS);iS,pS=find(ps,'Kırâat ilmini ayakta tutan en temel unsurlardan biri seneddir.') if any(norm(txt(q)).startswith(norm('Kırâat ilmini ayakta tutan en temel unsurlardan biri seneddir.')) for q in ps) else find(ps,'Sened, bu naklin kimlerden kimlere ulaştığını gösteren râvi zinciridir.')
        if not norm(txt(pS)).startswith(norm('Sened, bu naklin kimlerden kimlere ulaştığını gösteren râvi zinciridir.')):
            old='Kırâat ilmini ayakta tutan en temel unsurlardan biri seneddir. Çünkü kırâat sadece kelimelerin farklı okunma biçimlerini gösteren bir alan değildir, aynı zamanda bu okuyuşların kimden alındığını, hangi yolla aktarıldığını ve ne kadar güvenilir olduğunu araştıran bir ilimdir.'
            span(pS,old,'Sened, bu naklin kimlerden kimlere ulaştığını gösteren râvi zinciridir.');changed=True;st56='STRUCTURALLY_APPLIED'
        ps=body.xpath('./w:p',namespaces=NS);iO,pO=find(ps,'Kırâat ilmini yalnızca “Kur’an’ın farklı okuma biçimleri” olarak görmek') if any(norm(txt(q)).startswith(norm('Kırâat ilmini yalnızca “Kur’an’ın farklı okuma biçimleri” olarak görmek')) for q in ps) else find(ps,'Otorite ise okuyuşun öğretim ve aktarım geleneği içinde tanınan imam, râvi ve tarîklerle ilişkilendirilmesini ifade eder.')
        if not norm(txt(pO)).startswith(norm('Otorite ise okuyuşun öğretim ve aktarım geleneği içinde tanınan imam, râvi ve tarîklerle ilişkilendirilmesini ifade eder.')):
            old='Kırâat ilmini yalnızca “Kur’an’ın farklı okuma biçimleri” olarak görmek, bu alanın asıl yapısını tam olarak yansıtmaz. Çünkü kırâat ilmi, sadece farklılıkları kaydeden bir alan değil, aynı zamanda hangi okuyuşun güvenilir sayılacağını, hangi imamın okuyuşunun esas alınacağını, hangi rivâyetin kabul göreceğini ve hangi okuyuşun sahih kırâat dairesi içinde değerlendirileceğini belirleyen köklü bir ilim geleneğidir. Bu sebeple kırâat tarihinde “otorite” meselesi son derece önemlidir.'
            span(pO,old,'Otorite ise okuyuşun öğretim ve aktarım geleneği içinde tanınan imam, râvi ve tarîklerle ilişkilendirilmesini ifade eder.');changed=True;st56='STRUCTURALLY_APPLIED'
        res.append(('F4-056',i56,st56))

        R57='Kırâatlerde otoritenin bu çok katmanlı yapısı, sözlü aktarımın müşterek mushaf yazısıyla nasıl ilişkilendiği sorusunu gündeme getirir. Bu ilişki, yedi harf ile Osmânî mushaf meselesinde daha belirgin hâle gelmektedir.'
        ps=body.xpath('./w:p',namespaces=NS);h=[(i,p) for i,p in enumerate(ps) if norm(txt(p))==norm(R57)]
        if h:i57,p=h[0];st='ALREADY_SATISFIED'
        else:i57,p=find(ps,'Sonuç olarak kırâatlerde otorite ekseni');whole(p,R57);changed=True;st='APPLIED'
        res.append(('F4-057',i57,st))

        if not changed:shutil.copyfile(src,out);return res
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist():zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
    validate(src,out);return res
if __name__=='__main__':
    for row in apply(Path(sys.argv[1]),Path(sys.argv[2])):print('\t'.join(map(str,row)))
