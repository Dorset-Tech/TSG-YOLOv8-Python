import os
import uuid
from datetime import datetime
from typing import Any, Dict

from flask import jsonify, request

from src.common.constants import RAW
from src.common.responses import standard_response
from src.services.database_service import DatabaseService
from src.services.supabase_service import SupabaseService


class SupabaseController:
    def __init__(self):
        self.supabase_service = SupabaseService()
        self.database_service = DatabaseService()

    def upload_video(self, user_id: str) -> Dict[str, Any]:
        if request.method == "POST":
            if "file" not in request.files:
                return standard_response(False, "No file part")

            file = request.files["file"]
            if file.filename == "":
                return standard_response(False, "No selected file")

            unique_id = uuid.uuid4().hex[:8]  # Generate a random unique identifier
            time_now = datetime.now().strftime("%Y%m%d%H%M%S")  # Current timestamp

            # Create the custom file name
            custom_file_name = f"{user_id}_{unique_id}_{time_now}_{file.filename}"
            file_path = f"/{RAW}/{custom_file_name}"
            file.save(file_path)

            response = self.supabase_service.upload_video(file_path, "1")
            return standard_response(True, "File uploaded successfully", response)

    def get_all_videos(self, user_id: str) -> Dict[str, Any]:
        if request.method == "GET":
            videos = self.supabase_service.get_all_videos(user_id)
            return standard_response(True, "Videos retrieved successfully", videos)

    def insert_ball_session(
        self,
        user_id: str,
        public_raw_url: str,
        public_overlayed_url: str,
        average_speed: str,
        public_thumbnail_url: str,
    ) -> Dict[str, Any]:
        self.database_service.insert_ball_session(
            user_id,
            public_raw_url,
            public_overlayed_url,
            average_speed,
            public_thumbnail_url,
        )
        return standard_response(
            True,
            "Successfully inserted the ball session",
            {
                "user_id": user_id,
                "public_raw_url": public_raw_url,
                "public_overlayed_url": public_overlayed_url,
                "average_speed": average_speed,
                "public_thumbnail_url": public_thumbnail_url,
            },
        )
        
    def update_upload_status(
        self,
        id: str,
        is_uploading: bool,
        user_id: str,
    ) -> Dict[str, Any]:
        response = self.database_service.insert_or_update_upload_status(id, is_uploading, user_id)
        return response


# Create an instance of the controller using environment variables
supabase_controller = SupabaseController()
