# src/kopen_data_builder/cli/main.py

import logging

import typer

from kopen_data_builder.cli import (
    build_cmd,
    download_cmd,
    metadata_cmd,
    preprocess_cmd,
    split_cmd,
    upload_cmd,
)

app = typer.Typer(help="Korean Public Data Builder CLI")


def setup_logging(verbose: bool = False) -> None:
    """
    Configure logging for the CLI.
    Args:
        verbose (bool): If True, set logging level to DEBUG; otherwise, INFO.
    """
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        handlers=[logging.StreamHandler()],
    )
    logging.debug("🔍 Verbose logging enabled.")


@app.callback()
def main(verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose (debug) logging")) -> None:
    """
    Korean Public Data Builder CLI

    Use this CLI to validate, preprocess, split, and upload datasets to Hugging Face.
    """
    setup_logging(verbose)


# Register subcommands
app.add_typer(metadata_cmd.app, name="metadata")
app.add_typer(preprocess_cmd.app, name="preprocess")
app.add_typer(split_cmd.app, name="split")
app.add_typer(upload_cmd.app, name="upload")
app.add_typer(download_cmd.app, name="download")
app.add_typer(build_cmd.app, name="build")

if __name__ == "__main__":
    app()
