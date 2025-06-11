# tests/test_cli_metadata.py

import json
import os
import subprocess
import tempfile


def test_cli_validate_metadata_success() -> None:
    meta = {
        "name": "cli-dataset",
        "license": "CC-BY-4.0",
        "language": ["ko"],
        "tasks": ["문서분류"],
        "splits": {"train": 0.8, "test": 0.2},
    }
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".json", delete=False) as f:
        json.dump(meta, f)
        f.flush()
        path = f.name

    try:
        result = subprocess.run(
            ["python", "-m", "kopen_data_builder.cli.main", "metadata", "validate", path],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "✅ Metadata validation successful" in result.stdout
    finally:
        os.remove(path)


def test_cli_validate_metadata_failure() -> None:
    meta = {
        "name": "cli-dataset",
        "language": ["ko"],
        "tasks": ["문서분류"],
        "splits": {"train": 0.8, "test": 0.2},
    }
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".json", delete=False) as f:
        json.dump(meta, f)
        f.flush()
        path = f.name

    try:
        result = subprocess.run(
            ["python", "-m", "kopen_data_builder.cli.main", "metadata", "validate", path],
            capture_output=True,
            text=True,
        )
        assert result.returncode != 0
        assert "❌ Validation error" in result.stdout or result.stderr
    finally:
        os.remove(path)
