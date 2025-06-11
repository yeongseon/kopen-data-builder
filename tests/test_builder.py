# tests/test_builder.py

import os
import tempfile

import pandas as pd

from kopen_data_builder.core.builder import build_repository


def test_build_repository() -> None:
    df_train = pd.DataFrame({"text": ["A", "B"], "label": [0, 1]})
    df_test = pd.DataFrame({"text": ["C"], "label": [1]})

    with tempfile.TemporaryDirectory() as tmpdir:
        train_path = os.path.join(tmpdir, "train.csv")
        test_path = os.path.join(tmpdir, "test.csv")

        df_train.to_csv(train_path, index=False)
        df_test.to_csv(test_path, index=False)

        csv_paths = {"train": train_path, "test": test_path}
        out_dir = os.path.join(tmpdir, "output")

        build_repository(csv_paths, "my-dataset", out_dir)

        assert os.path.exists(os.path.join(out_dir, "train.csv"))
        assert os.path.exists(os.path.join(out_dir, "test.csv"))
        assert os.path.exists(os.path.join(out_dir, "README.md"))
        assert os.path.exists(os.path.join(out_dir, "dataset_infos.json"))
