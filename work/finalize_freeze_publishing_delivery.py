#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
import hashlib, shutil, sys

EXPECTED='67fc2e5e047957c2dd7ece5f065e612e1b51a331c9894bbb9d20d9b5b49e09f4'

def main():
    src=Path(sys.argv[1]); dst=Path(sys.argv[2])
    data=src.read_bytes(); sha=hashlib.sha256(data).hexdigest()
    assert sha==EXPECTED,(sha,EXPECTED)
    with ZipFile(src) as z:
        assert z.testzip() is None
        assert 'word/document.xml' in z.namelist()
        assert 'word/footnotes.xml' in z.namelist()
    dst.parent.mkdir(parents=True,exist_ok=True)
    dst.write_bytes(data)
    assert dst.read_bytes()==data
    print('FINALIZATION_ITEM4_PUBLISHING_FREEZE BYTE_COPY')
    print(f'SOURCE_SHA256={sha}')
    print(f'DELIVERY_SHA256={hashlib.sha256(dst.read_bytes()).hexdigest()}')
    print(f'FILE_SIZE_BYTES={len(data)}')
    print('BYTE_IDENTICAL_TO_ITEM3_CANDIDATE=PASS')
    print('NO_MANUSCRIPT_MUTATION=PASS')

if __name__=='__main__':
    main()
