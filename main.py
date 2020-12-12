import telebot
bot = telebot.TeleBot("1435505429:AAFdRhAAa8ETSnhfb8_ZIyzCRL54iW6mEp4")
@bot.message_handler(content_types=("text"))
def get_text_messages(message):
    print (message)
    words = message.json["text"].split()
    for word in words:
        bot.send_message(message.from_user.id, word)
bot.polling(none_stop=True, interval=0)