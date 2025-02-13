from yolo_service.services.config import outputFolder
from yolo_service.services.generate_overlay import generate_overlay
from yolo_service.services.get_pitch_frames import get_pitch_frames
from yolo_service.services.utils import NoFramesException


def overlay(file_path, file_name):
    try:
        ball_frames, width, height, fps = get_pitch_frames(file_path)
        pitch_frames = [ball_frames]

        if len(pitch_frames):
            return generate_overlay(
                pitch_frames, width, height, fps, (outputFolder + file_name)
            )
        else:
            raise NoFramesException("No frames")

    except NoFramesException as e:
        print(
            f"Error: Sorry we could not get enough baseball detection from the video, video {file_path} will not be overlayed"
        )  # raise e
