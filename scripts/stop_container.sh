#!/bin/bash
set -e

echo "Stopping running Streamlit application..."
docker stop sivapprakash1634_summa_streamlit 2>/dev/null || true
docker rm sivapprakash1634_summa_streamlit 2>/dev/null || true