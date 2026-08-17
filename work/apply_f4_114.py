#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil, sys

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
NS={'w':W}

K_BAD='https://doi.org/http://doi.org/1051702/esoguifd.791085'
M_BAD='https://doi.org/https://doi.org/10.56361/usul.173700'
M_GOOD='https://doi.org/10.56361/usul.173700'


def ptext(p):
    return ''.join(p.xpath('.//w:t/text()',namespaces=NS))


def sig(el):
    return tuple((n.tag,tuple(sorted(n.attrib.items()))) for n in el.iter())


def c14n(el):
    return etree.tostring(el,method='c14n')


def replace_range(p,start,end,new):
    nodes=p.xpath('.//w:t',namespaces=NS)
    vals=[n.text or '' for n in nodes]
    starts=[]; cur=0
    for v in vals:
        starts.append(cur); cur+=len(v)
    if not (0 <= start < end <= cur):
        raise RuntimeError(f'invalid replacement span {start}:{end}/{cur}')
    fi=next(i for i,(st,v) in enumerate(zip(starts,vals)) if start < st+len(v))
    li=next(i for i,(st,v) in enumerate(zip(starts,vals)) if end <= st+len(v))
    touched=nodes[fi:li+1]
    for n in touched:
        if n.xpath('ancestor::w:hyperlink',namespaces=NS):
            raise RuntimeError('target DOI occurs inside w:hyperlink; hold for relationship-aware handling')
    prefix=vals[fi][:start-starts[fi]]
    suffix=vals[li][end-starts[li]:]
    nodes[fi].text=prefix+new+(suffix if fi==li else '')
    if fi!=li:
        for j in range(fi+1,li): nodes[j].text=''
        nodes[li].text=suffix


def instrs(zipf):
    out=[]
    for name in zipf.namelist():
        if name.startswith('word/') and name.endswith('.xml'):
            try: root=etree.fromstring(zipf.read(name))
            except Exception: continue
            out += [''.join(x.itertext()).strip() for x in root.xpath('//w:instrText',namespaces=NS)]
    return out


def locate(ps,needle,prefix):
    hits=[]
    for i,p in enumerate(ps):
        t=ptext(p)
        if needle in t: hits.append((i,p,t))
    if len(hits)!=1:
        raise RuntimeError(f'{needle!r} occurrence count {len(hits)} != 1')
    i,p,t=hits[0]
    if not t.startswith(prefix):
        raise RuntimeError(f'target at P{i} has unexpected record prefix: {t[:80]!r}')
    return i,p,t


def satisfied_doc(d):
    ps=d.xpath('.//w:body/w:p',namespaces=NS)
    txt='\n'.join(ptext(p) for p in ps)
    if K_BAD in txt or M_BAD in txt or txt.count(M_GOOD)!=1:
        return False
    if len(ps)!=676 or not ptext(ps[578]).endswith('11-36.'):
        return False
    return True


def apply(src,out):
    with ZipFile(src,'r') as zin:
        original={i.filename:zin.read(i.filename) for i in zin.infolist()}
        d=etree.fromstring(original['word/document.xml'])
        ps=d.xpath('.//w:body/w:p',namespaces=NS)
        if len(ps)!=676: raise RuntimeError(f'body paragraph count {len(ps)} != 676')
        if satisfied_doc(d):
            shutil.copyfile(src,out)
            validate(src,out,expect_change=False)
            print('F4-114\tALREADY_SATISFIED')
            return

        k_i,k_p,k_before=locate(ps,K_BAD,'Kahraman, Ferruh.')
        m_i,m_p,m_before=locate(ps,M_BAD,'Maşalı, Mehmet Emin.')
        k_sig=sig(k_p); m_sig=sig(m_p)

        k_token=' '+K_BAD
        k_pos=k_before.find(k_token)
        if k_pos<0: raise RuntimeError('Kahraman DOI is not preceded by expected single space')
        replace_range(k_p,k_pos,k_pos+len(k_token),'')

        m_pos=m_before.find(M_BAD)
        replace_range(m_p,m_pos,m_pos+len(M_BAD),M_GOOD)

        if sig(k_p)!=k_sig or sig(m_p)!=m_sig:
            raise RuntimeError('target paragraph OOXML structure changed')

        k_after=ptext(k_p); m_after=ptext(m_p)
        if K_BAD in k_after or not k_after.endswith('11-36.'):
            raise RuntimeError('Kahraman postcondition failed')
        if M_BAD in m_after or m_after.count(M_GOOD)!=1:
            raise RuntimeError('Maşalı postcondition failed')

        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist():
                zout.writestr(info,xml if info.filename=='word/document.xml' else original[info.filename])

    validate(src,out,expect_change=True)
    print(f'F4-114\tAPPLIED\tKAHRAMAN=P{k_i}\tMASALI=P{m_i}')
    print(f'KAHRAMAN_BEFORE\t{k_before}')
    print(f'KAHRAMAN_AFTER\t{k_after}')
    print(f'MASALI_BEFORE\t{m_before}')
    print(f'MASALI_AFTER\t{m_after}')


