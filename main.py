from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from ultralytics import YOLO
from PIL import Image
import shutil
import uuid
import os
import mimetypes

app = FastAPI()

# Allow communicate with frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load pre-trained model
model = YOLO("dates_fruit_model.pt")

# Ensure the folder holds images exists
STATIC_IMAGE_DIR = "static/images"
os.makedirs(STATIC_IMAGE_DIR, exist_ok=True)


app.mount("/images", StaticFiles(directory=STATIC_IMAGE_DIR), name="images")


@app.get("/")
def read_root():
    return {"message": "Welcome to Saudi Date Classifier API"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Save temp file
    mime_type = file.content_type or "image/jpeg"
    extension = mimetypes.guess_extension(mime_type) or ".jpg"
    temp_filename = f"temp_{uuid.uuid4()}{extension}"
    
    with open(temp_filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    print("📥 Received image:", temp_filename)

    # Predict an image
    results = model(temp_filename)
    names = results[0].names
    boxes = results[0].boxes

    # classify the class
    if boxes and boxes.cls.numel() > 0:
        top_class_index = int(boxes.cls[0].item())
        predicted_class = names[top_class_index]
    else:
        predicted_class = "Unknown"

    print("🧠 Predicted class:", predicted_class)

    
    output_filename = f"{uuid.uuid4()}.jpg"
    output_path = os.path.join(STATIC_IMAGE_DIR, output_filename)

    plotted = results[0].plot()
    Image.fromarray(plotted).save(output_path)
    print("✅ Saved processed image at:", output_path)

    # remove it
    os.remove(temp_filename)


    return {
        "class": predicted_class,
        "image_path": f"/images/{output_filename}"
    }