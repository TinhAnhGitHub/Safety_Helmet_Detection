from ultralytics import YOLO
import cv2
import numpy as np
import streamlit as st
import os


def detect_helmet(image):
    st.write(os.getcwd())
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
 