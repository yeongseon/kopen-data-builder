# src/kopen_data_builder/cli/main.py

import typer

from kopen_data_builder.cli import (
    download_cmd,
    metadata_cmd,
    preprocess_cmd,
    split_cmd,
    upload_cmd,
)

app = typer.Typer(help="Korean Public Data Builder CLI")

app.add_typer(metadata_cmd.app, name="metadata")
app.add_typer(preprocess_cmd.app, name="preprocess")
app.add_typer(split_cmd.app, name="split")
app.add_typer(upload_cmd.app, name="upload")
app.add_typer(download_cmd.app, name="download")

if __name__ == "__main__":
    app()
