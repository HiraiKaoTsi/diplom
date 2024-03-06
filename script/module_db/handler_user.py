from .connect import *


@ConnectBaseReturnTypeList
def GetAllUser(cursor: MySQLCursor = None) -> tuple[tuple, ...]:
    """
    Функция выводит информацию о всех студентах
    """
    sql = "SELECT * FROM users;"
    cursor.execute(sql)
    result = cursor.fetchall()
    return tuple(result)


@ConnectBaseReturnTypeDict
def GetAboutUser(id_user: int, cursor: MySQLCursor = None) -> dict:
    """
    Функция возвращает информацию о пользователе по его id
    """
    sql = "SELECT * FROM users WHERE id = %s;"
    cursor.execute(sql, (id_user, ))
    result = cursor.fetchone()
    return result


@ConnectBaseReturnTypeList
def GetUsersBookDebtors(cursor: MySQLCursor = None) -> tuple[tuple, ...] | tuple:
    """
    Функция возвращает информацию о задолжниках
    """
    sql = """
    SELECT 
        users.*
    FROM 
        take_book 
    INNER JOIN 
        users ON user_id = users.id
    WHERE 
        date_return IS NULL;
    """
    cursor.execute(sql)
    result = cursor.fetchall()
    return tuple(result)


@ConnectBaseReturnTypeList
def GetInfoTheyFitDelivery(cursor: MySQLCursor = None) -> tuple[tuple, ...] | tuple:
    """
    Пользователи которые вскоре должны стать сдать книгу/книги (в течение 2 дней)
    :param cursor: MySQLCursor - (не требует ввода) предназначен для обращения к нему запросов
    :return: tuple[tuple, ...] - если нашел информацию
    tuple - если информация отсутствует или не найдена
    """
    sql = """
    SELECT 
        users.*
    FROM 
        take_book
    INNER JOIN
        users ON take_book.user_id = users.id
    WHERE
        DATEDIFF((DATE_ADD(take_book.date_take, INTERVAL take_book.how_many_days_give DAY)), CURRENT_DATE()) <= 2;
    """
    cursor.execute(sql)
    result = cursor.fetchall()
    return tuple(result)

@ConnectBaseReturnTypeList
def GetInfoByInputData(cursor: MySQLCursor = None):
    sql = """
    SELECT 
        * 
    FROM 
        users
     WHERE CONCAT_WS(FIO, number_group, student_id_number, number_phone, email, vk, telegram) LIKE '%%s%';
    """