import json
from main.adminCheck import jsonEditAdmin
from main.adminCheck import jsonCreateAdmin
from main.adminCheck import jsonRemove


def startCommand(message, simon):
    print(message)
    simon.reply_to(message, "Привіт, dear GaY. Я Саймон, а ти чмо іди нахуй")
    return 0


def helpCommand(message, simon):
    print(message)
    simon.reply_to(message, "Є 2 способи використовувати команди\n1 - відповідати на повідомлення"
                            "\n2 - після команди вписувати унікальний ід юзера ( не працює з адмінкою)")



def unBanUserCommand(message, simon):
    print(message)
    simon.reply_to(message, "Я ж пошутив, дебік")
    try:
        simon.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)

    except:
        text = message.text
        text = text.replace("/unban ", "")
        simon.unban_chat_member(message.chat.id, text)


def banUserCommand(message, simon):
    print(message)
    simon.reply_to(message, "БЕМ ОБЭМА")
    try:
        simon.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id, 9999999999999999)
    except:
        text = message.text
        text = text.replace("/ban ", "")
        simon.kick_chat_member(message.chat.id, text, 9999999999999999)


def muteCommand(message, simon):
    print(message)
    simon.reply_to(message, "Завали єбало")
    try:
        simon.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages=False,
                                   can_send_media_messages=False,
                                   can_send_other_messages=False,
                                   can_add_web_page_previews=False)
    except:
        text = message.text
        text = text.replace("/mute ", "")
        simon.restrict_chat_member(message.chat.id, text, can_send_messages=False,
                                   can_send_media_messages=False,
                                   can_send_other_messages=False,
                                   can_add_web_page_previews=False)

def unMuteCommand(message, simon):
    print(message)
    simon.reply_to(message, "Відкрий рот, холоп")
    try:
        simon.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages=True,
                                   can_send_media_messages=True,
                                   can_send_other_messages=True,
                                   can_add_web_page_previews=True)
    except:
        text = message.text
        text = text.replace("/unmute ", "")
        simon.restrict_chat_member(message.chat.id, text, can_send_messages=True,
                                   can_send_media_messages=True,
                                   can_send_other_messages=True,
                                   can_add_web_page_previews=True)

# Зробити штуку шоб додавати по ид
def addNewAdmin(message, simon):
    f = open('Data/listOfAdmins.txt', 'r')
    x = f.read()
    f.close()
    if x.__contains__(str(message.reply_to_message.from_user.id)):
        print("I`m in the list")
        jsonEditAdmin(message)
        simon.reply_to(message, "Велкам ту да боард")
    else:
        print("I`m not in the list")
        jsonCreateAdmin(message)
        f = open('Data/listOfAdmins.txt', 'a+')
        f.write("\n%s" % message.reply_to_message.from_user.id)
        f.close()


def removeAdminCommand(message, simon):
    f = open('Data/listOfAdmins.txt', 'r')
    x = f.read()
    f.close()
    if x.__contains__(str(message.reply_to_message.from_user.id)):
        print("I`m in the list")
        jsonRemove(message)
        simon.reply_to(message, "Тепер в тебе немає сили тут")

    else:
        simon.reply_to(message, "Так ти ітак лох")


def getIdCommand(message, simon):
    simon.reply_to(message, "%s :" % message.reply_to_message.from_user.first_name + " %s"
                   % message.reply_to_message.from_user.id)
