# src/kopen_data_builder/core/models.py

"""
Metadata module: Defines the DatasetMeta model for dataset metadata.
This model is used to describe datasets in a structured way,
including their name, license, languages, tasks, and additional properties
needed for Hugging Face dataset compatibility.
"""

from datetime import date
from typing import Dict, List, Optional, Union

from pydantic import BaseModel, HttpUrl, field_validator

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
    en: str
    ko: str


class LocalizedText(BaseModel):  # type: ignore[misc]
    en: Optional[str] = None
    ko: Optional[str] = None


class DatasetMeta(BaseModel):  # type: ignore[misc]
    pretty_name: Union[str, LocalizedText]
    description: Union[str, LocalizedText]
    languages: List[Language]
    tags: List[str]
    license: License

    annotations_creators: List[AnnotationCreator]
    language_creators: List[LanguageCreator]
    multilinguality: Multilinguality

    task_categories: List[Union[TaskCategory, str]]
    task_ids: Optional[List[str]] = None

    size_categories: List[SizeCategory]
    source_datasets: List[str]
    source_agency: SourceAgency
    original_url: HttpUrl

    update_frequency: str
    reference_date: Union[str, date]
    kogl_type: Union[int, str]

    splits: Optional[Dict[str, float]] = None

    @field_validator("size_categories", mode="before")
    @classmethod
    def _normalize_size_categories(cls, value: Union[SizeCategory, List[SizeCategory]]) -> List[SizeCategory]:
        if isinstance(value, list):
            return value
        return [value]
