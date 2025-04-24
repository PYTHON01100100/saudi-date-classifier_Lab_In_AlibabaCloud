# 🌴 Saudi Date Classifier (YOLOv8 + FastAPI + Streamlit + Docker + Alibaba Cloud)

A lightweight and fully containerized **YOLOv8 segmentation-based classifier** to detect and classify Saudi date types using AI.

---

## 🖼️ Example Predictions

<p align="center">
  <img src="/static/images/983e6103-05b6-4cbc-be9b-bbcfbe713930.jpg" alt="Sokari Prediction" width="300"/>
  <img src="/static/images/67b083d5-490d-4a71-aada-640f7261aa25.jpg" alt="Medjool Prediction" width="300"/>
</p>

<p align="center">
  <i>Examples of YOLOv8 Segmentation Output – Sokari & Medjool</i>
</p>

---

## 🚀 Tech Stack
- ⚙️ **YOLOv8-X Segmentation** – High-accuracy image segmentation  
- ⚡ **FastAPI** – Backend API for model prediction  
- 🎨 **Streamlit** – Interactive frontend UI  
- 🐳 **Docker** + **Docker Compose** – Easy containerization & service orchestration  
- ☁️ **ECS** – Cloud deployment and testing
- 🪣 **OSS** – To upload Model to OOS then download it on ecs on root fold  

---

## 🎯 Project Goal
My goal was to learn and experiment with:
- Deploying real segmentation models using **ECS + Docker**
- Building full-stack AI apps (backend + frontend)
- Using Docker Compose to coordinate services
- Validating deployment on cloud environments (ECS)
- Training on Alibaba cloud platform

---

## 🌐 Deployment

This project was successfully deployed and tested on an **ECS instance** using Docker Compose. 
Although the instance was temporary (~30 mins 😅), it confirmed the project’s cloud readiness and real-world functionality.

> ✅ FastAPI and Streamlit both worked smoothly over the public IP.

---

## ⚠️ Limitations
To get the best predictions:
- 📸 Upload **only one date fruit per image**
- ☁️ Use a **clean and plain background** (preferably white)
- 🚫 Avoid distractions (cups, hands, etc.)
- 💡 Ensure good lighting

---

## 📷 Supported Classes
- `Sokari`  
- `Sugaey`  
- `Ajwa`  
- `Medjool`  

---

## 🔗 Model File

⬇️ Download the trained model and place it in the root as:  
`date_fruit_model.pt`

[📥 Download from Google Drive](https://drive.google.com/file/d/1ZPvdR7CkQm37Ix3xho-aF_kFAoeL9uX8/view)

---

## 📦 Running the Project (Docker) ON ECS

```bash
BEFORE:
- upload Model on OSS
-Create an ECS Instance
-Install Docker on ECS and verify it works
-
# 1. Clone the repo
git clone https://github.com/DH99MJ/saudi-date-classifier.git
cd saudi-date-classifier

# 2. Build & run using Docker Compose
docker compose up --build


# 3. CTRL+C when it's installed
•	docker ps -a # to run it
•	take port from URL: http://0.0.0.0:8501
•	in Security Group you have to add rule 8501
•	link public IP with port like http://0.0.0.0:8501 #Note be sure docker Container
```

## ⚠️ Limitations
To get the best predictions:
- 📸 Upload **only one date fruit per image**
- ☁️ Use a **clean and plain background** (preferably white)
- 🚫 Avoid distractions (cups, hands, etc.)
- 💡 Ensure good lighting



