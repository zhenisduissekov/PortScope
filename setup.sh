#!/bin/bash

# Create .streamlit directory if it doesn't exist
mkdir -p .streamlit

# Create config.toml with recommended settings
echo '[scheduler]
pythonVersion = "3.10"

[server]
headless = true
port = $PORT
enableCORS = false
' > .streamlit/config.toml

# Install Python dependencies with --prefer-binary
pip install --prefer-binary -r requirements.txt
