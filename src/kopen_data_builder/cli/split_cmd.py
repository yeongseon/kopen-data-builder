# src/kopen_data_builder/cli/split_cmd.py
from pathlib import Path

import typer

from kopen_data_builder.core.splitter import split_by_quarter

app = typer.Typer(help="Split dataset by quarter using a date column.")


@app.command()
def split(
    input: str = typer.Option(..., "--input", "-i", help="Path to input CSV file"),
    output: str = typer.Option(..., "--output", "-o", help="Directory to save split files"),
    date_column: str = typer.Option("date", "--date-column", "-d", help="Date column name"),
    strategy: str = typer.Option("quarter", "--strategy", "-s", help="Split strategy (e.g. 'quarter')"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Verbose output"),
) -> None:
    """
    Split dataset using a given strategy (default: by quarter).
    """
    input_path = Path(input)
    output_dir = Path(output)

    try:
        if strategy == "quarter":
            split_by_quarter(input_path, output_dir, date_column)
        else:
            typer.echo(f"❌ Unsupported strategy: {strategy}", err=True)
            raise typer.Exit(code=2)

        if verbose:
            typer.echo("✅ Split completed.")
    except FileNotFoundError as e:
        typer.echo(f"❌ File not found: {e}", err=True)
        raise typer.Exit(code=1) from e
    except Exception as e:
        typer.echo(f"❌ Error: {e}", err=True)
        raise typer.Exit(code=2) from e
