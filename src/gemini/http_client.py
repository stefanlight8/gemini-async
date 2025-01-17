import time
from asyncio.events import AbstractEventLoop
from logging import Logger

from aiohttp import ClientResponse
from aiohttp.client import ClientConnectionError, ClientResponseError, ClientSession
from aiohttp.connector import TCPConnector

from gemini.consts import USER_AGENT
from gemini.logging.factory import LoggerFactory


class HTTPClient:
    def __init__(self, loop: AbstractEventLoop, *, session: ClientSession | None = None) -> None:
        self.__logger: Logger = LoggerFactory.create("http")
        self._loop: AbstractEventLoop = loop
        self._connector: TCPConnector | None = None
        self._session: ClientSession | None = session

    @property
    def session(self) -> ClientSession:
        if not self._connector:
            self._connector = TCPConnector(loop=self._loop)
        if not self._session:
            self._session = ClientSession(
                connector=self._connector,
                loop=self._loop,
                headers={"Content-Type": "application/json", "User-Agent": USER_AGENT},
            )
        return self._session

    async def request(self, method: str, url: str, *, data: bytes | None = None, stream: bool = False) -> ClientResponse | None:
        try:
            start: float = time.monotonic()
            self.__logger.debug(
                "send %s request to %s (0x%s)", method, url, id(start)
            )  # that's a silly move to identify requests, remove later maybe
            response = await self.session.request(method, url, data=data, raise_for_status=True)
            self.__logger.debug("got response in %.2f seconds (0x%s)", time.monotonic() - start, id(start))
            return response
        except ClientResponseError as error:
            self.__logger.error("got %s response code, message: %s", error.status, error.message)
            return
        except (ClientConnectionError, TimeoutError):
            self.__logger.critical("cannot connect")
            return
        except Exception as exception:
            self.__logger.error("unhandled exception occurred in request", exc_info=exception)
            return
