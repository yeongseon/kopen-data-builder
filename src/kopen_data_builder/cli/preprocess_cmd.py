# src/kopen_data_builder/core/preprocessing.py

"""
Preprocessing module: Contains functions for preprocessing dataset metadata.
This module provides utilities to validate and preprocess dataset metadata
before further processing or uploading.
"""

import pandas as pd
import typer

from kopen_data_builder.core.preprocessing import preprocess_data

app = typer.Typer()


@app.command()
def run(input_csv: str, output_csv: str) -> None:
    """Preprocess a CSV file and save the cleaned version."""
    df = pd.read_csv(input_csv)
    cleaned = preprocess_data(df)
    cleaned.to_csv(output_csv, index=False)
    typer.echo(f"✅ Preprocessed data saved to: {output_csv}")
