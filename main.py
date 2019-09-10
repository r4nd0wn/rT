import sys, time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import threading
import logging
import socket
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebKitWidgets


HOST = "irc.twitch.tv"
NICK = "r4nd0wn"
PORT = 6667
PASS = "oauth:m9aomgcvgacww3ybeo07m2pu162c0y"
readbuffer = ""
MODT = False
CHANNEL = "r4nd0wn"
username = ""
content = "something gone wrong"

PASSWORD = ("PASS " + PASS + "\r\n")
NICKNAME = ("NICK " + NICK + "\r\n")
CHANNELJOIN = ("JOIN #" + CHANNEL + "\r\n")



try:
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(PASSWORD.encode("utf-8"))
    s.send(NICKNAME.encode("utf-8"))
    s.send(CHANNELJOIN.encode("utf-8"))




except Exception as e:
    print("The error is:")
    print(e)

class Fenster(QWidget):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        self.setGeometry(0, 30, 530, 655)
        self.setFixedSize(530, 655)

        self.setWindowTitle("rT - created by r4nd0wn.")


        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 341, 631))
        self.textEdit.setObjectName("xD")

        self.textEdit.setReadOnly(True)
        self.textEdit.setText("Muhahaha")

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(380, 80, 88, 34))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(allinone(self))

        self.show()



def get_message():
    readbuffer = str(s.recv(1024))
    global message
    message = str(Parse_message(readbuffer))
    time.sleep(0.002)

def allinone(wd):
    wd.textEdit.setText("xD")
    print(wd.textEdit.toPlainText())
    print("am I already here?")


def Parse_message(message):
    username = message.split("!")[0]
    username = username[3:]
    try:
        global content
        tempmessage = message.split("PRIVMSG #" + CHANNEL +" :")[1]
        content = tempmessage[:-5]
        fullmessage = username + ": " + content

        return fullmessage
    except Exception as e:
        print("no real message, unparsed message here:")
        print(message)
        print("The error is: ")
        print(e)




app = QApplication(sys.argv)
window = Fenster()
sys.exit(app.exec_())



