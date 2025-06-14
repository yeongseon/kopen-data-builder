# tests/test_metadata.py

import tempfile
from pathlib import Path

import pytest

from kopen_data_builder.core.metadata import init_metadata, load_metadata
from kopen_data_builder.core.models import DatasetMeta


def test_init_metadata_creates_file_with_content() -> None:
    """Test that init_metadata creates a metadata.yaml file with expected fields."""
    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = Path(tmpdir) / "metadata.yaml"

        init_metadata(str(output_path))

        assert output_path.exists(), "metadata.yaml was not created."

        with output_path.open(encoding="utf-8") as f:
            raw_text = f.read()
            assert "# kopen-data-builder: metadata.yaml template" in raw_text
            assert "pretty_name:" in raw_text
            assert "license:" in raw_text
            assert "source_agency:" in raw_text


def test_init_metadata_raises_if_file_exists() -> None:
    """Test that init_metadata raises FileExistsError if the file already exists."""
    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = Path(tmpdir) / "metadata.yaml"
        output_path.write_text("already exists", encoding="utf-8")

        with pytest.raises(FileExistsError):
            init_metadata(str(output_path))


def test_load_metadata_returns_valid_model() -> None:
    """Test that load_metadata correctly parses and validates a metadata.yaml file."""
    content = """\
pretty_name: Sample Dataset
description: A simple description
languages: [ko]
tags: [sample]
license: cc-by-4.0
annotations_creators: [no-annotation]
language_creators: [found]
multilinguality: monolingual
task_categories: [text-classification]
task_ids: [sample-task]
size_categories: 1K<n<10K
source_datasets: [original]
source_agency:
  en: Example Agency
  ko: 예시기관
original_url: https://example.com
update_frequency: Monthly
reference_date: 2024-01-01 to 2024-12-31
kogl_type: 1
splits:
  train: 0.7
  test: 0.3
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / "metadata.yaml"
        path.write_text(content, encoding="utf-8")

        meta = load_metadata(str(path))

        assert isinstance(meta, DatasetMeta)
        assert meta.pretty_name == "Sample Dataset"
        assert meta.languages == ["ko"]
        assert meta.source_agency.en == "Example Agency"


def test_load_metadata_raises_on_invalid_yaml() -> None:
    """Test that load_metadata raises ValueError if metadata is invalid."""
    invalid_content = "pretty_name: 123\nlicense:\n"

    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / "invalid.yaml"
        path.write_text(invalid_content, encoding="utf-8")

        with pytest.raises(ValueError):
            load_metadata(str(path))


def test_load_metadata_raises_file_not_found() -> None:
    """Test that load_metadata raises FileNotFoundError if file is missing."""
    with tempfile.TemporaryDirectory() as tmpdir:
        fake_path = Path(tmpdir) / "not_here.yaml"
        with pytest.raises(FileNotFoundError):
            load_metadata(str(fake_path))


def test_load_metadata_fallback_to_cp949() -> None:
    """Test that load_metadata can fall back to cp949 encoding."""
    content = """\
pretty_name: Sample Dataset
description: 설명입니다
languages: [ko]
tags: [sample]
license: cc-by-4.0
annotations_creators: [no-annotation]
language_creators: [found]
multilinguality: monolingual
task_categories: [text-classification]
task_ids: [sample-task]
size_categories: 1K<n<10K
source_datasets: [original]
source_agency:
  en: Example Agency
  ko: 예시기관
original_url: https://example.com
update_frequency: Monthly
reference_date: 2024-01-01 to 2024-12-31
kogl_type: 1
splits:
  train: 0.7
  test: 0.3
"""
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / "metadata.yaml"
        path.write_text(content, encoding="cp949")  # intentionally non-utf-8

        meta = load_metadata(str(path))

        assert meta.pretty_name == "Sample Dataset"
        assert meta.source_agency.ko == "예시기관"


def test_load_metadata_raises_on_non_dict_yaml() -> None:
    """Test that load_metadata raises ValueError if YAML root is not a dict."""
    non_dict_yaml = "- a\n- b\n- c\n"

    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / "invalid.yaml"
        path.write_text(non_dict_yaml, encoding="utf-8")

        with pytest.raises(ValueError, match="expected a dictionary"):
            load_metadata(str(path))


def test_load_metadata_raises_on_validation_error() -> None:
    """Test that load_metadata raises ValueError if schema validation fails."""
    missing_required_field = """\
description: No name provided
languages: [ko]
tags: [sample]
license: cc-by-4.0
annotations_creators: [no-annotation]
language_creators: [found]
multilinguality: monolingual
task_categories: [text-classification]
size_categories: 1K<n<10K
source_datasets: [original]
source_agency:
  en: Example
  ko: 예
original_url: https://example.com
update_frequency: Monthly
reference_date: 2024-01-01
kogl_type: 1
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / "missing.yaml"
        path.write_text(missing_required_field, encoding="utf-8")

        with pytest.raises(ValueError, match="Metadata does not conform"):
            load_metadata(str(path))
