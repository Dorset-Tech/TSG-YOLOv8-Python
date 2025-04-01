from flask import Blueprint, request

from src.controllers.overlay_controller import overlay_controller
from src.controllers.supabase_controller import supabase_controller
from src.controllers.webhook_controller import webhook_controller
from src.common.responses import standard_response

routes = Blueprint("routes", __name__)


@routes.route("/", methods=["GET"])
def home():
    return "Hello World!"


@routes.route("/overlay", methods=["POST"])
def overlay_video():
    upload_status = supabase_controller.update_upload_status(
        request.form.get("id"),
        True,
        request.form.get("user_id"),
    )
    
    user_id = request.form.get("user_id")
    (
        custom_raw_file_path,
        custom_overlayed_file_path,
        average_speed,
        thumbnail_path,
    ) = overlay_controller.overlay_video(user_id)

    supabase_controller.insert_ball_session(
        user_id,
        custom_raw_file_path,
        custom_overlayed_file_path,
        average_speed,
        thumbnail_path,
    )
    
    print("upload_status", upload_status)
    
    supabase_controller.update_upload_status(
        upload_status[0]["id"],
        False,
        request.form.get("user_id"),
    )
    
    return standard_response(
        True,
        "Video processed successfully",
        {
            "custom_raw_file_path": custom_raw_file_path,
            "custom_overlayed_file_path": custom_overlayed_file_path,
            "average_speed": average_speed,
            "thumbnail_path": thumbnail_path,
        },
    )


@routes.route("/webhook", methods=["POST"])
def webhook():
    return webhook_controller.webhook()


@routes.route("/get-all-videos/<user_id>", methods=["GET"])
def supabase(user_id):
    return supabase_controller.get_all_videos(user_id)
