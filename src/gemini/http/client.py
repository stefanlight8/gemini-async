from __future__ import annotations

import time
from asyncio.events import AbstractEventLoop
from collections.abc import Sequence
from logging import Logger, getLogger
from typing import Literal

from aiohttp.client import ClientConnectionError, ClientResponse, ClientSession

from gemini.consts import USER_AGENT

__all__: Sequence[str] = ("HTTPClient",)

_LOGGER: Logger = getLogger("gemini.http")
HTTPMethod = Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "TRACE"]


class HTTPClient:
    __slots__: Sequence[str] = ("session",)

    def __init__(self, session: ClientSession | None = None, loop: AbstractEventLoop | None = None) -> None:
        self.session: ClientSession = session or ClientSession(
            headers={"Content-Type": "application/json", "User-Agent": USER_AGENT}, loop=loop
        )

    async def request(self, method: HTTPMethod, url: str, *, data: bytes) -> ClientResponse | None:
        _LOGGER.debug("send %s request", method)
        try:
            start, response = time.monotonic(), await self.session.request(method, url, data=data)
            _LOGGER.debug("got response in %.2f seconds", time.monotonic() - start)
        except (ClientConnectionError, TimeoutError):
            _LOGGER.error("cannot connect")
            return
        except Exception as exception:
            _LOGGER.error("unhandled exception occurred in request", exc_info=exception)
            return
        return response
