# src/kopen_data_builder/cli/metadata_cmd.py

"""
Metadata CLI: Validate dataset metadata JSON files.

This module provides a CLI command to validate metadata files against
predefined Pydantic schemas using the kopen_data_builder library.
"""

import json
import logging
from typing import Optional

import typer

from kopen_data_builder.core.metadata import init_metadata
from kopen_data_builder.core.validator import validate_metadata

logger = logging.getLogger(__name__)
app = typer.Typer(help="Manage dataset metadata files.")


@app.command("init", help="Generate a metadata.yaml template.")
def init(
    output_path: str = typer.Option(
        ..., "--output", "-o", prompt="Enter output path for metadata.yaml", help="Path to save metadata.yaml"
    )
) -> None:
    """
    Initialize a metadata.yaml file at the specified path.
    This command creates a metadata.yaml file with a predefined template
    that can be used for Hugging Face datasets.

    Example:
    $ kopen metadata init --output metadata.yaml

    Args:
        output_path (str): Path to save the metadata.yaml file.

    Raises:
        typer.Exit: Exits with code 1 if the file already exists or an error occurs.
    """
    try:
        init_metadata(output_path)
        typer.secho(f"✅ Metadata template created at: {output_path}", fg=typer.colors.GREEN)
    except FileExistsError as e:
        typer.secho(f"❌ {e}", fg=typer.colors.RED)
        raise typer.Exit(code=1) from e
    except Exception as e:
        logger.exception("Unexpected error during metadata init.")
        typer.secho(f"❌ Unexpected error: {e}", fg=typer.colors.RED)
        raise typer.Exit(code=1) from e


@app.command("validate", help="Validate a metadata JSON file.")
def validate(
    path: Optional[str] = typer.Option(
        None,
        prompt="Enter the path to the metadata JSON file",
        help="Path to the metadata JSON file",
    )
) -> None:
    """
    Validate a metadata JSON file via interactive prompt.

    Loads the file, validates it using internal schema rules,
    and prints the parsed and validated result to the terminal.

    Example:
    $ kopen metadata validate --path metadata.json

    Args:
        path (str): Path to the metadata JSON file to validate.

    Raises:
        typer.Exit: Exits with code 1 if validation fails.
    """
    logger.info(f"📂 Loading metadata file from: {path}")
    try:
        if path is None:
            raise typer.BadParameter("path is required")
        with open(path, encoding="utf-8") as f:
            meta = json.load(f)
        validated = validate_metadata(meta)
        logger.info("✅ Metadata validation succeeded.")
        typer.echo("✅ Metadata validation successful:")
        typer.echo(json.dumps(validated.model_dump(), indent=2, ensure_ascii=False))
    except Exception as e:
        logger.exception("❌ Metadata validation failed.")
        typer.echo(f"❌ Validation error: {e}", err=True)
        raise typer.Exit(code=1) from e
