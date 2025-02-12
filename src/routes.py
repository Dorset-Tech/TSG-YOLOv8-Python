from flask import Blueprint

from src.controllers.overlay_controller import overlay_controller
from src.controllers.webhook_controller import webhook_controller

routes = Blueprint("routes", __name__)


@routes.route("/", methods=["GET"])
def home():
    return "Hello World!"


@routes.route("/overlay", methods=["POST"])
def overlay_video():
    return overlay_controller.overlay_video()


@routes.route("/webhook", methods=["POST"])
def webhook():
    return webhook_controller.webhook()
