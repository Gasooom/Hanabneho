from loguru import logger

logger.remove()

logger.add(
    sink="logs/hanabneho.log",
    rotation="10 MB",
    retention="10 days",
    level="INFO",
)

logger.add(
    sink=lambda message: print(message, end=""),
    level="INFO",
)