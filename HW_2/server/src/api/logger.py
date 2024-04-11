import logging


def setup_uvi_loggers():
    # Disable main uvicorn logger
    uvi_logger = logging.getLogger("uvicorn")
    for handler in uvi_logger.handlers:
        uvi_logger.removeHandler(handler)
    uvi_logger.disabled = True

    # Set formater for uvicorn error logger
    for loggerName in ["uvicorn.access", "uvicorn.error"]:
        uvicorn_error = logging.getLogger(loggerName)
        formatter = logging.Formatter(
            "{asctime} | {levelname:<8s} | [uvicorn] | {message}",
            style="{",
        )
        for handler in uvicorn_error.handlers:
            uvicorn_error.removeHandler(handler)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        uvicorn_error.addHandler(stream_handler)


def get_logger():
    logger = logging.getLogger("emo_app")
    _formatter = logging.Formatter(
        "{asctime} | {levelname:<8s} | [emo_app] | {message}",
        style="{",
    )
    for _handler in logger.handlers:
        logger.removeHandler(_handler)
    _stream_handler = logging.StreamHandler()
    _stream_handler.setFormatter(_formatter)
    logger.addHandler(_stream_handler)
    logger.setLevel(logging.getLevelName(logging.INFO))

    return logger
