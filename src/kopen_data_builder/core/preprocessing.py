# src/kopen_data_builder/core/preprocessing.py

"""
Preprocessing module: Contains functions for standardizing and cleaning data in pandas DataFrames.
This module provides utilities to normalize column names, convert
data types, and prepare data for further processing.
"""
import logging
import re
from typing import List

import pandas as pd
from pandas import DataFrame, Series

logger = logging.getLogger(__name__)


def normalize_column_name(name: str) -> str:
    """
    Normalize a column name by:
    - Converting to lowercase
    - Replacing non-alphanumeric characters with underscores
    - Removing leading/trailing and repeated underscores

    Args:
        name (str): Original column name

    Returns:
        str: Normalized column name
    """
    normalized: str = re.sub(r"\W+", "_", name.strip().lower())
    normalized = re.sub(r"_+", "_", normalized).strip("_")
    return normalized


def is_probably_date_column(series: Series) -> bool:
    """
    Detect whether a column contains mostly date-like values.
    Returns True if over 80% of non-null values are parseable as datetime.
    """
    non_null = series.dropna()
    if non_null.empty:
        return False

    parsed = pd.to_datetime(non_null, errors="coerce", utc=True)
    success_ratio = parsed.notna().sum() / len(parsed)
    return bool(success_ratio >= 0.8)


def preprocess_data(df: DataFrame) -> DataFrame:
    """
    Perform standard preprocessing on a pandas DataFrame:
    1. Normalize column names to lowercase, underscore style
    2. Clean string columns by stripping whitespace
    3. Detect and convert date-like columns based on actual values

    Args:
        df (pd.DataFrame): The input raw DataFrame

    Returns:
        pd.DataFrame: The cleaned and normalized DataFrame
    """
    df = df.copy()

    # Normalize column names
    original_columns: List[str] = list(df.columns)  # Avoid mypy error on .tolist()
    df.columns = [normalize_column_name(col) for col in original_columns]
    logger.debug("Normalized columns from %s to %s", original_columns, list(df.columns))

    # Strip whitespace from string columns
    for col in df.select_dtypes(include=["object", "string"]).columns:
        try:
            df[col] = df[col].astype(str).str.strip()
        except Exception as e:
            logger.warning("Could not process string column '%s': %s", col, e)

    # Convert date-like columns
    for col in df.columns:
        if not pd.api.types.is_datetime64_any_dtype(df[col]):
            if is_probably_date_column(df[col]):
                try:
                    df[col] = pd.to_datetime(df[col], errors="coerce")
                    logger.debug("Converted column '%s' to datetime.", col)
                except Exception as e:
                    logger.warning("Failed to convert column '%s' to datetime: %s", col, e)

    return df
