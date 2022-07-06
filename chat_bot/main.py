from flask import Flask, request, render_template
from datetime import datetime
import json


app = Flask(__name__)
MESSAGES_FILE_NAME = "messages_file.json"


def load_messages():
    with open(MESSAGES_FILE_NAME, "r") as message_file:
        data = json.load(message_file)
        return data["messages"]


all_messages = load_messages()


def save_messages():
    with open(MESSAGES_FILE_NAME, "w") as message_file:
        data = {
            "messages": all_messages
        }
        json.dump(data, message_file)


def add_message(sender, text):
    new_message = {
        "text": text,
        "sender": sender,
        "time": datetime.now().strftime("%H:%M")
    }
    all_messages.append(new_message)
    save_messages()


def print_all():
    for msg in all_messages:
        print(f'[{msg["text"]}]: {msg["sender"]} / {msg["time"]}')


print_all()


@app.route("/")
def main_page():
    return "<h1>Hello! Welcome to ChatServer</h1>"


@app.route("/get_messages")
def get_messages():
    return {"messages": all_messages}


@app.route("/send_message")
def send_message():
    name = request.args["name"]
    text = request.args["text"]
    add_message(name, text)
    return "ok"


@app.route("/chat")
def chat():
    return render_template("form.html")


app.run()
