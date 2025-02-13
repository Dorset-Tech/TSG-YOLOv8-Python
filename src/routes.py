from flask import Blueprint, request

from src.controllers.overlay_controller import overlay_controller
from src.controllers.supabase_controller import supabase_controller
from src.controllers.webhook_controller import webhook_controller

routes = Blueprint("routes", __name__)


@routes.route("/", methods=["GET"])
def home():
    return "Hello World!"


@routes.route("/overlay", methods=["POST"])
def overlay_video():
    user_id = request.form.get("user_id")
    custom_raw_file_path, custom_overlayed_file_path, average_speed = (
        overlay_controller.overlay_video(user_id)
    )
    return supabase_controller.insert_ball_session(
        user_id,
        custom_raw_file_path,
        custom_overlayed_file_path,
        average_speed,
    )


@routes.route("/webhook", methods=["POST"])
def webhook():
    return webhook_controller.webhook()


@routes.route("/get-all-videos/<user_id>", methods=["GET"])
def supabase(user_id):
    return supabase_controller.get_all_videos(user_id)
