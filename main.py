#Made for the sole purpose of GCI-2019
from bot import fedorainfrabot
import getforks

bot = fedorainfrabot("config.cfg")

def make_reply(msg):
    reply = None
    if msg =="/forks":
        reply = getforks.text()
    elif msg =="hello" or msg=="Hello" or msg=="hi" or msg=="Hi":
        reply="Hi! How are you!?"
    elif msg=="/what":
        reply="I can get you the number of forks for each repository of fedors-infra\nJust type /forks\nTo get forks of an individual repository try /fork1 where the number signifies the repository number(Available from 1 till 30)\n Also you can type '/fork reponame' to get the forks for the same "
    elif msg=="/start":
        reply="Welcome to the Fedora-Infra Bot\nI am designed to fetch the number of forks for each repository of fedora-infra.\nJust type /forks\nFor more info type /what"

    elif msg[0:5]=="/fork" :
        if len(msg)>7:
            try:
                a=msg[6:]
                tmp1=getforks.textdict()
                reply="Forks for "+a+" :   "+ tmp1[a]+" forks"
            except:
                reply = "Not Found!"
        else:
            try:
                reply=getforks.textno()
                x=int(msg[5:])-1
                reply="Forks for "+reply[x]
            except:
                 reply="Not Found!"
    else:
        reply="Sorry, that's not a valid command!\nTry /what to know more."
    return reply


update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, from_)
