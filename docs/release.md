# 🚀 Release Guide

This project uses [Hatch](https://hatch.pypa.io/) to manage versioning and publishing to PyPI. Version numbers are stored in `src/kopen_data_builder/__init__.py`.

## 📦 Build Package

To create wheel and sdist files:

```bash
make build
```

Artifacts will be saved under the `dist/` directory.

---

## 🏷 Semantic Versioning

Use one of the following commands to bump version, commit, tag, and push:

```bash
make release-patch  # X.Y.Z → X.Y.(Z+1)
make release-minor  # X.Y.Z → X.(Y+1).0
make release-major  # X.Y.Z → (X+1).0.0
```

This will:
1. Update `__version__` in `src/kopen_data_builder/__init__.py`
2. Create a Git commit and tag (e.g. `v1.2.3`)
3. Push the commit and tag to the main branch

---

## 🚀 Publish to PyPI

To publish the latest built package:

```bash
make publish
```

Ensure that your PyPI token is set in your environment or GitHub Actions secret under `PYPI_API_TOKEN`.

Publishing is automatically handled via GitHub Actions when you push a version tag (`vX.Y.Z`).
