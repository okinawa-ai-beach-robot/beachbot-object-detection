from platformdirs import PlatformDirs
import os
import beachbot_od
from pathlib import Path
import logging

logging = logging.getLogger("beachbot_od")

BEACHBOT_OD_PATH = Path(os.path.dirname(beachbot_od.__file__))
BEACHBOT_OD_TESTS = Path(os.path.join(BEACHBOT_OD_PATH, "tests"))

# Define the directory paths you want to make available globally
_platform_dirs = PlatformDirs("beachbot_od", "okinawa-ai-beach-robot")
if os.getenv("BEACHBOT_HOME"):
    BEACHBOT_HOME = Path(os.getenv("BEACHBOT_HOME"))
else:
    BEACHBOT_HOME = Path(_platform_dirs.user_data_dir)

if os.getenv("BEACHBOT_CACHE"):
    BEACHBOT_CACHE = Path(os.getenv("BEACHBOT_CACHE"))
else:
    BEACHBOT_CACHE = Path(_platform_dirs.user_cache_dir)

if os.getenv("BEACHBOT_CONFIG"):
    BEACHBOT_CONFIG = Path(os.getenv("BEACHBOT_CONFIG"))
else:
    BEACHBOT_CONFIG = Path(_platform_dirs.user_config_dir)

if os.getenv("BEACHBOT_LOGS"):
    BEACHBOT_LOGS = Path(os.getenv("BEACHBOT_LOGS"))
else:
    BEACHBOT_LOGS = Path(_platform_dirs.user_log_dir)

if os.getenv("BEACHBOT_MODELS"):
    BEACHBOT_MODELS = Path(os.getenv("BEACHBOT_MODELS"))
else:
    BEACHBOT_MODELS = BEACHBOT_CACHE / "models"  # Use / operator to join paths

if os.getenv("BEACHBOT_DATASETS"):
    BEACHBOT_DATASETS = Path(os.getenv("BEACHBOT_DATASETS"))
else:
    BEACHBOT_DATASETS = BEACHBOT_CACHE / "datasets"  # Use / operator to join paths

# Ensure the directories exist
BEACHBOT_HOME.mkdir(parents=True, exist_ok=True)
BEACHBOT_CACHE.mkdir(parents=True, exist_ok=True)
BEACHBOT_CONFIG.mkdir(parents=True, exist_ok=True)
BEACHBOT_LOGS.mkdir(parents=True, exist_ok=True)
BEACHBOT_MODELS.mkdir(parents=True, exist_ok=True)
BEACHBOT_DATASETS.mkdir(parents=True, exist_ok=True)

# Optionally print for debugging (remove in production)
logging.info(f"BEACHBOT_OD_PATH: {BEACHBOT_OD_PATH}")
logging.info(f"BEACHBOT_OD_TESTS: {BEACHBOT_OD_TESTS}")
logging.info(f"BEACHBOT_HOME: {BEACHBOT_HOME}")
logging.info(f"BEACHBOT_CACHE: {BEACHBOT_CACHE}")
logging.info(f"BEACHBOT_CONFIG: {BEACHBOT_CONFIG}")
logging.info(f"BEACHBOT_LOGS: {BEACHBOT_LOGS}")
logging.info(f"BEACHBOT_MODELS: {BEACHBOT_MODELS}")
logging.info(f"BEACHBOT_DATASETS: {BEACHBOT_DATASETS}")
