from pathlib import Path
from typing import Generator

import polars as pl
import pytest

from kopen_data_builder.core.splitter import split_by_quarter
from kopen_data_builder.core.utils import save_csv

TEST_DIR = Path("tests/temp_split")
INPUT_FILE = TEST_DIR / "data.csv"
OUTPUT_DIR = TEST_DIR / "split"


@pytest.fixture(scope="module")  # type: ignore[misc]
def sample_quarter_data() -> pl.DataFrame:
    return pl.DataFrame({"date": ["2024-01-15", "2024-03-31", "2024-04-01", "2024-06-30"], "value": [10, 20, 30, 40]})


@pytest.fixture(autouse=True)  # type: ignore[misc]
def setup_and_teardown() -> Generator[None, None, None]:
    TEST_DIR.mkdir(parents=True, exist_ok=True)
    yield
    for file in TEST_DIR.rglob("*"):
        if file.is_file():
            file.unlink()
        elif file.is_dir():
            try:
                file.rmdir()
            except OSError:
                pass  # skip non-empty
    if TEST_DIR.exists():
        try:
            TEST_DIR.rmdir()
        except OSError:
            pass


def test_split_by_quarter(sample_quarter_data: pl.DataFrame) -> None:
    save_csv(sample_quarter_data, str(INPUT_FILE))
    split_by_quarter(str(INPUT_FILE), str(OUTPUT_DIR), date_column="date")

    assert OUTPUT_DIR.exists()
    output_files = list(OUTPUT_DIR.glob("*.csv"))
    output_file_names = {f.name for f in output_files}

    assert len(output_file_names) == 2
    assert "2024Q1.csv" in output_file_names
    assert "2024Q2.csv" in output_file_names
