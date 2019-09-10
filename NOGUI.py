from irc import IRC

username = "rTsFetcher"
oauth = "oauth:efhn2jfl093dyrdv94rd91vad3zdoy"
channel = "r4nd0wn"

chat1 = IRC(channel, username, oauth)

chat1.connect()
while(True):
    msg1 = chat1.get_parsed_message()
    print(msg1)

