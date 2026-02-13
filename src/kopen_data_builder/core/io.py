from pathlib import Path
from typing import Optional

import pandas as pd


def read_table(path: str, encoding: Optional[str] = None, sheet_name: Optional[str] = None) -> pd.DataFrame:
    file_path = Path(path)
    suffix = file_path.suffix.lower()

    if suffix in {".xls", ".xlsx", ".xlsm"}:
        return pd.read_excel(file_path, sheet_name=sheet_name)

    if encoding is not None:
        return pd.read_csv(file_path, encoding=encoding)

    last_error = None
    for candidate in ("utf-8", "cp949"):
        try:
            return pd.read_csv(file_path, encoding=candidate)
        except Exception as exc:
            last_error = exc
            continue

    raise ValueError(f"Failed to read file with supported encodings: {last_error}")


def write_csv(df: pd.DataFrame, path: str) -> None:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
