#!/bin/bash
set -e

echo "Hunting for existing summa_streamlit containers..."

# Get the container ID if it exists
CONTAINER_ID=$(docker ps -a -q --filter "ancestor=sivapprakash1634/summa_streamlit:latest")

# Check if the string is NOT empty (-n checks for a non-zero string length)
if [ -n "$CONTAINER_ID" ]; then
    echo "Stopping container: $CONTAINER_ID"
    docker stop $CONTAINER_ID || true
    
    echo "Removing container: $CONTAINER_ID"
    docker rm $CONTAINER_ID || true
else
    echo "No running or exited instances of summa_streamlit found. Proceeding cleanly!"
fi
