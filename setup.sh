#!/bin/bash
python3 -m venv translation_demo_venv

# Activate the virtual environment
source myenv/bin/translation_demo_venv

# Install dependencies from requirements.txt
pip install -r requirements.txt

# logging into gcloud to get translation api to work
gcloud auth application-default login
