# 🌴 Saudi Date Classifier (Segmentation + FastAPI + Streamlit)

This project is a lightweight **YOLOv8 segmentation-based classifier** built to detect and classify Saudi dates using AI.

## 🚀 Tech Stack
- **YOLOv8-X Segmentation** – For high-accuracy image segmentation
- **FastAPI** – Backend API for model prediction
- **Streamlit** – Interactive frontend for user upload and display
- **Docker** – For easy containerization and deployment

## 🔍 Project Goal
My goal was to learn and experiment with:
- Deploying segmentation models
- Building full-stack AI apps
- Using Docker and preparing for AWS deployment

## ⚠️ Limitations
To ensure maximum accuracy, the model performs best when:
- The image contains **only one date fruit**
- Background is **clean and plain** (preferably white)
- No additional items (coffee cups, hands, etc.) are present
- **Good lighting** and high-resolution images are used

## 📷 Supported Classes
- `Sokari`
- `Sugaey`
- `Ajwa`
- `Medjool`

## 🔗 Model File

Download the model manually from this Google Drive link and place it in the project root as: dates_fruit_model.pt

URL = https://drive.google.com/file/d/1ZPvdR7CkQm37Ix3xho-aF_kFAoeL9uX8/view

## 📦 Running the Project

```bash
# Build the Docker image
docker build -t date-classifier .

# Run the container
docker run -p 8000:8000 -p 8501:8501 date-classifier

# saudi-date-classifier
