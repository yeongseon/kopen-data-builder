from pathlib import Path
from typing import Generator

import polars as pl
import pytest

from kopen_data_builder.core.transformer import transform_data
from kopen_data_builder.core.utils import load_csv, save_csv

TEST_DIR = Path("tests/temp_transform")
RAW_FILE = TEST_DIR / "raw.csv"
CLEAN_FILE = TEST_DIR / "clean.csv"


@pytest.fixture(scope="module")  # type: ignore[misc]
def sample_dataframe() -> pl.DataFrame:
    return pl.DataFrame({"ID ": [1, 2], "Value": ["a", "b"], "NullCol": [None, "x"]})


@pytest.fixture(autouse=True)  # type: ignore[misc]
def setup_and_teardown() -> Generator[None, None, None]:
    TEST_DIR.mkdir(parents=True, exist_ok=True)
    yield
    for file in TEST_DIR.glob("*"):
        file.unlink()
    TEST_DIR.rmdir()


def test_transform_data(sample_dataframe: pl.DataFrame) -> None:
    save_csv(sample_dataframe, str(RAW_FILE))  # Path -> str
    transform_data(str(RAW_FILE), str(CLEAN_FILE))  # Path -> str
    assert CLEAN_FILE.exists()

    df = load_csv(str(CLEAN_FILE))  # Path -> str
    assert "id" in df.columns
    assert "value" in df.columns
    assert "nullcol" not in df.columns  # dropped due to nulls in column
