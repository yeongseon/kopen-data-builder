# tests/test_cli_preprocess.py

import os
import subprocess
import tempfile

import pandas as pd


def test_cli_preprocess_csv() -> None:
    """Test CLI preprocessing command with valid input and output CSV files."""
    df = pd.DataFrame({"이름 ": ["홍길동 ", "이순신"], "가입날짜": ["2024-01-01", "2024-02-01"]})

    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as infile:
        df.to_csv(infile.name, index=False)
        input_path = infile.name

    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as outfile:
        output_path = outfile.name

    try:
        result = subprocess.run(
            [
                "python",
                "-m",
                "kopen_data_builder.cli.main",
                "preprocess",
                "run",
                "--input-csv",
                input_path,
                "--output-csv",
                output_path,
            ],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, f"STDERR: {result.stderr}"
        assert os.path.exists(output_path)

        df_out = pd.read_csv(output_path)
        assert any("이름" in col or "이름_" in col for col in df_out.columns)
    finally:
        os.remove(input_path)
        os.remove(output_path)
