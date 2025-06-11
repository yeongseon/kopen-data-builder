# src/kopen_data_builder/cli/split_cmd.py

"""
Split CLI: Split or merge CSV datasets using specified rules.

This CLI provides commands to divide datasets into train/test splits
or to merge multiple datasets into a single file.
"""

import json
import logging
from pathlib import Path

import pandas as pd
import typer

from kopen_data_builder.core.splitter import merge_datasets, split_dataset

app = typer.Typer(help="Split and merge datasets using defined rules or input files.")
logger = logging.getLogger(__name__)


@app.command()
def split(
    input_csv: str = typer.Option(
        None,
        prompt="📥 Enter path to input CSV",
        help="Path to the input CSV file",
    ),
    split_json: str = typer.Option(
        None,
        prompt="⚙️ Enter path to split rules JSON",
        help="Path to JSON file with split ratios (e.g., {'train': 0.8, 'test': 0.2})",
    ),
    output_dir: str = typer.Option(
        None,
        prompt="📁 Enter directory to save split files",
        help="Directory where the split CSV files will be saved",
    ),
) -> None:
    """
    Split a CSV dataset using rules from a JSON file.

    Example:
    $ kopen split split --input-csv data.csv --split-json rules.json --output-dir ./splits
    """
    logger.info(f"Loading dataset from {input_csv}")
    df = pd.read_csv(input_csv)

    logger.info(f"Loading split rules from {split_json}")
    with open(split_json, encoding="utf-8") as f:
        rules = json.load(f)

    logger.info("Splitting dataset...")
    result = split_dataset(df, rules)

    Path(output_dir).mkdir(parents=True, exist_ok=True)
    for name, part in result.items():
        output_path = Path(output_dir) / f"{name}.csv"
        part.to_csv(output_path, index=False)
        logger.info(f"Saved {name} split to {output_path}")
        typer.echo(f"✅ {name} split saved to {output_path}")


@app.command()
def merge(
    input_csvs: str = typer.Option(
        None,
        prompt="📂 Enter comma-separated CSV file paths to merge",
        help="Comma-separated list of CSV file paths to merge",
    ),
    output_csv: str = typer.Option(
        None,
        prompt="📤 Enter path to save merged CSV",
        help="Path to output CSV file for merged result",
    ),
) -> None:
    """
    Merge multiple CSV files into a single dataset.

    Example:
    $ kopen split merge --input-csvs file1.csv,file2.csv --output-csv merged.csv
    """
    paths = [p.strip() for p in input_csvs.split(",")]
    logger.info(f"Merging files: {paths}")
    dfs = [pd.read_csv(p) for p in paths]

    merged = merge_datasets(dfs)
    merged.to_csv(output_csv, index=False)

    logger.info(f"Merged dataset saved to: {output_csv}")
    typer.echo(f"✅ Merged dataset saved to: {output_csv}")
