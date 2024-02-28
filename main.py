import telebot
from telebot import types

bot = telebot.TeleBot('6841649999:AAGshO59WA9ueHrLRqJeseVt8oHELYwO_yk')
my_chat_id = 631104511

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_dice(message.chat.id)
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Service')
    button2 = types.KeyboardButton(text='About us')
    button3 = types.KeyboardButton(text='Leave an application')
    keyboard.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Good afternoon! We are a company for accountants', reply_markup=keyboard)

def info_func(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text='Link to our website', url='https://yandex.ru/')
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Info about the company', reply_markup=keyboard)

def send_request(message):
    mes = f'New application: {message.text}'
    bot.send_message(my_chat_id, mes)
    bot.send_message(message.chat.id, 'Thanks for your application! Our staff will contact you soon.')

def send_service(message):
    services = [
        '1. Make a year report',
        '2. Pay a tax',
        '3. Account a budget'
    ]
    bot.send_message(message.chat.id, '\n'.join(services))

@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    if message.text.lower() == 'about us':
        info_func(message)
    elif message.text.lower() == 'leave an application':
        bot.send_message(message.chat.id, 'We would be glad to serve you! Please leave your contact data.')
        bot.register_next_step_handler(message, send_request)
    elif message.text.lower() == 'service':
        send_service(message)

if __name__ == '__main__':
    bot.infinity_polling()
