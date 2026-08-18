#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil, sys

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}; XMLSPACE='{http://www.w3.org/XML/1998/namespace}space'
PREFIX='İbnü’l-Cezerî’nin tanımında belirginleştiği üzere kırâat, Kur’an kelimelerinin edâ keyfiyetlerini ve bu keyfiyetlerdeki farklılıkları nakledenlere nispet ederek bilmeyi ifade eden bir rivâyet disiplinidir. '
OLD='Bir kırâat imamına nispet edilen genel okuyuş sistemi, bu okuyuşun belirli bir râvi üzerinden aktarılan rivâyeti ve râviden sonraki nakil kollarını gösteren tarîklerle aynı düzeyde değildir. Vecih ise belirli bir rivâyet veya tarîk içinde edâ bakımından câiz görülen uygulama seçeneğini belirtir.'
NEW='Kırâat, rivâyet, tarîk ve vecih, aktarım zincirinin farklı düzeylerini gösterir: kırâat imama, rivâyet râviye, tarîk râviden sonraki nakil koluna, vecih ise ilgili rivâyet veya tarîk içindeki edâ seçeneğine işaret eder.'
SUFFIX=' Telakki, okuyuşun ehil hocadan alınmasını; müşâfehe bunun yüz yüze ve ağızdan ağıza gerçekleşen yönünü; edâ ise lafzın fiilen icrasını anlatır. Bu ayrımlar, mushaf yazısının sağladığı imkân ile kırâatin rivâyet yoluyla sabit oluşunu birbirine karıştırmamak bakımından zorunludur.'

def text(el): return ''.join(el.xpath('.//w:t/text()',namespaces=NS))
def c14n(el): return etree.tostring(el,method='c14n')
def sig_no_xmlspace(el):
    out=[]
    for n in el.iter():
        attrs=tuple(sorted((k,v) for k,v in n.attrib.items() if k!=XMLSPACE))
        out.append((n.tag,attrs))
    return tuple(out)

def instrs(z):
    out=[]
    for name in z.namelist():
        if name.startswith('word/') and name.endswith('.xml'):
            try:r=etree.fromstring(z.read(name))
            except Exception:continue
            out += [''.join(x.itertext()).strip() for x in r.xpath('//w:instrText',namespaces=NS)]
    return out

def telakki_nodes(p):
    return [n for n in p.xpath('.//w:t',namespaces=NS) if (n.text or '').startswith(' Telakki,')]

def whitespace_ok(p):
    hits=telakki_nodes(p)
    return len(hits)==1 and hits[0].get(XMLSPACE)=='preserve'

def replace_range(p,start,end,new):
    nodes=p.xpath('.//w:t',namespaces=NS); vals=[n.text or '' for n in nodes]
    starts=[]; cur=0
    for v in vals: starts.append(cur); cur+=len(v)
    fi=next(i for i,(st,v) in enumerate(zip(starts,vals)) if start < st+len(v))
    li=next(i for i,(st,v) in enumerate(zip(starts,vals)) if end <= st+len(v))
    for n in nodes[fi:li+1]:
        if n.xpath('ancestor::w:hyperlink',namespaces=NS): raise RuntimeError('F5-007 target inside hyperlink')
    prefix=vals[fi][:start-starts[fi]]; suffix=vals[li][end-starts[li]:]
    nodes[fi].text=prefix+new+(suffix if fi==li else '')
    if fi!=li:
        for j in range(fi+1,li): nodes[j].text=''
        nodes[li].text=suffix

def satisfied(d):
    ps=d.xpath('.//w:body/w:p',namespaces=NS); t=text(ps[25]) if len(ps)>25 else ''
    return len(ps)==674 and t==PREFIX+NEW+SUFFIX and OLD not in t and whitespace_ok(ps[25])

