import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()


machine = TocMachine(
    states=["state1", "state2","state3","state4","state5","state6","state7","state8",
    "state9","state10","state11","state12","state13","state14","state15","state16"],
    transitions=[
        {
            "trigger": "advance",
            "source": "state1",
            "dest": "state2",
            "conditions": "right",
        },
        {
            "trigger": "advance",
            "source": "state2",
            "dest": "state1",
            "conditions": "left",
        },


        {
            "trigger": "advance",
            "source": "state2",
            "dest": "state6",
            "conditions": "down",
        },
        {
            "trigger": "advance",
            "source": "state6",
            "dest": "state2",
            "conditions": "up",
        },


        {
            "trigger": "advance",
            "source": "state6",
            "dest": "state5",
            "conditions": "left",
        },
        {
            "trigger": "advance",
            "source": "state5",
            "dest": "state6",
            "conditions": "right",
        },


        {
            "trigger": "advance",
            "source": "state5",
            "dest": "state9",
            "conditions": "down",
        },
        {
            "trigger": "advance",
            "source": "state9",
            "dest": "state5",
            "conditions": "up",
        },


        {
            "trigger": "advance",
            "source": "state9",
            "dest": "state13",
            "conditions": "down",
        },
        {
            "trigger": "advance",
            "source": "state13",
            "dest": "state9",
            "conditions": "up",
        },


        {
            "trigger": "advance",
            "source": "state6",
            "dest": "state7",
            "conditions": "right",
        },
        {
            "trigger": "advance",
            "source": "state7",
            "dest": "state6",
            "conditions": "left",
        },


        {
            "trigger": "advance",
            "source": "state7",
            "dest": "state11",
            "conditions": "down",
        },
        {
            "trigger": "advance",
            "source": "state11",
            "dest": "state7",
            "conditions": "up",
        },


        {
            "trigger": "advance",
            "source": "state11",
            "dest": "state10",
            "conditions": "left",
        },
        {
            "trigger": "advance",
            "source": "state10",
            "dest": "state11",
            "conditions": "right",
        },


        {
            "trigger": "advance",
            "source": "state10",
            "dest": "state14",
            "conditions": "down",
        },
        {
            "trigger": "advance",
            "source": "state14",
            "dest": "state10",
            "conditions": "up",
        },

        {
            "trigger": "advance",
            "source": "state14",
            "dest": "state15",
            "conditions": "right",
        },
        {
            "trigger": "advance",
            "source": "state15",
            "dest": "state14",
            "conditions": "left",
        },


        {
            "trigger": "advance",
            "source": "state7",
            "dest": "state3",
            "conditions": "up",
        },
        {
            "trigger": "advance",
            "source": "state3",
            "dest": "state7",
            "conditions": "down",
        },

        {
            "trigger": "advance",
            "source": "state3",
            "dest": "state4",
            "conditions": "right",
        },
        {
            "trigger": "advance",
            "source": "state4",
            "dest": "state3",
            "conditions": "left",
        },

        {
            "trigger": "advance",
            "source": "state4",
            "dest": "state8",
            "conditions": "down",
        },
        {
            "trigger": "advance",
            "source": "state8",
            "dest": "state4",
            "conditions": "up",
        },

        {
            "trigger": "advance",
            "source": "state8",
            "dest": "state12",
            "conditions": "down",
        },
        {
            "trigger": "advance",
            "source": "state12",
            "dest": "state8",
            "conditions": "up",
        },

        {
            "trigger": "advance",
            "source": "state12",
            "dest": "state16",
            "conditions": "down",
        },

        {
            "trigger": "go_back",
            "source": "state16",
            "dest": "state1",
        },
        
        {
            "trigger": "advance", 
            "source": ["state1", "state2","state3","state4","state5","state10","state15","state16"], 
            "dest": "state1",
            "conditions": "up",
        },
        {
            "trigger": "advance", 
            "source": ["state1", "state6","state11","state13","state14","state15","state16"], 
            "dest": "state1",
            "conditions": "down",
        },
        {
            "trigger": "advance", 
            "source": ["state2", "state4","state7","state8","state9","state11","state12","state13","state15","state16"], 
            "dest": "state1",
            "conditions": "right",
        },
        {
            "trigger": "advance", 
            "source": ["state1", "state3","state5","state8","state9","state10","state12","state13","state14"], 
            "dest": "state1",
            "conditions": "left",
        },
    ],
    initial="state1",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "Not Entering any State")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
