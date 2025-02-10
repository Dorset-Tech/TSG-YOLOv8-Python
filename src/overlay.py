from src.services.get_pitch_frames import get_pitch_frames
from src.services.generate_overlay import generate_overlay
from src.services.config import outputPath
from src.services.utils import NoFramesException

def overlay(file_path):
    try:
        ball_frames, width, height, fps = get_pitch_frames(file_path)
        pitch_frames = [ball_frames]
        generate_overlay(pitch_frames, width, height, fps, outputPath)
        print("Video overlayed successfully")
    except NoFramesException as e:
        print(
            f"Error: Sorry we could not get enough baseball detection from the video, video {file_path} will not be overlayed"
        )  # raise e
