import torch
import ultralytics
from ultralytics import YOLO

def main():
    # Check if GPU is available
    if torch.cuda.is_available():
        print("GPU is available. Training on GPU.")
        device = torch.device('cuda')
    else:
        print("GPU is not available. Training on CPU.")
        device = torch.device('cpu')

    print("Ultralytics")

    # Load the YOLO model
    model = YOLO("yolov8n.yaml")

    # Train the model
    model.train(data="data.yaml", epochs=10, device=device)

if __name__ == "__main__":
    main()