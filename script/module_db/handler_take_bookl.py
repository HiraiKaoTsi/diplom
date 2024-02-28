from .connect import *

from .handler_book import TakeQuantityBook


@ConnectBaseReturnTypeList
def IssuedBookAll(cursor: MySQLCursor = None) -> int:
    """
    Сколько книг выданно всего
    """
    sql = "SELECT COUNT(id) FROM take_book WHERE date_return is NULL;"
    cursor.execute(sql)
    result = cursor.fetchone()[0]
    return result

@ConnectBaseReturnTypeList
def CountIssuedBookToday(cursor: MySQLCursor = None) -> int:
    """
    Данная функция подсчитывает количество выданых книг за сегодня
    """
    sql = "SELECT COUNT(id) FROM take_book WHERE date_return IS NULL AND date_take = CURRENT_DATE();"
    cursor.execute(sql)
    result = cursor.fetchone()[0]
    return result


@ConnectBaseReturnTypeList
def CountReturnBookToday(cursor: MySQLCursor = None) -> int:
    """
    Данная функция подсчитывает количество вернутых книг за сегодня
    """
    sql = "SELECT COUNT(id) FROM take_book WHERE date_return = CURRENT_DATE();"
    cursor.execute(sql)
    result = cursor.fetchone()[0]

    return result


@ConnectBaseReturnTypeList
def CountQuantityDebtors(cursor: MySQLCursor = None) -> int:
    """
    Выводит количество задолжников книг
    """
    sql = "SELECT COUNT(ID) FROM take_book WHERE date_take < DATE_SUB(CURRENT_DATE(), INTERVAL how_many_days_give DAY) AND date_return IS NULL;"
    cursor.execute(sql)
    result = cursor.fetchone()[0]

    return result


@ConnectBaseReturnTypeList
def WhichBookTakeUser(user_id, cursor: MySQLCursor = None) -> tuple:
    """
    Выводит все книги которые брал пользоватль (которые вернул)
    """
    sql = f"SELECT * FROM library_database.take_book WHERE user_id = %s AND date_return IS NOT NULL;"
    cursor.execute(sql, (user_id, ))
    result = cursor.fetchall()

    return result


@ConnectBaseReturnTypeList
def WhichNowBookAtUser(user_id, cursor: MySQLCursor = None) -> tuple:
    """
    Выводит все книги которые сейчас у пользователя
    """
    sql = f"SELECT * FROM library_database.take_book WHERE user_id = %s AND date_return IS NOT NULL;"
    cursor.execute(sql, (user_id, ))
    result = cursor.fetchall()

    return result
