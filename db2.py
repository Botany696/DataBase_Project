# -*- coding: utf-8 -*-
import sqlite3
conn = sqlite3.connect('professors.db')
c = conn.cursor()

# Создание таблицы
c.execute('''CREATE TABLE IF NOT EXISTS professors (id int, name varchar, year varchar)''')
# Наполнение таблицы
# Подтверждение отправки данных в базу
conn.commit()
# Завершение соединения


# Функция занесения пользователя в базу
def add_user(p_name, p_year):
    c.execute("INSERT INTO professors (name, year) VALUES ('%s','%s')" % (p_name, p_year))
    conn.commit()
    print('A new professor was inserted! Number: ', c.lastrowid)

# Вводим данные
name = input("Введите ФИО профессора с Физтеха\n")
year = input("Введите год его рождения\n")
print('\n')

# Делаем запрос в базу
add_user(name, year)

print("List of professors:\n")

c.execute('SELECT * FROM professors')
row = c.fetchone()

# выводим список пользователей в цикле
while row is not None:
    print("id:"+str(row[0])+" | professors.name: "+row[1]+" | professors.year: "+row[2])
    row = c.fetchone()
# закрываем соединение с базой
c.close()
conn.close()
