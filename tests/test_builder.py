import tempfile
from pathlib import Path

from kopen_data_builder.builder import build_dataset, load_data


def test_load_data_csv() -> None:
    """Test loading a CSV file using polars."""
    content = "year,value\n2022,100\n2023,200"
    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".csv") as f:
        f.write(content)
        f.flush()
        df = load_data(Path(f.name))
        assert df.shape == (2, 2)
        assert "year" in df.columns
        assert "value" in df.columns


def test_build_dataset_by_column_year() -> None:
    """Test building a DatasetDict split by year based on a datetime column."""
    csv_content = "rental_start_time,value\n2022-01-01 09:00:00,100\n2023-01-01 10:00:00,200"
    metadata = {
        "split_type": "by_column_year",
        "split_column": "rental_start_time",
        "split_column_format": "%Y-%m-%d %H:%M:%S",
    }
    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".csv") as f:
        f.write(csv_content)
        f.flush()
        df = load_data(Path(f.name))
        dataset_dict = build_dataset(metadata, df)
        assert "2022" in dataset_dict
        assert "2023" in dataset_dict
        assert len(dataset_dict["2022"]) == 1
        assert len(dataset_dict["2023"]) == 1


def test_build_dataset_full_split() -> None:
    """Test building a full dataset with a single 'train' split."""
    csv_content = "x,y\n1,2\n3,4\n5,6"
    metadata = {"split_type": "full"}
    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".csv") as f:
        f.write(csv_content)
        f.flush()
        df = load_data(Path(f.name))
        dataset_dict = build_dataset(metadata, df)
        assert "train" in dataset_dict
        assert len(dataset_dict["train"]) == 3
