#!/bin/bash
set -e

# Target the exact container name used in your start script
CONTAINER_NAME="sivapprakash1634_streamlit_app"

echo "Stopping and removing the Streamlit container: $CONTAINER_NAME..."

# Safely stop and remove the container if it exists, without throwing errors
docker stop $CONTAINER_NAME 2>/dev/null || true
docker rm $CONTAINER_NAME 2>/dev/null || true

echo "Cleanup phase completed successfully!"