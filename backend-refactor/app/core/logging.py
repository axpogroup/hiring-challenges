"""Logging configuration module."""
import logging
import sys

VALID_LOG_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}

def setup_logging(log_level: str = "INFO"):
    level = log_level.upper()
    if level not in VALID_LOG_LEVELS:
        level = "INFO"

    logging.basicConfig(
        level=level,
        format="%(asctime)s │ %(levelname)s │ %(name)s - %(message)s",
        stream=sys.stdout,
    )

    # Reduce verbosity of dependency logs
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.error").setLevel(logging.WARNING)
