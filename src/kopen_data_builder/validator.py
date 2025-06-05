# src/kopen_data_builder/validator.py

from pathlib import Path
from typing import Any, Union

import yaml  # type: ignore

REQUIRED_FIELDS = ["name", "title", "description", "license", "source_url", "language"]

OPTIONAL_FIELDS = [
    "category",
    "tags",
    "split_type",
    "update_frequency",
    "copyright",
    "processed_note",
    "columns",
]


def load_metadata(path: Union[str, Path]) -> dict[str, Any]:
    """Load metadata from a YAML file and return it as a dictionary."""
    with open(path, "r", encoding="utf-8") as f:
        data: dict[str, Any] = yaml.safe_load(f)
        return data


def validate_metadata(metadata: dict[str, Any]) -> list[str]:
    """Return a list of missing required fields from the metadata dictionary."""
    missing = [field for field in REQUIRED_FIELDS if field not in metadata]
    return missing
