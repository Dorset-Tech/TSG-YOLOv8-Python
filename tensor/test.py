import cv2
from ultralytics import YOLO

# Load the YOLO model
model = YOLO("best_300.pt")


# Function to process video and debug confidence
def process_video(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Perform inference on the frame
        results = model(frame)

        # Debug confidence
        for result in results:
            for detection in result.boxes:
                confidence = detection.conf.item()

                print(f"Confidence: {confidence}")
                # Ensure detection.xyxy returns four values
                x1, y1, x2, y2 = (
                    detection.xyxy[0, 0].item(),
                    detection.xyxy[0, 1].item(),
                    detection.xyxy[0, 2].item(),
                    detection.xyxy[0, 3].item(),
                )
                label = f"{detection.cls} {confidence:.2f}"
                cv2.rectangle(
                    frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2
                )
                cv2.putText(
                    frame,
                    label,
                    (int(x1), int(y1) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, 255, 0),
                    2,
                )

        # Display the frame
        cv2.imshow("Video", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


# Path to the video file
video_path = "videos/4.mp4"

# Process the video
process_video(video_path)
