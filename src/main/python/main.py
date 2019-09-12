from irc import IRC
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from requests import Session
from threading import Thread
from time import sleep
from irc import IRC
import datetime

username = "rTsFetcher"
oauth = "oauth:efhn2jfl093dyrdv94rd91vad3zdoy"
channel = "r4nd0wn"
chat1 = IRC(channel, username, oauth)
chat1.connect()



app = QApplication([])
text_area = QPlainTextEdit()
text_area.setFocusPolicy(Qt.NoFocus)
message = QLineEdit()
layout = QVBoxLayout()
layout.addWidget(text_area)
layout.addWidget(message)
window = QWidget()
window.setLayout(layout)
window.show()


new_messages = []
def fetch_new_messages():
    while True:
        response = chat1.get_parsed_message()
        
        if response:
            new_messages.append(response)

thread = Thread(target=fetch_new_messages, daemon=True)
thread.start()

def display_new_messages():
    while new_messages:
        text_area.appendPlainText(new_messages.pop(0))

def send_message():
    try:
        chat1.send(message.text())
        timestamp = datetime.datetime.now()
        fullmessage = "<small>" + chat1.timestamp() + "</small>" + " - " + """<b><span style="color: #00BFFF;">""" + username + "</span>" + ": " + "</b>" + message.text()

        text_area.appendHtml(fullmessage)
        message.clear()

    except Exception as e:
        print(e)


message.returnPressed.connect(send_message)
timer = QTimer()
timer.timeout.connect(display_new_messages)
timer.start(1000)

app.exec_()
