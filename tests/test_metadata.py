import json
from pathlib import Path
from typing import Generator

import pytest

from kopen_data_builder.core.metadata import generate_metadata

TEST_DIR = Path("tests/temp_metadata")
SPLIT_DIR = TEST_DIR / "splits"
META_FILE = TEST_DIR / "dataset_infos.json"


@pytest.fixture(autouse=True)  # type: ignore[misc]
def setup_and_teardown() -> Generator[None, None, None]:
    SPLIT_DIR.mkdir(parents=True, exist_ok=True)
    (SPLIT_DIR / "2024Q1.csv").write_text("dummy")
    (SPLIT_DIR / "2024Q2.csv").write_text("dummy")
    yield
    for file in SPLIT_DIR.glob("*.csv"):
        file.unlink()
    if META_FILE.exists():
        META_FILE.unlink()
    SPLIT_DIR.rmdir()
    TEST_DIR.rmdir()


def test_generate_metadata() -> None:
    generate_metadata(str(SPLIT_DIR), str(META_FILE))
    assert META_FILE.exists()

    with open(META_FILE, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    assert "splits" in metadata
    assert "2024q1" in metadata["splits"]
    assert metadata["splits"]["2024q1"]["path"] == "2024Q1.csv"
