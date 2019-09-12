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
#        self.irc.send(bytes('PASS %s \r\n' % (self.password), 'UTF-8'))
#        self.irc.send(bytes('NICK %s \r\n' % (self.nick), 'UTF-8'))
#        self.irc.send(bytes('JOIN #%s\r\n' % (self.channel), 'UTF-8'))

    def send(self, msg):
        try:
            self.irc.send(bytes('PRIVMSG #%s :%s\r\n' % (self.channel, msg), 'UTF-8'))
        except Exception as e:
            print(e)
    def get_message(self):
        text = self.irc.recv(2040)
        return text

    def get_parsed_message(self):
        text = self.irc.recv(2040).decode("utf-8")


        if text.find("PING") != -1:
            self.irc.send(bytes('PONG ' + text.split()[1] + '\r\n', "UTF-8 "))
            print("received a ping, send a pong")

        if text.find("PRIVMSG") != -1:
            msgun = text.split("!")[0][1:]
            tempmsg = text.split("PRIVMSG #" + self.channel + " :")
            content = tempmsg[1][:-2]
            fullmessage = self.timestamp() + " - " + msgun + ": " + content
            return fullmessage

    def get_splitted_message(self):
        text = self.irc.recv(2040).decode("utf-8")
        if text.find("PING") != -1:
            self.irc.send(bytes('PONG ' + text.split()[1] + '\r\n', "UTF-8 "))
            print("received a ping, send a pong")

        if text.find("PRIVMSG") != -1:
            msgun = text.split("!")[0][1:]
            tempmsg = text.split("PRIVMSG #" + self.channel + " :")
            content = tempmsg[1][:-2]
            fullmessage = [self.timestamp(), msgun, content]
            print(text)
            return fullmessage
        else:
            print(text)
    def allow_Tags(self):
        self.irc.send(bytes('CAP REQ :twitch.tv/tags', 'UTF-8'))
        self.irc.send(bytes('CAP REQ :twitch.tv/membership', 'UTF-8'))

# -------------------------------helping stuff-----------------------------
    def timestamp(self):
        now = datetime.datetime.now()
        timeun = [str(now.hour), str(now.minute), str(now.second)]
        for i, t in enumerate(timeun):
            if len(t) == 1:
                timeun[i] = "0" + t
        return timeun[0] + ":" + timeun[1]
