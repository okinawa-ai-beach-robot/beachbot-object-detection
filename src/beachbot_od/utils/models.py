from pathlib import Path
from typing import Optional

import yolov5
from beachbot.config import config
from beachbot_od.huggingface_api import get_weights
from beachbot_od.utils.supported_models import SupportedModels
from huggingface_hub import HfApi

BEACHBOT_MODELS = Path(config.BEACHBOT_MODELS)


class Model:
    """
    Wrapper for HF API with default values for beachbot
    Args:
    ----
        local_path: Path (defaults to None which uses HF cache system)
        model_type: SupportedModels
        resolution: int within the set {160, 320, 640, 1280}
        version: int (should be vX, where X is an integer. Defaults to tip of
                 main branch when None)
        weights_path: Path (defaults to None which uses HF cache system)
    """

    def __init__(
        self,
        model_type: SupportedModels = SupportedModels.YOLOV5S,
        resolution: int = 160,
        version: Optional[str] = None,
        local_path: Optional[Path] = None,
        weights_path: Optional[Path] = None,
    ):
        self.local_path = local_path
        self.model_type: SupportedModels = model_type
        self.resolution: int = resolution
        self.version: Optional[str] = version
        self.weights_path = weights_path
        self.hfapi = HfApi()

        if self.local_path is None:
            self.weights_path = get_weights(
                self.model_type,
                resolution=self.resolution,
                version=self.version,
            )
            if self.weights_path is not None and self.local_path is None:
                self.local_path = self.weights_path.parent
