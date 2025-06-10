# src/kopen_data_builder/core/uploader.py

"""
Uploader module: Uploads the dataset directory to the Hugging Face Hub
using the huggingface_hub Python client.
"""

import logging
from pathlib import Path
from typing import Optional, Union

from huggingface_hub import create_repo, upload_folder

logger = logging.getLogger(__name__)


def upload_to_huggingface(dataset_dir: Union[str, Path], repo_id: str, token: Optional[str] = None) -> None:
    """
    Uploads the dataset directory to the Hugging Face Hub under the specified repository ID.

    Args:
        dataset_dir (str | Path): Local path to the dataset folder (must include metadata and CSV splits).
        repo_id (str): Hugging Face repo ID in the form "username/repo_name".
        token (Optional[str]): Optional Hugging Face access token.

    Raises:
        FileNotFoundError: If the dataset directory does not exist.
        Exception: On any upload failure.
    """
    path = Path(dataset_dir)
    if not path.exists():
        raise FileNotFoundError(f"Dataset directory not found: {path}")

    logger.info("Preparing to upload to Hugging Face Hub: %s", repo_id)

    try:
        create_repo(repo_id=repo_id, token=token, repo_type="dataset", exist_ok=True)

        upload_folder(
            folder_path=str(path),
            repo_id=repo_id,
            repo_type="dataset",
            token=token,
            path_in_repo=".",
        )

        logger.info(
            "Dataset successfully uploaded to Hugging Face: https://huggingface.co/datasets/%s",
            repo_id,
        )

    except Exception as e:
        logger.error("Failed to upload dataset: %s", str(e))
        raise
