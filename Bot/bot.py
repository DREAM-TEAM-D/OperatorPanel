from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters

TG_TOKEN = "1031631815:AAH7Ahdqdnj6SCoCvM5dYw9i_yvny-rz-mk"

def message_handler(bot: Bot, update: Update):
    file = open('log.txt', 'a')
    user = update.effective_user
    if user:
        name = user.first_name
    else:
        name = "unknown"

    text = update.effective_message.text
    reply_text = f'Hello, {name}!\n\n{text}'
    file.seek(2)
    file.write(text + '\n')
    file.close()

    bot.send_message(
        chat_id = update.effective_message.chat_id,
        text = reply_text,
        )


def main():
    print('start')
    bot = Bot(
        token = TG_TOKEN,
        )
    updater = Updater(
        bot = bot,
        )
    handler = MessageHandler(
        Filters.all,
        message_handler,
        )
    updater.dispatcher.add_handler(handler)

    updater.start_polling()
    updater.idle()
    print()

if __name__ == '__main__':
    main()
