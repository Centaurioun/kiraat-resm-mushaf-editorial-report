# F4-W10 Deterministic Replay Specification

## Certification / use gate

`CANDIDATE_REPLAY_ONLY — DEPENDENCY_BLOCKED`

This script has **not** been certified on the contract-required reconstructed F4-047 binary. Do not treat it as integration-ready. First reconstruct F4-047 with the existing replay pipeline, verify exact SHA-256 `6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7`, then audit/run this candidate replay. If that prerequisite fails, stop.

Replay artifact: `parallel/results/fourth/F4-W10/replay_f4_w10.py`

## Scope

The replay implements only F4-112, F4-114, F4-115 and F4-116. It does not implement or alter F4-111/F4-113, any other Fourth item, any Fifth item, the ledger, canonical branch selection, or integrator-owned state.

## Worker-proof invocation after dependency resolution

```bash
python parallel/results/fourth/F4-W10/replay_f4_w10.py \
  /path/to/F4-047.docx /tmp/F4-W10.docx \
  --require-f4-047-sha \
  --report-json /tmp/F4-W10-report.json
```

`--require-f4-047-sha` rejects any input whose SHA-256 is not exactly `6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7`.

## Intended transformations (not yet certified on F4-047)

1. F4-112: target genuine footnotes 32/41/105 and remove only the exact stale work-note tails.
2. F4-114: remove the unresolved malformed Kahraman DOI without inventing a replacement; normalize the duplicated Maşalı DOI resolver; never rewrite a protected field instruction.
3. F4-115: remove only the two repository-evidence-unused editions; require all authorized keep-edition anchors to remain.
4. F4-116: preserve both Ebû Şâme editions and require the current 1993/full and 1975/short citation anchors.

## Intended protected invariants

The candidate replay compares pre/post footnote IDs/references, field instructions and counts, Zotero markers, bookmarks, RTL markers, sections, comments/revisions, package members, XML parseability and protected OOXML parts. Unexpected change causes failure.

## Required idempotency proof after dependency resolution

Replay the genuine F4-047 once, replay the resulting DOCX a second time, and require byte-identical first/second outputs. The worker contract's technical validation and visual QA must then be completed before any `READY_FOR_INTEGRATION` disposition is possible.
