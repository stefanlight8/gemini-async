from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from gemini.enums import FinishReason
from gemini.structs.base import BaseStruct
from gemini.structs.content import Content
from gemini.structs.tools import Tool

__all__: Sequence[str] = ("GenerationConfig", "GenerateContentRequest", "GenerateContentResponse", "Candidate")


class GenerationConfig(BaseStruct):
    candidate_count: int | None = None
    max_output_tokens: int | None = None
    temperature: float | None = None
    top_p: float | None = None
    top_k: int | None = None
    seed: int | None = None
    frequency_penalty: float | None = None


class GenerateContentRequest(BaseStruct):
    contents: Sequence[Content] | None = None
    tools: Sequence[Tool] | None = None


class GenerateContentResponse(BaseStruct):
    candidates: Sequence[Candidate] | None = None
    error: Error | None = None


class Candidate(BaseStruct):
    content: Content
    finish_reason: FinishReason | None = None
    token_count: int = 0
    index: int = 0


class Error(BaseStruct):
    code: int | None = None
    message: str | None = None
    status: str | None = None
    details: Sequence[dict[str, Any]] | None = None
