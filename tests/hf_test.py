from pathlib import Path

import pandas as pd
import yolov5
from beachbot.config import config, logger
from beachbot_od.huggingface_api import (create_model_card,
                                         generate_results_table,
                                         get_base_weights, get_file,
                                         get_weights)
from beachbot_od.utils.models import Model
from beachbot_od.utils.supported_models import SupportedModels


def test_get_file():
    get_file(version="v13", resolution=160, filename="weights/best.pt")


def test_get_weights():
    get_weights(SupportedModels.YOLOV5S, version="v13", resolution=160)


def test_get_base_weights():
    get_base_weights()


def test_generate_results_table():
    # touch tmp csv file for testing
    evaluation_csv = Path("tmp.csv")
    evaluation_csv.touch(exist_ok=True)
    # add random data to tmp csv file
    data = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    data.to_csv(evaluation_csv, index=False)
    # touch tmp README.md file for testing
    markdown_file = Path("tmp.md")
    markdown_file.touch(exist_ok=True)
    generate_results_table(evaluation_csv, markdown_file)
    # remove tmp csv file
    evaluation_csv.unlink()
    # remove tmp README.md file
    markdown_file.unlink()


def test_create_model_card():
    create_model_card(save=False)


def test_model():
    Model(
        model_type=SupportedModels.YOLOV5S,
        resolution=160,
        version="v13",
    )
