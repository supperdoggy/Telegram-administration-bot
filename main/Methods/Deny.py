import telebot


def denyAcces(message, simon):
    simon.reply_to(message, "Тебе нельзя такое писать, "
                            "что мама скажет?")
