# src/kopen_data_builder/core/utils.py

"""
Utils module: Common utility functions for loading and saving CSV files using Polars.
Encapsulates repetitive I/O operations for consistency and reuse.
"""

import logging
from pathlib import Path

import polars as pl

logger = logging.getLogger(__name__)


def load_csv(path: str) -> pl.DataFrame:
    """
    Load a CSV file into a Polars DataFrame.

    Args:
        path (str): Path to the CSV file.

    Returns:
        pl.DataFrame: Loaded data.

    Raises:
        FileNotFoundError: If the CSV file does not exist.
    """
    csv_path = Path(path)
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    logger.info("Loading CSV file: %s", csv_path)
    return pl.read_csv(csv_path)


def save_csv(df: pl.DataFrame, path: str) -> None:
    """
    Save a Polars DataFrame to a CSV file.

    Args:
        df (pl.DataFrame): Data to save.
        path (str): Destination file path.
    """
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.write_csv(output_path)
    logger.info("Saved CSV file to: %s", output_path)
