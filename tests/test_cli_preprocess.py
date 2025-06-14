import os
import subprocess
import tempfile

import pandas as pd


def test_cli_preprocess_csv() -> None:
    """Test the CLI preprocess command with a sample CSV file."""
    # Create a sample input CSV file
    df = pd.DataFrame(
        {
            "이름 ": ["홍길동 ", "이순신"],
            "가입날짜": ["2024-01-01", "2024-02-01"],
        }
    )

    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as infile:
        df.to_csv(infile.name, index=False)
        input_path = infile.name

    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as outfile:
        output_path = outfile.name

    try:
        # Run CLI command
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

        # Check command success and output file exists
        assert result.returncode == 0, f"STDERR: {result.stderr}"
        assert os.path.exists(output_path)

        # Confirm column was normalized
        df_out = pd.read_csv(output_path)
        assert "이름" in df_out.columns or "이름_" in df_out.columns
    finally:
        os.remove(input_path)
        os.remove(output_path)
