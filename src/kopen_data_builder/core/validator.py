# src/kopen_data_builder/validator.py

"""
Validator module: Validates dataset metadata against predefined standards
and returns a structured DatasetMeta object.
"""

import logging
from typing import Any, List, Set

from .models import DatasetMeta

logger = logging.getLogger(__name__)

# ✅ Allowed values (based on Hugging Face and internal conventions)
ALLOWED_LICENSES: Set[str] = {"CC-BY-4.0", "MIT", "Apache-2.0"}
ALLOWED_LANGUAGES: Set[str] = {"ko", "en"}
ALLOWED_TASKS: Set[str] = {"문서분류", "번역", "요약"}


def validate_metadata(meta: Any) -> DatasetMeta:
    """
    Validate the user-provided metadata dictionary and
    return a DatasetMeta object if valid.

    Args:
        meta (Any): Metadata dictionary to validate.

    Returns:
        DatasetMeta: Validated metadata object.

    Raises:
        ValueError: If required fields are missing or contain invalid values
    """
    # Step 1: Pydantic schema validation
    validated = DatasetMeta(**meta)

    # Step 2: Enum value checks
    _validate_field("license", validated.license, ALLOWED_LICENSES)
    _validate_subset("language", validated.language, ALLOWED_LANGUAGES)
    _validate_subset("tasks", validated.tasks, ALLOWED_TASKS)

    logger.debug("Metadata validated successfully: %s", validated)
    return validated


def _validate_field(field: str, value: str, allowed: Set[str]) -> None:
    if value not in allowed:
        raise ValueError(f"Invalid {field}: '{value}' (allowed: {sorted(allowed)})")


def _validate_subset(field: str, values: List[str], allowed: Set[str]) -> None:
    invalid = [v for v in values if v not in allowed]
    if invalid:
        raise ValueError(f"Invalid {field}(s): {invalid}. Allowed: {sorted(allowed)}")
