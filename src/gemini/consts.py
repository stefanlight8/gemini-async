from __future__ import annotations

from collections.abc import Sequence
from typing import Final, Literal

__version__: Final[str] = "0.1.0"
__all__: Sequence[str] = (
    "__version__",
    "USER_AGENT",
    "API_URL",
    "MODELS_URL",
    "MODEL_METHOD_URL",
    "ApiVersion",
    "Model",
)

USER_AGENT: Final[str] = f"gemini-async/{__version__}"

API_URL: Final[str] = "https://generativelanguage.googleapis.com/{version}"
MODELS_URL: Final[str] = API_URL + "/models/"
MODEL_METHOD_URL: Final[str] = MODELS_URL + "{model}:{method}?key={key}"

ApiVersion = Literal["v1", "v1beta"]
Model = Literal[
    "aqa",
    "text-embedding-004",
    "gemini-1.0-pro",  # deprecated
    "gemini-1.5-pro",
    "gemini-1.5-flash-8b",
    "gemini-1.5-flash",
    "gemini-2.0-flash-exp",
]
