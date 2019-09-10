import sys, time
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from irc import IRC


HOST = "irc.twitch.tv"
NICK = "r4nd0wn"
PORT = 6667
PASS = "oauth:m9aomgcvgacww3ybeo07m2pu162c0y"
readbuffer = ""
MODT = False
CHANNEL = "r4nd0wn"

irc = IRC()
irc.connect(HOST, CHANNEL, NICK, PASS)

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
        self.show()

    def starter(self):
        try:
            self.textEdit.insertPlainText(str(irc.get_text()))
        except Exception as e:
            print(e)

app = QApplication(sys.argv)
window = Fenster()
sys.exit(app.exec_())

