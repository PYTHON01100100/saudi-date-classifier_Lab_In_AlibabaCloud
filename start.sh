#!/bin/bash

# Start FastAPI (as background)
uvicorn main:app --host 0.0.0.0 --port 8000 &

# Start Streamlit
streamlit run frontend.py --server.port 8501 --server.address 0.0.0.0