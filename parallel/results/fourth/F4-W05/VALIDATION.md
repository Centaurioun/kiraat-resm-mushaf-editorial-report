# VALIDATION — F4-W05

## Overall result

`DEPENDENCY_BLOCKED`

Mandatory F4-047 baseline reconstruction and SHA-256 verification could not be completed; therefore no post-edit DOCX exists and no editorial mutation was attempted.

## Baseline manifest values expected

- logical F4-047 SHA-256: `6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7`
- genuine footnotes: `469`
- footnote references: `469`
- Word fields: `520`
- Zotero item fields: `465`
- Zotero bibliography fields: `1`
- RTL inventory: `365`
- bookmark starts: `53`
- bookmark ends: `53`
- hyperlinks: `52`
- sections: `10`
- comments: `0`
- revisions: `0`

These are manifest expectations only, not independently re-measured by this blocked worker.

## Bootstrap validation attempts

| Check | Result | Evidence / exception |
|---|---|---|
| Exact worker branch created from orchestration branch | PASS | `worker/f4/w05-074-082` created from `orchestration/f4f5-parallel-v1` |
| Orchestration commit recorded | PASS | `5e7bdf4cd24d45e06e733da87b2e695c75751226` |
| F4-047 manifest read | PASS | Expected SHA and invariant inventory recorded |
| F4-047 checkpoint tree inspected | PASS | Existing replay scripts through F4-047 identified; no committed logical F4-047 binary located |
| Canonical DOCX materialized to execution container | BLOCKED | GitHub connector rejects binary fetch/materialization; direct clone has no GitHub DNS/network access |
| Logical F4-047 replay executed | BLOCKED | Binary source unavailable |
| Logical F4-047 SHA independently verified | BLOCKED | No reconstructed binary available |

## Required post-edit technical validation

The following checks were **not run**, because doing so requires an actual verified F4-047 pre-image and a generated post-image:

- genuine footnote reference count and IDs;
- orphan/dangling/duplicate footnotes;
- Word field inventory;
- Zotero item and bibliography field counts;
- bookmarks;
- hyperlinks;
- RTL/Arabic runs in the edit span;
- comments/revisions;
- section count;
- ZIP/XML parse integrity;
- protected OOXML-part comparison;
- replay idempotence;
- outside-scope diff check.

## Mutation validation

No mutation occurred, so there is no post-edit diff to validate. This is intentional fail-closed behavior under the worker contract.

## Boundary check

- F4-073: no touch.
- F4-083: no touch.
- Fifth items: no touch.
- main: no touch.
- canonical application branch: no mutation.
- canonical application state files: no mutation.
