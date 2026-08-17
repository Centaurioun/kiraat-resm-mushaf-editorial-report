# F4-W10 Validation Record

## Result

`DEPENDENCY_BLOCKED`

The mandatory Fourth-worker baseline prerequisite was not satisfied in this runtime. Under `parallel/WORKER-CONTRACT.md`, that prevents W10 from applying or validating F4-112/F4-114/F4-115/F4-116.

## Required baseline and durable repository evidence

The contract requires reconstruction of logical F4-047 and exact SHA-256 verification:

`6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7`

Repository durable state independently records the F4-047 output SHA and prior checkpoint inventory: 469 footnotes / 469 references; 520 fields; 465 Zotero item fields + 1 bibliography field; 53/53 bookmarks; 52 hyperlinks; 365 RTL markers; 10 sections; no comments/revisions; valid ZIP/XML; byte-idempotent prior F4-043–047 replay.

That durable record is evidence of the prior checkpoint, but the worker contract expressly requires **this worker to reconstruct and verify it before assigned edits**. It is not a substitute for the required worker bootstrap.

## Blocking runtime fact

The canonical/bootstrap DOCX is present in GitHub as a 406,091-byte binary blob. The GitHub connector could read repository metadata/base64, but the local execution container could not materialize the raw DOCX; direct raw download was unavailable in this runtime. Consequently W10 could not:

- reconstruct F4-047 from the canonical source plus existing replay pipeline;
- hash the reconstructed local DOCX;
- apply W10 edits to that real binary;
- compare real pre/post protected structures;
- render the real affected pages.

Per contract section 3, execution stops at this dependency boundary.

## Preparatory checks preserved (not acceptance evidence)

Before the baseline-rule conflict was identified, a local prototype of the candidate replay logic was compiled and exercised twice on a purpose-built synthetic OOXML fixture. It behaved idempotently on that fixture and preserved the fixture's protected fields/footnote IDs. This is useful engineering evidence only; it **does not satisfy** the required F4-047 replay, technical validation, or visual QA and is not used to elevate the disposition.

## Required rerun gate

A later worker/integrator environment must first materialize the canonical DOCX, reconstruct F4-047 with the durable replay pipeline, and verify the exact required SHA. Only then may W10's candidate replay be audited/executed, followed by full pre/post technical validation and visual QA. Until then all four assigned items remain canonically `PENDING`.
