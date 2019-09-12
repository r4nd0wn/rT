from irc import IRC
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from requests import Session
from threading import Thread
from time import sleep
from irc import IRC
import datetime
import random
import hashlib


username = "rTsFetcher"
oauth = "oauth:efhn2jfl093dyrdv94rd91vad3zdoy"
channel = "thiseguy"
chat1 = IRC(channel, username, oauth)
chat1.connect()
chat1.allow_Tags()
userlist = []
colorid = []




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
        response = chat1.get_splitted_message()

        if response:
            new_messages.append(response)


thread = Thread(target=fetch_new_messages, daemon=True)
thread.start()

def display_new_messages():
    while new_messages:
        message = new_messages.pop(0)
        prefix = """<b><span style="color: """ + getUserColor(message[1]) + """;">"""
        postfix = "</span></b>"
        print(message)
        text_area.appendHtml("<small>" + message[0] + "</small>" + " " + prefix + message[1] + postfix + ": " + message[2])

def send_message():
    try:
        chat1.send(message.text())
        timestamp = datetime.datetime.now()
        fullmessage = "<small>" + chat1.timestamp() + "</small>" + " - " + """<b><span style="color: #00BFFF;">""" + username + "</span>" + ": " + "</b>" + message.text()

        text_area.appendHtml(fullmessage)
        message.clear()

    except Exception as e:
        print(e)

def getUserColor(usr):
    color = "#" + str(hashlib.sha512(usr.encode("UTF-8")).hexdigest())[0:6]
    return color

def random_color():
    color = "#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    return color

def create_user(username):
    userlist.append(username)
    colorid.insert(userlist.index(username), random_color())
message.returnPressed.connect(send_message)
timer = QTimer()
timer.timeout.connect(display_new_messages)
timer.start(100)

app.exec_()
