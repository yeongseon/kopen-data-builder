# src/kopen_data_builder/validator.py

"""
Validator module: Validates dataset metadata against predefined standards
and returns a structured DatasetMeta object.
"""

from typing import Any

from .models import DatasetMeta

# Allowed values based on Hugging Face dataset metadata standards
ALLOWED_LICENSES = {"CC-BY-4.0", "MIT", "Apache-2.0"}
ALLOWED_LANGUAGES = {"ko", "en"}
ALLOWED_TASKS = {"문서분류", "번역", "요약"}


def validate_metadata(meta: Any) -> DatasetMeta:
    """
    Validate the user-provided metadata dictionary and
    return a DatasetMeta object if valid.

    Raises:
        ValueError: If required fields are missing or contain invalid values
    """
    # Basic structural/type validation via Pydantic
    validated = DatasetMeta(**meta)

    # Additional value validation
    if validated.license not in ALLOWED_LICENSES:
        raise ValueError(f"Invalid license: {validated.license}")
    if not set(validated.language).issubset(ALLOWED_LANGUAGES):
        raise ValueError(f"Invalid language(s): {validated.language}")
    if not set(validated.tasks).issubset(ALLOWED_TASKS):
        raise ValueError(f"Invalid task(s): {validated.tasks}")

    return validated
