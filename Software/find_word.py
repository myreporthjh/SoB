"""Demo based on ModelAPI."""
# Copyright (C) 2021-2022 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
#
import os
import sys
import cv2
import numpy as np
from argparse import SUPPRESS, ArgumentParser
from pathlib import Path

import importlib
import json
from openvino.model_api.adapters import OpenvinoAdapter, create_core
from openvino.model_api.models import ImageModel, Model

from otx.api.serialization.label_mapper import LabelSchemaMapper
from otx.api.entities.model_template import TaskType
from otx.api.serialization.label_mapper import LabelSchemaMapper
from otx.api.utils.detection_utils import detection2array

from otx.api.usecases.exportable_code.demo.demo_package.utils import (
    create_output_converter,
)

from otx.api.entities.annotation import (
    Annotation,
    AnnotationSceneEntity,
    NullAnnotationSceneEntity,
)

# from typing import (
#     Callable,
#     Generic,
#     List,
#     NewType,
#     Optional,
#     Sequence,
#     Tuple,
#     Type,
#     TypeVar,
#     Union,
# )


from utils import get_model_path, get_parameters

#os.environ["FEATURE_FLAGS_OTX_ACTION_TASKS"] = "1"

# pylint: disable=no-name-in-module, import-error
# from otx.api.usecases.exportable_code.demo.demo_package import (
#     AsyncExecutor,
#     ChainExecutor,
#     ModelContainer,
#     SyncExecutor,
#     create_visualizer,
# )


def build_argparser():
    """Parses command line arguments."""
    parser = ArgumentParser(add_help=False)
    args = parser.add_argument_group("Options")
    args.add_argument(
        "-h",
        "--help",
        action="help",
        default=SUPPRESS,
        help="Show this help message and exit.",
    )
    args.add_argument(
        "-i",
        "--input",
        required=False,
        default=[Path("../model")],
        help="Required. An input to process. The input must be a single image, "
        "a folder of images, video file or camera id.",
    )
    args.add_argument(
        "-m",
        "--models",
        help="Optional. Path to directory with trained model and configuration file. "
        "If you provide several models you will start the task chain pipeline with "
        "the provided models in the order in which they were specified. Default value "
        "points to deployed model folder '../model'.",
        nargs="+",
        default=[Path("./model2")],
        type=Path,
    )
    args.add_argument(
        "-it",
        "--inference_type",
        help="Optional. Type of inference for single model.",
        choices=["sync", "async"],
        default="sync",
        type=str,
    )
    args.add_argument(
        "-d",
        "--device",
        help="Optional. Device to infer the model.",
        choices=["CPU", "GPU"],
        default="CPU",
        type=str,
    )
    args.add_argument(
        "--output",
        default=None,
        type=str,
        help="Optional. Output path to save input data with predictions.",
    )

    return parser


def get_inferencer_class(type_inference):
    return EXECUTORS[type_inference]


def model2_demo():
    args = build_argparser().parse_args()

    # create models
    model_dir=args.models[0]
    #model_dir="model2"
    print(args.models[0])
    model_adapter = OpenvinoAdapter(create_core(), get_model_path(model_dir / "model.xml"), device=args.device)
    parameters = get_parameters(model_dir / "config.json")
    labels = LabelSchemaMapper.backward(parameters["model_parameters"]["labels"])
    task_type = TaskType[parameters["converter_type"]]
    model_parameters = parameters["model_parameters"]
    model_parameters["labels"] = []
    confidence = model_parameters["confidence_threshold"]
    importlib.import_module("model_wrappers")

    core_model = Model.create_model(
        model_adapter,
        parameters["type_of_model"],
        model_parameters,
        preload=True,
    )

    #inferencer = SyncExecutor
    converter = create_output_converter(task_type, labels, model_parameters)
    
    # 파일 열기 (쓰기모드)
    f = open("word.txt",'w')
    
    # Load image
    for i in os.listdir('./images/cropped_images/'):
        path = './images/cropped_images/'+i
        print(path)
        img = cv2.imread(path, cv2.IMREAD_COLOR)
        
        #cv2.imshow("image", img_color)
        #cv2.waitKey(0)


    # Load image
    #img = cv2.imread("sample.jpg", cv2.IMREAD_COLOR)
    #if img is None:
     #   print(f"Can't read the image!")
     #   exit

        # Inference
        predictions = core_model(img)

        # x1가 작은순서대로 정렬
        x1_values = []
        
        # Post Processing
        predictions = detection2array(predictions.objects)
        frame_meta = {"original_shape": img.shape}

        results = converter.convert_to_annotation(predictions, frame_meta)
        
        for annotation in results.annotations:
            probability = annotation.get_labels()[0].probability
            if probability > confidence:
                entity = annotation.shape
                name = annotation.get_labels()[0].name
                c = annotation.get_labels()[0].color
                #print(f"name = {name}")
                #print(f"entity = {entity}")
                x1, y1 = int(entity.x1 * img.shape[1]), int(entity.y1 * img.shape[0])
                x2, y2 = int(entity.x2 * img.shape[1]), int(entity.y2 * img.shape[0])
                
                x1_values.append([x1, name])
                
                img = cv2.rectangle(img=img, pt1=(x1, y1), pt2=(x2, y2), color=(c.red, c.green, c.blue, c.alpha), thickness=2)

    
        print(x1_values)
        sorted_list = sorted(x1_values, key=lambda x: x[0]) # 오름차순 정렬
        print(sorted_list)
        
        
        # 리스트 요소 접근
        for sublist in sorted_list:
            f.write(sublist[1]+"\n")
            print(sublist[1])
        
        
        cv2.imshow("ret", img)
        cv2.waitKey(0)
    
    # 파일 종료
    f.close()

if __name__ == "__main__":
    sys.exit(model2_demo() or 0)
