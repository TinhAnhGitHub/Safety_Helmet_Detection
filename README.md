# Safety_Helmet_Detection
## 1. Project Title

This project uses YOLOv10 for object detection to determine whether construction workers are wearing safety helmets on site.

[Click here to download the dataset](https://drive.google.com/file/d/1twdtZEfcw4ghSZIiPDypJurZnNXzMO7R/view)

[Click here to have more detail about the dataset](https://universe.roboflow.com/dataperson/safety-helmet-dataset-uvh1t)

## 2. Project Description
This project aims to enhance safety on construction sites by using state-of-the-art object detection techniques. We employ the YOLOv10 model to determine whether construction workers are wearing safety helmets. The initial implementation allows the application to process image inputs to identify helmet usage. The future goal is to expand this capability to real-time detection using a webcam, providing continuous monitoring and ensuring compliance with safety regulations.

### Key Features
* **Image-Based Detection**: The current system processes images to detect the presence of safety helmets.
* **High-Accuracy**: By leveraging the YOLOv10 model, the project ensures precise detection, minimizing false positives and negatives.
* **Real-time Detection (Future Goal)**: Plan to integrate real-time video processing through webcam feeds to continuously monitor helmet usage.

### Technology Stack:
* **YOLOv10**: Chosen for its superior speed and accuracy in object detection tasks.
* **Python**: Used as the primary programming language for model implementation and integration.
* **OpenCV**: Utilized for image processing and handling video data in the future expansion.

This project is designed to provide a simple yet practical and efficient solution to enhance safety measures on construction sites by leveraging the latest advancements in computer vision and machine learning.

## 3. How to Install and Run the Project

1. Git clone this project
```sh
git clone https://github.com/TinhAnhGitHub/Safety_Helmet_Detection.git
```

2. Create virtual environment, and activate it
```sh
python -m venv venv
.\venv\Scripts\activate
```

3. Go to folder yolov10, install the requirements and ultralytics
```
pip install -r requirements.txt
```

4. Run the streamlit application, feel free to use the test images in the Safety_Helmet_Dataset
```sh
streamlit run app.py
```
## 4. Demo
[Demo using Streamlit Deployment](https://safetyhelmetdetection-p5d5n6rvnn4kgzf7uopwdk.streamlit.app/)
