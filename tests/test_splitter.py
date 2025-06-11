# tests/test_splitter.py

import pandas as pd

from kopen_data_builder.core.splitter import merge_datasets, split_dataset


def test_split_dataset_basic() -> None:
    df = pd.DataFrame({"value": list(range(100))})
    splits = split_dataset(df, {"train": 0.8, "test": 0.2})
    assert len(splits["train"]) > 0
    assert len(splits["test"]) > 0
    assert len(splits["train"]) + len(splits["test"]) == len(df)


def test_merge_datasets() -> None:
    df1 = pd.DataFrame({"id": [1, 2]})
    df2 = pd.DataFrame({"id": [3]})
    merged = merge_datasets([df1, df2])
    assert len(merged) == 3
