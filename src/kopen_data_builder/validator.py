# src/kopen_data_builder/validator.py

from pathlib import Path
from typing import Any, Union

import yaml  # type: ignore

REQUIRED_FIELDS = [
    "name",
    "title",
    "description",
    "license",
    "source_url",
    "language",
]

ALLOWED_COLUMN_TYPES = {"string", "int", "float", "datetime", "bool"}


def load_metadata(path: Union[str, Path]) -> dict[str, Any]:
    """Load metadata from a YAML file and return it as a dictionary."""
    with open(path, "r", encoding="utf-8") as f:
        data: dict[str, Any] = yaml.safe_load(f)
        return data


def validate_metadata(metadata: dict[str, Any]) -> list[str]:
    """Return a list of validation error messages."""
    errors = []

    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in metadata:
            errors.append(f"Missing required field: '{field}'")

    # Check columns field (if present)
    columns = metadata.get("columns")
    if columns:
        if not isinstance(columns, dict):
            errors.append("The 'columns' field must be a dictionary of column definitions.")
        else:
            for col_name, col_info in columns.items():
                if not isinstance(col_info, dict):
                    errors.append(
                        f"Column '{col_name}' must be a dictionary with 'type' and 'description'."
                    )
                    continue
                col_type = col_info.get("type")
                if not col_type:
                    errors.append(f"Column '{col_name}' is missing 'type'.")
                elif col_type not in ALLOWED_COLUMN_TYPES:
                    sorted_types = ", ".join(sorted(ALLOWED_COLUMN_TYPES))
                    errors.append(
                        f"Column '{col_name}' has invalid type '{col_type}'. "
                        f"Allowed types: {sorted_types}"
                    )

    return errors
