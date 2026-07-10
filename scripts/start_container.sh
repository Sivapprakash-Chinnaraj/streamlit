#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
docker pull sivapprakash1634/summa_streamlit:latest

# Run the Docker image as a container
docker run -d -p 8501:8501 --name summa_streamlit_app sivapprakash1634/summa_streamlit:latest streamlit run app.py --server.port=8501 --server.address=0.0.0.0
