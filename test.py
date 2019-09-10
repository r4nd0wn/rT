import sys, time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import threading
from _thread import start_new_thread
import multiprocessing
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

s = socket.socket()


class Fenster(QWidget):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
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
        self.pushButton.clicked.connect(self.starter)
        self.textEdit.moveCursor(QtGui.QTextCursor.End)
        self.setsocket()
        self.show()

    def writer(self, mess):
        self.textEdit.insertPlainText(mess)

    def starter(self):
        try:

            t1 = multiprocessing.Process(target=self.fetch)
            t1.start()
            t1.join()
        except Exception as e:
            print(e)
        print("Im not hanging on that thread")
    def setsocket(self):
        try:
            s.connect((HOST, PORT))
            s.send(PASSWORD.encode("utf-8"))
            s.send(NICKNAME.encode("utf-8"))
            s.send(CHANNELJOIN.encode("utf-8"))

        except Exception as e:
            print("The error is:")
            print(e)

    def Parse_message(self, message):
        try:
            username = message.split("!")[0]
            username = username[3:]
            tempmessage = message.split("PRIVMSG #" + CHANNEL +" :")[1]
            content = tempmessage[:-5]
            return username + ": " + content
        except Exception as e:
            print("no real message, unparsed message here:")
            print(message)
            print(e)

    def fetch(self):
        print("printmeatestmessage")
        readbuffer = str(s.recv(1024))
        message = self.Parse_message(readbuffer)
        print(message)
        self.textEdit.insertPlainText("testtest")
        time.sleep(5)


app = QApplication(sys.argv)
window = Fenster()
sys.exit(app.exec_())



