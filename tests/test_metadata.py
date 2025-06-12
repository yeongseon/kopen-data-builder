# tests/test_metadata.py

import tempfile
from pathlib import Path

import pytest
import yaml  # type: ignore[import-untyped]

from kopen_data_builder.core.metadata import init_metadata


def test_init_metadata_creates_file_with_content() -> None:
    """Test that init_metadata creates a metadata.yaml file with the correct content."""
    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = Path(tmpdir) / "metadata.yaml"

        init_metadata(str(output_path))

        assert output_path.exists(), "metadata.yaml does not exist."

        with output_path.open(encoding="utf-8") as f:
            data = yaml.safe_load(f)

        assert isinstance(data, dict)
        assert "name" in data
        assert data["name"] == "your-dataset-name"


def test_init_metadata_raises_if_file_exists() -> None:
    """Test that init_metadata raises FileExistsError if the file already exists."""
    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = Path(tmpdir) / "metadata.yaml"
        output_path.write_text("Already exists", encoding="utf-8")

        with pytest.raises(FileExistsError):
            init_metadata(str(output_path))
