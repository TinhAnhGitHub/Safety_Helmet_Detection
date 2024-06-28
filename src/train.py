from ultralytics import YOLO
import torch

def main():
    model_path = "../models/yolov10n.pt"
    model = YOLO(model_path)
    
    YAML_PATH = "../Safety_Helmet_Dataset/data.yaml"
    EPOCHS = 50
    IMG_SIZE = 640
    BATCH_SIZE = 2
    DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
    
    model.train(
        data=YAML_PATH,
        epochs=EPOCHS,
        imgsz=IMG_SIZE,
        batch=BATCH_SIZE,
        device=DEVICE
    )
    # you could access the model in runs/detect/train/weights/best.pt
if __name__ == "__main__":
    main()
