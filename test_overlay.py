import os
import sys
import warnings
from optparse import OptionParser
from yolo_service.services.get_pitch_frames import get_pitch_frames
from yolo_service.services.generate_overlay import generate_overlay
from yolo_service.services.config import DEFAULT_VIDEOS_FOLDER, outputPath
from yolo_service.services.utils import NoFramesException

# Ignore warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")

if __name__ == "__main__":
    optparser = OptionParser()
    optparser.add_option(
        "-f",
        "--videos_folder",
        dest="rootDir",
        help="Root directory that contains your pitching videos",
        default=DEFAULT_VIDEOS_FOLDER,
    )
    (options, args) = optparser.parse_args()

    # Store the pitch frames and ball location of each video
    pitch_frames = []

    # Iterate all videos in the folder
    for idx, path in enumerate(sorted(os.listdir(options.rootDir))):
        if not path.endswith(".mp4"):
            continue

        video_path = options.rootDir + "/" + path
        try:
            ball_frames, width, height, fps = get_pitch_frames(video_path)
            pitch_frames.append(ball_frames)
        except NoFramesException as e:
            print(
                f"Error: Sorry we could not get enough baseball detection from the video, video {path} will not be overlayed"
            )  # raise e

    print("Pitch frames len: ", len(pitch_frames))
    if len(pitch_frames):
        generate_overlay(pitch_frames, width, height, fps, outputPath)
