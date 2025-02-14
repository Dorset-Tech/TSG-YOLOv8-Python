from flask import jsonify


def standard_response(success: bool, message: str, data: dict = None):
    response = {"success": success, "message": message, "data": data if data else {}}
    return jsonify(response)
