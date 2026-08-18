#!/usr/bin/env python3
from pathlib import Path
import hashlib, shutil, sys
EXPECTED='ffd4c4e8fabd7bd157cd21251f18da065e5466ecce357b63efe80361a18e4543'
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
if len(sys.argv)!=3: raise SystemExit('usage: inspect_f5_remaining_batch.py INPUT OUTPUT')
src=Path(sys.argv[1]); out=Path(sys.argv[2]); got=sha(src)
if got!=EXPECTED: raise RuntimeError(f'input sha mismatch {got}')
shutil.copyfile(src,out)
if sha(out)!=got: raise RuntimeError('copy mismatch')
print('F5-REMAINING\tIDENTITY_INSPECTION\tPASS')
