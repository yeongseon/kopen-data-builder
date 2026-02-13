# 🏗️ Kopen Data Builder

> **A universal CLI and SDK tool for transforming Korean public data into Hugging Face-compatible datasets.**

[![PyPI](https://img.shields.io/pypi/v/kopen-data-builder)](https://pypi.org/project/kopen-data-builder/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-wiki-blue)](https://yeongseon.github.io/kopen-data-builder/)

---

## 🚀 Overview

**Kopen Data Builder** is an open-source **command-line interface (CLI)** and **Python SDK** for converting **Korean public datasets** into the standardized [Hugging Face Datasets](https://huggingface.co/docs/datasets) format.

It is designed to simplify the process of metadata construction, file preparation, and automated uploads—particularly for **Korean government or institutional data**.

This tool automates the full pipeline:

1. Metadata creation and validation (YAML-based)
2. Optional preprocessing via hooks
3. Dataset splitting or merging
4. Hugging Face dataset repository construction
5. Uploading and verifying on Hugging Face Hub

Especially helpful for **data scientists**, **AI engineers**, and **public sector developers** aiming to share well-documented, multilingual, and reproducible datasets.

---

## 🔧 Features

* ✅ Modular CLI with [Typer](https://typer.tiangolo.com/) for each stage of processing
* ✅ YAML-based metadata schema aligned with Hugging Face conventions
* ✅ Custom preprocessing support using `hooks/preprocessing.py`
* ✅ Built-in Hugging Face-compatible repository builder
* ✅ Upload automation with verification logic
* ✅ Tabular handling (CSV, Excel) via Pandas
* ✅ Extensible CLI/SDK with test coverage and CI workflows

---

## 📦 Installation

```bash
pip install kopen-data-builder
```

---

## 🧪 CLI Usage Example

```bash
# 1. Generate metadata.yaml template
kopen-data-builder metadata init --output ./metadata.yaml

# 2. Run preprocessing (optional)
kopen-data-builder preprocess run --input-csv ./raw.csv --output-csv ./preprocessed.csv

# 3. Split dataset into train/test
kopen-data-builder split split --input-csv ./preprocessed.csv --split-json ./splits.json --output-dir ./splits

# 4. Build HF repository structure
kopen-data-builder build run --dataset-name cli-test --csv-json-path ./splits.json --output-dir ./hf_repo --metadata-path ./metadata.yaml

# 5. Upload to Hugging Face Hub
kopen-data-builder upload run --repo-dir ./hf_repo --repo-id username/seoul-bike
```

---

## 📁 Project Structure

```
kopen-data-builder/
├── src/kopen_data_builder/
│   ├── cli/               # Typer CLI commands
│   ├── core/              # Core logic: validation, upload, split, build
│   ├── hooks/             # Optional user preprocessing hook
│   └── registry.py        # Metadata registry and helpers
├── tests/                 # Unit tests for CLI and core
├── docs/                  # Documentation site (built with MkDocs)
├── .github/workflows/     # Linting, test, and deploy workflows
├── pyproject.toml         # Build system
└── README.md
```

---

## 📄 Metadata Design Principles

* The metadata follows a custom YAML schema compatible with Hugging Face Hub's dataset card system.
* Each dataset must define multilingual fields (e.g., `pretty_name.en`, `pretty_name.ko`) when possible.
* Column names in the original CSV/Excel file are preserved without renaming—even if they don't follow Python conventions—to maintain traceability.
* KOGL types and public license types are supported (e.g., Type 1 KOGL, CC-BY-4.0).
* The metadata document must include an accurate reference period (e.g., `2024-07-01 to 2024-12-31`) to reflect the update cycle.

Example: See `docs/Metadata Guide.md` for a detailed template.

---

## 🧪 Sample Metadata (Simplified)

```yaml
pretty_name:
  en: Seoul Public Bike Usage Summary (Jul–Dec 2024)
  ko: 서울시 공공자전거 이용정보 요약 (2024년 7–12월)
description:
  en: Monthly usage statistics of Seoul's public bike-sharing service (Ddareungi).
  ko: 서울시 공공자전거(따릉이)의 월별 이용 통계를 담은 데이터셋입니다.
languages:
  - ko
  - en
tags:
  - summarization
  - public-data
  - bike-sharing
  - timeseries
license: cc-by-4.0
annotations_creators:
  - machine-generated
language_creators:
  - found
multilinguality: monolingual
task_categories:
  - summarization
source_agency:
  en: Seoul Open Data Plaza
  ko: 서울열린데이터광장
original_url: https://data.seoul.go.kr/dataList/OA-15248/F/1/datasetView.do
update_frequency: Semiannual
reference_date: 2024-07-01 to 2024-12-31
```

---

## 📚 Documentation

👉 [**Full Documentation**](https://yeongseon.github.io/kopen-data-builder/) – includes field definitions, YAML examples, CLI usage, and advanced guides.

---

## 🪪 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋 Contributing

Issues and contributions are welcome! Please follow conventional commits and submit PRs with test coverage if possible.
