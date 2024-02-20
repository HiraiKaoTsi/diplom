from .connect import *

from .handler_book import TakeQuantityBook

@ConnectBase
def UserTakeBook(id_user: int, id_book: int, cursor: sqlite3.Cursor = None) -> bool:
    """
    Создает запись, о том что пользователь берет книгу
    :return: True - если все успешно 
    """
    sql = "INSERT INTO take_book(user_id, book_id, date_take) VALUES(?, ?, strftime('%d.%m.%Y', datetime('now'))));"
    cursor.execute(sql, (id_user, id_book))
    return True

@ConnectBase
def ReturnBook(user_id: int, id_book: int, cursor: sqlite3.Cursor = None) -> bool:
    """
    Обновлят информацию о записи, что пользователь вернул книгу обратно
    :return: True - если все успешно 
    """
    sql = "UPDATE take_book SET date_return = strftime('%d.%m.%Y', datetime('now'))) WHERE user_id = ? AND book_id = ? AND date_return IS NULL;"
    cursor.execute(sql, (user_id, id_book))
    return True

@ConnectBase
def CheckTheRemainedBook(id_book: int, cursor: sqlite3.Cursor = None) -> bool:
    """
    По введенному id книги проверят в наличии ли она
    :return: True если книга имееться False - если отсуствует
    """

    quantity_book = TakeQuantityBook(id_book)

    sql = "SELECT COUNT(id) FROM take_book WHERE book_id = ? AND date_return IS NULL"
    cursor.execute(sql, (id_book, ))
    result = cursor.fetchone()[0]

    if result < quantity_book:
        return True
    return False

@ConnectBase
def NumberBooksIssuedToday(cursor: sqlite3.Cursor = None) -> int:
    """
    Данная функция подсчитывает количество выданых книг за сегодня
    """
    sql = "SELECT COUNT(id) FROM take_book WHERE date_return is NULL AND date_take = strftime('%d.%m.%Y', datetime('now'));"
    cursor.execute(sql)
    result = cursor.fetchone()[0]
    return result


@ConnectBase
def IssuedBookAll(cursor: sqlite3.Cursor = None) -> int:
    """
    Сколько книг выданно всего
    """
    sql = "SELECT COUNT(id) FROM take_book WHERE date_return is NULL;"
    cursor.execute(sql)
    result = cursor.fetchone()[0]
    return result


@ConnectBase
def QuantityDebtors(cursor: sqlite3.Cursor = None) -> int:
    """
    Выводит количество задолжников книг
    """

    sql = "SELECT COUNT(id) FROM take_book WHERE date_take < strftime('%d.%m.%Y', date('now', '-14 days'));"
    cursor.execute(sql)
    result = cursor.fetchone()[0]

    return result


def CountReturnBookToday(cursor: sqlite3.Cursor = None) -> int:
    """
    Выводит количество вернутых книг сегодня
    """

    sql = "SELECT COUNT(id) FROM take_book WHERE date_return = strftime('%d.%m.%Y', datetime('now'));"
    cursor.execute(sql)
    result = cursor.fetchone()[0]

    return result