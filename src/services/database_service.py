import os
from datetime import datetime

from supabase import Client, create_client


class DatabaseService:
    def __init__(self):
        self.supabase: Client = create_client(
            os.getenv("SUPABASE_URL"),
            os.getenv("SECRET_KEY"),
        )

    def insert_ball_session(
        self,
        user_id: str,
        public_raw_url: str,
        public_overlayed_url: str,
        average_speed: str,
        public_thumbnail_url: str,
    ):
        created_at = datetime.now().isoformat()
        data = {
            "user_id": user_id,
            "public_raw_url": public_raw_url,
            "public_overlayed_url": public_overlayed_url,
            "speed": average_speed,
            "public_thumbnail_url": public_thumbnail_url,
            "created_at": created_at,
        }
        response = self.supabase.table("ball_session").insert(data).execute()
        return response
