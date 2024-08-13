import os
import sys
def get_project_root() -> str:
    current_abspath = os.path.abspath(os.getcwd())
    while True:
        if os.path.split(current_abspath)[1] == 'Safety_Helmet_Detection':
            project_root = current_abspath
            break
        else:
            current_abspath = os.path.dirname(current_abspath)
    
    return project_root

PROJECR_ROOT = get_project_root()
os.chdir(PROJECR_ROOT)
sys.path.append(PROJECR_ROOT)


from ultralytics import YOLO
import cv2
import numpy as np
import streamlit as st


def detect_helmet(image):
    # st.write(os.getcwd())
    # print(os.listdir("../runs/detect/train/weights"))
    model = YOLO('./runs/detect/train/weights/best.pt')
    results = model.predict(image)
    annotated_image = results[0].plot()

    has_helmet = any(result.cls.item() == 1 for result in results[0].boxes)
    return annotated_image, has_helmet

def process_image(image):
    img_array = np.frombuffer(image.read(), np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return img_rgb
 