# src/kopen_data_builder/core/preprocessing.py

"""
Preprocessing module: Contains functions for standardizing and cleaning data in pandas DataFrames.
This module provides utilities to normalize column names, convert
data types, and prepare data for further processing.
"""
import logging
import re

import pandas as pd

logger = logging.getLogger(__name__)


def normalize_column_name(name: str) -> str:
    """Normalize a single column name."""
    return re.sub(r"\W+", "_", name.strip().lower())


def is_date_column(name: str) -> bool:
    """Determine if a column likely represents a date."""
    return any(keyword in name.lower() for keyword in ["date", "날짜", "일자"])


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform standard preprocessing on a pandas DataFrame:
    - Normalize column names
    - Ensure string columns are stripped and consistent
    - Convert date-like columns to datetime

    Args:
        df (pd.DataFrame): The input raw DataFrame.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    df = df.copy()

    # 1. Normalize column names
    df.columns = [normalize_column_name(col) for col in df.columns]
    logger.debug("Normalized column names: %s", list(df.columns))

    # 2. Convert string-like columns
    object_cols = df.select_dtypes(include=["object"]).columns
    for col in object_cols:
        try:
            df[col] = df[col].astype(str).str.strip()
        except Exception as e:
            logger.warning("Failed to convert column '%s' to string: %s", col, str(e))

    # 3. Convert date columns
    for col in df.columns:
        if is_date_column(col):
            try:
                df[col] = pd.to_datetime(df[col], errors="coerce")
            except Exception as e:
                logger.warning("Failed to convert column '%s' to datetime: %s", col, str(e))

    return df
