from enum import Enum


class FinishReason(int, Enum):
    FINISH_REASON_UNSPECIFIED = 0
    STOP = 1
    MAX_TOKENS = 2
    SAFETY = 3
    RECITATION = 4
    LANGUAGE = 5
    OTHER = 6
    BLOCKLIST = 7
    PROHIBITED_CONTENT = 8
    SPII = 9
    MALFORMED_FUNCTION_CALL = 10


class ModelMethod(str, Enum):
    GENERATE_CONTENT = "generateContent"
