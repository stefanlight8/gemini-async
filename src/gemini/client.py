from aiohttp.client import ClientSession
from msgspec.json import decode, encode

from gemini.consts import API_VERSION_STRING, MODEL_METHOD_URL, MODEL_STRING, USER_AGENT
from gemini.enums import ModelMethod
from gemini.structs import Content, GenerateContentResponse, Part


class Gemini:
    def __init__(
        self,
        key: str,
        *,
        version: API_VERSION_STRING = "v1",
        model: MODEL_STRING = "gemini-1.5-pro",
        session: ClientSession | None = None,
    ) -> None:
        self._key: str = key
        self._session: ClientSession | None = session
        self.version: API_VERSION_STRING = version
        self.model: MODEL_STRING = model

    @property
    def session(self) -> ClientSession:
        if not self._session:
            self._session = ClientSession()
        return self._session

    async def generate_content(self, text: str) -> GenerateContentResponse:
        try:
            async with self.session.post(
                MODEL_METHOD_URL.format(
                    version=self.version, model=self.model, method=ModelMethod.GENERATE_CONTENT.value, key=self._key
                ),
                headers={"Content-Type": "application/json", "User-Agent": USER_AGENT},
                data=encode({"contents": [Content(parts=[Part(text)])]}),
            ) as response:
                return decode(await response.read(), type=GenerateContentResponse)
        except Exception:
            raise
