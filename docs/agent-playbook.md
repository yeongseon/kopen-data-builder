# Agent Playbook

## Source Of Truth
- `README.md` for CLI usage and dataset-building workflow.
- `pyproject.toml` and `Makefile` for environment, scripts, and packaging behavior.
- Existing docs under `docs/` for supplemental detail.

## Repository Map
- `src/kopen_data_builder/` main package.
- `tests/` package coverage.
- `docs/` project documentation.

## Change Workflow
1. Decide whether the change affects metadata handling, dataset transforms, or CLI orchestration.
2. Keep command examples in the README current when public behavior changes.
3. Maintain backward compatibility for file layout and CLI arguments unless intentionally versioning a contract change.
4. Update tests before broad refactors.

## Validation
- `make install`
- `make test`
- `make lint`
- `make typecheck`
- `make build`
