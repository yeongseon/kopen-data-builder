# kopen_data_builder/core/uploader.py

"""
Uploader module: Uploads prepared dataset repositories to Hugging Face Hub.
This module provides functionality to upload a prepared dataset repository
to the Hugging Face Hub using the CLI.
"""

import subprocess
from pathlib import Path

import typer


def upload_to_hf(repo_dir: str, repo_id: str) -> None:
    """
    Upload prepared dataset repository to Hugging Face using CLI.

    Args:
        repo_dir (str): Path to the local HF dataset repository directory.
        repo_id (str): Target Hugging Face repo ID (e.g., username/dataset-name).
    """
    repo_path = Path(repo_dir).resolve()
    if not repo_path.exists():
        raise FileNotFoundError(f"Repository directory does not exist: {repo_dir}")

    typer.echo(f"🚀 Uploading to Hugging Face Hub: {repo_id}")
    try:
        subprocess.run(["huggingface-cli", "repo", "create", repo_id, "--type", "dataset", "--yes"], check=True)
    except subprocess.CalledProcessError:
        typer.echo(f"⚠️  Repository {repo_id} may already exist. Continuing...")

    subprocess.run(["git", "init"], cwd=repo_dir, check=True)
    subprocess.run(
        ["git", "remote", "add", "origin", f"https://huggingface.co/datasets/{repo_id}"], cwd=repo_dir, check=True
    )
    subprocess.run(["git", "add", "."], cwd=repo_dir, check=True)
    subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=repo_dir, check=True)
    subprocess.run(["git", "branch", "-M", "main"], cwd=repo_dir, check=True)
    subprocess.run(["git", "push", "-u", "origin", "main", "--force"], cwd=repo_dir, check=True)

    typer.echo("✅ Upload complete.")


def verify_upload(repo_id: str) -> bool:
    """
    Check if the dataset repository exists on Hugging Face.

    Args:
        repo_id (str): Target Hugging Face repo ID.

    Returns:
        bool: True if repo exists, False otherwise.
    """
    import requests

    url = f"https://huggingface.co/datasets/{repo_id}"
    response = requests.get(url)
    if response.status_code == 200:
        typer.echo(f"✅ Verified: {repo_id} exists on the Hub.")
        return True
    else:
        typer.echo(f"❌ Not found: {repo_id}")
        return False
