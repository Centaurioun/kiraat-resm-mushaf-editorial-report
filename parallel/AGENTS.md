# PARALLEL APPLICATION AGENTS

This file governs work under `parallel/` for the Fourth/Fifth report application phase.

## Instruction precedence

1. The assigned worker task file.
2. This `parallel/AGENTS.md`.
3. `parallel/WORKER-CONTRACT.md` and the applicable integration/audit protocol.
4. Root `AGENTS.md` academic, source, citation, and Git-safety principles.

The root `AGENTS.md` was written for the earlier seven-stage report-production phase. Its academic/source/Git-safety rules remain binding. Its stage-specific execution rules and old `editorial/fourth-report` branch instruction are superseded for these parallel application tasks by this file and the assigned task.

## Non-negotiable scientific rules

- Use only repository project sources. No web or external research.
- Do not invent dates, works, page numbers, readings, textual variants, bibliographic data, or historical claims.
- Preserve the central distinction: qirāʾāt are transmitted primarily through telakki, müşâfehe, edâ, isnad and rivâyet; resm-i Osmânî is not an independent generator/source of readings but a complementary written compatibility/acceptance framework.
- Distinguish historical evidence, later classical interpretation, normative argument, and theological/hikmet commentary.
- Never move a footnote onto a materially different proposition without support.
- Do not rewrite direct quotations merely for style.
- If a safe citation destination cannot be established, do not guess.

## Protected repository state

Workers MUST NOT modify:

- `main`;
- `source/`;
- `prompts/`;
- `editorial/apply-fourth-fifth-reports`;
- `work/APPLICATION-STATE.md`;
- `work/application-ledger.jsonl`;
- `work/VALIDATION-LOG.md`;
- `work/NEXT-HANDOFF.md`.

Those application-state files are single-writer resources owned by the integrator.

## Scope isolation

A worker may act only on the report item IDs listed in its assigned task. It must not opportunistically fix adjacent problems, perform global cleanup, apply Fifth items during the Fourth wave, or take over another worker's task.

If an assigned item requires a change outside the worker's permitted structural region, record the dependency in the handoff rather than expanding scope.

## Canonical mutation rule

Worker outputs are proposals plus proven replay artifacts. A worker may create and validate a temporary/local DOCX derived from the frozen baseline, but that DOCX is not authoritative and is not merged. Authoritative mutation occurs only during integration.

## Stop rather than guess

Stop or mark the item for adjudication when:

- the expected target cannot be uniquely located;
- multiple plausible anchors exist;
- a citation would lose its supported proposition;
- a Word field/bookmark/Zotero/RTL structure would require speculative manipulation;
- report wording is materially ambiguous;
- an unexpected dependency on another worker's edit is discovered.
