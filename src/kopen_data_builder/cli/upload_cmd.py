# src/kopen_data_builder/cli/upload_cmd.py

"""
Upload CLI: Upload prepared dataset to Hugging Face and verify upload.
This command uploads a dataset directory to the Hugging Face Hub and verifies the upload.
It requires the dataset to be in a Hugging Face-compatible format.
"""

import logging

import typer

from kopen_data_builder.core.uploader import upload_to_hf, verify_upload

app = typer.Typer(help="Upload prepared dataset to Hugging Face and verify upload.")
logger = logging.getLogger(__name__)


@app.command("run")
def run(
    repo_dir: str = typer.Option(
        None,
        prompt="📁 Enter the path to the Hugging Face dataset directory",
        help="Path to the prepared Hugging Face dataset directory.",
    ),
    repo_id: str = typer.Option(
        None,
        prompt="📦 Enter the Hugging Face repository ID (e.g., username/dataset-name)",
        help="Target repository ID on Hugging Face (e.g., username/dataset-name).",
    ),
) -> None:
    """
    Upload the dataset directory to Hugging Face Hub and verify the result.

    Example:
    $ kopen upload run --repo-dir ./my_dataset_repo --repo-id username/dataset-name

    Args:
        repo_dir (str): Path to the Hugging Face dataset directory to upload.
        repo_id (str): The repository ID on Hugging Face where the dataset will be uploaded.
    """
    logger.info(f"Uploading dataset from: {repo_dir} to repo: {repo_id}")
    upload_to_hf(repo_dir, repo_id)
    verify_upload(repo_id)
    typer.echo("✅ Dataset successfully uploaded and verified.")
