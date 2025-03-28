from __future__ import annotations

from asyncio.events import AbstractEventLoop
from collections.abc import Sequence
from typing import Any, overload

from aiohttp import ClientResponse
from aiohttp.client import ClientSession
from msgspec.json import decode, encode

from gemini.consts import MODEL_METHOD_URL, ApiVersion, Model
from gemini.enums import ModelMethod
from gemini.http.client import HTTPClient
from gemini.structs import Content, Error, GenerateContentResponse, GenerationConfig, Part

__all__: Sequence[str] = ("Client",)


class Client(HTTPClient):
    __slots__: Sequence[str] = ("_key", "version", "model", "generation_config")

    def __init__(
        self,
        key: str,
        *,
        version: ApiVersion = "v1",
        model: Model = "gemini-1.5-pro",
        session: ClientSession | None = None,
        loop: AbstractEventLoop | None = None,
        generation_config: GenerationConfig | None = None,
    ) -> None:
        super().__init__(session, loop)
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
    ) -> GenerateContentResponse | Error | None:
        body: dict[str, Any] = {"contents": list(contents)}
        if text:
            body["contents"].append(Content(parts=[Part(text=text)]))
        if system_instruction:
            body["system_instruction"] = Content(parts=[Part(text=system_instruction)])
        response: ClientResponse | None = await self.request(
            "POST",
            self.get_url(
                MODEL_METHOD_URL, version=version, model=model or self.model, method=ModelMethod.GENERATE_CONTENT.value
            ),
            data=encode(body),
        )
        if not response:
            return
        return decode(await response.read(), type=GenerateContentResponse)
