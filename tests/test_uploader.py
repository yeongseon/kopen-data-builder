# tests/test_uploader.py

from kopen_data_builder.core.uploader import verify_upload


def test_verify_upload_public_dataset() -> None:
    """This test checks a known public dataset."""
    verify_upload("glue/sst2")  # Assumes public dataset is always accessible
