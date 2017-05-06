import sqlite3


conn = sqlite3.connect('Restaurant.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS Заказы(
    Заказ INT,
    Блюдо INT,
    Столик INT,
    Дата TIMESTAMP WITHOUT TIME ZONE
);
''')

c.execute('''
CREATE TABLE IF NOT EXISTS Блюда (
    Блюдо INT,
    Ингредиенты TEXT,
    Цена MONEY,
    Наличие BOOLEAN,
    Скидка INT,
    Вегетарианское BOOLEAN,
    PRIMARY KEY(Блюдо)
);
''')

c.execute('''
CREATE TABLE IF NOT EXISTS Бронирование (
    Столик INT,
    Тип Text,
    Места INT,
    Доступен BOOLEAN,
    Цена MONEY,
    Дата TIMESTAMP,
    Время INTERVAL,
    PRIMARY KEY(Столик)
);
''')

c.execute('''
CREATE TABLE IF NOT EXISTS Доходы (
    Дата TIMESTAMP WITHOUT TIME ZONE,
    Доход MONEY,
    Состояние_счета MONEY
);
''')
conn.commit()

c.executescript('''
insert into Доходы values ('01.05.2016',10,10000)''')
c.execute('''
SELECT * FROM Доходы;''')

results = c.fetchall()
print(results)
conn.commit()


# Функция занесения пользователя в базу
def add_user(z, b, s, d):
    c.execute("INSERT INTO Заказы (Заказ, Блюдо, Столик, Дата) VALUES ('%s','%s','%s','%s')" % (z, b, s, d))
    conn.commit()
    print('A new string was inserted! Number: ', c.lastrowid)

# Вводим данные
Заказ = input("Введите Заказ\n")
Блюдо = input("Введите Блюдо\n")
Столик = input("Введите Столик\n")
Дата = input("Введите Дату\n")

print('\n')

# Делаем запрос в базу
add_user(Заказ, Блюдо, Столик, Дата)

print("Table 'Заказы':\n")

c.execute('SELECT * FROM Заказы')
row = c.fetchone()

# выводим список пользователей в цикле
while row is not None:
    print(" | Заказы.Заказ: "
          +str(row[0])+" | Заказы.Блюдо: "
          +str(row[1])+" | Заказы.Столик: "
          +str(row[2])+" | Заказы.Дата: "+str(row[3]))
    row = c.fetchone()


# закрываем соединение с базой
c.close()

conn.close()
