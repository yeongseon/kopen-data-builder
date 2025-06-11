import os
import subprocess
import tempfile

import pandas as pd


def test_cli_split_merge() -> None:
    """Test merging two CSV files using the CLI."""
    df1 = pd.DataFrame({"val": [1, 2]})
    df2 = pd.DataFrame({"val": [3, 4]})

    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f1:
        df1.to_csv(f1.name, index=False)
        path1 = f1.name

    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f2:
        df2.to_csv(f2.name, index=False)
        path2 = f2.name

    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as fout:
        output_path = fout.name

    try:
        result = subprocess.run(
            [
                "python",
                "-m",
                "kopen_data_builder.cli.main",
                "split",
                "merge",
                "--input-csvs",
                f"{path1},{path2}",
                "--output-csv",
                output_path,
            ],
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0, f"STDERR: {result.stderr}"
        assert os.path.exists(output_path)

        df_out = pd.read_csv(output_path)
        assert len(df_out) == 4
        assert set(df_out["val"]) == {1, 2, 3, 4}

    finally:
        os.remove(path1)
        os.remove(path2)
        os.remove(output_path)
