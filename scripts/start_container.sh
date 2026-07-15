#!/bin/bash
set -e

echo "Pulling the latest Docker image from Docker Hub..."
docker pull sivapprakash1634/summa_streamlit:latest

# Safety check: Clean up any old container matching your specific name
echo "Cleaning up any old running instances..."
docker stop sivapprakash1634_summa_streamlit 2>/dev/null || true
docker rm sivapprakash1634_summa_streamlit 2>/dev/null || true

echo "Starting the new Streamlit container..."
# -d runs in the background; -p maps the host port to container port; --name defines the container name
docker run -d -p 8501:8501 --name sivapprakash1634_summa_streamlit sivapprakash1634/summa_streamlit:latest