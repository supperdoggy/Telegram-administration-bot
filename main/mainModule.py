import telebot
from main.botToken import botTokenID
from main.botToken.handlers.messageHandlers import startCommand
from main.botToken.handlers.messageHandlers import helpCommand
from main.botToken.handlers.messageHandlers import unBanUserCommand
from main.botToken.handlers.messageHandlers import banUserCommand
from main.botToken.handlers.messageHandlers import muteCommand
from main.botToken.handlers.messageHandlers import unMuteCommand
from main.Methods.Deny import denyAcces
from main.adminCheck import AdminCheck
from main.botToken.handlers.messageHandlers import addNewAdmin
from main.botToken.handlers.messageHandlers import removeAdminCommand
from main.botToken.handlers.messageHandlers import getIdCommand


def theMain():
    simon = telebot.TeleBot(botTokenID.token)

    # Мій найкращий друг

    @simon.message_handler(commands=["start"])
    def greetings(message):
        print("start\n")
        print(message)

        startCommand(message, simon)

    @simon.message_handler(commands=["help"])
    def help(message):
        print("help\n")
        print(message)

        helpCommand(message, simon)

    @simon.message_handler(commands=["unban"])
    def unBanUser(message):
        print("unban\n")
        print(message)

        if AdminCheck(message):
            try:
                unBanUserCommand(message, simon)

            except:
                simon.reply_to(message, "Я йобнувся \n(mainModule.py line 40")

        else:
            denyAcces(message, simon)

    @simon.message_handler(commands=["ban"])
    def banPerson(message):
        print("ban\n")
        print(message)

        if AdminCheck(message):
            try:
                banUserCommand(message, simon)

            except:
                simon.reply_to(message, "Я йобнувся \n(mainModule.py line 55)")

        else:
            denyAcces(message, simon)

    @simon.message_handler(commands=["mute"])
    def mutePerson(message):
        print("mute\n")
        print(message)

        if AdminCheck(message):
            try:
                muteCommand(message, simon)

            except:
                simon.reply_to(message, "Я йобнувся \n(mainModule.py line 70)")

        else:
            denyAcces(message, simon)

    @simon.message_handler(commands=["unmute"])
    def unmutePerson(message):
        print("unmute\n")
        print(message)

        if AdminCheck(message):
            try:
                unMuteCommand(message, simon)

            except:
                simon.reply_to(message, "Я йобнувся \n(mainModule.py line 85)")

        else:
            denyAcces(message, simon)

    # Ше залишилася команда яка забирає адміна
    @simon.message_handler(commands=['newadmin'])
    def admin(message):
        print('newAdmin \n')
        print(message)

        if AdminCheck(message):
            try:
                addNewAdmin(message, simon)

            except:
                simon.reply_to(message, 'Я йобнувся \n(mainModule.py line 100)')

        else:
            denyAcces(message, simon)

    @simon.message_handler(commands=["removeadmin"])
    def removeAdmin(message):
        print("removeAdmin\n")
        print(message)

        if AdminCheck(message):
            try:
                removeAdminCommand(message, simon)

            except:
                simon.reply_to(message, "Я йобнувся \n(mainModule.py line 115)")

        else:
            denyAcces(message, simon)

    @simon.message_handler(commands=['getid'])
    def getId(message):
        try:
            getIdCommand(message, simon)
        except:
            simon.reply_to(message, "Я йобнувся \n(mainModule.py line 129)")

    @simon.message_handler(content_types=["text"])
    def textGet(message):
        print("text\n")
        print(message)
        print("\n")
        print(str(message.from_user.first_name) + "  %s" % message.text)

    simon.polling(none_stop=True)
