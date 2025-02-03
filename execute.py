import ultralytics
from ultralytics import YOLO

print(f"Ultralytics")

model = YOLO("yolov8n.yaml")

model.train(data = "data.yaml", epochs = 1)