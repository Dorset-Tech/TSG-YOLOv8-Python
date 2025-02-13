import uuid
from datetime import datetime

from flask import jsonify, request

from src.common.constants import OVERLAYED, RAW
from src.services import overlay_service
from src.services.file_service import FileService
from src.services.supabase_service import SupabaseService
from yolo_service.overlay import overlay
from yolo_service.services.config import outputFolder


class OverlayController:
    def __init__(self):
        self.supabase_service = SupabaseService()
        self.file_service = FileService()

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
            custom_file_name = f"{user_id}_{unique_id}_{time_now}.{file_extension}"
            custom_raw_file_path = f"{user_id}/{RAW}/{custom_file_name}"

            # save the file temporarily
            file_path = self.file_service.save_file(file)

            # Upload to Supabase
            self.supabase_service.upload_video(file_path, custom_raw_file_path)

            average_speed = overlay(file_path, file.filename)

            overlayed_file_path = outputFolder + file.filename

            custom_overlayed_file_path = f"{user_id}/{OVERLAYED}/{custom_file_name}"

            self.supabase_service.upload_video(
                overlayed_file_path, custom_overlayed_file_path
            )

            # # Delete the raw file
            self.file_service.delete_file(file_path)
            # # Delete the overlayed file
            self.file_service.delete_file(overlayed_file_path)

            public_raw_url = self.supabase_service.get_public_url(
                custom_raw_file_path,
            )
            public_overlayed_url = self.supabase_service.get_public_url(
                custom_overlayed_file_path,
            )

            return public_raw_url, public_overlayed_url, average_speed


# Create an instance of the controller
overlay_controller = OverlayController()
