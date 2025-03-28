from __future__ import annotations

from collections.abc import Sequence
from typing import Literal

from gemini.structs.base import BaseStruct
from gemini.structs.functions import FunctionCall, FunctionResponse

__all__: Sequence[str] = ("Content", "Part", "Blob")


class Content(BaseStruct):
    parts: Sequence[Part]
    role: Literal["user", "model"] | None = None


class Part(BaseStruct):
    text: str | None = None
    inline_data: Blob | None = None
    function_call: FunctionCall | None = None
    function_response: FunctionResponse | None = None


class Blob(BaseStruct):
    mimetype: str
    data: str
