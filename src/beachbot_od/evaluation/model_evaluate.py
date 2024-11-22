from globox import AnnotationSet, COCOEvaluator, BoxFormat
import torch
from pathlib import Path
import shutil
from beachbot.config import logger


def model_evaluate(model_path: Path, weights_path: Path, dataset_path: Path):
    if not model_path.exists():
        RuntimeError("Model not found")
    if not weights_path.exists():
        RuntimeError("Weights not found")
    if not dataset_path.exists():
        RuntimeError("Dataset not found")

    test_dataset_path = dataset_path / "test"
    gt_label_path = test_dataset_path / "_annotations.coco.json"

    if not gt_label_path.exists():
        raise ValueError(f"{gt_label_path} does not exist")

    # Make detections parent folder to hold model-specific detections
    detections_path = model_path / "detections"
    detections_path.mkdir(parents=True, exist_ok=True)

    gt = AnnotationSet.from_coco(
        file_path=gt_label_path,
    )
    # replace path with reference to dataset_path
    images = [test_dataset_path / item for item in list(gt.image_ids)]

    # Load model
    model = torch.hub.load("ultralytics/yolov5", "custom", path=weights_path)

    # set model parameters
    model.conf = 0.70  # NMS confidence threshold
    model.iou = 0.50  # NMS IoU threshold
    model.agnostic = False  # NMS class-agnostic
    model.multi_label = False  # NMS multiple labels per box
    model.max_det = 10  # maximum number of detections per image

    # Run inference on all images within dataset
    results = model(images)
    results.save(save_dir=detections_path / "detection_images", exist_ok=True)

    # Remove cached or previous predictions:
    if Path("detections").exists():
        logger.info("Removing previous detections")
        shutil.rmtree("detections")

    # Loop over each image in results and save detection annotations
    for i in range(len(results.pandas().xywh)):
        filename = results.files[i]
        # Remove .jpg extension
        filename = filename[:-4]
        # drop class column and reorder for globox expected order
        df = results.pandas().xywh[i][
            ["name", "xcenter", "ycenter", "width", "height", "confidence"]
        ]

        filepath = detections_path / f"{filename}.txt"
        filepath.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(filepath, sep=" ", index=False, header=False)

    # Not using from_yolo_v5 as it doesn't allow to override relative=False
    # See https://github.com/laclouis5/globox/discussions/48
    # and https://github.com/laclouis5/globox/issues/49
    predictions = AnnotationSet.from_txt(
        folder=detections_path,
        image_folder=test_dataset_path,
        box_format=BoxFormat.XYWH,
        relative=False,
        separator=None,
        conf_last=True,
    )
    evaluator = COCOEvaluator(ground_truths=gt, predictions=predictions)
    evaluator.show_summary()
    evaluator.save_csv(model_path / "evaluation.csv")
