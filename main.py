import os

from flask import Flask, send_from_directory

from src.routes import routes

app = Flask(__name__)
app.register_blueprint(routes)

# Absolute path to the public directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PUBLIC_FOLDER = os.path.join(BASE_DIR, "public")


@app.route("/public/<path:filename>")
def serve_file(filename):
    return send_from_directory(PUBLIC_FOLDER, filename)


if __name__ == "__main__":
    # app.run(debug=True, port=9999, host="192.168.1.10")
    app.run(debug=True, port=9999, host="0.0.0.0")
