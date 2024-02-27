from mysql.connector import connect, Error 

from config import *

try:
    connection = connect(host=HOST, port=PORT, user=USER, password=PASSWORD, db=NAME_DATABASE, charset=CHARSET)
    # Подключение к базе данных


    # Создание курсора с параметром dictionary=True
    cursor = connection.cursor(dictionary=True)

    # Выполнение запроса
    cursor.execute("SELECT * FROM library_database.take_book WHERE user_id = 1 AND date_return IS NOT NULL;")

    # Получение результатов в виде списка словарей
    rows = cursor.fetchall()
    print(rows)
    # # Вывод результатов
    # for row in rows:
    #     print(row)

except Error as e:
    print(e)

finally:
    # Закрытие соединения
    if connection.is_connected():
        cursor.close()
        connection.close()
