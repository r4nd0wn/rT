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


