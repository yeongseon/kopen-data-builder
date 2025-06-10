# src/kopen_data_builder/validator.py

"""
Validator module: Performs checks on a dataset directory to ensure it is complete and valid.
This includes file existence, format consistency, and metadata structure.
"""

import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def validate_dataset(path: str) -> bool:
    """
    Validate that a dataset directory contains expected files and structure.

    Args:
        path (str): Path to the dataset directory.

    Returns:
        bool: True if the dataset is valid, False otherwise.

    Raises:
        FileNotFoundError: If the path does not exist.
    """
    dataset_path = Path(path)
    if not dataset_path.exists():
        raise FileNotFoundError(f"Dataset path does not exist: {dataset_path}")

    metadata_file = dataset_path / "dataset_infos.json"
    if not metadata_file.exists():
        logger.warning("Missing metadata file: %s", metadata_file)
        return False

    try:
        with open(metadata_file, "r", encoding="utf-8") as f:
            metadata = json.load(f)
        if "splits" not in metadata:
            logger.warning("Invalid metadata structure: 'splits' key missing")
            return False

        for _split_name, split_info in metadata["splits"].items():
            split_path = dataset_path / split_info["path"]
            if not split_path.exists():
                logger.warning("Missing split file: %s", split_path)
                return False

        logger.info("Dataset validation passed: %s", dataset_path)
        return True

    except Exception as e:
        logger.error("Validation failed: %s", str(e))
        return False
