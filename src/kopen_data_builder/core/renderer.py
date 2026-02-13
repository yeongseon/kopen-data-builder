from __future__ import annotations

from typing import Iterable

from kopen_data_builder.core.models import DatasetMeta, LocalizedText


def render_dataset_card(metadata: DatasetMeta, dataset_name: str) -> str:
    title = _select_localized(metadata.pretty_name) or dataset_name
    description = _select_localized(metadata.description) or ""

    front_matter = [
        "---",
        "language:",
        *_format_list(metadata.languages),
        "license:",
        f"- {metadata.license}",
        "task_categories:",
        *_format_list(metadata.task_categories),
        "tags:",
        *_format_list(metadata.tags),
        "size_categories:",
        *_format_list(metadata.size_categories),
        "---",
        "",
    ]

    body = [
        f"# {title}",
        "",
        description,
        "",
        "## Source",
        f"- Agency (EN): {metadata.source_agency.en}",
        f"- Agency (KO): {metadata.source_agency.ko}",
        f"- URL: {metadata.original_url}",
        "",
        "## Update Frequency",
        f"{metadata.update_frequency}",
        "",
        "## Reference Date",
        f"{metadata.reference_date}",
    ]

    if metadata.splits:
        body.extend(["", "## Splits"])
        for split_name, ratio in metadata.splits.items():
            body.append(f"- {split_name}: {ratio}")

    return "\n".join(front_matter + body).strip() + "\n"


def _select_localized(value: str | LocalizedText) -> str:
    if isinstance(value, LocalizedText):
        return value.ko or value.en or ""
    return value


def _format_list(values: Iterable[object]) -> list[str]:
    return [f"- {value}" for value in values]
