# src/kopen_data_builder/core/builder.py

"""
Builder module: Prepares a Hugging Face dataset repository from CSV files.
This module provides functionality to create a local directory structure
for a dataset, including saving splits, writing metadata, and preparing for upload.
"""

import logging
import shutil
from pathlib import Path
from typing import Dict

import pandas as pd

logger = logging.getLogger(__name__)


def prepare_hf_repository(
    dataset_name: str,
    splits: Dict[str, pd.DataFrame],
    output_dir: str,
) -> None:
    """
    Prepare a local directory in Hugging Face dataset format.

    Args:
        dataset_name (str): Name of the dataset.
        splits (dict): Dictionary of split name to pandas DataFrame.
        output_dir (str): Target directory to prepare.
    """
    repo_dir = Path(output_dir).resolve()
    if repo_dir.exists():
        shutil.rmtree(repo_dir)
    repo_dir.mkdir(parents=True, exist_ok=True)

    _save_splits(repo_dir, splits)
    _write_readme(repo_dir, dataset_name)
    _write_placeholder_metadata(repo_dir)

    logger.info("✅ Hugging Face repository prepared at %s", repo_dir)


def _save_splits(repo_dir: Path, splits: Dict[str, pd.DataFrame]) -> None:
    for split_name, df in splits.items():
        split_path = repo_dir / f"{split_name}.csv"
        df.to_csv(split_path, index=False, encoding="utf-8-sig")  # UTF-8 with BOM for Excel compatibility
        logger.debug("Saved split %s to %s", split_name, split_path)


def _write_readme(repo_dir: Path, dataset_name: str) -> None:
    readme_path = repo_dir / "README.md"
    content = f"# Dataset: {dataset_name}\n\nThis dataset was prepared for upload to Hugging Face Datasets.\n"
    readme_path.write_text(content, encoding="utf-8")
    logger.debug("README.md created at %s", readme_path)


def _write_placeholder_metadata(repo_dir: Path) -> None:
    placeholder = repo_dir / "dataset_infos.json"
    placeholder.write_text("{}", encoding="utf-8")
    logger.debug("Empty dataset_infos.json created at %s", placeholder)


def build_repository(csv_paths: Dict[str, str], dataset_name: str, output_dir: str) -> None:
    """
    Build the Hugging Face dataset directory structure from CSVs.

    Args:
        csv_paths (dict): Dictionary mapping split name (e.g., 'train') to CSV path.
        dataset_name (str): Name of the dataset.
        output_dir (str): Path to the output directory.
    """
    splits = {}
    for name, path in csv_paths.items():
        df = pd.read_csv(path)
        splits[name] = df
        logger.debug("Loaded CSV: %s → %s rows", path, len(df))

    prepare_hf_repository(dataset_name, splits, output_dir)
    logger.info("✅ Dataset build process completed.")
