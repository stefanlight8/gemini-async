from asyncio.events import AbstractEventLoop, get_event_loop
from collections.abc import Sequence
from typing import Any

from aiohttp import ClientResponse
from aiohttp.client import ClientSession
from msgspec.json import decode, encode

from gemini.consts import API_VERSION_STRING, MODEL_METHOD_URL, MODEL_STRING
from gemini.enums import ModelMethod
from gemini.http_client import HTTPClient
from gemini.structs import Content, GenerateContentResponse, Part


class Gemini:
    __slots__: Sequence[str] = ("__logger", "_key", "_loop", "_http", "version", "model")

    def __init__(
        self,
        key: str,
        *,
        version: API_VERSION_STRING = "v1",
        model: MODEL_STRING = "gemini-1.5-pro",
        loop: AbstractEventLoop | None = None,
        session: ClientSession | None = None,
    ) -> None:
        self._key: str = key
        self._loop: AbstractEventLoop | None = loop or get_event_loop()
        self._http: HTTPClient = HTTPClient(self._loop, session=session)
        self.version: API_VERSION_STRING = version
        self.model: MODEL_STRING = model

    async def generate_content(
        self,
        *content: Content,
        version: API_VERSION_STRING | None = None,
        model: MODEL_STRING | None = None,
        system_instruction: str | None = None,  # only text available for system instruction (Google)
    ) -> GenerateContentResponse | None:
        body: dict[str, Any] = {"contents": content}
        if system_instruction:
            body["system_instruction"] = Content(parts=[Part(text=system_instruction)])
        response: ClientResponse | None = await self._http.request(
            "POST",
            MODEL_METHOD_URL.format(
                version=version or self.version,
                model=model or self.model,
                method=ModelMethod.GENERATE_CONTENT.value,
                key=self._key,
            ),
            data=encode(body),
        )
        if not response:
            return
        return decode(await response.read(), type=GenerateContentResponse)
