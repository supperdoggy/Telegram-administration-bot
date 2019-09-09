import json
from main.groupTypeCheck import groupTypeCheckFunc
import telebot
from main.botToken import botTokenID


def AdminCheck(message):
    if groupTypeCheckFunc(message, simon=telebot.TeleBot(botTokenID.token)):
        try:
            with open('Data/%s.json' % message.from_user.id) as f:
                data = json.load(f)
                if data["firstChat"] == str(message.chat.id) or data["secondChat"] \
                        == str(message.chat.id) or data["thirdChat"] == str(message.chat.id) or data["fourthChat"] \
                        == str(message.chat.id):
                    f.close()
                    return True
                elif data["firstChat"] == "GOD" or data["secondChat"] \
                        == "GOD" or data["thirdChat"] == "GOD" or data["fourthChat"] \
                        == "GOD":
                    f.close()
                    return True
                elif data["inactive"] == "True":
                    return False
                else:
                    f.close()
                    return False
        except:
            print("Я йобнувся \n(adminCheck.py line 24)")
            return False
    else:
        return False


def jsonEditAdmin(message):
    with open('Data/%s.json' % message.reply_to_message.from_user.id) as f:
        data = json.load(f)
        f.close()

    if data["numOfChats"] == 0:
        data["firstChat"] = str(message.chat.id)
        data["numOfChats"] += 1

    elif data["numOfChats"] == 1:
        data["secondChat"] = str(message.chat.id)
        data["numOfChats"] += 1

    elif data["numOfChats"] == 2:
        data["thirdChat"] = str(message.chat.id)
        data["numOfChats"] += 1

    elif data["numOfChats"] == 3:
        data["fourthChat"] = str(message.chat.id)
        data["numOfChats"] += 1

    with open('Data/%s.json' % message.reply_to_message.from_user.id, "w+") as f:
        json.dump(data, f)


def jsonCreateAdmin(message):
    x = {
        "numOfChats": 1,
        "firstChat": "%s" % message.chat.id,
        "secondChat": "",
        "thirdChat": "",
        "fourthChat": "",
        "inactive": "False"
    }
    with open("Data/%s.json" % message.reply_to_message.from_user.id, 'w+') as f:
        json.dump(x, f)
    f.close()


def jsonRemove(message):
    f = open('Data/%s.json' % message.reply_to_message.from_user.id)
    data = json.load(f)
    f.close()
    if data["firstChat"] == str(message.chat.id):
        data["firstChat"] = ""

    elif data["secondChat"] == str(message.chat.id):
        data["secondChat"] = ""

    elif data["thirdChat"] == str(message.chat.id):
        data["thirdChat"] = ""

    elif data["fourthChat"] == str(message.chat.id):
        data["fourthChat"] = ""

    with open("Data/%s.json" % message.reply_to_message.from_user.id, 'w+') as f:
        json.dump(data, f)
    f.close()
