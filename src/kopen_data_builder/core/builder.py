# src/kopen_data_builder/core/builder.py

from pathlib import Path
from typing import Any, Dict, Union

import polars as pl
from datasets import Dataset, DatasetDict


def load_data(file_path: Union[str, Path]) -> pl.DataFrame:
    """
    Load a CSV or Excel file using polars.

    Args:
        file_path (str | Path): Path to the CSV or Excel file.

    Returns:
        pl.DataFrame: Loaded Polars DataFrame.

    Raises:
        ValueError: If the file extension is unsupported.
    """
    path = Path(file_path)
    if path.suffix == ".csv":
        return pl.read_csv(path)
    elif path.suffix in [".xls", ".xlsx"]:
        return pl.read_excel(path)
    else:
        raise ValueError(f"Unsupported file format: {path.suffix}")


def build_dataset(metadata: Dict[str, Any], df: pl.DataFrame) -> DatasetDict:
    """
    Convert a polars DataFrame into a Hugging Face DatasetDict based on
    split_type and metadata settings.

    Supported split types:
        - "by_column_year": Extract year from specified datetime column (e.g., "rental_start_time")
        - "full" (default): Return the entire dataset as a single 'train' split

    Args:
        metadata (dict): Metadata dictionary with 'split_type' and optionally
                         'split_column' and 'split_column_format'
        df (pl.DataFrame): Source data

    Returns:
        DatasetDict: A Hugging Face DatasetDict with one or more splits

    Raises:
        ValueError: If required metadata is missing or invalid
    """
    split_type = metadata.get("split_type", "full")
    split_column = metadata.get("split_column")
    datetime_format = metadata.get("split_column_format")

    if split_type == "by_column_year":
        if not split_column or split_column not in df.columns:
            raise ValueError(f"Missing or invalid split_column: '{split_column}'")

        # Parse datetime column
        if datetime_format:
            df = df.with_columns([pl.col(split_column).str.strptime(pl.Datetime, format=datetime_format)])
        else:
            df = df.with_columns([pl.col(split_column).str.strptime(pl.Datetime)])

        # Extract year into a temporary column
        df = df.with_columns([pl.col(split_column).dt.year().alias("_year")])

        dataset_dict: Dict[str, Dataset] = {}
        for year in df["_year"].unique().to_list():
            split_df = df.filter(pl.col("_year") == year).drop("_year")
            dataset = Dataset.from_pandas(split_df.to_pandas())
            dataset_dict[str(year)] = dataset

        return DatasetDict(dataset_dict)

    # Default: return entire DataFrame as a single 'train' split
    return DatasetDict({"train": Dataset.from_pandas(df.to_pandas())})
