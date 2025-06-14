# /src/kopen_data_builder/core/enums.py

"""
Enum definitions for constrained metadata fields.
These ensure metadata values are limited to valid options (e.g., license types, languages).
"""

from enum import Enum


class License(str, Enum):
    cc_by_4_0 = "cc-by-4.0"
    cc0_1_0 = "cc0-1.0"
    mit = "MIT"
    apache_2_0 = "Apache-2.0"


class Language(str, Enum):
    ko = "ko"
    en = "en"


class AnnotationCreator(str, Enum):
    no_annotation = "no-annotation"
    crowdsourced = "crowdsourced"
    machine_generated = "machine-generated"
    expert_generated = "expert-generated"


class LanguageCreator(str, Enum):
    found = "found"
    crowdsourced = "crowdsourced"
    machine_generated = "machine-generated"


class Multilinguality(str, Enum):
    monolingual = "monolingual"
    multilingual = "multilingual"
    translation = "translation"


class TaskCategory(str, Enum):
    text_classification = "text-classification"
    translation = "translation"
    summarization = "summarization"
    time_series_forecasting = "time-series-forecasting"


class SizeCategory(str, Enum):
    n_lt_1k = "n<1K"
    n_1k_to_10k = "1K<n<10K"
    n_10k_to_100k = "10K<n<100K"
    n_100k_to_1m = "100K<n<1M"
    n_1m_to_10m = "1M<n<10M"
    n_gt_10m = "n>10M"
