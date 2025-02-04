import torch
import ultralytics
from ultralytics import YOLO

# Check if GPU is available
if torch.cuda.is_available():
    print("GPU is available. Training on GPU.")
else:
    print("GPU is not available. Training on CPU.")

print(f"Ultralytics")

model = YOLO("yolov8n.yaml")

model.train(data = "data.yaml", epochs = 30)