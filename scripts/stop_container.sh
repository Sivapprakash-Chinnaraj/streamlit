#!/bin/bash
set -e

echo "Cleaning up old Streamlit container..."

# Use -q to get ONLY raw IDs, and filter specifically by your image name
CONTAINER_ID=$(sudo docker ps -a -q --filter "ancestor=sivapprakash1634/summa_streamlit:latest")

# Check if a container was actually found before running the delete command
if [ -n "$CONTAINER_ID" ]; then
    echo "Found container(s): $CONTAINER_ID. Force removing..."
    # -f stops the container if it's running and deletes it in one go
    sudo docker rm -f $CONTAINER_ID
else
    echo "No matching containers found. Safe to proceed!"
fi
