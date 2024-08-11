from flask import Flask, request, jsonify
from slack_sdk.web import WebClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Initialize Slack client
slack_token = os.environ.get("SLACK_BOT_TOKEN")
client = WebClient(token=slack_token)

@app.route("/slack/slash", methods=["POST"])
def slash_command():
    user_id = request.form.get("user_id")
    if not user_id:
        return jsonify(
            response_type="ephemeral",
            text="User ID not found"
        )
    
    response_text = f"Your Slack ID is: {user_id}"

    return jsonify(
        response_type="ephemeral",
        text=response_text
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
