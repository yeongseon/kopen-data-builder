# src/kopen_data_builder/cli/upload_cmd.py

from pathlib import Path
from typing import Optional

import typer

from kopen_data_builder.core.uploader import upload_to_huggingface

app = typer.Typer(help="Upload a dataset folder to the Hugging Face Hub.")


@app.command("run")
def run(
    dataset_dir: str = typer.Argument(..., help="Local path to the dataset folder"),
    repo_id: str = typer.Argument(..., help='Target Hugging Face repo ID (e.g., "username/my_dataset")'),
    token: Optional[str] = typer.Option(None, "--token", "-t", help="Hugging Face access token"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose output"),
) -> None:
    """
    Upload the dataset folder to Hugging Face Hub under the specified repo ID.
    """
    dataset_path = Path(dataset_dir)

    try:
        if verbose:
            typer.echo(f"📁 Dataset directory: {dataset_path}")
            typer.echo(f"🚀 Target repo: {repo_id}")
            if token:
                typer.echo("🔐 Token: [provided]")

        upload_to_huggingface(dataset_path, repo_id, token)

        typer.echo(f"✅ Successfully uploaded to https://huggingface.co/datasets/{repo_id}")
    except FileNotFoundError as e:
        typer.echo(f"❌ Directory not found: {e}", err=True)
        raise typer.Exit(code=1) from e
    except Exception as e:
        typer.echo(f"❌ Upload failed: {e}", err=True)
        raise typer.Exit(code=2) from e
