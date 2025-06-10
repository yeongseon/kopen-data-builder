# src/kopen_data_builder/stransformer.py

"""
Transformer module: Cleans and preprocesses raw data into a standardized format.
Designed to be modular and reusable for various datasets.
"""

import logging
from pathlib import Path
from typing import Union

import polars as pl

logger = logging.getLogger(__name__)


def transform_data(input_path: Union[str, Path], output_path: Union[str, Path]) -> None:
    """
    Load raw data from a CSV file, apply basic cleaning, and save the cleaned result.

    Args:
        input_path (str | Path): Path to the input CSV file.
        output_path (str | Path): Path to write the cleaned CSV output.

    Raises:
        FileNotFoundError: If the input file does not exist.
        Exception: For any other processing-related failures.
    """
    in_path = Path(input_path)
    out_path = Path(output_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    logger.info("Reading raw data from: %s", in_path)

    if not in_path.exists():
        raise FileNotFoundError(f"Input file not found: {in_path}")

    try:
        df = pl.read_csv(in_path)

        # Standardize column names
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

        # Drop columns with any nulls
        columns_without_nulls = [col for col in df.columns if df[col].null_count() == 0]
        df = df.select(columns_without_nulls)

        # Drop any remaining rows with nulls
        df = df.drop_nulls()

        logger.info("Transformed shape: %s rows, %s columns", df.height, df.width)
        df.write_csv(out_path)
        logger.info("Cleaned data saved to: %s", out_path)

    except Exception as e:
        logger.error("Transformation failed: %s", str(e))
        raise
