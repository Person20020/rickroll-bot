from dotenv import load_dotenv
from flask import Flask, request, jsonify
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

load_dotenv()

app = Flask(__name__)

client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))


@app.route('/')
def index():
    return "Rickroll Bot is running!"

@app.route('/slack/events', methods=['POST'])
def slack_events():
    data = request.json
    if "challenge" in data:
        return jsonify({"challenge": data["challenge"]})
    
    if "event" in data:
        event = data["event"]
        if event.get("type") == "message" and "subtype" not in event:
            channel_id = event["channel"]
            user_id = event["user"]
            text = event["text"]

            if "rickroll" in text.lower():
                try:
                    client.chat_postMessage(
                        channel=channel_id,
                        text="""
                            :rickdetailed-00::rickdetailed-01::rickdetailed-02::rickdetailed-03::rickdetailed-04::rickdetailed-05::rickdetailed-06::rickdetailed-07::rickdetailed-08::rickdetailed-09:\n:rickdetailed-10::rickdetailed-11::rickdetailed-12::rickdetailed-13::rickdetailed-14::rickdetailed-15::rickdetailed-16::rickdetailed-17::rickdetailed-18::rickdetailed-19:\n:rickdetailed-20::rickdetailed-21::rickdetailed-22::rickdetailed-23::rickdetailed-24::rickdetailed-25::rickdetailed-26::rickdetailed-27::rickdetailed-28::rickdetailed-29:\n:rickdetailed-30::rickdetailed-31::rickdetailed-32::rickdetailed-33::rickdetailed-34::rickdetailed-35::rickdetailed-36::rickdetailed-37::rickdetailed-38::rickdetailed-39:\n:rickdetailed-40::rickdetailed-41::rickdetailed-42::rickdetailed-43::rickdetailed-44::rickdetailed-45::rickdetailed-46::rickdetailed-47::rickdetailed-48::rickdetailed-49:\n:rickdetailed-50::rickdetailed-51::rickdetailed-52::rickdetailed-53::rickdetailed-54::rickdetailed-55::rickdetailed-56::rickdetailed-57::rickdetailed-58::rickdetailed-59:\n:rickdetailed-60::rickdetailed-61::rickdetailed-62::rickdetailed-63::rickdetailed-64::rickdetailed-65::rickdetailed-66::rickdetailed-67::rickdetailed-68::rickdetailed-69:\n:rickdetailed-70::rickdetailed-71::rickdetailed-72::rickdetailed-73::rickdetailed-74::rickdetailed-75::rickdetailed-76::rickdetailed-77::rickdetailed-78::rickdetailed-79:
                        """
                    )
                except SlackApiError as e:
                    print(f"Error posting message: {e.response['error']}")
    return jsonify({"status": "ok"})
                    

if __name__ == '__main__':
    app.run(port=int(os.getenv("PORT", 5000)), debug=True)