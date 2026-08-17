# Six-Cycle Refinement Record

The orchestration design was reviewed cumulatively in six cycles before repository implementation.

1. **Accuracy / file integrity:** abandoned multi-DOCX merge; authoritative mutation is single-lineage only.
2. **Dependency correctness:** enforced Fourth-before-Fifth; isolated global and structural items from ordinary workers.
3. **Reproducibility:** pinned the frozen F4-047 checkpoint, canonical source hash, report blobs, deterministic replay requirement, and task-specific handoffs.
4. **Integration safety:** replaced paragraph-index dependence with contextual anchoring; added fail-closed zero/one/multiple-match behavior and GREEN/AMBER/RED integration gates.
5. **Speed:** parallelized editorial reasoning and local proof while retaining bounded visual QA; allowed independent assigned items to continue when one item blocks; reserved full-page QA for acceptance gates.
6. **Operational simplicity:** made canonical state single-writer, isolated worker branches, reduced user interaction to short task-launch prompts, and required fresh independent audit before phase advancement.

Final design: ten workers per wave, High integrator, independent High auditor, no worker branch merge, no binary DOCX merge, no Fifth execution before a verified Fourth baseline.
