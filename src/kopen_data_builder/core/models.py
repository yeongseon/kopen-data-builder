# src/kopen_data_bu/core/models.py

"""
Metadata module: Defines the DatasetMeta model for dataset metadata.
This model is used to describe datasets in a structured way,
including their name, license, languages, tasks, and split proportions.
"""

from typing import Dict, List

from pydantic import BaseModel


class DatasetMeta(BaseModel):  # type: ignore[misc]
    name: str
    license: str
    language: List[str]
    tasks: List[str]
    splits: Dict[str, float]  # Example: {"train": 0.8, "test": 0.2}
