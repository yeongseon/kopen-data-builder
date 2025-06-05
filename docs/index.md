# Welcome to `kopen-data-builder` Documentation 📘

`kopen-data-builder` is a Python-based CLI tool starter template built with [Typer](https://typer.tiangolo.com/) and modern development tools. This documentation provides an overview of its usage, structure, and development workflow.

---

## 🚀 What is `kopen-data-builder`?

`kopen-data-builder` helps you:

- Bootstrap new CLI projects with best practices.
- Use `Typer` for intuitive, type-safe command-line interfaces.
- Apply type checking, linting, and formatting out of the box.
- Write clean and testable code using `pytest` and `coverage`.
- Automate your build, release, and documentation tasks.

---

## 🧪 Usage

Once installed, run the CLI with:

```bash
kopen-data-builder --help
```

Example:

```bash
kopen-data-builder hello --name Alice
```

---

## 🧱 Project Structure

```
kopen-data-builder/
├── src/
│   └── kopen-data-builder/
│       ├── __init__.py
│       └── cli.py
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
