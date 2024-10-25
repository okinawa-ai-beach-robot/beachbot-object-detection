# beachbot_od/__init__.py
import logging
import sys

# Create and configure the package-wide bb_logger
bb_logger = logging.getLogger("beachbot_od")
bb_logger.setLevel(logging.INFO)  # Set default level; adjust as needed

# Set up a console handler with a simple format
console_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)

# Avoid adding multiple handlers if the bb_logger is reused
if not bb_logger.hasHandlers():
    bb_logger.addHandler(console_handler)
