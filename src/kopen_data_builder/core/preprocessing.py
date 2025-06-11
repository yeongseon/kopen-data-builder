# src/kopen_data_builder/core/preprocessing.py

"""
Preprocessing module: Contains functions for preprocessing dataset metadata.
This module provides utilities to validate and preprocess dataset metadata
before further processing or uploading.
"""

import pandas as pd


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform standard preprocessing on a pandas DataFrame:
    - Strip and normalize column names
    - Convert date columns to datetime
    - Ensure all string columns are proper strings

    Args:
        df (pd.DataFrame): The input raw DataFrame.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    df = df.copy()

    # Normalize column names: lowercase, replace spaces/symbols with underscore
    df.columns = df.columns.str.strip().str.lower().str.replace(r"\W+", "_", regex=True)

    # Convert string columns to str type
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].astype(str).str.strip()

    # Convert date columns (if any)
    for col in df.columns:
        if "date" in col or "날짜" in col:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    return df
