from ultralytics import YOLO

CONFIG_FILE = "../configs/data.yaml"
MODEL_PATH = "../models/fine_tuned_model/weights/best.pt"

if __name__ == "__main__":
    model = YOLO(MODEL_PATH)
    results = model.val(data=CONFIG_FILE)
    print("Validation results:", results)