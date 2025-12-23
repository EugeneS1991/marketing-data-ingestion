import logging
import sys

# Configure the root logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    datefmt="%Y-%m-%d %H:%M:%S",
    fmt="%(levelname)-9s %(asctime)s.%(msecs)03d - %(module)-10s - %(funcName)s:%(lineno)-10d - %(message)s - [%(pathname)s]",
)

# Check if handlers already exist to avoid duplication
if not logger.hasHandlers():
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
