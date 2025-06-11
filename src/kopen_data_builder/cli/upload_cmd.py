# src/kopen_data_builder/cli/upload_cmd.py

"""
Upload CLI: Upload prepared dataset to Hugging Face and verify upload.
This command uploads a dataset directory to the Hugging Face Hub and verifies the upload.
It requires the dataset to be in a Hugging Face-compatible format.
"""

import typer

from kopen_data_builder.core.uploader import upload_to_hf, verify_upload

app = typer.Typer(help="Upload prepared dataset to Hugging Face and verify upload.")


@app.command("run")
def run(
    repo_dir: str = typer.Argument(..., help="Path to the prepared Hugging Face dataset directory."),
    repo_id: str = typer.Argument(..., help="Target repository ID on Hugging Face (e.g., username/dataset-name)."),
) -> None:
    upload_to_hf(repo_dir, repo_id)
    verify_upload(repo_id)
