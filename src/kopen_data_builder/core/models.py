# src/kopen_data_builder/core/models.py

"""
Metadata module: Defines the DatasetMeta model for dataset metadata.
This model is used to describe datasets in a structured way,
including their name, license, languages, tasks, and additional properties
needed for Hugging Face dataset compatibility.
"""

from datetime import date
from typing import Dict, List, Optional, Union

from pydantic import BaseModel, HttpUrl

from kopen_data_builder.core.enums import (
    AnnotationCreator,
    Language,
    LanguageCreator,
    License,
    Multilinguality,
    SizeCategory,
    TaskCategory,
)


class SourceAgency(BaseModel):  # type: ignore[misc]
    en: str  # Name of the dataset provider in English
    ko: str  # Name of the dataset provider in Korean


class DatasetMeta(BaseModel):  # type: ignore[misc]
    pretty_name: str  # Human-readable name of the dataset
    description: str  # Detailed multi-line description of the dataset
    languages: List[Language]  # ISO 639-1 codes, e.g., [Language.ko, Language.en]
    tags: List[str]  # Searchable tags for dataset discovery
    license: License  # License identifier (Enum)

    annotations_creators: List[AnnotationCreator]  # Annotation source (Enum)
    language_creators: List[LanguageCreator]  # Language creation method (Enum)
    multilinguality: Multilinguality  # Language structure (Enum)

    task_categories: List[TaskCategory]  # ML task categories (Enum)
    task_ids: Optional[List[str]] = None  # Fine-grained task identifiers

    size_categories: SizeCategory  # Estimated dataset size category
    source_datasets: List[str]  # Names of source datasets
    source_agency: SourceAgency  # Dataset provider names
    original_url: HttpUrl  # Source data link

    update_frequency: str  # e.g., Monthly, Quarterly, etc.
    reference_date: Union[str, date]  # Coverage period, can be string or ISO date
    kogl_type: Union[int, str]  # KOGL license type (e.g., 1, "Type 1 KOGL")

    splits: Optional[Dict[str, float]] = None  # e.g., {"train": 0.8, "test": 0.2}
