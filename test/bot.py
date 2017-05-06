import config
import telebot
import sqlite3
from telebot import types
from datetime import datetime
step = {}

conn = sqlite3.connect('Restaurant.db')
c = conn.cursor()
c.execute('''
SELECT * FROM Блюда;''')
results = c.fetchall()
print(results)
conn.commit()


# Функция занесения пользователя в базу
def add_user(a, b, s, d):
    c.execute("INSERT INTO Заказы (Заказ, Блюдо, Столик, Дата) VALUES ('%s', %s','%s','%s')" % (a, b, s, d))
    conn.commit()
    print('A new string was inserted! Number: ', c.lastrowid)

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['заказ'])
def order(message):
    markup = types.ForceReply(selective=False)
    bot.send_message(message.chat.id, 'Введите столик заказа:', reply_markup=markup)
    step[message.chat.id] = 1


@bot.message_handler(func=lambda message: step.get(message.chat.id) == 1)
def add_order(m):
    step[m.chat.id] = 2
    conn1 = sqlite3.connect('Restaurant.db')
    c1 = conn1.cursor()
    date = str(datetime.now())
    c1.execute("INSERT INTO Заказы (Столик, Дата) VALUES ('%s','%s')" % (m.text, date))
    c1.execute("SELECT Заказ FROM Заказы WHERE Столик = '%s' AND Дата = '%s'" % (m.text, date))
    add_dishes.a = c1.fetchone()
    print(add_dishes.a)
    conn1.commit()
    c1.close()
    conn1.close()
    markup = types.ForceReply(selective=False)
    bot.send_message(m.chat.id, 'Введите блюда заказа (введите /конец, если вы закончили):', reply_markup=markup)
    step[m.chat.id] = 2


@bot.message_handler(commands=['конец'])
def end(m):
    step[m.chat.id] = 0
    bot.send_message(m.chat.id, 'Сделано!')


@bot.message_handler(func=lambda message: step.get(message.chat.id) == 2)
def add_dishes(m):
    conn1 = sqlite3.connect('Restaurant.db')
    c1 = conn1.cursor()
    c1.execute("INSERT INTO Заказы_Блюда (Заказ, Блюдо) VALUES ('%s','%s')" % (add_dishes.a, m.text))
    conn1.commit()
    c1.close()
    conn1.close()
    markup = types.ForceReply(selective=False)
    bot.send_message(m.chat.id, 'Введите блюда заказа (введите /конец, если вы закончили):', reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def repeat_all_messages(message):  # Название функции не играет никакой роли, в принципе
    i = 0
    while i < len(results):
            bot.send_message(message.chat.id, str(results[i]))
            i += 1


bot.polling()

c.close()
conn.close()
