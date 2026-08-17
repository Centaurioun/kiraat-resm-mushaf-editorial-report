# HANDOFF — F4-W06

## Worker

- Task: `F4-W06`
- Scope: `F4-083`–`F4-090` only
- Branch: `worker/f4/w06-083-090`
- Orchestration base: `5e7bdf4cd24d45e06e733da87b2e695c75751226`
- Substantive evidence-package commit: `f3a67210eb6d9e6a853411f366d31d5a68325fd5`
- This handoff commit: `SELF`

## Disposition

All assigned items: `DEPENDENCY_BLOCKED`.

No manuscript edit was applied and no canonical/application state was touched.

## Exact blocker

The shared worker contract requires reconstruction of logical F4-047 and direct verification of SHA-256:

`6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7`

before any F4-083–090 edit may be targeted or applied.

The current runtime could read text repository files but could not materialize the binary DOCX through the connected GitHub path; its execution container also lacked external network/DNS access for repository clone/download. Therefore the required byte-level baseline check could not be performed.

Per contract, the worker stopped rather than substituting the extracted Markdown or another checkpoint.

## Integrator/coordinator action

Do **not** integrate any F4-083–090 editorial mutation from this branch; none exists.

Resume/re-run F4-W06 only in a runtime that can:

1. reconstruct the logical F4-047 DOCX from the canonical source plus the existing replay pipeline;
2. verify the exact required SHA-256;
3. inspect genuine footnotes and protected OOXML in 4.1–4.2;
4. apply deterministic exact-anchor replay for F4-083–090;
5. run invariant checks and bounded rendered visual QA.

The report-level intended operations and item-specific citation risks are preserved in `REPLAY-SPEC.md` and `CITATION-MAP.md`; they are not claims of completed edits.

## Risks carried forward

- RED: F4-090 citation placement must be inventoried before conclusion-block consolidation.
- AMBER: F4-084 evidence strength must not be overstated.
- AMBER: F4-086 heterogeneous Companion-mushaf material must not be collapsed.
- AMBER: F4-089 must not retain unsupported psychological motive attribution.

Task boundary reached. Stop here.
