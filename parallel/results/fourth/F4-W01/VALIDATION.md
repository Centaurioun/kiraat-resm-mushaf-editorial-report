# F4-W01 Validation

## Verdict

`DEPENDENCY_BLOCKED` — validation stopped at the mandatory baseline gate.

## Checks completed

- Task scope confirmed as F4-048–056 only.
- Worker branch confirmed as `worker/f4/w01-048-056` based on `orchestration/f4f5-parallel-v1`.
- Orchestration commit recorded as `5e7bdf4cd24d45e06e733da87b2e695c75751226`.
- Frozen F4-047 manifest read; required logical SHA-256 confirmed as `6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7`.
- `work/APPLICATION-STATE.md` and `work/F4-043-047-REPLAY-SPEC.md` agree on the required F4-047 output SHA and integrity inventory.
- Canonical DOCX binary fetch through the GitHub connector was attempted in base64 mode, but the response was truncated by connector output limits and could not be materialized into the local runtime.
- Direct local `git ls-remote` access was attempted and failed because the execution runtime could not resolve `github.com`.

## Checks not validly executable

Because the required F4-047 binary could not be reconstructed and hashed, none of the following post-edit checks can be truthfully performed or claimed:

- pre/post genuine footnote reference and ID comparison;
- orphan/dangling/duplicate footnote checks;
- Word field inventory;
- Zotero item/bibliography field counts;
- bookmark inventory;
- hyperlink inventory;
- Arabic/RTL run comparison;
- comments/revisions comparison;
- section count comparison;
- protected OOXML part comparison;
- ZIP/XML parse integrity after edits;
- edit idempotency;
- out-of-scope mutation diff.

## Mutation result

No manuscript or canonical application-state mutation occurred. Therefore there is no fabricated post-edit SHA, no false PASS, and no claim that F4-048–056 are applied.