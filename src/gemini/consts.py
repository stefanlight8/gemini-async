from typing import Final, Literal

from gemini import __version__

USER_AGENT: Final[str] = f"gemini-async/{__version__}"

API_URL: Final[str] = "https://generativelanguage.googleapis.com/{version}"
MODELS_URL: Final[str] = API_URL + "/models/"
MODEL_METHOD_URL: Final[str] = MODELS_URL + "{model}:{method}?key={key}"

API_VERSION_STRING = Literal["v1", "v1beta"]
MODEL_STRING = Literal[
    "aqa",
    "text-embedding-004",
    "gemini-1.0-pro",  # deprecated
    "gemini-1.5-pro",
    "gemini-1.5-flash-8b",
    "gemini-1.5-flash",
    "gemini-2.0-flash-exp",
]
