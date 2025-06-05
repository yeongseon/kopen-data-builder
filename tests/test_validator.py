import tempfile
from pathlib import Path
from typing import Any

from kopen_data_builder.validator import load_metadata, validate_metadata


def test_validate_complete_metadata() -> None:
    """Test with a complete metadata YAML containing all required and optional fields."""
    content = """\
name: seoul-public-bike
title: Seoul Public Bicycle Rental Data
description: >
  Public rental data of Seoul’s public bike system including rental/return
  time and stations.
license: Public Domain
source_url: https://data.seoul.go.kr/dataList/OA-15242/S/1/datasetView.do
language: [ko]
category: transportation
tags: [bike, seoul, mobility]
split_type: by_year
update_frequency: monthly
copyright: Seoul Metropolitan Government
processed_note: Cleaned column names and removed missing values
columns:
  - Rental Time: Date and time when the bike was rented
  - Return Time: Date and time when the bike was returned
"""
    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".yaml") as f:
        f.write(content)
        f.flush()
        metadata: dict[str, Any] = load_metadata(Path(f.name))
        missing: list[str] = validate_metadata(metadata)
        assert missing == []


def test_validate_missing_required_fields() -> None:
    """Test with incomplete metadata missing several required fields."""
    incomplete: dict[str, Any] = {"name": "test-dataset", "description": "Missing title and others"}
    missing: list[str] = validate_metadata(incomplete)
    assert "title" in missing
    assert "license" in missing
    assert "source_url" in missing
    assert "language" in missing
