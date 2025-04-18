from beachbot_od.evaluation.model_evaluate import model_evaluate
from beachbot_od.huggingface_api import (
    get_weights,
    generate_results_table,
    create_model_card,
)
from beachbot.config import config, logger
from beachbot_od.utils.models import SupportedModels
from beachbot_od.roboflow_api import connect, get_dataset
from roboflow.core.dataset import Dataset
from pathlib import Path


def test_model_evaluate():
    model_type = SupportedModels.YOLOV5S
    weights_path = get_weights(model_type, version="v13", resolution=160)
    # Just a temp workaround until I understand the HfApi better regarding repo management
    model_path = weights_path.parent.parent
    dataset = get_dataset(ver=13, overwrite=False)
    model_evaluate(model_path, weights_path, Path(dataset.location))
