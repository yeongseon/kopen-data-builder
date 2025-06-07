# src/kopen_data_builder/core/downloader.py

"""
Downloader module: Handles downloading files from a given URL to a local file path.
This module ensures directory creation, proper error handling, and logging.
"""

import logging
from pathlib import Path
from typing import Union

import requests

logger = logging.getLogger(__name__)


def download_data(url: str, output_path: Union[str, Path]) -> None:
    """
    Download data from a URL and save it to the specified output path.

    Args:
        url (str): The URL of the file to download.
        output_path (str | Path): The local file path to save the downloaded file.

    Raises:
        HTTPError: If the HTTP request returns an unsuccessful status code.
        RequestException: For general network-related errors during the download.
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    logger.info("Starting download: %s", url)

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        with open(path, "wb") as f:
            f.write(response.content)
        logger.info("Download complete: %s → %s", url, path)
    except requests.RequestException as e:
        logger.error("Download failed: %s (%s)", url, str(e))
        raise
