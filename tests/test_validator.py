import json
from pathlib import Path
from typing import Generator

import pytest

from kopen_data_builder.core.validator import validate_dataset

TEST_DIR = Path("tests/temp_validator")
VALID_DIR = TEST_DIR / "valid"
INVALID_DIR = TEST_DIR / "invalid"


@pytest.fixture(autouse=True)  # type: ignore[misc]
def setup_and_teardown() -> Generator[None, None, None]:
    VALID_DIR.mkdir(parents=True, exist_ok=True)
    INVALID_DIR.mkdir(parents=True, exist_ok=True)

    # valid setup
    (VALID_DIR / "2024q1.csv").write_text("dummy")
    with open(VALID_DIR / "dataset_infos.json", "w") as f:
        json.dump({"splits": {"2024q1": {"path": "2024q1.csv"}}}, f)

    # invalid setup (metadata present, file missing)
    with open(INVALID_DIR / "dataset_infos.json", "w") as f:
        json.dump({"splits": {"2024q2": {"path": "missing.csv"}}}, f)

    yield

    for path in [VALID_DIR, INVALID_DIR]:
        for file in path.glob("*"):
            file.unlink()
        path.rmdir()
    TEST_DIR.rmdir()


def test_validate_valid_dataset() -> None:
    assert validate_dataset(str(VALID_DIR)) is True


def test_validate_invalid_dataset() -> None:
    assert validate_dataset(str(INVALID_DIR)) is False
