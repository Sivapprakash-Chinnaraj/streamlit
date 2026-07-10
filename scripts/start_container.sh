#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
docker pull sivapprakash1634/summa_streamlit:latest

# Run the Docker image as a container
docker run -d -p 8501:8501 sivapprakash1634/summa_streamlit:latest
