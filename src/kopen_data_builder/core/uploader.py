# kopen_data_builder/core/uploader.py

"""
Uploader module: Uploads prepared dataset repositories to Hugging Face Hub.
This module provides functionality to upload a prepared dataset repository
to the Hugging Face Hub using the CLI.
"""

from pathlib import Path
from typing import Optional

from huggingface_hub import HfApi
from huggingface_hub.utils import HfHubHTTPError


def upload_to_hf(repo_dir: str, repo_id: str, token: Optional[str] = None, private: Optional[bool] = None) -> str:
    """
    Upload prepared dataset repository to Hugging Face using CLI.

    Args:
        repo_dir (str): Path to the local HF dataset repository directory.
        repo_id (str): Target Hugging Face repo ID (e.g., username/dataset-name).
    """
    repo_path = Path(repo_dir).resolve()
    if not repo_path.exists():
        raise FileNotFoundError(f"Repository directory does not exist: {repo_dir}")

    api = HfApi()
    try:
        api.create_repo(repo_id, repo_type="dataset", token=token, exist_ok=True, private=private)
    except HfHubHTTPError:
        api.create_repo(repo_id, repo_type="dataset", token=token, exist_ok=True)

    api.upload_folder(repo_id=repo_id, repo_type="dataset", folder_path=str(repo_path), token=token)

    return f"https://huggingface.co/datasets/{repo_id}"


def verify_upload(repo_id: str, token: Optional[str] = None) -> bool:
    """
    Check if the dataset repository exists on Hugging Face.

    Args:
        repo_id (str): Target Hugging Face repo ID.

    Returns:
        bool: True if repo exists, False otherwise.
    """
    api = HfApi()
    try:
        api.repo_info(repo_id, repo_type="dataset", token=token)
        return True
    except HfHubHTTPError:
        return False
