# src/kopen_data_builder/cli/build_cmd.py

"""
Build CLI: Build Hugging Face dataset directory from CSV splits.
This command reads a JSON file mapping dataset splits to their respective CSV files,
and generates a Hugging Face-compatible dataset repository structure.
"""

import json

import typer

from kopen_data_builder.core.builder import build_repository

app = typer.Typer(help="Build Hugging Face-compatible dataset structure.")


@app.command()
def run(
    dataset_name: str,
    csv_json_path: str,
    output_dir: str,
) -> None:
    """
    Build a Hugging Face-compatible dataset from split CSVs.

    Args:
        dataset_name: Name of the dataset.
        csv_json_path: Path to JSON file mapping split names to CSV file paths.
        output_dir: Output directory for Hugging Face-compatible dataset.
    """
    with open(csv_json_path, "r", encoding="utf-8") as f:
        csv_paths = json.load(f)

    build_repository(csv_paths=csv_paths, dataset_name=dataset_name, output_dir=output_dir)
    typer.echo("✅ Dataset repository prepared.")
