from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn
import cv2
import numpy as np
from ultralytics import YOLO


app = FastAPI()

# Load the trained YOLO model
MODEL_PATH = "../models/saved_models/best.pt"
model = YOLO(MODEL_PATH)

# Define a response model for prediction
class PredictionResponse(BaseModel):
    filename: str
    predictions: list

@app.post("/predict", response_model=PredictionResponse)
async def predict(file: UploadFile = File(...)):
    try:
        # Read the uploaded file
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Run YOLO inference
        results = model.predict(source=image, conf=0.25, save=False, verbose=False)

        # Process results
        predictions = []
        for box in results[0].boxes:
            predictions.append({
                "class": model.names[int(box.cls)],
                "confidence": float(box.conf),
                "coordinates": box.xyxy.tolist()  
            })

        return PredictionResponse(filename=file.filename, predictions=predictions)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get("/")
def home():
    return {"message": "Welcome to YOLO Defective Image Detection API!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)