from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "mysecuretoken123"  # Must match what you enter in Meta

@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge"), 200
        return "Token mismatch", 403

    if request.method == "POST":
        data = request.get_json()
        print("📩 New Lead Notification:", data)
        return "Webhook received", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
