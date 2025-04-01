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
    
    
    # supabase table: upload_status
    # columns: id, is_uploading, user_id, created_at
    def insert_or_update_upload_status(
        self,
        id: str,
        is_uploading: bool,
        user_id: str,
    ):
        
        # if id exists in the database, update the status
        # else, insert a new record
        if self.supabase.table("upload_status").select("*").eq("id", id).execute().data:
            data = {
                "is_uploading": is_uploading,
            }
            response = self.supabase.table("upload_status").update(data).eq("id", id).execute()
        else:
            created_at = datetime.now().isoformat()
            data = {
                "id": id,
                "is_uploading": is_uploading,
                "user_id": user_id,
                "created_at": created_at,
            }
            response = self.supabase.table("upload_status").insert(data).execute()
        return response
    
