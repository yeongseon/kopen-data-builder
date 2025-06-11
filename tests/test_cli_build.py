import json
import os
import subprocess
import tempfile

import pandas as pd


def test_cli_build_repository() -> None:
    """Test building a Hugging Face-compatible dataset repository via CLI."""
    df_train = pd.DataFrame({"text": ["a", "b"], "label": [0, 1]})
    df_test = pd.DataFrame({"text": ["c"], "label": [1]})

    with tempfile.TemporaryDirectory() as tmpdir:
        train_path = os.path.join(tmpdir, "train.csv")
        test_path = os.path.join(tmpdir, "test.csv")
        json_path = os.path.join(tmpdir, "splits.json")
        out_path = os.path.join(tmpdir, "out_repo")

        df_train.to_csv(train_path, index=False)
        df_test.to_csv(test_path, index=False)

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump({"train": train_path, "test": test_path}, f)

        result = subprocess.run(
            [
                "python",
                "-m",
                "kopen_data_builder.cli.main",
                "build",
                "run",
                "--dataset-name",
                "cli-test",
                "--csv-json-path",
                json_path,
                "--output-dir",
                out_path,
            ],
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            print("STDOUT:", result.stdout)
            print("STDERR:", result.stderr)

        assert result.returncode == 0
        assert os.path.exists(os.path.join(out_path, "train.csv"))
        assert os.path.exists(os.path.join(out_path, "test.csv"))
        assert os.path.exists(os.path.join(out_path, "README.md"))
        assert os.path.exists(os.path.join(out_path, "dataset_infos.json"))
