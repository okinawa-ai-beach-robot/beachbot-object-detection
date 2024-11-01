from beachbot_od.yolo_v5_api.train import train_model
from beachbot_od.utils.models import SupportedModels


train_model(
    model_format=SupportedModels.YOLOV5S,
    img_width=160,
    dataset_version=13,
    epochs=1,
    overwrite=True,
)
