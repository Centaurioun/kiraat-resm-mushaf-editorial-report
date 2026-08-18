#!/usr/bin/env python3
from pathlib import Path
import json, subprocess
R=Path('.')
b=json.loads((R/'work/CHECKPOINT-BULK-SPEC.json').read_text(encoding='utf-8'))
updates={}
applied={int(k):v for k,v in b.get('applied_paragraphs',{}).items()}
for n in range(int(b['start_f5']),int(b['last_f5'])+1):
    iid=f'F5-{n:03d}'
    if n in applied:
        updates[iid]={
            'status':'APPLIED','section':f'Fifth Report item {n}',
            'action_type':'TARGETED_FIFTH_STYLE_SCIENTIFIC_REWRITE',
            'resolved_location':'word/document.xml P'+','.join(str(x) for x in applied[n]),
            'affected_body_paragraphs':applied[n],
            'verification':b['verification_applied'],
            'notes':b['notes_applied']
        }
    else:
        updates[iid]={
            'status':'VERIFIED_NO_CHANGE','section':f'Fifth Report item {n}',
            'action_type':'FOURTH_PRECEDENCE_OR_CURRENT_TEXT_SATISFIED_NOOP',
            'resolved_location':'current durable manuscript inspected in locked sequence',
            'affected_body_paragraphs':[],
            'verification':b['verification_noop'],
            'notes':b['notes_noop']
        }
spec={k:v for k,v in b.items() if k not in {'start_f5','applied_paragraphs','verification_applied','verification_noop','notes_applied','notes_noop'}}
spec['updates']=updates
(R/'work/CHECKPOINT-BATCH-SPEC.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
subprocess.run(['python','work/checkpoint_fifth.py'],check=True)
