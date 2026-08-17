#!/usr/bin/env python3
from pathlib import Path
import sys
import apply_f4_073_077 as batch

_original_whole=batch.h.whole

def _whole_with_rtl_preservation(p,text,expected_fn=()):
    s=batch.h.spec(p)
    if s['fn']==['281'] and s['rtl']==3 and list(expected_fn)==[281]:
        old=("Resm-i Osmânî’nin diğer özelliklerinden biri de, bazı kelimelerin bağlama göre farklı biçimlerde yazılması ve bu yazım farkının anlam farkına işaret etmesidir. "
             "Ulûmu’l-Kur’ân kaynaklarında bu husus, kelimenin bir yerde “maktu” yani ayrı, başka bir yerde “mevsûl” yani bitişik yazılmasıyla açıklanmıştır. "
             "Bu yazım farkı yalnızca yazıma dair bir tercih değildir, aynı zamanda nahivsel işlevi de yansıtmaktadır. ")
        st=batch.h.span(p,old,text+' ')
        # Keep the existing Arabic أم runs; only qualify the connective introducing their interpretation.
        st2=batch.h.span(p,'Zira ','Bu yorumlarda, ')
        if st not in ('APPLIED','ALREADY_SATISFIED') or st2 not in ('APPLIED','ALREADY_SATISFIED'):
            raise RuntimeError('F4-073 RTL-preserving opening rewrite failed')
        if batch.h.spec(p)['fn']!=['281'] or batch.h.spec(p)['rtl']!=3:
            raise RuntimeError('F4-073 RTL/footnote structure changed')
        return
    return _original_whole(p,text,expected_fn)

batch.h.whole=_whole_with_rtl_preservation

if __name__=='__main__':
    for row in batch.apply(Path(sys.argv[1]),Path(sys.argv[2])):
        print('\t'.join(map(str,row)))
