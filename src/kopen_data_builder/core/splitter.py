# src/kopen_data_builder/core/splitter.py

"""
Splitter module: Contains functions for splitting and merging datasets.
This module provides utilities to split a dataset into training and test sets
and to merge multiple datasets into one.
"""

from typing import Dict, List

import pandas as pd
from sklearn.model_selection import train_test_split


def split_dataset(df: pd.DataFrame, rules: Dict[str, float]) -> Dict[str, pd.DataFrame]:
    """
    Split a DataFrame according to given ratio rules.

    Args:
        df (pd.DataFrame): The full dataset.
        rules (dict): Dictionary like {"train": 0.8, "test": 0.2}

    Returns:
        Dict[str, pd.DataFrame]: A dictionary with keys like "train", "test"
    """
    if "train" in rules and "test" in rules:
        df_train, df_test = train_test_split(df, test_size=rules["test"], random_state=42)
        return {"train": df_train, "test": df_test}
    return {"full": df}


def merge_datasets(dfs: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Merge multiple DataFrames into one.

    Args:
        dfs (List[pd.DataFrame]): A list of DataFrames to merge.

    Returns:
        pd.DataFrame: A single merged DataFrame.
    """
    return pd.concat(dfs, ignore_index=True)
