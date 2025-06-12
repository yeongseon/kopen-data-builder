# src/kopen_data_builder/core/metadata.py (추가 코드)

"""
Metadata generation module: Provides utility to create an initial metadata.yaml template
for Hugging Face-compatible datasets.
"""

import logging
from pathlib import Path

import yaml  # type: ignore[import-untyped]

logger = logging.getLogger(__name__)

# Predefined template for metadata.yaml
TEMPLATE = {
    "name": "your-dataset-name",
    "title": "데이터셋 제목",
    "description": "간단한 설명",
    "source_url": "https://example.com",
    "license": "CC-BY-4.0",
    "language": ["ko"],
    "tasks": ["문서분류"],
    "split_type": "full",
    "category": "etc",
    "tags": ["tag1", "tag2"],
}


def init_metadata(output_path: str) -> None:
    """
    Generate an initial metadata.yaml template file at the specified location.

    Args:
        output_path (str): Target path to save the metadata.yaml file.

    Raises:
        FileExistsError: If the file already exists at the given path.
    """
    path = Path(output_path).resolve()

    if path.exists():
        logger.error("Metadata file already exists: %s", path)
        raise FileExistsError(f"Metadata already exists: {path}")

    path.parent.mkdir(parents=True, exist_ok=True)

    try:
        with path.open("w", encoding="utf-8") as f:
            yaml.safe_dump(TEMPLATE, f, allow_unicode=True, sort_keys=False)
        logger.info("Metadata template created at: %s", path)
    except Exception as e:
        logger.exception("Failed to write metadata template: %s", e)
        raise
