import os

import cv2


class VideoService:
    def __init__(self, directory="public/videos/thumbnails/"):
        self.directory = directory

    def save_thumbnail(self, video_path, custom_file_name):
        video_capture = cv2.VideoCapture(video_path)
        success, frame = video_capture.read()
        if success:
            thumbnail_path = os.path.join(
                self.directory, f"{custom_file_name}_thumbnail.jpg"
            )
            cv2.imwrite(thumbnail_path, frame)
        video_capture.release()
        return thumbnail_path
