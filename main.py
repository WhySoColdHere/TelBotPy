from exchange_rate import list_of_money
from horoskope import list_with_horoscope
from numpy import array
from telebot import types
import telebot as tb
from commands_list import *
from without_bot_funcs import *
from charts_fuctional import return_chart
from os import remove
from token_file import token

bot = tb.TeleBot(token)


def return_mess(mess, x):
    return bot.send_message(mess.chat.id, x, parse_mode='html')


@bot.message_handler(commands=mass_commands[0])
def start_com(mess):
    res = f'Hello, <b><em>{mess.from_user.first_name} {mess.from_user.last_name}</em></b>'
    return_mess(mess, res)


@bot.message_handler(commands=mass_commands[1])
def help_com(mess):
    return_mess(mess, txt_commands)


@bot.message_handler(commands=mass_commands[4])
def cute_tyan_com(mess):
    try:
        bot.send_photo(mess.chat.id, random_photo())
    except:
        return 'Hey! You caught the error! Be proud of it and..try the next time :)'


@bot.message_handler(commands=mass_commands[2])
def horoscope_com(mess):
    bl_hor = array([types.InlineKeyboardButton('Aries', callback_data=id_btn_mass[0]),
                    types.InlineKeyboardButton('Taurus', callback_data=id_btn_mass[1]),
                    types.InlineKeyboardButton('Gemini', callback_data=id_btn_mass[2]),
                    types.InlineKeyboardButton('Cancer', callback_data=id_btn_mass[3]),
                    types.InlineKeyboardButton('Leo', callback_data=id_btn_mass[4]),
                    types.InlineKeyboardButton('Virgo', callback_data=id_btn_mass[5]),
                    types.InlineKeyboardButton('Libra', callback_data=id_btn_mass[6]),
                    types.InlineKeyboardButton('Scorpio', callback_data=id_btn_mass[7]),
                    types.InlineKeyboardButton('Sagittarius', callback_data=id_btn_mass[8]),
                    types.InlineKeyboardButton('Capricorn', callback_data=id_btn_mass[9]),
                    types.InlineKeyboardButton('Aquarius', callback_data=id_btn_mass[10]),
                    types.InlineKeyboardButton('Pisces', callback_data=id_btn_mass[11])])
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(bl_hor[0], bl_hor[1], bl_hor[2], bl_hor[3], bl_hor[4], bl_hor[5],
               bl_hor[6], bl_hor[7], bl_hor[8], bl_hor[9], bl_hor[10], bl_hor[11])
    bot.send_message(mess.chat.id, 'Choose your sign', reply_markup=markup)


@bot.message_handler(commands=mass_commands[3])
def money_func_com(mess):
    bl_money = array([types.InlineKeyboardButton(list_of_money[0][0], callback_data=id_btn_mass[12]),
                      types.InlineKeyboardButton(list_of_money[1][0], callback_data=id_btn_mass[13]),
                      types.InlineKeyboardButton(list_of_money[2][0], callback_data=id_btn_mass[14]),
                      types.InlineKeyboardButton(list_of_money[3][0], callback_data=id_btn_mass[15])])
    murkup = types.InlineKeyboardMarkup(row_width=2)
    murkup.add(bl_money[0], bl_money[1], bl_money[2], bl_money[3])
    bot.send_message(mess.chat.id, 'Choose MONEY MODE', reply_markup=murkup)


@bot.message_handler(commands=mass_commands[5])
def chart_com(mess):
    bot.send_message(mess.chat.id, "Enter list of numbs like: '1 2 3 4...'")
    bot.register_next_step_handler(mess, get_chart)


def get_chart(mess):
    bot.send_photo(mess.chat.id, return_chart(mess.text))
    try:
        remove("ffile.png")
    except WindowsError:
        print("File is already deleted")


@bot.callback_query_handler(func=lambda call: True)
def callback_func(call):
    if call.message:
        but_hor_func(call.data, id_btn_mass, call, list_with_horoscope, return_mess, list_of_money)


@bot.message_handler()
def user_txt(mess):
    txt = 'Sry, imma just machine...For now {^-^}'
    return_mess(mess, txt)


bot.polling(none_stop=True)
