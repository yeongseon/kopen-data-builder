# tests/test_preprocessing.py

import pandas as pd

from kopen_data_builder.core.preprocessing import preprocess_data


def test_preprocess_data_basic() -> None:
    """Test basic preprocessing functionality."""
    raw = pd.DataFrame(
        {
            "Name ": [" Alice ", "Bob", "Charlie", "Dana", "Eve"],
            "가입일": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "not a date"],
            "나이": [25, 30, 35, 40, 45],
        }
    )

    processed = preprocess_data(raw)

    assert list(processed.columns) == ["name", "가입일", "나이"]
    assert processed["name"].iloc[0] == "Alice"
    assert pd.isna(processed["가입일"].iloc[4])
