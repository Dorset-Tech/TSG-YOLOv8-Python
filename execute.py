import torch
import torchvision
from ultralytics import YOLO


def main():
    print("PyTorch version:", torch.__version__)
    print("Torchvision version:", torchvision.__version__)
    print("CUDA available:", torch.cuda.is_available())
    print("CUDA version:", torch.version.cuda)
    print("Number of GPUs:", torch.cuda.device_count())
    # Check if GPU is available
    if torch.cuda.is_available():
        print("GPU is available. Training on GPU.")
        device = torch.device("cuda")
    else:
        print("GPU is not available. Training on CPU.")
        device = torch.device("cpu")
    return
    # Load the YOLO model
    model = YOLO("yolov8n.yaml")

    # Train the model
    model.train(data="data.yaml", epochs=500, device=device)


if __name__ == "__main__":
    main()
