# src/kopen_data_builder/cli/transform_cmd.py

from pathlib import Path

import typer

from kopen_data_builder.core.transformer import transform_data

app = typer.Typer(help="Transform raw data into a clean standardized format.")


@app.command("run")
def run(
    input: str = typer.Argument(..., help="Path to input CSV file"),
    output: str = typer.Argument(..., help="Path to save cleaned output"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose output"),
) -> None:
    """
    Run the data transformation pipeline.
    """
    input_path = Path(input)
    output_path = Path(output)

    try:
        if verbose:
            typer.echo(f"📥 Input: {input_path}")
            typer.echo(f"📤 Output: {output_path}")

        transform_data(input_path=input_path, output_path=output_path)

        typer.echo("✅ Data transformation completed successfully.")
    except FileNotFoundError as e:
        typer.echo(f"❌ File not found: {e}", err=True)
        raise typer.Exit(code=1) from e
    except Exception as e:
        typer.echo(f"❌ Transformation failed: {e}", err=True)
        raise typer.Exit(code=2) from e
