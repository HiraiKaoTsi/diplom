from .connect import *

from .handler_book import TakeQuantityBook


@ConnectBase
def IssuedBookAll(cursor: MySQLCursor = None) -> int:
    """
    Сколько книг выданно всего
    """
    sql = "SELECT COUNT(id) FROM take_book WHERE date_return is NULL;"
    cursor.execute(sql)
    result = cursor.fetchone()[0]
    return result


@ConnectBase
def NumberBooksIssuedToday(cursor: MySQLCursor = None) -> int:
    """
    Данная функция подсчитывает количество выданых книг за сегодня
    """
    sql = "SELECT COUNT(id) FROM take_book WHERE date_return IS NULL AND date_take = CURRENT_DATE();"
    cursor.execute(sql)
    result = cursor.fetchone()[0]
    return result


@ConnectBase
def QuantityDebtors(cursor: MySQLCursor = None) -> int:
    """
    Выводит количество задолжников книг
    """
    sql = "SELECT COUNT(id) FROM take_book WHERE date_take < DATE_SUB(CURRENT_DATE(), INTERVAL 14 DAY) AND date_return IS NULL;"
    cursor.execute(sql)
    result = cursor.fetchone()[0]

    return result

@ConnectBase
def CountReturnBookToday(cursor: MySQLCursor = None) -> int:
    """
    Выводит количество вернутых книг сегодня
    """

    sql = "SELECT COUNT(id) FROM take_book WHERE date_return = CURRENT_DATE();"
    cursor.execute(sql)
    result = cursor.fetchone()[0]

    return result
