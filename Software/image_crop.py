import cv2
import matplotlib.pyplot as plt
import numpy as np
import openvino as ov
import ipywidgets as widgets
from pathlib import Path


## 디바이스 선택
core = ov.Core()
device = widgets.Dropdown(
    options=core.available_devices + ["AUTO"],
    value='AUTO',
    description='Device:',
    disabled=False,
)


## 모델 로드
base_model_dir = Path("./braille_model").expanduser()

model_xml_name = 'model.xml'
model_bin_name = 'model.bin'

model_xml_path = base_model_dir / model_xml_name
model_bin_path = base_model_dir / model_bin_name

model = core.read_model(model=model_xml_path)
compiled_model = core.compile_model(model=model, device_name="CPU")

input_layer_ir = compiled_model.input(0)
output_layer_ir = compiled_model.output("boxes")
print("컴파일모델 - input: ", input_layer_ir)
print("컴파일모델 - output: ", output_layer_ir)


## 이미지 로드
image_filename = './images/sample.jpg'
image = cv2.imread(str(image_filename))

# 이미지 리사이징
H = 736
W = 992
resized_image = cv2.resize(image, (W, H))

# Reshape to the network input shape.
input_image = np.expand_dims(resized_image.transpose(2, 0, 1), 0)

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# box 정보 얻어오기
boxes = compiled_model([input_image])[output_layer_ir]
boxes = boxes[0]

def convert_result_to_image(bgr_image, resized_image, boxes, threshold=0.3, conf_labels=True):
    
    colors = {"red": (255, 0, 0), "green": (0, 255, 0)}

    (real_y, real_x), (resized_y, resized_x) = bgr_image.shape[:2], resized_image.shape[:2]
    ratio_x, ratio_y = real_x / resized_x, real_y / resized_y

    rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)

    for box in boxes:

        conf = box[-1]
        if conf > threshold:

            (x_min, y_min, x_max, y_max) = [
                int(max(corner_position * ratio_y, 10)) if idx % 2 
                else int(corner_position * ratio_x)
                for idx, corner_position in enumerate(box[:-1])
            ]

            # Draw a box, rectangle function: image, start_point, end_point, color, thickness
            rgb_image = cv2.rectangle(rgb_image, (x_min, y_min), (x_max, y_max), colors["green"], 3)
            
            # 자르기
            crop_image = image[y_min:y_max, x_min:x_max]
            cv2.imshow("Cropped Image", crop_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
            # Add text to the image based on position and confidence.
            # Parameters in text function are: image, text, bottom-left_corner_textfield, font, font_scale, color, thickness, line_type.
            if conf_labels:
                rgb_image = cv2.putText(
                    rgb_image,
                    f"{conf:.2f}",
                    (x_min, y_min - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    colors["red"],
                    1,
                    cv2.LINE_AA,
                )

    return rgb_image


#plt.figure(figsize=(10, 6))
#plt.axis("off")
#plt.imshow(convert_result_to_image(image, resized_image, boxes, conf_labels=False))

cv2.imshow('image Convert', convert_result_to_image(image, resized_image, boxes, conf_labels=False))
cv2.waitKey(0)
cv2.destroyAllWindows()
