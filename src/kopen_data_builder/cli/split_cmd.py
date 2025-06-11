# src/kopen_data_builder/cli/split_cmd.py

"""
Split command module: Contains commands for splitting and merging datasets.
This module provides CLI commands to split a dataset into training, test, etc.
and to merge multiple datasets into one.
"""

import json
from typing import List

import pandas as pd
import typer

from kopen_data_builder.core.splitter import merge_datasets, split_dataset

app = typer.Typer(help="Split and merge datasets using specified rules or input files.")


@app.command(name="run", help="Split a dataset into train/test/etc. using rules in JSON format.")
def run(input_csv: str, split_json: str, output_dir: str) -> None:
    """Split a dataset into train/test/etc. using rules in JSON format."""
    df = pd.read_csv(input_csv)
    with open(split_json, "r", encoding="utf-8") as f:
        rules = json.load(f)

    splits = split_dataset(df, rules)
    for name, split_df in splits.items():
        out_path = f"{output_dir.rstrip('/')}/{name}.csv"
        split_df.to_csv(out_path, index=False)
        typer.echo(f"✅ Saved split '{name}' to {out_path}")


@app.command(name="merge", help="Merge multiple CSV files into one dataset.")
def merge(input_csvs: List[str], output_csv: str) -> None:
    """Merge multiple CSV files into a single dataset."""
    dfs = [pd.read_csv(path) for path in input_csvs]
    merged = merge_datasets(dfs)
    merged.to_csv(output_csv, index=False)
    typer.echo(f"✅ Merged dataset saved to: {output_csv}")
