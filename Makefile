# ==============================================================================
# 🧱 Makefile — for Hatch + Typer based Python CLI project
# ==============================================================================

# -----------------------------
# 🧰 Setup & Installation
# -----------------------------

.PHONY: check-hatch
check-hatch:
	@command -v hatch >/dev/null 2>&1 || { echo "❌ 'hatch' not found. Install with: pip install hatch"; exit 1; }

.PHONY: install
install: check-hatch
	hatch env create
	hatch run pip install -e ".[dev]"
	@make precommit-install

.PHONY: reset
reset:
	@make clean-all
	@make install
	@echo "🔁 Project reset complete."

.PHONY: shell
shell:
	hatch shell

.PHONY: hatch-clean
hatch-clean:
	@hatch env remove || echo "⚠️ No hatch environment to remove"

# -----------------------------
# 🧹 Code Quality
# -----------------------------

.PHONY: format
format:
	hatch run format

.PHONY: style
style:
	hatch run style

.PHONY: typecheck
typecheck:
	hatch run typecheck

.PHONY: lint
lint:
	hatch run lint

.PHONY: check
check:
	@make lint
	@make typecheck
	@echo "✅ Lint & type check passed!"

.PHONY: check-all
check-all:
	@make check
	@make test
	@make cov
	@echo "✅ All checks including coverage passed!"

.PHONY: precommit
precommit:
	hatch run pre-commit run --all-files

.PHONY: precommit-install
precommit-install:
	hatch run pre-commit install

# -----------------------------
# 🧪 Testing & Coverage
# -----------------------------

.PHONY: test
test:
	@echo "🔬 Running tests..."
	hatch run test

.PHONY: cov
cov:
	hatch run cov
	@echo "📂 Open htmlcov/index.html in your browser to view the coverage report"

# -----------------------------
# 📦 Build & Release
# -----------------------------

.PHONY: build
build:
	hatch build

.PHONY: publish
publish:
	hatch publish

.PHONY: release
release:
ifndef VERSION
	$(error VERSION is not set. Usage: make release VERSION=0.1.0)
endif
	@git tag -a v$(VERSION) -m "Release v$(VERSION)"
	@git push origin v$(VERSION)

.PHONY: release-patch
release-patch:
	hatch version patch
	@make commit-version

.PHONY: release-minor
release-minor:
	hatch version minor
	@make commit-version

.PHONY: release-major
release-major:
	hatch version major
	@make commit-version

.PHONY: commit-version
commit-version:
	@VERSION=$$(grep -oE '[0-9]+\.[0-9]+\.[0-9]+' src/kopen-data-builder/__init__.py); 	echo "🔖 Releasing version $$VERSION"; 	git add src/kopen-data-builder/__init__.py && 	git commit -m "🔖 Release v$$VERSION" && 	git tag -a v$$VERSION -m "Release v$$VERSION" && 	git push origin main --tags

# -----------------------------
# 📚 Documentation
# -----------------------------

.PHONY: docs
docs:
	hatch run docs

.PHONY: build-docs
build-docs:
	hatch run mkdocs build

# -----------------------------
# 🩺 Diagnostic
# -----------------------------

.PHONY: doctor
doctor:
	@echo "🔍 Python version:" && python --version
	@echo "🔍 Installed packages:" && hatch env run pip list || echo "⚠️ No hatch env found"
	@echo "🔍 Azure Function Core Tools version:" && func --version || echo "⚠️ func not found. Install with: npm i -g azure-functions-core-tools@4"
	@echo "🔍 Pre-commit hook installed:"
	@if [ -f .git/hooks/pre-commit ]; then echo ✅ Yes; else echo ❌ No; fi

# -----------------------------
# 🧼 Clean-up
# -----------------------------

.PHONY: clean
clean:
	rm -rf *.egg-info dist build __pycache__ .pytest_cache

.PHONY: clean-all
clean-all: clean
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type f \( -name "*.pyc" -o -name "*.pyo" \) -delete
	@rm -rf .mypy_cache .ruff_cache .pytest_cache .coverage coverage.xml .DS_Store .venv htmlcov

# -----------------------------
# 🆘 Help
# -----------------------------

.PHONY: help
help:
	@echo "📖 Available commands:"
	@grep -E '^\.PHONY: ' Makefile | cut -d ':' -f2 | xargs -n1 echo "  - make"
