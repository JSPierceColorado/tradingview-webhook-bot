from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Webhook listener is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        raw_data = request.data.decode("utf-8")
        json_data = request.get_json(force=True, silent=True)

        print("🛰️ Raw Webhook Received:", raw_data, flush=True)
        print("✅ Parsed JSON:", json_data, flush=True)

        if json_data is None:
            return jsonify({"status": "error", "message": "No JSON received"}), 400

        return jsonify({
            "status": "success",
            "message": "Webhook received and parsed.",
            "data": json_data
        }), 200

    except Exception as e:
        print("❌ Error handling webhook:", str(e), flush=True)
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
