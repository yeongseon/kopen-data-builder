# tests/test_preprocessing.py

import pandas as pd

from kopen_data_builder.core.preprocessing import preprocess_data


def test_preprocess_data_basic() -> None:
    raw = pd.DataFrame({"Name ": [" Alice ", "Bob"], "가입일": ["2023-01-01", "not a date"], "나이": [25, 30]})
    processed = preprocess_data(raw)
    assert list(processed.columns) == ["name", "가입일", "나이"]
    assert processed["name"].iloc[0] == "Alice"
    assert pd.to_datetime(processed["가입일"].iloc[1], errors="coerce", utc=True, dayfirst=True) is pd.NaT
