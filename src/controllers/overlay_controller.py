import uuid
from datetime import datetime

from flask import jsonify, request

from src.common.constants import OVERLAYED, RAW
from src.services import overlay_service
from src.services.file_service import FileService
from src.services.supabase_service import SupabaseService
from src.services.video_service import VideoService
from yolo_service.overlay import overlay
from yolo_service.services.config import outputFolder


class OverlayController:
    def __init__(self):
        self.supabase_service = SupabaseService()
        self.file_service = FileService()
        self.video_service = VideoService()

    def overlay_video(self, user_id: str):
        if request.method == "POST":
            if "file" not in request.files:
                return jsonify({"error": "No file part"})

            file = request.files["file"]
            if file.filename == "":
                return jsonify({"error": "No selected file"})

            # Extract the file extension
            file_extension = file.filename.split(".")[-1]

            unique_id = uuid.uuid4().hex[:8]  # Generate a random unique identifier
            time_now = datetime.now().strftime("%Y%m%d%H%M%S")  # Current timestamp

            # Create the custom file name
            custom_file_name = f"{user_id}_{unique_id}_{time_now}"
            custom_file_name_extension = f"{custom_file_name}.{file_extension}"

            # save the raw video file
            file_path = self.file_service.save_file(file, custom_file_name_extension)

            # Capture the first frame and save it as a thumbnail
            thumbnail_path = self.video_service.save_thumbnail(
                file_path, custom_file_name
            )

            # Overlay the video
            # And get the average speed
            average_speed = overlay(file_path, custom_file_name_extension)

            return (
                file_path,
                (outputFolder + custom_file_name_extension),
                average_speed,
                thumbnail_path,
            )


# Create an instance of the controller
overlay_controller = OverlayController()
