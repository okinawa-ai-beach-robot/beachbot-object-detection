import roboflow
from roboflow.core.dataset import Dataset
import keyring
import os
from beachbot_od.config import load_config_file, CONFIG_TYPE
from beachbot.config import config, logger

BEACHBOT_DATASETS = config.BEACHBOT_DATASETS
config_type = CONFIG_TYPE.ROBOFLOW


def connect() -> roboflow.Roboflow:
    # Access API from huggingface secrets
    api_key = os.getenv("ROBOFLOW_KEY")

    if not api_key:
        # For local installations use keyring to securely store the API key
        api_key = keyring.get_password("roboflow", "api_key")

    if not api_key:
        raise ValueError(
            """API key not found in keyring.
        Make sure it is stored securely.
        HuggingFace Usage:
        os.getenv("ROBOFLOW_API_KEY")
        Local Usage:
        pip install keyring
        python -c "import keyring; keyring.set_password('roboflow', 'api_key', 'your_actual_api_key')"
        """
        )
    rf = roboflow.Roboflow(api_key)
    return rf


def generate_version(config_path=None) -> int:
    # Return version ID
    # See https://docs.roboflow.com/api-reference/versions/create-a-project-version for more information

    rf = connect()
    project = rf.workspace().project("beach-cleaning-object-detection")

    version: int
    # Load default config settings
    settings = load_config_file(config_type)

    version = project.generate_version(settings)
    logger.info(f"Version {version} created.")
    return version


def get_dataset(
    ver: int = 1, dataset_format="coco", location=None, overwrite=False
) -> Dataset:
    """
    Downloads dataset from Roboflow
    """
    rf = connect()
    project = rf.workspace("okinawaaibeachrobot").project(
        "beach-cleaning-object-detection"
    )
    version = project.version(ver)

    # Show warning if not overwriting and location already exists so users know new data will not be used
    if location is None:
        location = BEACHBOT_DATASETS / str(ver) / dataset_format
        logger.info(
            f"Dataset location not specified, using default location: {location}."
        )
    if os.path.exists(location) and not overwrite:
        logger.warning(
            f"Dataset directory already exists at {location}. Will not overwrite. To overwrite, set overwrite=True"
        )
    else:
        logger.info(f"Dataset will be downloaded to {location}.")

    dataset = version.download(dataset_format, str(location), overwrite)
    logger.info(f"Dataset downloaded to {location}.")
    return dataset
