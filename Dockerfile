# Use Python base image
FROM python:3.10

# Install OS-level dependencies (for opencv)
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Set working directory
WORKDIR /app

# Copy everything
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Make the start.sh executable
RUN chmod +x start.sh

# Expose FastAPI (8000) + Streamlit (8501)
EXPOSE 8000
EXPOSE 8501

# Start both servers
CMD ["./start.sh"]