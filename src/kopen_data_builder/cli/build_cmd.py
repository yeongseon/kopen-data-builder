# src/kopen_data_builder/cli/build_cmd.py

"""
Build CLI: Build Hugging Face dataset directory from CSV splits.
This command reads a JSON file mapping dataset splits to their respective CSV files,
and generates a Hugging Face-compatible dataset repository structure.
"""

import json
import logging

import typer

from kopen_data_builder.core.builder import build_repository

app = typer.Typer(help="Build Hugging Face-compatible dataset structure.")
logger = logging.getLogger(__name__)


@app.command()
def run(
    dataset_name: str = typer.Option(
        None,
        prompt="📛 Enter the dataset name",
        help="The name to use for the Hugging Face dataset repository",
    ),
    csv_json_path: str = typer.Option(
        None,
        prompt="📄 Enter path to split JSON (e.g. {'train': 'train.csv', ...})",
        help="Path to JSON file that maps split names to CSV file paths",
    ),
    output_dir: str = typer.Option(
        None,
        prompt="📁 Enter output directory for the dataset",
        help="Directory where the Hugging Face-compatible dataset structure will be saved",
    ),
) -> None:
    """
    Build a Hugging Face-compatible dataset from split CSVs.

    This command reads split definitions from a JSON file and generates
    the necessary dataset files and structure to upload to Hugging Face Hub.

    Example:
    $ kopen build run --dataset-name my-dataset --csv-json-path ./splits.json --output-dir ./my_dataset_repo

    Args:
        dataset_name (str): Name of the dataset to create.
        csv_json_path (str): Path to a JSON file mapping split names to CSV file paths.
        output_dir (str): Directory where the dataset repository will be created.
    """
    logger.info(f"Reading split definition from: {csv_json_path}")
    with open(csv_json_path, "r", encoding="utf-8") as f:
        csv_paths = json.load(f)

    logger.info(f"Building dataset repository for: {dataset_name}")
    build_repository(csv_paths=csv_paths, dataset_name=dataset_name, output_dir=output_dir)

    typer.echo("✅ Dataset repository prepared.")
