#!/bin/bash
python3 -m venv jamcity_venv

# Activate the virtual environment
source myenv/bin/jamcity_venv

# Install dependencies from requirements.txt
pip install -r requirements.txt

# logging into gcloud to get translation api to work
gcloud auth application-default login
