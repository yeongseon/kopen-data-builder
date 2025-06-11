# src/kopen_data_builder/core/builder.py

"""
Builds a Hugging Face dataset repository from CSV files.
This module provides functionality to prepare a local directory structure
for a Hugging Face dataset, including saving splits as CSV files,
"""

import shutil
from pathlib import Path
from typing import Dict

import pandas as pd


def prepare_hf_repository(
    output_dir: str,
    dataset_name: str,
    splits: Dict[str, pd.DataFrame],
) -> None:
    """
    Prepare a local directory in Hugging Face dataset format.

    Args:
        output_dir (str): Target directory to prepare.
        dataset_name (str): Name of the dataset.
        splits (dict): Dictionary of split name to pandas DataFrame.
    """
    repo_dir = Path(output_dir).resolve()
    if repo_dir.exists():
        shutil.rmtree(repo_dir)
    repo_dir.mkdir(parents=True)

    # Save each split to CSV
    for split_name, df in splits.items():
        split_path = repo_dir / f"{split_name}.csv"
        df.to_csv(split_path, index=False)

    # Create README.md
    readme_path = repo_dir / "README.md"
    with readme_path.open("w", encoding="utf-8") as f:
        f.write(f"# Dataset: {dataset_name}\n")
        f.write("\nThis dataset was prepared for upload to Hugging Face Datasets.\n")

    # Create dataset card template (optional)
    dataset_card_path = repo_dir / "dataset_infos.json"
    with dataset_card_path.open("w", encoding="utf-8") as f:
        f.write("{}")  # empty placeholder for now

    print(f"✅ Hugging Face repository prepared at {repo_dir}")


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

    prepare_hf_repository(output_dir, dataset_name, splits)
    print("✅ Dataset build process completed.")
