# tests/test_cli.py
from typer.testing import CliRunner

from kopen_data_builder.cli.main import app

runner = CliRunner()


def test_cli_root_help() -> None:
    """Test that the root CLI help command works."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Korean Public Data Builder CLI" in result.output
    assert "metadata" in result.output
    assert "split" in result.output


def test_split_help() -> None:
    """Test that the split command help works."""
    result = runner.invoke(app, ["split", "--help"])
    assert result.exit_code == 0
    # Match updated help text from split_cmd.py
    assert "Split and merge datasets" in result.output


def test_metadata_help() -> None:
    """Test that the metadata command help works."""
    result = runner.invoke(app, ["metadata", "--help"])
    assert result.exit_code == 0
