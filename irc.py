import socket
import datetime
class IRC:
    irc = socket.socket()

    def __init__(self, channel, nick, password):
        self.channel = channel
        self.nick = nick
        self.password = password
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        print("connecting to channel: " + self.channel)
        self.irc.connect(("irc.twitch.tv", 6667))

        self.irc.send(("PASS " + self.password + "\r\n").encode("utf-8"))
        self.irc.send(("NICK " + self.nick + "\r\n").encode("utf-8"))
        self.irc.send(("JOIN #" + self.channel + "\r\n").encode("utf-8"))

    def send(self, msg):
        self.irc.send(("PRIVMSG " + self.channel + " " + msg + "n").encode("utf-8"))


    def get_message(self):
        text = self.irc.recv(2040)
        return text

    def get_parsed_message(self):
        text = self.irc.recv(2040).decode("utf-8")

        timestamp = datetime.datetime.now()

        if text.find("PING") != -1:
            self.irc.send(('PONG ' + text.split()[1] + '\r\n').decode("utf-8"))

        if text.find("PRIVMSG") != -1:
            msgun = text.split("!")[0][1:]
            tempmsg = text.split("PRIVMSG #" + self.channel + " :")
            content = tempmsg[1][:-2]
            fullmessage = str(timestamp.hour) + ":" + str(timestamp.minute) + ":" + str(timestamp.second) + " - " + msgun + ": " + content
            return fullmessage