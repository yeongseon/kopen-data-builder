# src/kopen_data_builder/core/metadata.py

"""
Metadata I/O module: Handles generation and loading of metadata.yaml files
with human-readable comments and schema validation.
"""

import logging
from pathlib import Path

import yaml  # type: ignore
from pydantic import ValidationError

from kopen_data_builder.core.models import DatasetMeta

logger = logging.getLogger(__name__)


def init_metadata(output_path: str) -> None:
    """
    Create a metadata.yaml template with comments and valid example values.
    This version preserves field-level guidance using a string-based template.

    Args:
        output_path (str): Path where the metadata.yaml file should be created.

    Raises:
        FileExistsError: If the file already exists.
        OSError: If writing fails.
    """
    path = Path(output_path).resolve()

    if path.exists():
        raise FileExistsError(f"Metadata already exists at: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)

    template = """\
# -----------------------------------------------------------------------------
# kopen-data-builder: metadata.yaml template
#
# This file defines metadata used to publish your dataset to Hugging Face.
#
# INSTRUCTIONS:
# - Replace example values below with your actual dataset information.
# - Some fields accept only predefined values. See 'Allowed:' comments below.
# - For details, visit: https://github.com/yeongseon/kopen-data-builder
# -----------------------------------------------------------------------------

pretty_name: "Seoul Public Bike Usage (Monthly)"  # Human-readable name

description: |
  This dataset contains monthly usage data for public bikes in Seoul.
  Includes trip count, distance, and CO₂ emissions saved.

languages:  # Language(s) used in the actual dataset content (not the README)
  - ko
  - en  # Only include if the data content includes English

tags:
  - tabular
  - transportation  # Free-form searchable tags

license: cc-by-4.0  # Allowed: cc-by-4.0, cc0-1.0, MIT, Apache-2.0

annotations_creators:
  - no-annotation  # Allowed: no-annotation, crowdsourced, machine-generated, expert-generated

language_creators:
  - found  # Allowed: found, crowdsourced, machine-generated

multilinguality: monolingual  # Allowed: monolingual, multilingual, translation

task_categories:
  - time-series-forecasting  # Allowed: any valid HF task (e.g., text-classification)

task_ids:
  - bike-usage-forecasting  # Optional: fine-grained task identifier

size_categories: 100K<n<1M  # Allowed: n<1K, 1K<n<10K, 10K<n<100K, 100K<n<1M, 1M<n<10M, n>10M

source_datasets:
  - original  # Usually: original or list of upstream datasets

source_agency:
  en: Seoul Open Data Plaza
  ko: 서울열림데이터광장

original_url: https://data.seoul.go.kr/dataList/OA-15248/F/1/datasetView.do

update_frequency: Semiannual  # e.g., Monthly, Quarterly, Annual

reference_date: 2018-01-01 to 2025-12-31  # Format: YYYY-MM-DD or range

kogl_type: Type 1 KOGL  # Allowed: 1, 2, 3, 4 or 'Type X KOGL'

splits:  # Optional: split ratios (values should sum to 1.0)
  train: 0.8
  test: 0.2
"""

    try:
        path.write_text(template, encoding="utf-8")
        logger.info("Commented metadata template created at: %s", path)
    except Exception as e:
        logger.exception("Failed to write metadata template: %s", e)
        raise


def load_metadata(input_path: str) -> DatasetMeta:
    """
    Load metadata.yaml file and parse it into a validated DatasetMeta object.

    Args:
        input_path (str): Path to the metadata.yaml file.

    Returns:
        DatasetMeta: Validated Pydantic model of the metadata.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is malformed, improperly encoded, or fails schema validation.
    """
    path = Path(input_path).resolve()

    if not path.exists():
        raise FileNotFoundError(f"Metadata file not found at: {path}")

    # Try reading as UTF-8, then fallback to cp949
    raw = None
    last_error = None
    for encoding in ("utf-8", "cp949"):
        try:
            with path.open("r", encoding=encoding) as f:
                raw = yaml.safe_load(f)
            if raw is not None:
                if encoding != "utf-8":
                    logger.warning("Metadata file loaded with fallback encoding: %s", encoding)
                break
        except (UnicodeDecodeError, yaml.YAMLError) as e:
            last_error = e
            continue

    if raw is None:
        raise ValueError(f"Failed to read metadata file due to encoding or YAML error: {last_error}")

    if not isinstance(raw, dict):
        raise ValueError(f"Invalid metadata format: expected a dictionary, got {type(raw).__name__}")

    try:
        return DatasetMeta.parse_obj(raw)
    except ValidationError as e:
        raise ValueError(f"Metadata does not conform to expected schema: {e}") from e
