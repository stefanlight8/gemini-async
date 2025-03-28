from __future__ import annotations

from collections.abc import Sequence

from msgspec.structs import Struct

from gemini.structs.base import BaseStruct, Schema

__all__: Sequence[str] = ("FunctionDeclaration", "FunctionCall", "FunctionResponse")


class FunctionDeclaration(BaseStruct):
    name: str
    description: str
    parameters: Schema
    response: Schema


class FunctionCall(BaseStruct):
    id: str
    name: str
    args: Struct


class FunctionResponse(BaseStruct):
    id: str
    name: str
    args: Struct
