import beachbot_od
from beachbot.config import config, logger
from enum import Enum
import shutil
from pathlib import Path
import os
import yaml


BEACHBOT_OD_PATH = Path(os.path.dirname(beachbot_od.__file__))
BEACHBOT_OD_TESTS = Path(os.path.join(BEACHBOT_OD_PATH, "tests"))

# Optionally print for debugging (remove in production)
logger.info(f"BEACHBOT_OD_PATH: {BEACHBOT_OD_PATH}")
logger.info(f"BEACHBOT_OD_TESTS: {BEACHBOT_OD_TESTS}")


class CONFIG_TYPE(Enum):
    ROBOFLOW = 1
    HF_MODEL_CARD = 2


def load_config_file(config_type: CONFIG_TYPE, config_path: Path = None) -> dict:
    """
    config_type: CONFIG_TYPE
    config_path: Path (Optional) use to override default config file locations with a custom one
    """

    if config_path is None:
        if config_type == CONFIG_TYPE.ROBOFLOW:
            filename = "roboflow_version_config.yaml"
            config_path = Path(config.BEACHBOT_CONFIG / filename)
            config_src_path = Path(BEACHBOT_OD_PATH) / "config" / filename
        if config_type == CONFIG_TYPE.HF_MODEL_CARD:
            filename = "model_card_config.yaml"
            config_path = Path(config.BEACHBOT_CONFIG / filename)
            config_src_path = Path(BEACHBOT_OD_PATH) / "config" / filename
        logger.info(
            f"Config file not specified, using default location of {config_path}."
        )
        if not config_path.exists():
            # Copy file from beachbot_od to user config directory
            logger.info(
                f"Config file not found at {config_path}. Copying from {config_src_path}."
            )
            # Ensure config_path parent directories exist
            config_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(config_src_path, config_path)

    # Load the YAML configuration file
    with open(config_path, "r") as file:
        config_file = yaml.safe_load(file)
    return config_file
