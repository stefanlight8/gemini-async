from __future__ import annotations

from collections.abc import Sequence

from msgspec import field

from gemini.structs.base import BaseStruct
from gemini.structs.functions import FunctionDeclaration

__all__: Sequence[str] = ("Tool",)


class Tool(BaseStruct):
    functions: Sequence[FunctionDeclaration] | None = field(default=None, name="function_declarations")
    # google_search_retrieval: GoogleSearchRetrieval | None = None
    # code_execution: CodeExecution | None = None
    # google_search: GoogleSearch | None = None
