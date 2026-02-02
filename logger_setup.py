import logging


def init_logger():
    """
    Initializes and configures a logger.

    This logger outputs to both the system console and a local file.
    It uses a consistent fomrat including timestamps,logger name ,level name, and a message.

    Returns:
        logger: A configured logger instance named "my_logger".
    """
    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(name)s %(levelname)s - %(message)s")

    file_handler = logging.FileHandler("app.log")
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
