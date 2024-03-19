from .connect import *


@ConnectBaseReturnTypeList
def InsertNewUser(value: tuple[str, str, str, str, str, str], cursor: MySQLCursor = None) -> bool:
    """
    Осуществляет добавление нового пользователя
    :param value: [фио, номер_группы, студенческий, номер_телефона, почта, телеграм, вк]
    :param cursor: (не требует ввода) предназначен для обращения к нему запросов
    :return: True если успешна добавлена запись
    """

    sql = """
    INSERT INTO 
        users(FIO, number_group, student_id_number, number_phone, email, telegram, vk) 
    VALUES
        (%s, %s, %s, %s, %s, %s, %s);
    """
    cursor.execute(sql, value)
    cursor.fetchone()
    return True


@ConnectBaseReturnTypeList
def DeleteUserById(id_user: int, cursor: MySQLCursor = None) -> bool:
    """
    Осуществляет удаление пользователя по введенному id номеру
    :param id_user: id книги
    :param cursor: (не требует ввода) предназначен для обращения к нему запросов
    :return: True если успешна удаление
    """

    sql = "DELETE FROM users WHERE id = %s;"
    cursor.execute(sql, (id_user, ))
    cursor.fetchone()
    return True


# МБ ПЕРЕЙТИ НА БОРЕЕ СТАТИЧНОЕ ПЕРЕДАЧА ИФНОРАМЦММ БЕЗ ЦИКЛА ВНУТРИ
@ConnectBaseReturnTypeList
def UpdateDataUser(id_user: int, param: dict, cursor: MySQLCursor = None) -> bool:
    """
    Осуществляет изменение информации пользователя по его id номеру
    :param id_user: id книги
    :param param: значение которые требуется изменить где key - это столбец, а value это значение
    :param cursor: (не требует ввода) предназначен для обращения к нему запросов
    :return: True если успешна добавлена запись
    """

    param_edit_for_sql = ""
    for key, value in zip(param.keys(), param.values()):
        param_edit_for_sql += f"""{key} = {'NULL' if value == "" else f'"{value}"'}, """
    param_edit_for_sql = param_edit_for_sql[:-2]

    sql = f"""
    UPDATE users
    SET {param_edit_for_sql}
    WHERE id = %s;
    """

    cursor.execute(sql, (id_user, ))
    cursor.fetchone()
    return True


@ConnectBaseReturnTypeList
def GetAllUser(cursor: MySQLCursor = None) -> tuple[tuple, ...]:
    """
    Осуществляет получение информации о всех пользователей
    :param cursor: (не требует ввода) предназначен для обращения к нему запросов
    """

    sql = "SELECT * FROM users;"
    cursor.execute(sql)
    result = cursor.fetchall()
    return tuple(result)


@ConnectBaseReturnTypeDict
def GetAboutUser(id_user: int, cursor: MySQLCursor = None) -> dict:
    """
    Осуществляет поиск информацию о пользователе по его id номеру
    :param id_user: id пользователе, которую требуется найти
    :param cursor: (не требует ввода) предназначен для обращения к нему запросов
    """

    sql = "SELECT * FROM users WHERE id = %s;"
    cursor.execute(sql, (id_user, ))
    result = cursor.fetchone()
    return result


@ConnectBaseReturnTypeList
def GetUsersTakesBook(cursor: MySQLCursor = None) -> tuple[tuple, ...]:
    """
    Осуществляет поиск пользователей которые взяли книгу в библиотеке
    :param cursor: (не требует ввода) предназначен для обращения к нему запросов
    """
    sql = """
    SELECT DISTINCT
        users.*
    FROM 
        take_book 
    INNER JOIN 
        users ON user_id = users.id
    WHERE 
        date_return IS NULL
    """
    cursor.execute(sql)
    result = cursor.fetchall()
    return tuple(result)


@ConnectBaseReturnTypeList
def GetUsersBookDebtors(cursor: MySQLCursor = None) -> tuple[tuple, ...]:
    """
    Осуществляет поиск пользователей которые задолжали книгу/книги
    :param cursor: (не требует ввода) предназначен для обращения к нему запросов
    """

    sql = """
    SELECT DISTINCT
        users.*
    FROM 
        take_book 
    INNER JOIN 
        users ON user_id = users.id
    WHERE 
        date_return IS NULL
    AND 
        DATE_ADD(date_take, INTERVAL how_many_days_give DAY) <= CURDATE();
    """
    cursor.execute(sql)
    result = cursor.fetchall()
    return tuple(result)


@ConnectBaseReturnTypeList
def GetInfoTheyFitDelivery(cursor: MySQLCursor = None) -> tuple[tuple, ...]:
    """
    Пользователи которые вскоре должны стать сдать книгу/книги (в течение 2 дней)
    :param cursor: (не требует ввода) предназначен для обращения к нему запросов
    """

    sql = """
    SELECT 
        users.*
    FROM 
        take_book
    INNER JOIN
        users ON take_book.user_id = users.id
    WHERE
        take_book.date_return IS NULL 
    AND
        DATEDIFF((DATE_ADD(take_book.date_take, INTERVAL take_book.how_many_days_give DAY)), CURRENT_DATE()) <= 3 
    AND
        DATEDIFF((DATE_ADD(take_book.date_take, INTERVAL take_book.how_many_days_give DAY)), CURRENT_DATE()) > 0;
    """
    cursor.execute(sql)
    result = cursor.fetchall()
    return tuple(result)


@ConnectBaseReturnTypeList
def GetInfoByInputDataUsers(input_data: str, cursor: MySQLCursor = None) -> tuple[tuple, ...] | tuple:
    """
    Осуществляет поиск пользователя по введенной информации из всей таблицы users
    :param input_data: любая текстовая информация
    :param cursor: (не требует ввода) предназначен для обращения к нему запросов
    """

    input_data = f"%{input_data}%"
    sql = """
    SELECT 
        * 
    FROM 
        users
    WHERE 
        CONCAT_WS(FIO, number_group, student_id_number, number_phone, email, vk, telegram) LIKE %s;
    """
    cursor.execute(sql, (input_data, ))
    result = cursor.fetchall()
    return tuple(result)
