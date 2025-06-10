# src/kopen_data_builder/cli/download_cmd.py

from pathlib import Path

import typer

from kopen_data_builder.core.downloader import download_data

app = typer.Typer(help="Download data from a given URL to a local file path.")


@app.command("run")
def run(
    url: str = typer.Argument(..., help="The URL to download from"),
    output: str = typer.Argument(..., help="Where to save the downloaded file"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose logging"),
) -> None:
    """
    Download data from the given URL and save it to the specified local path.
    """
    try:
        output_path = Path(output)

        if verbose:
            typer.echo(f"🌐 Downloading from: {url}")
            typer.echo(f"💾 Saving to: {output_path}")

        download_data(url, output_path)

        typer.echo("✅ Download completed successfully.")
    except Exception as e:
        typer.echo(f"❌ Error: {e}", err=True)
        raise typer.Exit(code=1) from e
