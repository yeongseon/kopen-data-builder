# Welcome to `kopen-data-builder` Documentation 📘

`kopen-data-builder` is a Python library and CLI for transforming Korean public data (CSV/Excel) into Hugging Face-compatible datasets. This documentation provides an overview of its usage, structure, and development workflow.

---

## 🚀 What is `kopen-data-builder`?

`kopen-data-builder` helps you:

- Define metadata for public datasets using a YAML schema aligned with Hugging Face.
- Preprocess CSV/Excel data with standard normalization.
- Split datasets into train/test (and future splits) for ML workflows.
- Build Hugging Face dataset repository structures.
- Upload and verify datasets on the Hugging Face Hub.

---

## 🧪 Usage

Once installed, run the CLI with:

```bash
kopen-data-builder --help
```

Example:

```bash
kopen-data-builder metadata init --output metadata.yaml
```

---

## 🧱 Project Structure

```
kopen-data-builder/
├── src/
│   └── kopen_data_builder/
│       ├── __init__.py
│       ├── cli/
│       └── core/
├── tests/
│   └── test_cli.py
├── docs/
│   └── index.md
├── Makefile
├── pyproject.toml
└── README.md
```

---

## 🛠 Development Workflow

To develop and maintain this project:

```bash
make install          # Set up the development environment
make check            # Run all quality checks and tests
make docs             # Preview documentation locally
make release-patch    # Bump patch version and tag
```

---

## 📚 Documentation with MkDocs

This site is generated using [MkDocs](https://www.mkdocs.org/) and the [Material theme](https://squidfunk.github.io/mkdocs-material/).

To run the site locally:

```bash
make docs
```

Then visit [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📄 License

Licensed under the MIT License.
