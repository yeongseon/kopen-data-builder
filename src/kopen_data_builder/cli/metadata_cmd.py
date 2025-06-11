# src/kopen_data_builder/cli/metadata_cmd.py

"""
Metadata CLI: Validate dataset metadata JSON files.
This module provides a command-line interface to validate metadata files
against predefined standards using the `kopen_data_builder` library.
"""

import json

import typer

from kopen_data_builder.core.validator import validate_metadata

app = typer.Typer()


@app.command()
def validate(path: str) -> None:
    """Validate a metadata JSON file.
    Args:
        path (str): Path to the metadata JSON file to validate.
    Raises:
        typer.Exit: If validation fails, exits with code 1.
    """
    with open(path, encoding="utf-8") as f:
        meta = json.load(f)
    try:
        validated = validate_metadata(meta)
        typer.echo("✅ Metadata validation successful:")
        typer.echo(json.dumps(validated.model_dump(), indent=2, ensure_ascii=False))  # 수정된 부분
    except Exception as e:
        typer.echo(f"❌ Validation error: {e}", err=True)
        raise typer.Exit(code=1) from e
