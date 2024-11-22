from beachbot_od.roboflow_api import connect, get_dataset
from roboflow.core.dataset import Dataset

from pathlib import Path


def test_connect():
    rf = connect()
    # If rf is None, this indicates roboflow was unable to connect
    assert rf is not None


# Need a way to test `generate_version` without actually generating a new one. Guess there is some test arg for this
# rf.generate_version(config_path="roboflow_version_config_test.yaml")


def test_get_dataset():
    # 13 being the dummy tiny dataset
    dataset = get_dataset(ver=13, overwrite=False)
    assert dataset is not None
    assert isinstance(dataset, Dataset)
    assert Path(dataset.location).exists()
