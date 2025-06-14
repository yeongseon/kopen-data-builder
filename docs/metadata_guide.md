# 📊 Hugging Face Metadata Guide for Public Datasets

This guide explains how to structure metadata when uploading public datasets to the Hugging Face Hub. It includes recommended formats, allowed values, and examples, especially for Korean open datasets (공공데이터).

---

## 🧪 Field Definition Table (with Example)

This table provides a clear definition of each metadata field used in Hugging Face dataset cards. Each row includes the field name, its expected type, allowed values or formats, an example value (based on a public dataset such as bike usage or text summarization), and a concise explanation.

| Field                  | Type                     | Allowed Values                                                           | Example                                                                                                                        | Description                                                                                                                                                                                    |
| ---------------------- | ------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pretty_name`          | string                   | any string                                                               | Seoul Public Bike Usage (Monthly)                                                                                              | Human-readable name of the dataset                                                                                                                                                             |
| `description`          | string (multi-line)      | any string                                                               | Monthly stats for Seoul's public bikes, including distance and CO₂ savings.                                                    | Description of dataset content                                                                                                                                                                 |
| `languages`            | list\[string]            | ISO 639-1 codes                                                          | `["ko", "en"]`                                                                                                                 | Languages used **in the actual dataset content**, not just README. If the data is in Korean, use `["ko"]`. Only add `en` if the content itself is in English or includes parallel translation. |
| `tags`                 | list\[string]            | any string                                                               | `["tabular", "transportation"]`                                                                                                | Searchable topics or categories                                                                                                                                                                |
| `license`              | string                   | `cc-by-4.0`, `cc0-1.0`, `MIT`, `Apache-2.0`                              | `cc-by-4.0`                                                                                                                    | Usage license compatible with HF datasets                                                                                                                                                      |
| `annotations_creators` | list\[string]            | `no-annotation`, `crowdsourced`, `machine-generated`, `expert-generated` | `["no-annotation"]`                                                                                                            | How labels (if any) were created                                                                                                                                                               |
| `language_creators`    | list\[string]            | `found`, `crowdsourced`, `machine-generated`                             | `["found"]`                                                                                                                    | How language data was collected                                                                                                                                                                |
| `multilinguality`      | string                   | `monolingual`, `multilingual`, `translation`                             | `monolingual`                                                                                                                  | Language structure of the dataset                                                                                                                                                              |
| `task_categories`      | list\[string]            | Must match Hugging Face tasks                                            | `["time-series-forecasting"]`                                                                                                  | Main ML task(s) for this dataset                                                                                                                                                               |
| `task_ids`             | list\[string] (optional) | any string                                                               | `["bike-usage-forecasting"]`                                                                                                   | Fine-grained task identifiers                                                                                                                                                                  |
| `size_categories`      | string                   | `n<1K`, `1K<n<10K`, ..., `n>10M`                                         | `100K<n<1M`                                                                                                                    | Estimated data size category                                                                                                                                                                   |
| `source_datasets`      | list\[string]            | any string                                                               | `["original"]`                                                                                                                 | Source datasets, if applicable                                                                                                                                                                 |
| `source_agency`        | object                   | `{ en, ko }`                                                             | `{ en: Seoul Open Data Plaza, ko: 서울여림데이터관재 }`                                                                                 | Dataset provider name in both languages                                                                                                                                                        |
| `original_url`         | string (URL)             | valid URL                                                                | [https://data.seoul.go.kr/dataList/OA-15248/F/1/datasetView.do](https://data.seoul.go.kr/dataList/OA-15248/F/1/datasetView.do) | Original public source link                                                                                                                                                                    |
| `update_frequency`     | string                   | any string                                                               | Semiannual                                                                                                                     | Dataset update interval                                                                                                                                                                        |
| `reference_date`       | string or range          | ISO 8601 date / range                                                    | 2018-01-01 to 2025-12-31                                                                                                       | Period the dataset covers                                                                                                                                                                      |
| `kogl_type`            | int or string            | 1–4 or any string                                                        | Type 1 KOGL                                                                                                                    | Korean KOGL license type                                                                                                                                                                       |

---

## 📝 Metadata YAML Example: Seoul Public Bike Usage (Summarization, Jul–Dec 2024)

```yaml
---
pretty_name:
  en: Seoul Public Bike Usage Summary (Jul–Dec 2024)
  ko: 서울시 공공자전거 이용정보 요약 (2024년 7–12월)
description: >
  en: This dataset provides monthly usage statistics of Seoul's public bike-sharing service (Ddareungi),
      paired with short machine-generated textual summaries. It is intended for use in training summarization
      models that generate insights from tabular time-series data.
  ko: 서울시 공공자전거(따링이)의 월별 이용 통계에 대한 요약 데이터를 포함합니다.
      표 기반 시계열 데이터를 요약문으로 생성하는 모델 학습에 활용될 수 있습니다.

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
  - table-to-text

task_ids:
  - table-summary-generation

size_categories:
  - 100K<n<1M

source_datasets:
  - original

source_agency:
  en: Seoul Open Data Plaza
  ko: 서울여림데이터관재

original_url: https://data.seoul.go.kr/dataList/OA-15248/F/1/datasetView.do

update_frequency: Semiannual

reference_date: 2024-07-01 to 2024-12-31
```
