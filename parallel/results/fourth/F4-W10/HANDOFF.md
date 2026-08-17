# F4-W10 Integrator Handoff

## Final worker disposition

`DEPENDENCY_BLOCKED`

This handoff is authoritative for W10. It **supersedes** the earlier intermediate commit `da497468e09a882eeab77c84e98d02d816cd25bb`, which prematurely used `READY_FOR_INTEGRATION` before the mandatory baseline rule was rechecked.

## Exact payload commit

`59a0d15c85165f4be7dc7c282c3cc0f39d893443`

That commit contains the corrected task receipt, item results, citation map, candidate replay specification, technical validation record and visual-QA status. The worker branch is:

`worker/f4/w10-footnotes-bibliography`

Orchestration base:

`5e7bdf4cd24d45e06e733da87b2e695c75751226`

## Blocking dependency

`parallel/WORKER-CONTRACT.md` section 3 requires a Fourth worker to reconstruct logical F4-047 from the canonical source plus existing replay pipeline and verify exact SHA-256:

`6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7`

The DOCX binary was visible in GitHub metadata/base64, but this runtime could not materialize it into the local execution container. W10 therefore could not perform the required reconstruction/hash check. By contract, assigned edits cannot be treated as applied or integration-ready.

## Assigned-item state

- `F4-112` — `DEPENDENCY_BLOCKED`; provisional mapping identifies genuine footnotes 32/41/105 and the exact editorial-note tails to remove, but no real F4-047 application/validation occurred.
- `F4-114` — `DEPENDENCY_BLOCKED`; repository evidence supports removing the malformed unresolved Kahraman DOI and normalizing Maşalı to `https://doi.org/10.56361/usul.173700`, but no real F4-047 application/validation occurred.
- `F4-115` — `DEPENDENCY_BLOCKED`; provisional edition keep/remove matrix is recorded in `CITATION-MAP.md`, including preservation of both genuinely used `Muhtasaru't-tebyîn` editions, but no real F4-047 application/validation occurred.
- `F4-116` — `DEPENDENCY_BLOCKED`; project evidence resolves the content decision provisionally as **KEEP BOTH 1975 and 1993 Ebû Şâme editions**. The key internal mapping is archive genuine footnote 131 (Tayyar Altıkulaç/Beyrut/1975, `1/173`) to current extracted genuine footnote 131 (`el-Murşidu'l-vecîz, 1/173`). This is not a canonical verification because the required reconstructed F4-047 was not inspected.

All four proposed canonical statuses remain `PENDING`.

## Preserved preparatory artifacts

- `CITATION-MAP.md` — repository-only provisional citation/bibliography mapping.
- `replay_f4_w10.py` — candidate fail-closed replay artifact; **not certified on F4-047**.
- `REPLAY-SPEC.md` — mandatory use gate and intended invariants.
- `VALIDATION.md` — exact dependency failure and non-acceptance status.
- `VISUAL-QA.md` — explicitly not executed; future acceptance checklist.
- `ITEM-RESULTS.jsonl` — four `DEPENDENCY_BLOCKED` records.

## Required next action for a later execution environment

1. Materialize the canonical/bootstrap DOCX locally.
2. Reconstruct F4-047 with the repository's existing replay pipeline.
3. Verify exact SHA-256 `6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7`.
4. Only after that succeeds, independently audit and execute the W10 candidate replay against F4-047.
5. Run required pre/post structural validation, idempotency replay and affected-region visual QA.
6. Only a successful rerun may change W10 from `DEPENDENCY_BLOCKED` to `READY_FOR_INTEGRATION`.

## Scope / safety confirmation

No changes were made to `main`, `editorial/apply-fourth-fifth-reports`, canonical `work/` state, F4-111, F4-113, another worker's items, or any Fifth Report item. Worker output is confined to `parallel/results/fourth/F4-W10/`.

## Amber/red risks

- **RED:** mandatory F4-047 worker bootstrap was not executable in this runtime; do not integrate W10 as-is.
- **AMBER:** candidate replay logic was only exercised as a local synthetic prototype before the contract blocker was recognized; it must be audited on the genuine baseline.
- **AMBER:** bibliography edits interact with live Zotero bibliography field results/hyperlinks; exact field integrity and visual behavior must be confirmed on the real DOCX, not inferred from extracted Markdown.

Stop boundary reached. W10 performs no further task work.
