# src/kopen_data_builder/cli/preprocess_cmd.py

"""
Preprocess CLI: Clean up and standardize raw CSV files.

This module provides a command-line interface to preprocess CSV datasets
using built-in cleaning utilities before further transformation or upload.
"""

import logging

import pandas as pd
import typer

from kopen_data_builder.core.preprocessing import preprocess_data

app = typer.Typer(help="Preprocess and clean raw CSV data before transformation.")
logger = logging.getLogger(__name__)


@app.command()
def run(
    input_csv: str = typer.Option(
        None,
        prompt="📥 Enter the path to the input CSV file",
        help="Path to the raw input CSV file",
    ),
    output_csv: str = typer.Option(
        None,
        prompt="📤 Enter the path to save the cleaned output CSV",
        help="Path where the cleaned CSV will be saved",
    ),
) -> None:
    """
    Preprocess a CSV file and save the cleaned version.

    This function loads a CSV file, applies standard cleaning rules using
    `preprocess_data`, and writes the result to the specified output path.

    Example:
    $ kopen preprocess run --input-csv raw_data.csv --output-csv cleaned_data.csv

    Args:
        input_csv (str): Path to the raw input CSV file.
        output_csv (str): Path where the cleaned CSV will be saved.
    """
    logger.info(f"Loading CSV from: {input_csv}")
    df = pd.read_csv(input_csv)

    logger.info("Preprocessing data...")
    cleaned = preprocess_data(df)

    logger.info(f"Saving cleaned data to: {output_csv}")
    cleaned.to_csv(output_csv, index=False)
    typer.echo(f"✅ Preprocessed data saved to: {output_csv}")