def apply(src,out):
    with ZipFile(src,'r') as zin:
        original={i.filename:zin.read(i.filename) for i in zin.infolist()}
        d=etree.fromstring(original['word/document.xml']); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        if len(ps)!=674: raise RuntimeError(f'body paragraph count {len(ps)} !=674')
        if satisfied(d):
            shutil.copyfile(src,out); validate(src,out,False); print('F5-007\tALREADY_SATISFIED'); return
        p=ps[25]; before=text(p); expected=PREFIX+OLD+SUFFIX
        if before!=expected: raise RuntimeError('P25 no longer matches exact F5-007 precondition')
        before_sig=sig_no_xmlspace(p)
        s=before.index(OLD); replace_range(p,s,s+len(OLD),NEW)
        hits=telakki_nodes(p)
        if len(hits)!=1: raise RuntimeError(f'Telakki whitespace node count {len(hits)} !=1')
        hits[0].set(XMLSPACE,'preserve')
        after=text(p)
        if after!=PREFIX+NEW+SUFFIX: raise RuntimeError('F5-007 postcondition failed')
        if sig_no_xmlspace(p)!=before_sig: raise RuntimeError('P25 structure changed beyond xml:space preservation')
        if not whitespace_ok(p): raise RuntimeError('Telakki boundary whitespace not preserved')
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else original[info.filename])
    validate(src,out,True)
    print('F5-007\tAPPLIED\tP25')
    print('BEFORE\t'+before)
    print('AFTER\t'+after)
    print('WHITESPACE\tTelakki run xml:space=preserve')
    print('SCOPE\tOnly the negative hierarchy sentence and adjacent vecih sentence were consolidated; source definition and Telakki+ remainder preserved.')

def validate(src,out,expect_change):
    with ZipFile(src) as za, ZipFile(out) as zb:
        if za.namelist()!=zb.namelist(): raise RuntimeError('ZIP member/order changed')
        if zb.testzip() is not None: raise RuntimeError('ZIP CRC failure')
        for name in za.namelist():
            if name!='word/document.xml' and za.read(name)!=zb.read(name): raise RuntimeError(f'unexpected package change: {name}')
            if name.endswith('.xml') or name.endswith('.rels'): etree.fromstring(zb.read(name))
        da=etree.fromstring(za.read('word/document.xml')); db=etree.fromstring(zb.read('word/document.xml'))
        pa=da.xpath('.//w:body/w:p',namespaces=NS); pb=db.xpath('.//w:body/w:p',namespaces=NS)
        if len(pa)!=674 or len(pb)!=674: raise RuntimeError('body count changed')
        changed=[i for i,(a,b) in enumerate(zip(pa,pb)) if c14n(a)!=c14n(b)]
        expected=[25] if expect_change else []
        if changed!=expected: raise RuntimeError(f'changed paragraphs {changed} != expected {expected}')
        if sig_no_xmlspace(pa[25])!=sig_no_xmlspace(pb[25]): raise RuntimeError('P25 structure changed beyond allowed xml:space attribute')
        if not satisfied(db): raise RuntimeError('F5-007 corrected-state postcondition failed')
        ia=instrs(za); ib=instrs(zb)
        if ia!=ib or len(ib)!=520: raise RuntimeError('field instruction inventory changed')
        addin=sum('ADDIN ' in x for x in ib); item=sum('ZOTERO_ITEM' in x for x in ib); bib=sum('ZOTERO_BIBL' in x for x in ib)
        if (addin,item,bib)!=(466,465,1): raise RuntimeError('ADDIN/Zotero inventory changed')
        ra=da.xpath('//w:footnoteReference/@w:id',namespaces=NS); rb=db.xpath('//w:footnoteReference/@w:id',namespaces=NS)
        if ra!=rb or len(rb)!=469 or len(set(rb))!=469: raise RuntimeError('footnote references changed')
        if da.xpath('//w:bookmarkStart/@w:id',namespaces=NS)!=db.xpath('//w:bookmarkStart/@w:id',namespaces=NS): raise RuntimeError('bookmark starts changed')
        if da.xpath('//w:bookmarkEnd/@w:id',namespaces=NS)!=db.xpath('//w:bookmarkEnd/@w:id',namespaces=NS): raise RuntimeError('bookmark ends changed')
        if len(db.xpath('//w:hyperlink',namespaces=NS))!=52: raise RuntimeError('hyperlink inventory changed')
        if len(da.xpath('//w:rtl',namespaces=NS))!=len(db.xpath('//w:rtl',namespaces=NS)): raise RuntimeError('RTL inventory changed')

if __name__=='__main__': apply(Path(sys.argv[1]),Path(sys.argv[2]))
