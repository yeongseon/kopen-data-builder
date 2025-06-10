# src/kopen_data_builder/cli/__init__.py

from .download_cmd import app as download_cmd
from .main import app as app
from .metadata_cmd import app as metadata_cmd
from .split_cmd import app as split_cmd
from .transform_cmd import app as transform_cmd
from .upload_cmd import app as upload_cmd

__all__ = [
    "app",
    "metadata_cmd",
    "split_cmd",
    "transform_cmd",
    "upload_cmd",
    "download_cmd",
]
