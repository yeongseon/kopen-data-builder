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
    csv_json: str,
    output_dir: str,
) -> None:
    """
    Build a dataset repository from split CSVs and metadata.
    """
    with open(csv_json, "r", encoding="utf-8") as f:
        csv_paths = json.load(f)
    build_repository(csv_paths, dataset_name, output_dir)
    typer.echo(f"✅ Dataset '{dataset_name}' repository prepared at: {output_dir}")
