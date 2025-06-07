# src/kopen_data_builder/core/metadata.py

"""
Metadata module: Generates a Hugging Face-compatible dataset_infos.json file
based on the contents of a directory containing split CSV files.
"""

import json
import logging
from pathlib import Path
from typing import Union

logger = logging.getLogger(__name__)


def generate_metadata(data_dir: Union[str, Path], output_path: Union[str, Path]) -> None:
    """
    Generate a dataset_infos.json metadata file describing the available splits.

    Args:
        data_dir (str | Path): Directory containing split CSV files.
        output_path (str | Path): Path to write the generated JSON metadata.

    Raises:
        FileNotFoundError: If the input directory does not exist.
        Exception: For any metadata generation or file I/O errors.
    """
    data_path = Path(data_dir)
    out_path = Path(output_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if not data_path.exists():
        raise FileNotFoundError(f"Split data directory not found: {data_path}")

    try:
        files = sorted(data_path.glob("*.csv"))
        logger.info("Generating metadata from %d files in %s", len(files), data_path)

        infos = {}
        for file in files:
            split_name = file.stem.lower()
            infos[split_name] = {
                "description": f"Split file for {split_name}.",
                "path": file.name,
            }

        with out_path.open("w", encoding="utf-8") as f:
            json.dump({"splits": infos}, f, indent=2, ensure_ascii=False)

        logger.info("Metadata saved to: %s", out_path)

    except Exception as e:
        logger.error("Metadata generation failed: %s", str(e))
        raise
