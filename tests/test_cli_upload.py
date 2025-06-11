# tests/test_cli_upload.py

import tempfile

from pytest_mock import MockerFixture

from kopen_data_builder.cli.upload_cmd import run


def test_cli_upload_run_direct(mocker: MockerFixture) -> None:
    """Test upload command directly with patched subprocess."""

    # Patch subprocess.run to avoid actual git and huggingface CLI calls
    mocker.patch("subprocess.run")
    mocker.patch("kopen_data_builder.core.uploader.upload_to_hf")
    mocker.patch("kopen_data_builder.core.uploader.verify_upload")

    with tempfile.TemporaryDirectory() as tmpdir:
        run(repo_dir=tmpdir, repo_id="username/test-dataset")
