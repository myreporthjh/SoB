import cv2
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import openvino as ov
import ipywidgets as widgets
from pathlib import Path
from os.path import exists


def delete_files(file_path):
    # 파일 잔여데이터 삭제
    #file_path = './images/cropped_images/'
    if os.path.exists(file_path):
        for file in os.scandir(file_path):
            os.remove(file.path)
        return '모든 파일 삭제 완료'
    else:
        return '파일 삭제 에러'

## 이미지 저장
def save_image(image):
    
    # 파일 갯수 세기
    file_list=os.listdir('images/cropped_images')
    file_number = len(file_list)
    
    cv2.imshow("Cropped Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(f'./images/cropped_images/cropped_image{file_number}.jpg', image)


## 라벨링된 이미지로 컨버팅
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
            
            # crop & save
            crop_image = bgr_image[y_min:y_max, x_min:x_max]
            save_image(crop_image)
            
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


## 웹캠 사용
# cap= cv2.VideoCapture(0)
# if cap.isOpened():
    
#     while True:
#         ret,frame = cap.read()
        
#         if ret:
#             cv2.imshow('camera', frame)

#             if cv2.waitKey(1) != -1:
#                 #cv2.imwrite('photo.jpg', frame)
                
#                 resized_image = cv2.resize(frame, (W, H))

#                 # Reshape to the network input shape.
#                 input_image = np.expand_dims(resized_image.transpose(2, 0, 1), 0)

#                 # box 정보 얻어오기
#                 boxes = compiled_model([input_image])[output_layer_ir]
#                 boxes = boxes[0]
                
#                 cv2.imshow('image Convert', convert_result_to_image(frame, resized_image, boxes, conf_labels=True))
#                 cv2.waitKey(0)
#                 cv2.destroyAllWindows()
#                 break
            
#         else:
#             print('no frame')
#             break
# else:
#     print('no camera!')
# cap.release()
# cv2.destroyAllWindows()


## mode1 데모
def model1_demo():
    ## 디바이스 선택
    core = ov.Core()
    device = widgets.Dropdown(
        options=core.available_devices + ["AUTO"],
        value='AUTO',
        description='Device:',
        disabled=False,
    )


    ## 모델 로드
    base_model_dir = Path("./model1").expanduser()
    model_xml_name = 'model.xml'
    #model_bin_name = 'model.bin'
    model_xml_path = base_model_dir / model_xml_name
    #model_bin_path = base_model_dir / model_bin_name
    model = core.read_model(model=model_xml_path)
    compiled_model = core.compile_model(model=model, device_name="CPU")
    #input_layer_ir = compiled_model.input(0)
    output_layer_ir = compiled_model.output("boxes")


    ## Height, Width 지정
    H = 736
    W = 992


    ## 정적 이미지 사용
    img_filename = './images/full_images/sample.png'
    braille_iamge = cv2.imread(img_filename)
    resized_image = cv2.resize(braille_iamge, (W, H))
    input_image = np.expand_dims(resized_image.transpose(2, 0, 1), 0)
    boxes = compiled_model([input_image])[output_layer_ir]
    boxes = boxes[0]

    ## 파일 삭제(초기화 작업)
    print(delete_files('images/cropped_images'))

    cv2.imshow('image Convert', convert_result_to_image(braille_iamge, resized_image, boxes, conf_labels=True))
    cv2.waitKey(0)
    cv2.destroyAllWindows()