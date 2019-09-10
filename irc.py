import socket
import sys


class IRC:
    irc = socket.socket()

    def __init__(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, chan, msg):
        self.irc.send(("PRIVMSG " + chan + " " + msg + "n").encode("utf-8"))

    def connect(self, server, channel, nick, password):
        # defines the socket
        print("connecting to:" + server)
        self.irc.connect((server, 6667))  # connects to the server
        self.irc.send(("NICK " + nick + "\r\n").encode("utf-8"))
        self.irc.send(("PASS " + password + "\r\n").encode("utf-8"))
        self.irc.send(("JOIN " + channel + "\r\n").encode("utf-8"))

    def get_text(self):
        text = self.irc.recv(2040)  # receive the text

        #if text.find('PING') != -1:
        #    self.irc.send(('PONG ' + text.split()[1] + '\r\n').encode("utf-8"))

        return text