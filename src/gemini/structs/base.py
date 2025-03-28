from __future__ import annotations

from collections.abc import Sequence

from msgspec import field
from msgspec.structs import Struct

from gemini.enums import Type

__all__: Sequence[str] = ("BaseStruct", "Schema")


class BaseStruct(Struct, omit_defaults=True): ...


class Schema(BaseStruct):
    type: Type
    format: str | None = None
    title: str | None = None
    description: str | None = None
    nullable: bool | None = None
    enum: Sequence[str] | None = None
    max_items: int | None = None
    min_items: int | None = None
    properties: dict[str, Schema] | None = None
    required: Sequence[str] | None = None
    items: Schema | None = None
    min: int | None = field(default=None, name="minimum")
    max: int | None = field(default=None, name="maximum")
