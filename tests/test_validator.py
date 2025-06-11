import typing

import pytest

from kopen_data_builder.core.validator import validate_metadata

valid_meta = {
    "name": "my-dataset",
    "license": "CC-BY-4.0",
    "language": ["ko"],
    "tasks": ["문서분류"],
    "splits": {"train": 0.8, "test": 0.2},
}


def test_valid_metadata() -> None:
    meta = validate_metadata(valid_meta)
    assert meta.name == "my-dataset"


@pytest.mark.parametrize("license", ["INVALID", "", None])  # type: ignore
def test_invalid_license(license: typing.Any) -> None:
    bad = valid_meta.copy()
    bad["license"] = license
    with pytest.raises(ValueError):
        validate_metadata(bad)


@pytest.mark.parametrize("language", [["xx"], ["en", "fr"]])  # type: ignore
def test_invalid_language(language: typing.List[str]) -> None:
    bad = valid_meta.copy()
    bad["language"] = language
    with pytest.raises(ValueError):
        validate_metadata(bad)


@pytest.mark.parametrize("tasks", [["image-classification"], ["잘못된태스크"]])  # type: ignore
def test_invalid_tasks(tasks: typing.List[str]) -> None:
    bad = valid_meta.copy()
    bad["tasks"] = tasks
    with pytest.raises(ValueError):
        validate_metadata(bad)
