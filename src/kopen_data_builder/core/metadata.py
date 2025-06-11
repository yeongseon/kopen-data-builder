# src/kopen_data_builder/core/metadata.py

"""
Metadata module: Generates a Hugging Face-compatible dataset_infos.json file
based on the contents of a directory containing split CSV files.
"""

import json
import logging
from pathlib import Path
from typing import Any, Dict, Union

logger = logging.getLogger(__name__)


def generate_metadata(data_dir: Union[str, Path], output_path: Union[str, Path]) -> Dict[str, Any]:
    """
    Generate a dataset_infos.json metadata file describing the available splits.

    Args:
        data_dir (str | Path): Directory containing split CSV files.
        output_path (str | Path): Path to write the generated JSON metadata.

    Returns:
        dict: The generated metadata dictionary.

    Raises:
        FileNotFoundError: If the input directory does not exist or contains no CSV files.
        Exception: For any metadata generation or file I/O errors.
    """
    data_path = Path(data_dir).resolve()
    out_path = Path(output_path).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if not data_path.exists():
        raise FileNotFoundError(f"Split data directory not found: {data_path}")

    files = sorted(data_path.glob("*.csv"))
    if not files:
        raise FileNotFoundError(f"No CSV files found in {data_path}")

    try:
        logger.info("Generating metadata from %d files in %s", len(files), data_path)

        infos = {
            file.stem.lower(): {
                "description": f"Split file for {file.stem}.",
                "path": file.name,
            }
            for file in files
        }

        with out_path.open("w", encoding="utf-8") as f:
            json.dump({"splits": infos}, f, indent=2, ensure_ascii=False)

        logger.info("Metadata saved to: %s", out_path)
        return {"splits": infos}

    except Exception:
        logger.exception("Metadata generation failed.")
        raise
