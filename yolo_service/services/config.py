from datetime import datetime

# Basic conf
# DEFAULT_VIDEOS_FOLDER = "./videos/lot"
VIDEOS_ROOT = "yolo_service/videos/"
DEFAULT_VIDEOS_FOLDER = VIDEOS_ROOT

modelPath = (
    "yolo_service/models/best_300.pt"
    # "runs/detect/train/weights/epoch24.pt"
)
# Detect config
PADDING = 100  # maybe should be % of video height 10 = 108 with full hd 1920x1080
iou_threshold = 0.2
score_threshold = 0.5

# SORT config
tracker_min_hits = 4
tracker_iou_threshold = 0.1
max_age = 14

distance_threshold = 100

outputFolder = "yolo_service/predictions/"
f = f"{datetime.today().strftime('%H%M')}_"
e = f".mp4"
outputPath = outputFolder + (
    ## spacing
    f"{f}{PADDING}_{iou_threshold}_{score_threshold}_{tracker_min_hits}_{tracker_iou_threshold}_{max_age}{e}"
)

# Overlay config
fps_percentage = 0.95  # 1 = full fps, 0.5 = half
base_frame_weight = 0.55  # orig 0.55

ball_size = 10  # TODO count from bbox heights
line_thickness = round(2 * ball_size)
trajectory_weight = 0.7  # orig 0.7 # line opacity

before_frames = 20
after_frames = 100
