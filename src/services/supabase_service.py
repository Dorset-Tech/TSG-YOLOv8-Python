import os
import tempfile
from io import BytesIO
from typing import Dict, List

from dotenv import load_dotenv
from supabase import Client, create_client

# Load environment variables from .env file
load_dotenv()


class SupabaseService:
    def __init__(self):
        self.client: Client = create_client(
            os.getenv("SUPABASE_URL"),
            os.getenv("SECRET_KEY"),
        )

    def upload_video(self, file_path, raw_file_path):
        with open(file_path, "rb") as file:
            response = self.client.storage.from_(
                os.getenv("SUPABASE_BUCKET_NAME")
            ).upload(raw_file_path, file)
        return response

    def get_public_url(self, file_path: str) -> str:
        public_url = self.client.storage.from_(
            os.getenv("SUPABASE_BUCKET_NAME")
        ).get_public_url(file_path)
        return public_url

    def get_all_videos(self, user_id: str) -> List[Dict[str, str]]:
        bucket_name = os.getenv("SUPABASE_BUCKET_NAME")
        response = self.client.storage.from_(bucket_name).list(user_id)
        videos = []
        for file in response:
            public_url = self.client.storage.from_(bucket_name).get_public_url(
                user_id + "/" + file["name"]
            )
            videos.append({"id": file["id"], "url": public_url})
        return videos
