# src/kopen_data_builder/core/splitter.py

"""
Splitter module: Divides the cleaned dataset by quarter based on a date column.
Useful for organizing time-series datasets into smaller segments.
"""

import logging
from pathlib import Path
from typing import Union

import polars as pl

logger = logging.getLogger(__name__)


def split_by_quarter(
    input_path: Union[str, Path],
    output_dir: Union[str, Path],
    date_column: str = "date",
) -> None:
    """
    Split the input CSV dataset into separate files by quarter using a specified date column.

    Args:
        input_path (str | Path): Path to the cleaned input CSV file.
        output_dir (str | Path): Directory to store the split output CSV files.
        date_column (str): Column name containing date values (default is "date").

    Raises:
        FileNotFoundError: If the input file does not exist.
        Exception: For processing or parsing errors.
    """
    in_path = Path(input_path)
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    logger.info("Splitting dataset by quarter: %s", in_path)

    if not in_path.exists():
        raise FileNotFoundError(f"Input file not found: {in_path}")

    try:
        df = pl.read_csv(in_path)

        df = df.with_columns(
            [
                pl.col(date_column).str.strptime(pl.Date, "%Y-%m-%d").alias("parsed_date"),
                pl.col(date_column).str.strptime(pl.Date, "%Y-%m-%d").dt.year().alias("year"),
                pl.col(date_column).str.strptime(pl.Date, "%Y-%m-%d").dt.quarter().alias("quarter"),
            ]
        )

        unique_groups = df.select(["year", "quarter"]).unique()

        for row in unique_groups.iter_rows(named=True):
            year = row["year"]
            quarter = row["quarter"]
            group_df = df.filter((pl.col("year") == year) & (pl.col("quarter") == quarter))
            filename = f"{year}Q{quarter}.csv"
            path = out_dir / filename
            group_df.write_csv(path)
            logger.info("Saved split: %s", path)

    except Exception as e:
        logger.error("Quarter splitting failed: %s", str(e))
        raise
