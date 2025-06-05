# 🧰 Development Guide

This project is a modern Python CLI project template using [Typer](https://typer.tiangolo.com/), [Hatch](https://hatch.pypa.io/), and pre-configured development tooling.

## 🛠 Setup

First, make sure you have [Hatch](https://hatch.pypa.io/latest/install/) installed:

```bash
pip install hatch
```

Then install the development environment:

```bash
make install
```

This will:
- Create a virtual environment using Hatch
- Install the package in editable mode (`-e .`)
- Install all `[dev]` dependencies (linters, test runners, docs, etc.)

## 🔁 Reset Environment

To remove all build and cache files and start fresh:

```bash
make reset
```

---

## 🧪 Quality Checks

### Linting & Formatting

```bash
make lint      # ruff, black --check, mypy
make format    # auto-fix with ruff + black
make typecheck # mypy static analysis
```

### Testing

```bash
make test      # Run pytest
make cov       # Run coverage and open htmlcov/index.html
```

### All-in-One

```bash
make check        # Lint + typecheck + test
make check-all    # Lint + typecheck + test + coverage
```

---

## 🧪 CI Compatibility

To run the same checks used in GitHub Actions:

```bash
make ci-check
```

---

## 🧪 Activate Environment Shell

```bash
make shell
```

This opens a shell with the Hatch-managed environment.

---

## 🧹 Clean Up

```bash
make clean
```

This removes all caches, build artifacts, and coverage files.
