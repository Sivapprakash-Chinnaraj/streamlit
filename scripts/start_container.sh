#!/bin/bash
set -e

# Define the correct image name and container name
IMAGE_NAME="sivapprakash1634/streamlit-app:latest"
CONTAINER_NAME="sivapprakash1634_streamlit_app"

echo "Pulling the latest Docker image: $IMAGE_NAME..."
docker pull $IMAGE_NAME

# Safety check: Clean up any old container matching your specific name
echo "Cleaning up any old running instances..."
docker stop $CONTAINER_NAME 2>/dev/null || true
docker rm $CONTAINER_NAME 2>/dev/null || true

echo "Starting the new Streamlit container..."
# -d runs in the background; -p maps the ports; --name defines the container name
# We append the Streamlit run command at the end to keep the container running persistently
docker run -d \
  -p 8501:8501 \
  --name $CONTAINER_NAME \
  $IMAGE_NAME \
  streamlit run app.py --server.port=8501 --server.address=0.0.0.0