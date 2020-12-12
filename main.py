bot = telebot.TeleBot("1435505429:AAFdRhAAa8ETSnhfb8_ZIyzCRL54iW6mEp4")
@bot.message_handler(content_types=("text"))
def get_text_messages(message):
    bot.send_message(message.from_user.id, message.json["text"])
    if message.json == "Привет":
        bot.send_message(message.from_user.id, "Привет")
    print(message)
bot.polling(none_stop=True, interval=0)