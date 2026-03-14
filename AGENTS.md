# AGENTS.md

## Purpose
`kopen-data-builder` is a Python CLI and SDK for transforming Korean public data into dataset packages.

## Read First
- `README.md`
- `docs/agent-playbook.md`

## Working Rules
- Preserve the CLI-first workflow and dataset packaging expectations.
- Keep metadata schema expectations and docs synchronized.
- Prefer incremental changes around existing commands instead of adding parallel flows.
- Add tests for every behavior change in preprocessing, splitting, or upload logic.

## Validation
- `make test`
- `make lint`
- `make typecheck`
- `make build`
