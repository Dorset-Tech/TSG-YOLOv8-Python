from flask import Flask, request, jsonify
from src.overlay import overlay

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Hello World!"

# Send a POST request to the server with the video file
@app.route("/overlay", methods=["POST"])
def overlay_video():
    if request.method == "POST":
        # Check if the post request has the file part
        if "file" not in request.files:
            return jsonify({"error": "No file part"})

        file = request.files["file"]
        if file.filename == "":
            return jsonify({"error": "No selected file"})

        # Save the file to the server
        file_path = "src/videos/" + file.filename
        file.save(file_path)

        # Overlay the video
        overlay(file_path)

        return jsonify({"message": "Video overlayed successfully"})

if __name__ == "__main__":
    app.run(debug=True)