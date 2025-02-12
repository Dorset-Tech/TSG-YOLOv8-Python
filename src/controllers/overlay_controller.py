from flask import jsonify, request

from src.services import overlay_service
from src.services.file_service import FileService
from yolo_service.overlay import overlay


class OverlayController:
    def __init__(self):
        self.file_service = FileService()

    def overlay_video(self):
        if request.method == "POST":
            if "file" not in request.files:
                return jsonify({"error": "No file part"})

            file = request.files["file"]
            if file.filename == "":
                return jsonify({"error": "No selected file"})

            file_path = self.file_service.save_file(file)

            overlay(file_path)

            return jsonify({"message": "Video overlayed successfully"})


# Create an instance of the controller
overlay_controller = OverlayController()
