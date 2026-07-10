#!/bin/bash
set -e

echo "Hunting for existing summa_streamlit containers..."

# 1. Safely find the container ID using Docker's native filtering matching the image name
CONTAINER_ID=$(sudo docker ps -a -q --filter "ancestor=sivapprakash1634/summa_streamlit:latest")

# 2. If a container ID was found, stop and delete it cleanly
if [ -not -z "$CONTAINER_ID" ]; then
    echo "Stopping container: $CONTAINER_ID"
    docker stop $CONTAINER_ID
    
    echo "Removing container: $CONTAINER_ID"
    sudo docker rm $CONTAINER_ID
else
    echo "No running or exited instances of summa_streamlit found. Proceeding cleanly!"
fi
