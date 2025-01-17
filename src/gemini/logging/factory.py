from logging import Logger, getLogger


class LoggerFactory:
    _base_logger: Logger = getLogger("gemini")

    @classmethod
    def create(cls, name: str) -> Logger:
        return cls._base_logger.getChild(name)
