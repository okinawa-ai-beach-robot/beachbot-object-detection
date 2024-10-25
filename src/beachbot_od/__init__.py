# beachbot_od/__init__.py
import logging
import sys


def setup_logging(level=logging.INFO):
    # Basic configuration
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],  # Output to console
    )


# Call this function when the package is loaded or from a main entry point
setup_logging()
