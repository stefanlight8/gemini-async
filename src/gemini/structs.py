from collections.abc import Sequence
from typing import Literal

from msgspec import Struct

from gemini.enums import FinishReason


class Part(Struct):
    text: str


class Content(Struct):
    parts: Sequence[Part]
    role: Literal["user", "model"] | None = None


class Candidate(Struct):
    content: Content
    finish_reason: FinishReason | None = None
    token_count: int = 0
    index: int = 0


class GenerateContentResponse(Struct):
    candidates: Sequence[Candidate]
