import tempfile
from pathlib import Path
from typing import Any

from kopen_data_builder.validator import load_metadata, validate_metadata


def test_validate_complete_metadata() -> None:
    content = """\
name: seoul-public-bike
title: Seoul Public Bicycle Rental Data
description: |-
  Public rental data of Seoul’s public bike system including rental/return
  time and stations.
license: Public Domain
source_url: https://data.seoul.go.kr/dataList/OA-15242/S/1/datasetView.do
language: [ko]
split_type: by_column_year
split_column: rental_start_time
split_column_format: "%Y-%m-%d %H:%M:%S"
columns:
  rental_start_time:
    type: datetime
    description: Date and time when the rental started
  distance_km:
    type: float
    description: Distance traveled in kilometers
"""
    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".yaml") as f:
        f.write(content)
        f.flush()
        metadata: dict[str, Any] = load_metadata(Path(f.name))
        errors = validate_metadata(metadata)
        assert errors == []


def test_validate_missing_required_fields() -> None:
    metadata: dict[str, Any] = {"name": "incomplete-dataset", "description": "Missing fields"}
    errors = validate_metadata(metadata)
    assert "Missing required field: 'title'" in errors
    assert "Missing required field: 'license'" in errors
    assert "Missing required field: 'source_url'" in errors
    assert "Missing required field: 'language'" in errors


def test_validate_invalid_column_type() -> None:
    content = """\
name: invalid-columns
title: Bad Column Types
description: Test invalid column types
license: CC-BY-4.0
source_url: https://example.com
language: [en]
columns:
  start_time:
    type: timestamp
    description: Invalid type
"""
    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".yaml") as f:
        f.write(content)
        f.flush()
        metadata = load_metadata(Path(f.name))
        errors = validate_metadata(metadata)
        assert any("Column 'start_time' has invalid type 'timestamp'" in e for e in errors)
