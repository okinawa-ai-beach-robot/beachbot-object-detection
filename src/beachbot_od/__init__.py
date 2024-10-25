# beachbot_od/__init__.py
import logging
import sys

# Create and configure the package-wide logger
logger = logging.getLogger("beachbot_od")
logger.setLevel(logging.INFO)  # Set default level; adjust as needed

# Set up a console handler with a simple format
console_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)

# Avoid adding multiple handlers if the logger is reused
if not logger.hasHandlers():
    logger.addHandler(console_handler)
