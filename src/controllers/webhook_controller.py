from flask import jsonify, request


class WebhookController:
    def webhook(self):
        if request.method == "POST":
            data = request.get_json()
            print(data)
            return jsonify({"message": "Webhook received"})


# Create an instance of the controller
webhook_controller = WebhookController()
