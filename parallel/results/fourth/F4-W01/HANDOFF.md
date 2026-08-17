# F4-W01 Integrator Handoff

## Worker state

- Task: `F4-W01`
- Scope: `F4-048`–`F4-056` only
- Branch: `worker/f4/w01-048-056`
- Orchestration source commit: `5e7bdf4cd24d45e06e733da87b2e695c75751226`
- Last evidence commit before this handoff: `95457061da2054675c04f34d2ecef30b2ff531df`
- Worker disposition: `DEPENDENCY_BLOCKED`

## Why blocked

The shared worker contract requires a worker to reconstruct the logical F4-047 DOCX and independently verify SHA-256 `6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7` before applying any Fourth-wave edit. In this execution environment the repository text/replay artifacts were readable, but the canonical DOCX binary could not be fully materialized into the local runtime: connector base64 output was truncated and direct local GitHub network resolution failed. Proceeding would have required trusting recorded state instead of reproducing it, which the contract forbids.

## Item handoff

- F4-048 — **BLOCKED** (`DEPENDENCY_BLOCKED`)
- F4-049 — **BLOCKED** (`DEPENDENCY_BLOCKED`)
- F4-050 — **BLOCKED** (`DEPENDENCY_BLOCKED`)
- F4-051 — **BLOCKED** (`DEPENDENCY_BLOCKED`)
- F4-052 — **BLOCKED** (`DEPENDENCY_BLOCKED`)
- F4-053 — **BLOCKED** (`DEPENDENCY_BLOCKED`)
- F4-054 — **BLOCKED** (`DEPENDENCY_BLOCKED`)
- F4-055 — **BLOCKED** (`DEPENDENCY_BLOCKED`)
- F4-056 — **BLOCKED** (`DEPENDENCY_BLOCKED`)

No item is claimed `READY_FOR_INTEGRATION`; none is claimed canonically `VERIFIED`.

## Red/amber risks for resume

**RED**
- F4-049 deletes/consolidates three paragraphs; every genuine footnote on the affected propositions must be mapped before deletion.
- F4-051 crosses the First/Second Section boundary; preserve the Second Section heading, bookmarks, fields and section structure.

**AMBER**
- F4-048 requires reuse/preservation of Arabic/RTL runs and safe retention of genuine citations while correcting Bakara `2/85` → `2/132` and the example wording.
- F4-050 requires actual-document determination of whether `İbn Mücâhid` is first or repeated use before retaining/removing `(ö. 324/936)`.
- F4-052–056 must preserve the transmission-first thesis and avoid turning resm into an independent source of readings.

## Resume condition

Resume this same worker scope only in an environment that can materialize the canonical DOCX, execute the existing replay chain through F4-047, and independently obtain the required F4-047 SHA. Then inspect actual DOCX footnotes/fields/RTL/bookmarks before producing deterministic edit replay artifacts and bounded visual QA.

Canonical `work/` application-state files were not modified. No Fifth item, F4-047-or-earlier item, F4-057-or-later item, `main`, or canonical application branch was touched.