# Codex Prompt — Create and Seed the Private GitHub Repository

> **Historical bootstrap record.** The repository setup described below has already been completed. Do not execute this prompt again. The active editorial workflow was subsequently refined to **seven stages**; use `AGENTS.md`, `README.md`, and `prompts/stage-01.md` through `prompts/stage-07.md` for current instructions.

You are setting up a GitHub repository for a staged academic editorial project.

## User authorization

The user explicitly authorizes you, for this setup task only, to:

- create a new **private** GitHub repository under the user account `Centaurioun`;
- initialize the supplied local folder as the repository working tree if needed;
- create the initial `main` commit and push it;
- create and push one working branch named `editorial/fourth-report`;
- add or adjust normal repository scaffolding only when necessary for a clean repository setup.

Do not create any public repository. Do not modify unrelated repositories.

## Required repository

Create:

`Centaurioun/kiraat-resm-mushaf-editorial-report`

Visibility: **private**.

Use the local folder supplied by the user as the complete bootstrap contents of the repository.

## Preserve source integrity

The contents under `source/` are project evidence and inputs. Do **not** edit, rewrite, normalize, re-save, convert, rename, or silently replace the source DOCX/Markdown files unless required solely to preserve the exact folder layout already supplied. Do not change their internal content.

If a duplicate or suspicious source file is found, report it; do not delete it without explicit authorization.

## Expected repository structure

Preserve the supplied structure, including at least:

- `README.md`
- `AGENTS.md`
- `.gitignore`
- `.gitattributes`
- `CODEX_REPO_SETUP_PROMPT.md`
- `docs/`
- `source/manuscript/current/`
- `source/manuscript/archive/`
- `source/reports/`
- `source/notes/`
- `prompts/stage-01.md` through `prompts/stage-06.md`
- `work/`
- `final/`

You may add a small repository metadata file only if it materially improves provenance or verification. Do not add unnecessary frameworks, CI, packages, generated boilerplate, or dependencies.

## Git workflow

1. Inspect the supplied folder and confirm the expected files are present.
2. If the folder is not already a Git repository, initialize it.
3. Ensure the default branch is `main`.
4. Create one initial commit containing the bootstrap package.
5. Create the private GitHub repository `Centaurioun/kiraat-resm-mushaf-editorial-report`.
6. Add the GitHub remote and push `main`.
7. Create `editorial/fourth-report` from the exact pushed `main` commit and push that branch.
8. Do **not** make editorial-content changes during this setup task.
9. Do **not** create a pull request yet.
10. Do not force-push, rewrite history, squash, delete branches, or alter any other repository.

## Integrity / evidence

After setup, verify and report:

- repository URL;
- confirmation that visibility is private;
- `main` commit SHA;
- `editorial/fourth-report` starting commit SHA;
- remote name and URL;
- concise repository tree (top level and key subfolders);
- whether every expected source/report/prompt file was present;
- any missing file or deviation;
- `git status` result showing a clean working tree.

If feasible, record a SHA-256 manifest for the supplied source files before any Git operation and add it as `docs/SOURCE_SHA256.txt`. This file may be added to the initial commit. Do not change source files to make hashes match anything.

## Stop condition

Once the private repository is created, both branches are pushed, and the checks above pass, stop. Do not execute any of the six editorial stage prompts. Those will be run later, one by one, after ChatGPT and the user refine them.

Return a compact handoff containing the repository URL, branches, commit SHA(s), verification status, and any missing or unexpected files.
