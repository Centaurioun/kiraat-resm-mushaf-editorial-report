# F5-002 correction note — prior metadata adjudication superseded

A source-order verification found that the previously checkpointed F5-002 metadata had been bound to the wrong Fifth Report issue.

## What happened

The previous F5-002 checkpoint treated an unsupported cem/istinsah motive-attribution issue as F5-002 and recorded `VERIFIED_NO_CHANGE`.

The locked Fifth Report shows that the actual F5-002 item is instead the Giriş sentence:

`Bu sorular birbirinden bağımsız değildir.`

with the stylistic objective of expressing the relation positively.

## Safety impact

No manuscript corruption resulted from the misbinding:

- the wrongly bound F5-002 operation was a byte-identical no-op;
- the current durable F5-002 binary at that checkpoint was byte-for-byte identical to the globally validated Fourth/F5-001 binary;
- no incorrect Fifth wording was inserted into the manuscript.

## Corrected interpretation

Current P22 still begins with the actual F5-002 target sentence. The safe correction is narrowly scoped:

`Bu sorular birbirinden bağımsız değildir.`

→

`Araştırma soruları birbirine bağlıdır.`

The following accepted Fourth-scientific sentences are to be preserved rather than replaced by the Fifth Report's broader causal formulation.

## Durable-boundary rule

Until this actual P22 edit passes deterministic replay, structural validation, human visual QA, and checkpoint completion:

- last durable Fifth item = F5-001;
- F5-002 = PENDING;
- F5-003 must not be started.

This correction note supersedes the earlier F5-002 no-op adjudication as the authoritative interpretation of Fifth Report item numbering.
