# tests/test_cli_metadata.py

import os
import subprocess
import tempfile


def test_cli_init_metadata_success() -> None:
    """Test successful metadata initialization via CLI"""
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "metadata.yaml")

        result = subprocess.run(
            [
                "python",
                "-m",
                "kopen_data_builder.cli.main",
                "metadata",
                "init",
                "--output",
                path,
            ],
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0
        assert "✅ Metadata template created at" in result.stdout
        assert os.path.exists(path)


def test_cli_validate_metadata_success() -> None:
    """Test successful metadata validation via CLI using valid metadata.yaml"""
    valid_yaml = """\
pretty_name: CLI Dataset
description: Example
languages: [ko]
tags: [example]
license: cc-by-4.0
annotations_creators: [no-annotation]
language_creators: [found]
multilinguality: monolingual
task_categories: [text-classification]
task_ids: [cli-task]
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
  train: 0.8
  test: 0.2
"""

    with tempfile.NamedTemporaryFile(mode="w+", suffix=".yaml", delete=False) as f:
        f.write(valid_yaml)
        f.flush()
        path = f.name

    try:
        result = subprocess.run(
            [
                "python",
                "-m",
                "kopen_data_builder.cli.main",
                "metadata",
                "validate",
                "--path",
                path,
            ],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "✅ Metadata validation successful" in result.stdout
        assert "CLI Dataset" in result.stdout
    finally:
        os.remove(path)


def test_cli_validate_metadata_failure() -> None:
    """Test failure when metadata.yaml is invalid (missing required fields)"""
    invalid_yaml = """\
pretty_name: Invalid Dataset
languages: [ko]
tags: [example]
# license is missing!
"""

    with tempfile.NamedTemporaryFile(mode="w+", suffix=".yaml", delete=False) as f:
        f.write(invalid_yaml)
        f.flush()
        path = f.name

    try:
        result = subprocess.run(
            [
                "python",
                "-m",
                "kopen_data_builder.cli.main",
                "metadata",
                "validate",
                "--path",
                path,
            ],
            capture_output=True,
            text=True,
        )
        assert result.returncode != 0
        assert "❌ Validation error" in (result.stdout + result.stderr)
    finally:
        os.remove(path)
