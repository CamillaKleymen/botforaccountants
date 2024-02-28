import telebot
from telebot import types
bot = telebot.TeleBot('6841649999:AAGshO59WA9ueHrLRqJeseVt8oHELYwO_yk')
my_chat_id =631104511


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_dice(message.chat.id)
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Service')
    button2 = types.KeyboardButton(text='About us')
    button3 = types.KeyboardButton(text='Leave an application')
    keyboard.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Good afternoon! We are company for accountants', reply_markup=keyboard)


def info_func(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text='Link on the our website', url='https://yandex.ru/')
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Info about company', reply_markup=keyboard)

def send_request(message):
    mes = f'New apllication: {message.text}'
    bot.send_message(my_chat_id, mes)
    bot.send_message(message.chat.id, 'Thanks for application! Our employers will connect to you soon')

def send_service(message):
    bot.send_message(message.chat.id, '1.Make a year report')
    bot.send_message(message.chat.id, '2 Pay a tax')
    bot.send_message(message.chat.id, '3.Account a budget')


@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    if message.text.lower() == 'About us':
        info_func(message)
    if message.text.lower() == 'Leave an application':
        bot.send_message(message.chat.id, 'We will glad to serve you! Leave your contact data')
        bot.register_next_step_handler(message, send_request)
    if message.text.lower() == 'service':
        send_service(message)


if __name__ == '__main__':
    bot.infinity_polling()