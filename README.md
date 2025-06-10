# 🏗️ Kopen Data Builder

> **A universal CLI and SDK tool for transforming Korean public data into Hugging Face-compatible datasets.**

[![PyPI](https://img.shields.io/pypi/v/kopen-data-builder)](https://pypi.org/project/kopen-data-builder/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-wiki-blue)](https://github.com/yeongseon/kopen-data-builder/wiki)

---

## 🚀 Overview

**Kopen Data Builder** is an open-source CLI and Python SDK designed to convert **Korean public datasets** into [Hugging Face Datasets](https://huggingface.co/docs/datasets) format.

It streamlines the process of:

- Metadata initialization
- Dataset conversion (from CSV/Excel to `DatasetDict`)
- Validation and upload to the Hugging Face Hub

Designed for **researchers, data scientists, and public AI practitioners**, this tool makes dataset publishing intuitive and scalable.

---

## 🔧 Features

- ✅ CLI + SDK support (`data-builder`)
- ✅ Metadata template generation
- ✅ YAML validation and dataset preview
- ✅ Automatic Hugging Face README creation
- ✅ SQLite-based dataset registry
- ✅ Plugin-style preprocessing hooks
- ✅ Fast data handling with [Polars](https://www.pola.rs/)

---

## 📦 Installation

```bash
pip install kopen-data-builder
```

---

## 🧪 Example Usage

```bash
# 1. Initialize metadata template
data-builder init-metadata --name seoul-bike

# 2. Generate dataset from metadata
data-builder generate-dataset --metadata ./metadata.yaml

# 3. Upload to Hugging Face
data-builder upload --metadata ./metadata.yaml
```

---

## 📁 Project Structure

```
kopen-data-builder/
├── src/kopen_data_builder/
│   ├── cli.py
│   ├── builder.py
│   ├── validator.py
│   ├── uploader.py
│   ├── registry.py
│   └── hooks/
│       └── preprocessing.py
├── tests/
├── registry.db
├── pyproject.toml
├── README.md
└── LICENSE
```

---

## 🌐 Metadata Example (`metadata.yaml`)

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

## 📚 Documentation

👉 Visit our [![Docs](https://img.shields.io/badge/docs-online-blue)](https://yeongseon.github.io/kopen-data-builder/) for full usage guide and developer instructions.

---

## 🪪 License

This project is licensed under the [MIT License](LICENSE).
