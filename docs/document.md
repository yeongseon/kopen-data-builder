# 📚 Documentation Guide

This project uses [MkDocs](https://www.mkdocs.org/) with the Material theme to build and deploy documentation.

## 🏗 Documentation Structure

```
docs/
├── index.md          # Home page for the documentation site
├── document.md       # This guide
├── development.md    # Development environment and contribution guide
├── release.md        # Release process and automation
└── assets/           # Images or other static files
```

## 🧰 Tools Used

- **MkDocs**: Static site generator for project documentation.
- **Material for MkDocs**: Modern, responsive theme.
- **GitHub Actions**: Automated workflows to build and deploy docs.

## ⚙️ MkDocs Configuration (`mkdocs.yml`)

```yaml
site_name: Korea Open Data Builder
site_description: A universal CLI and SDK tool for transforming Korean public data into Hugging Face-compatible datasets.
site_author: Yeongseon Choe
repo_url: https://github.com/yeongseon/python-project-template

theme:
  name: material

nav:
  - Home: index.md
  - Documentation: document.md
  - Development: development.md
  - Release: release.md

docs_dir: docs
```

## 🚀 GitHub Actions Workflows

Two documentation-related workflows are included:

### 1. 📦 `docs-build.yml`

Validates that documentation builds correctly using MkDocs.

Typical checks include:
- Broken links
- Markdown formatting errors
- Configuration issues

### 2. 🌐 `docs-deploy.yml`

Deploys the documentation to GitHub Pages when changes are pushed to `main`.

Steps:
1. Builds static site using `mkdocs build`.
2. Pushes output from `site/` directory to `gh-pages` branch.
3. GitHub Pages serves the latest version.

Ensure the GitHub repository is configured to serve from the `gh-pages` branch under Settings → Pages.

---

## 📝 Local Development

To preview documentation locally:

```bash
# 1. Install dependencies
hatch env create

# 2. Launch local server
hatch run docs
```

Or using `Makefile`:

```bash
make docs
```

Then open `http://localhost:8000` in your browser.

---

## 🧪 Linting & Testing Docs

Check for broken links and structure issues:

```bash
make check-docs
```

---

## 📬 Feedback

For any issues or suggestions regarding documentation, please open an issue or pull request.

---
