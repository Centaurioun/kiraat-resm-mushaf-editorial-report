# Parallel Fourth/Fifth Application Orchestration

Bu dizin, `Kırâatlerin Rivayetinde Resm-i Mushaf’ın Etkisi` kitabında Dördüncü ve Beşinci düzeltme raporlarının kalan maddelerini güvenli biçimde paralelleştirmek için bağlayıcı çalışma katmanıdır.

## Temel ilke

Paralelleştirilen şey nihai DOCX değildir; **edit kararı, deterministic replay/edit bundle, kanıt ve lokal doğrulamadır**. Tek authoritative DOCX zinciri yalnız integrator tarafından seri biçimde oluşturulur. Worker DOCX'leri birbirleriyle veya canonical DOCX ile binary merge edilmez.

## Başlangıç durumu

- Authoritative application branch: `editorial/apply-fourth-fifth-reports`
- Frozen application checkpoint: `c473b24d3f6f24508c761805218bbaa29686b47c`
- Last completed Fourth item: `F4-047`
- Next Fourth item: `F4-048`
- Logical F4-047 DOCX SHA-256: `6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7`
- Orchestration branch: `orchestration/f4f5-parallel-v1`

## Execution waves

1. Ten Fourth workers execute their isolated tasks.
2. A High integrator replays accepted worker outputs serially, applies integrator-reserved F4-111 and F4-113, and produces F4-116.
3. A fresh High auditor independently validates the complete Fourth result.
4. Only after a verified F4 baseline is frozen may ten fresh Fifth workers start.
5. A High integrator replays Fifth outputs and performs the reserved global Fifth sweep F5-086–094.
6. A fresh High final auditor performs Fourth/Fifth reconciliation, full technical validation, and all-page visual QA before final DOCX release.

## Read order for workers

Each worker starts from its own file under `parallel/tasks/fourth/` or `parallel/tasks/fifth/`. The task file identifies the only permitted report items, required branch, known risks, output location, and stop conditions. It incorporates `parallel/AGENTS.md` and `parallel/WORKER-CONTRACT.md` by reference.

No worker may perform another worker's task, change `main`, change `source/`, mutate the authoritative application branch, or update the canonical application ledger/state files.