def validate(src,out,expect_change):
    with ZipFile(src) as za, ZipFile(out) as zb:
        if za.namelist()!=zb.namelist(): raise RuntimeError('ZIP member/order changed')
        if zb.testzip() is not None: raise RuntimeError('ZIP CRC failure')
        for name in za.namelist():
            if name!='word/document.xml' and za.read(name)!=zb.read(name):
                raise RuntimeError(f'unexpected package change: {name}')
            if name.endswith('.xml') or name.endswith('.rels'):
                etree.fromstring(zb.read(name))

        da=etree.fromstring(za.read('word/document.xml'))
        db=etree.fromstring(zb.read('word/document.xml'))
        pa=da.xpath('.//w:body/w:p',namespaces=NS); pb=db.xpath('.//w:body/w:p',namespaces=NS)
        if len(pa)!=676 or len(pb)!=676: raise RuntimeError('body paragraph count changed')

        changed=[]
        for i,(a,b) in enumerate(zip(pa,pb)):
            if c14n(a)!=c14n(b): changed.append(i)
        expected={578,599} if expect_change else set()
        if set(changed)!=expected:
            raise RuntimeError(f'unexpected changed body paragraphs: {changed}; expected={sorted(expected)}')
        for i in changed:
            if sig(pa[i])!=sig(pb[i]):
                raise RuntimeError(f'P{i} structure changed')

        ia=instrs(za); ib=instrs(zb)
        if ia!=ib or len(ib)!=520: raise RuntimeError('field instruction inventory changed')
        addin=sum(1 for x in ib if 'ADDIN ' in x)
        item=sum(1 for x in ib if 'ZOTERO_ITEM' in x)
        bibl=sum(1 for x in ib if 'ZOTERO_BIBL' in x)
        if (addin,item,bibl)!=(466,465,1):
            raise RuntimeError(f'Zotero/ADDIN field inventory changed: {(addin,item,bibl)}')

        ha=da.xpath('//w:hyperlink',namespaces=NS); hb=db.xpath('//w:hyperlink',namespaces=NS)
        if len(ha)!=52 or len(hb)!=52: raise RuntimeError(f'hyperlink count changed: {len(ha)}->{len(hb)}')
        if [sig(x) for x in ha] != [sig(x) for x in hb]: raise RuntimeError('hyperlink structure changed')

        ra=da.xpath('//w:footnoteReference/@w:id',namespaces=NS); rb=db.xpath('//w:footnoteReference/@w:id',namespaces=NS)
        if ra!=rb or len(rb)!=469 or len(set(rb))!=469: raise RuntimeError('footnote reference identity/order changed')
        if da.xpath('//w:bookmarkStart/@w:id',namespaces=NS)!=db.xpath('//w:bookmarkStart/@w:id',namespaces=NS): raise RuntimeError('bookmark starts changed')
        if da.xpath('//w:bookmarkEnd/@w:id',namespaces=NS)!=db.xpath('//w:bookmarkEnd/@w:id',namespaces=NS): raise RuntimeError('bookmark ends changed')
        if len(db.xpath('//w:bookmarkStart',namespaces=NS))!=53 or len(db.xpath('//w:bookmarkEnd',namespaces=NS))!=53: raise RuntimeError('bookmark count changed')
        if len(da.xpath('//w:rtl',namespaces=NS))!=len(db.xpath('//w:rtl',namespaces=NS)): raise RuntimeError('RTL inventory changed')

        if not satisfied_doc(db): raise RuntimeError('F4-114 postconditions not satisfied')

if __name__=='__main__':
    apply(Path(sys.argv[1]),Path(sys.argv[2]))
