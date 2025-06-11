# src/kopen_data_builder/core/splitter.py

"""
Splitter module: Contains functions for splitting and merging datasets.
This module provides utilities to split a dataset into training and test sets
and to merge multiple datasets into one.
"""

import logging
from typing import Dict, List

import pandas as pd
from sklearn.model_selection import train_test_split

logger = logging.getLogger(__name__)


def split_dataset(df: pd.DataFrame, rules: Dict[str, float]) -> Dict[str, pd.DataFrame]:
    """
    Split a DataFrame according to given ratio rules.

    Args:
        df (pd.DataFrame): The full dataset.
        rules (dict): e.g., {"train": 0.8, "test": 0.2}

    Returns:
        Dict[str, pd.DataFrame]: A dict of split names to DataFrames.

    Raises:
        ValueError: If rules are invalid or unsupported.
    """
    if not rules or not isinstance(rules, dict):
        raise ValueError("Rules must be a non-empty dictionary.")

    total_ratio = sum(rules.values())
    if not abs(total_ratio - 1.0) < 1e-6:
        raise ValueError(f"Split ratios must sum to 1.0, got {total_ratio:.3f}")

    logger.debug("Splitting dataset with rules: %s", rules)

    if set(rules.keys()) == {"train", "test"}:
        df_train, df_test = train_test_split(df, test_size=rules["test"], random_state=42)
        return {"train": df_train, "test": df_test}

    raise NotImplementedError("Only 'train/test' split is currently supported.")


def merge_datasets(dfs: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Merge multiple DataFrames into one.

    Args:
        dfs (List[pd.DataFrame]): A list of DataFrames to merge.

    Returns:
        pd.DataFrame: A single merged DataFrame.

    Raises:
        ValueError: If dfs is empty.
    """
    if not dfs:
        raise ValueError("No datasets provided to merge.")
    logger.debug("Merging %d datasets", len(dfs))
    return pd.concat(dfs, ignore_index=True)
