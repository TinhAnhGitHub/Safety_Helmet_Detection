# Safety_Helmet_Detection
## 1. Project Title

This project uses YOLOv10 for object detection to determine whether construction workers are wearing safety helmets on site.

[Click here to download the dataset](https://drive.google.com/file/d/1twdtZEfcw4ghSZIiPDypJurZnNXzMO7R/view)

[Click here to have more details about the dataset](https://universe.roboflow.com/dataperson/safety-helmet-dataset-uvh1t)

[Click here to download the model's weight](https://drive.google.com/file/d/1jwxJkd9bAY2TGapzkvvGmM_Uop-XehS_/view?usp=sharing)



## 2. Project Description
This project aims to enhance safety on construction sites by using state-of-the-art object detection techniques. We employ the YOLOv10 model to determine whether construction workers are wearing safety helmets.

### Key Features
* **Image-Based Detection**: The current system processes images to detect the presence of safety helmets.
* **High-Accuracy**: By leveraging the YOLOv10 model, the project ensures precise detection, minimizing false positives and negatives.

### Technology Stack:
* **YOLOv10**: 
* **Pytorch**: 
* **OpenCV**

This project is designed to provide a simple yet practical and efficient solution to enhance safety measures on construction sites by leveraging the latest advancements in computer vision and machine learning.

## 3. Folder Structure and Installation
```txt
Safety_Helmet_Detection/
├── .gitignore
├── app.py
├── README.md
├── requirements.txt
├── sonar-project.properties
├── tmp.py
├── .github/
│   ├── workflows/
│   │   ├── build.yml
├── models/ 
│   ├── best.pt
├── src/
│   ├── detect.py
```

- Download the model's weights, create a folder in the Safety_Helmet_Detection repo, name it `models`, and put the weight in that folder 


## 3. How to Install and Run the Project

1. Git clone this project
```sh
git clone https://github.com/TinhAnhGitHub/Safety_Helmet_Detection.git
```

2. Create a virtual environment, and activate it
```sh
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies
```
pip install -r requirements.txt
```




4. Run the streamlit application, don't forget to create the `models` and download the weight
```sh
streamlit run app.py
```
