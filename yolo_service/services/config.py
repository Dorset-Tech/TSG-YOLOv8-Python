from datetime import datetime

# Basic conf
VIDEOS_ROOT = "yolo_service/videos/"
DEFAULT_VIDEOS_FOLDER = VIDEOS_ROOT

modelPath = (
    "yolo_service/models/best_300.pt"
    # "runs/detect/train/weights/epoch24.pt"
)
# Detect config
video_height = 1280  # Example value, replace with actual video height
# PADDING = int(0.1 * video_height)  # 10% of video height
PADDING = 100  # 10% of video height
iou_threshold = 0.2
score_threshold = 0.4

# SORT config
tracker_min_hits = 2
tracker_iou_threshold = 0.1
max_age = 20

distance_threshold = 100

outputFolder = "yolo_service/predictions/"
f = f"{datetime.today().strftime('%H%M')}_"
e = f".mp4"

# Overlay config
fps_percentage = 1  # 1 = full fps, 0.5 = half
base_frame_weight = 0.3  # orig 0.55

ball_size = 10  # TODO count from bbox heights
line_thickness = round(2 * ball_size)
trajectory_weight = 0.9  # orig 0.7 # line opacity

before_frames = 20
after_frames = 100
