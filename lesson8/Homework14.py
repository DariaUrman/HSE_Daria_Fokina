from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext

button_1 = KeyboardButton("Написание -тся и -ться в глаголах")
button_2 = KeyboardButton("Когда -тся?")
button_3 = KeyboardButton("Когда -ться?")
button_4 = KeyboardButton("Где посмотреть подробнее?")

main_menu = [[button_1, button_2, button_3, button_4]]

def start(update:Update, context:CallbackContext):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Привет. Я бот-справочник по -тся и -ться в глаголах.", reply_markup=ReplyKeyboardMarkup(main_menu, one_time_keyboard=False, resize_keyboard=True))

def button_1(update:Update, context:CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Если глагол стоит в 3-м лице единственного или множественного числа, то пишется «-тся». Если глагол стоит в неопределенной форме (инфинитиве), то пишется «-ться».", reply_markup=ReplyKeyboardMarkup(main_menu, one_time_keyboard=False, resize_keyboard=True))

def button_2(update:Update, context:CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Если в вопросе отсутствует мягкий знак: «что делает (сделает)?», «что делают (сделают)?», то в глаголе пишется -тся (без мягкого знака).", reply_markup=ReplyKeyboardMarkup(main_menu, one_time_keyboard=False, resize_keyboard=True))

def button_3(update:Update, context:CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Если к глаголу задать вопрос «что делать?» или «что сделать?», то пишется -ться, так как это глагол неопределённой формы.", reply_markup=ReplyKeyboardMarkup(main_menu, one_time_keyboard=False, resize_keyboard=True))

def button_4(update:Update, context:CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text = "Подробнее можно посмотреть в школьной программе за 5-й класс и погуглить", reply_markup=ReplyKeyboardMarkup(main_menu, one_time_keyboard=False, resize_keyboard=True))

def echo(update:Update, context:CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text = "Это Ваш текст:"+update.message.text,reply_markup=ReplyKeyboardMarkup(main_menu, one_time_keyboard=False))

def main():
    BOT_TOKEN = "6198941920:AAGxEt9_P6yKbQ02DUbHPJbEu8Ons2hiLGU"
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.regex("Написание -тся и -ться в глаголах") & ~ Filters.command, button_1))
    dispatcher.add_handler(MessageHandler(Filters.regex("Когда -тся?") & ~ Filters.command, button_2))
    dispatcher.add_handler(MessageHandler(Filters.regex("Когда -ться?") & ~ Filters.command, button_3))
    dispatcher.add_handler(MessageHandler(Filters.regex("Где посмотреть подробнее?") & ~ Filters.command, button_4))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
