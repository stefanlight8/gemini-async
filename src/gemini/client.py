from __future__ import annotations

import sys
import warnings
from collections.abc import Sequence
from logging import Logger, getLogger
from typing import Any, Literal, TypeVar, overload

import httpx
import msgspec
from msgspec.json import decode, encode

from gemini.consts import HEADERS, MODEL_METHOD_URL, ApiVersion, Model
from gemini.enums import ModelMethod
from gemini.structs import Content, GenerateContentResponse, GenerationConfig, Part

__all__: Sequence[str] = ("Client",)

_LOGGER: Logger = getLogger("gemini.http")
HTTPMethod = Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "TRACE"]

T = TypeVar("T", bound=msgspec.Struct)


def _check_h2() -> None:
    try:
        __import__("h2")
    except (ImportError, ModuleNotFoundError):
        warnings.warn(
            "For using http/2 you need 'h2' package, but it's not installed.\n"
            "Consider to install 'gemini-async' with 'http2' optional. Or 'pip install gemini-async[http2]'",
            stacklevel=2
        )
        sys.exit(1)


class BaseClient:
    def __init__(self, key: str, *, http1: bool, http2: bool) -> None:
        _check_h2()

        self._key: str = key
        self.http: httpx.AsyncClient = httpx.AsyncClient(headers=HEADERS, http1=http1, http2=http2)

    async def request(self, method: HTTPMethod, url: str, *, data: bytes, type: type[T] | None = None) -> T | None:
        response: httpx.Response = await self.http.request(method, url, content=data)
        return decode(response.read(), type=type)


class Client(BaseClient):
    __slots__: Sequence[str] = ("_key", "version", "model", "generation_config")

    def __init__(
        self,
        key: str,
        *,
        version: ApiVersion = "v1",
        model: Model = "gemini-1.5-pro",
        generation_config: GenerationConfig | None = None,
        http1: bool = True,
        http2: bool = False
    ) -> None:
        super().__init__(key, http1=http1, http2=http2)
        self._key: str = key
        self.version: ApiVersion = version
        self.model: Model = model
        self.generation_config: GenerationConfig | None = generation_config

    def get_url(self, url: str, version: ApiVersion | None = None, **kwargs: str) -> str:
        return url.format(key=self._key, version=version or self.version, **kwargs)

    @overload
    async def generate_content(
        self,
        *contents: Content,
        version: ApiVersion | None = None,
        model: Model | None = None,
        system_instruction: str | None = None,
    ) -> GenerateContentResponse | None: ...

    @overload
    async def generate_content(
        self,
        *,
        text: str | None = None,
        version: ApiVersion | None = None,
        model: Model | None = None,
        system_instruction: str | None = None,
    ) -> GenerateContentResponse | None: ...

    async def generate_content(
        self,
        *contents: Content,
        text: str | None = None,
        version: ApiVersion | None = None,
        model: Model | None = None,
        system_instruction: str | None = None,
    ) -> GenerateContentResponse | None:
        body: dict[str, Any] = {"contents": list(contents)}
        if text:
            body["contents"].append(Content(parts=[Part(text=text)]))
        if system_instruction:
            body["system_instruction"] = Content(parts=[Part(text=system_instruction)])
        return await self.request(
            "POST",
            self.get_url(
                MODEL_METHOD_URL, version=version, model=model or self.model, method=ModelMethod.GENERATE_CONTENT.value
            ),
            data=encode(body),
            type=GenerateContentResponse,
        )
