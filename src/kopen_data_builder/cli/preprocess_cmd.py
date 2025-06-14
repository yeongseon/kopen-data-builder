# src/kopen_data_builder/cli/preprocess_cmd.py

"""
Preprocess CLI: Clean up and standardize raw CSV files.

This module provides a command-line interface to preprocess CSV datasets
using built-in cleaning utilities before further transformation or upload.
"""

import logging

import pandas as pd
import typer
from typer import Option

from kopen_data_builder.core.preprocessing import preprocess_data

# Create a Typer app for the "preprocess" command group
app = typer.Typer(help="Preprocess and clean raw CSV data before transformation.")

# Set up logger for this module
logger = logging.getLogger(__name__)


@app.command()
def run(
    input_csv: str = Option(
        None,
        prompt="📥 Enter the path to the input CSV file",
        help="Path to the raw input CSV file",
    ),
    output_csv: str = Option(
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
        $ kopen preprocess run --input-csv raw.csv --output-csv clean.csv

    Args:
        input_csv (str): Path to the raw input CSV file.
        output_csv (str): Path where the cleaned CSV will be saved.
    """
    # 1. Load the input CSV file into a DataFrame
    logger.info("Loading CSV from: %s", input_csv)
    df: pd.DataFrame = pd.read_csv(input_csv)

    # 2. Apply preprocessing (clean column names, strip strings, convert dates)
    logger.info("Preprocessing data...")
    cleaned: pd.DataFrame = preprocess_data(df)

    # 3. Save the cleaned DataFrame to the output CSV path
    logger.info("Saving cleaned data to: %s", output_csv)
    cleaned.to_csv(output_csv, index=False)

    # 4. Provide confirmation to the user
    typer.echo(f"✅ Preprocessed data saved to: {output_csv}")
