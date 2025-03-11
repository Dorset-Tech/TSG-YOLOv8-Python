#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Run the Python script with xvfb
xvfb-run -a python main.py