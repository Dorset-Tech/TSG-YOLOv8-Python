# Project Overview

This project trains a YOLO model to detect cricket balls using a dataset from Roboflow and converts the trained model to TFLite format.

## Requirements

- **Python Version**: 3.11.0
  - Download here: [Python 3.11.0](https://www.python.org/downloads/release/python-3110/)
  - Note: Do not install the latest version as it does not support TensorFlow yet.
- **CUDA**: 11.8
  - Download here: [CUDA 11.8](https://developer.nvidia.com/cuda-11-8-0-download-archive)
  -  ```
      pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
      ```

## Running as server

- ```sh
   python main.py
  ```

## VENV
- ```
   python -m venv tsg
   ```
- Activate `.\tsg\Scripts\activate`

## Install Requirements
- ```
   pip install -r requirements.txt
   ```