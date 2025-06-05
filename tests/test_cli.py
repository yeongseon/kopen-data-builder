from typer.testing import CliRunner

from kopen_data_builder.cli import app

runner = CliRunner()


def test_hello_default() -> None:
    """Test the hello command with the default name."""
    result = runner.invoke(app, ["hello"])
    assert result.exit_code == 0
    assert "Hello, World" in result.output


def test_hello_custom() -> None:
    """Test the hello command with a custom name."""
    result = runner.invoke(app, ["hello", "--name", "Alice"])
    assert result.exit_code == 0
    assert "Hello, Alice" in result.output
