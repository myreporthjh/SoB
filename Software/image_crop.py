import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
import openvino as ov
import ipywidgets as widgets
from datetime import datetime
from pathlib import Path

import cv2


## 디바이스 선택
core = ov.Core()
device = widgets.Dropdown(
    options=core.available_devices + ["AUTO"],
    value='AUTO',
    description='Device:',
    disabled=False,
)


## 모델 로드
base_model_dir = Path("./model").expanduser()

model_xml_name = 'model.xml'
model_bin_name = 'model.bin'

model_xml_path = base_model_dir / model_xml_name
model_bin_path = base_model_dir / model_bin_name

model = core.read_model(model=model_xml_path)
compiled_model = core.compile_model(model=model, device_name="CPU")

input_layer_ir = compiled_model.input(0)
output_layer_ir = compiled_model.output("boxes")


## Height, Width 지정
H = 736
W = 992


## 이미지 저장
def save_image(image,now_time):    
    folder_name = "./images/cropped_images/"+now_time
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    file_list=os.listdir(folder_name)
    #파일 갯수 세기
    file_number = len(file_list)
    print("현재 파일개수: ", file_number)
    
    cv2.imshow("Cropped Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(f'{folder_name}/{file_number}.jpg', image)
    

## 라벨링된 이미지로 컨버팅
def convert_result_to_image(bgr_image, resized_image, boxes, threshold=0.3, conf_labels=True):
    
    #frame = bgr_image
    colors = {"red": (255, 0, 0), "green": (0, 255, 0)}

    (real_y, real_x), (resized_y, resized_x) = bgr_image.shape[:2], resized_image.shape[:2]
    ratio_x, ratio_y = real_x / resized_x, real_y / resized_y

    rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
    current_datetime = datetime.now()
    now_time = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
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
                        
            # crop & save
            crop_image = bgr_image[y_min:y_max, x_min:x_max]
            save_image(crop_image,now_time)
            
            # Add text to the image based on position and confidence.
            # Parameters in text function are: image, text, bottom-left_corner_textfield, font, font_scale, color, thickness, line_type.
            #if conf_labels:
            rgb_image = cv2.putText(
                rgb_image,
                f"dot: {conf:.2f}",
                (x_min, y_min - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                colors["red"],
                1,
                cv2.LINE_AA,
            )

    return rgb_image



## 웹캠 사용
cap= cv2.VideoCapture(0)
if cap.isOpened():
    
    while True:
        ret,frame = cap.read()
        
        if ret:
            
            original_frame = frame
            resized_image = cv2.resize(frame, (W, H))

            # Reshape to the network input shape.
            input_image = np.expand_dims(resized_image.transpose(2, 0, 1), 0)
            
            # box 정보 얻어오기
            boxes = compiled_model([input_image])[output_layer_ir]
            boxes = boxes[0]
            colors = {"red": (255, 0, 0), "green": (0, 255, 0)}

            (real_y, real_x), (resized_y, resized_x) = frame.shape[:2], resized_image.shape[:2]
            ratio_x, ratio_y = real_x / resized_x, real_y / resized_y
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            for box in boxes:
                threshold = 0.3    
                conf = box[-1]
                if conf > threshold:

                    (x_min, y_min, x_max, y_max) = [
                        int(max(corner_position * ratio_y, 10)) if idx % 2 
                        else int(corner_position * ratio_x)
                        for idx, corner_position in enumerate(box[:-1])
                    ]

                    # Draw a box, rectangle function: image, start_point, end_point, color, thickness
                    frame = cv2.rectangle(rgb_image, (x_min, y_min), (x_max, y_max), colors["green"], 3)    
     
                    frame = cv2.putText(
                        rgb_image,
                        f"dot: {conf:.2f}",
                        (x_min, y_min - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        colors["red"],
                        1,
                        cv2.LINE_AA,
                    )                
            
            cv2.imshow('camera', frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('w'):
                #cv2.imwrite('photo.jpg', frame)
                                
                cv2.imshow('image Convert', convert_result_to_image(original_frame, resized_image, boxes, conf_labels=False))
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                continue
            
            elif key == ord('q'):
                break
            
        else:
            print('no frame')
            break
else:
    print('no camera!')
cap.release()
cv2.destroyAllWindows()
