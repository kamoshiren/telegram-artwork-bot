#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created by kamoshiren
import telebot
from telebot.types import Message

token = "" # Inser your Telegram bot token here

bot = telebot.TeleBot(token)
keyboard1 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
keyboard1.row('О нас', 'Наш инстаграм')
keyboard1.row("Цены", "Отзывы")

@bot.message_handler(commands=['start', 'help'])
def start(message):
    #markup = telebot.types.InlineKeyboardMarkup()
    #button = telebot.types.InlineKeyboardButton(text='CLick me', callback_data='add')
    #markup.add(button)
    bot.send_message(chat_id=message.chat.id, text="""Арт-студия
🔶Картины масляными красками
◼️Портреты карандашом
🔶Только ручная работа
⚫️Доставка по России
📍Для заказа пишите нам

Нажми на одну из кнопок ниже, чтобы узнать больше о нас и нашей деятелности, или напиши /help чтобы снова вывести это сообщение :)""", reply_markup=keyboard1)

@bot.message_handler(content_types=["text"])
def default_test(message: Message):
    if message.text.lower() == 'о нас':
        bot.send_message(message.chat.id, 'Мы занимаемся тем, что рисуем картины на заказ и высылаем их Вам по почте. Мы работаем давно и в нашем коллективе находятся только опытные художники, которые выполнят работу по Вашим предпочтениям.', reply_markup=keyboard1)
    elif message.text.lower() == 'цены':
        bot.send_message(message.chat.id, 'Портрет в стиле DREAM ART - от 1000 руб.\nПортрет карандашом - от 1100 руб.\nКартина маслом - от 3000 руб.\nКонкретные цены можете узнать, отправив нам свое фото. В среднем мы выполняем заказ от 2 до 5 дней.', reply_markup=keyboard1)
    elif message.text.lower() == 'наш инстаграм':
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text="Перейти в Инстаграм", url="https://www.instagram.com/*")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Ссылка на инстаграм по кнопке ниже:", reply_markup=keyboard)
    elif message.text.lower() == 'отзывы':
        #bot.send_message(message.chat.id, "(тут будут отзывы)", " ", reply_markup=keyboard1)
        bot.send_photo(message.chat.id, open('./review1.jpg', 'rb'))
        bot.send_photo(message.chat.id, open('./review2.jpg', 'rb'))
        bot.send_photo(message.chat.id, open('./review3.jpg', 'rb'))
        bot.send_photo(message.chat.id, open('./review4.jpg', 'rb'), reply_markup=keyboard1)
    else:
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text="Перейти в Инстаграм", url="https://www.instagram.com/*")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Уточни свой вопрос :)\nКстати, у нас есть свой инстаграм. Там мы выкладываем свежие новости и свои работы. Обязательно загляни!\nДля отображения меню напиши мне /help", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == 'add':
        bot.answer_callback_query(callback_query_id=call.id, text='Hello world')

if __name__ == '__main__':
    bot.polling()
