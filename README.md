# 🏗️ Kopen Data Builder

> **A universal CLI and SDK tool for transforming Korean public data into Hugging Face-compatible datasets.**

[![PyPI](https://img.shields.io/pypi/v/kopen-data-builder)](https://pypi.org/project/kopen-data-builder/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-wiki-blue)](https://yeongseon.github.io/kopen-data-builder/)

---

## 🚀 Overview

**Kopen Data Builder** is an open-source **command-line interface (CLI)** and **Python SDK** for converting **Korean public datasets** into the standardized [Hugging Face Datasets](https://huggingface.co/docs/datasets) format.

This tool automates the full pipeline:

1. Metadata creation and validation  
2. Preprocessing (optional)  
3. Dataset splitting or merging  
4. Hugging Face dataset repository building  
5. Uploading and verifying on Hugging Face Hub  

Perfect for **researchers**, **data scientists**, and **public sector AI developers** aiming to share clean, reusable datasets.

---

## 🔧 Features

- ✅ Modular CLI with `typer` for each processing step  
- ✅ YAML-based metadata management  
- ✅ Custom preprocessing hook support  
- ✅ Hugging Face-compatible repo structure builder  
- ✅ Upload automation with verification  
- ✅ High-performance CSV/Excel handling using [Polars](https://www.pola.rs/)  
- ✅ Easily testable, extensible, and CI-friendly  

---

## 📦 Installation

```bash
pip install kopen-data-builder
```

---

## 🧪 CLI Usage Example

```bash
# 1. Generate metadata.yaml template
data-builder metadata run --name seoul-bike --output ./metadata.yaml

# 2. Run preprocessing (optional)
data-builder preprocess run --metadata ./metadata.yaml --output ./preprocessed.csv

# 3. Split dataset into train/valid/test
data-builder split run --metadata ./metadata.yaml --input ./preprocessed.csv --output ./splits.json

# 4. Build HF repository structure
data-builder build run cli-test ./splits.json ./hf_repo

# 5. Upload to Hugging Face Hub
data-builder upload run --repo-dir ./hf_repo --repo-id username/seoul-bike
```

---

## 📁 Updated Project Structure

```
kopen-data-builder/
├── src/kopen_data_builder/
│   ├── cli/
│   │   ├── main.py
│   │   ├── metadata_cmd.py
│   │   ├── preprocess_cmd.py
│   │   ├── split_cmd.py
│   │   ├── build_cmd.py
│   │   └── upload_cmd.py
│   ├── core/
│   │   ├── builder.py
│   │   ├── uploader.py
│   │   ├── splitter.py
│   │   └── validator.py
│   ├── hooks/
│   │   └── preprocessing.py
│   └── registry.py
├── tests/
├── pyproject.toml
├── README.md
└── LICENSE
```

---

## 🧾 Metadata Example (`metadata.yaml`)

```yaml
name: seoul-bike
title: 서울 공공자전거 대여정보
description: 서울시의 공공자전거 대여 이력 데이터를 기반으로 한 머신러닝용 데이터셋
source_url: https://data.seoul.go.kr/
license: Public Domain
language: [ko, en]
split_type: by_year
category: transportation
tags: [bike, public-data, seoul, mobility]
```

---

## 🧑‍💻 Developer Notes

- Commands are modular: each stage (`metadata`, `preprocess`, `split`, `build`, `upload`) is implemented as an independent Typer CLI.
- Pytest-based test suite with CLI mocks and temporary files ensures isolated coverage.
- CI workflows provided in `.github/workflows` for linting, tests, and docs.

---

## 📚 Documentation

👉 [**Full Documentation**](https://yeongseon.github.io/kopen-data-builder/) – includes developer guide, CLI reference, and examples.

---

## 🪪 License

This project is licensed under the [MIT License](LICENSE).