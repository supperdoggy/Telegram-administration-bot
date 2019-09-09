def groupTypeCheckFunc(message, simon):
    if message.chat.type == "supergroup":
        return True

    elif message.chat.type == "group":
        simon.reply_to(message, "Ти шо поц, спочатку перетвори "
                                "групу в супергрупу")
        return False
    elif message.chat.type == "private":
        simon.reply_to(message, "Для початку добав мене в груповий чат"
                                "супергрупи")
        return False
    else:
        return False