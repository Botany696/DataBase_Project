CREATE TABLE Заказы(
    Заказ INT,
    Блюдо INT,
    Столик INT,
    Дата TIMESTAMP WITHOUT TIME ZONE
); 

CREATE TABLE Блюда (
    Блюдо INT UNIQUE,
    Ингредиенты TEXT,
    Цена MONEY,
    Наличие BOOLEAN,
    Скидка INT,
    Вегетарианское BOOLEAN
);

CREATE TYPE MyType AS ENUM('VIP', 'У окна', 'Зал');
CREATE TABLE Бронирование (
    Столик INT UNIQUE,
    Тип MyType,
    Места INT,
    Доступен BOOLEAN,
    Цена MONEY,
    Дата TIMESTAMP WITHOUT TIME ZONE,
    Время INTERVAL
);

CREATE TABLE Доходы (
    Дата TIMESTAMP WITHOUT TIME ZONE,
    Доход MONEY,
    Состояние_счета MONEY
);
