from ultralytics import YOLO

CONFIG_FILE = "../configs/data.yaml"
MODEL_WEIGHTS = "yolov8n.pt"
OUTPUT_DIR = "../models"

if __name__ == "__main__":
    model = YOLO(MODEL_WEIGHTS)
    model.train(
        data=CONFIG_FILE,
        epochs=50,
        batch=16,
        imgsz=640,
        save=True,
        project=OUTPUT_DIR,
        name="fine_tuned_model"
    )