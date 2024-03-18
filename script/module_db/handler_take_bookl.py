from .connect import *


@ConnectBaseReturnTypeList
def IssuedBookAll(cursor: MySQLCursor = None) -> int:
    """
    Сколько книг выдано всего
    """
    sql = "SELECT COUNT(id) FROM take_book WHERE date_return is NULL;"
    cursor.execute(sql)
    result = cursor.fetchone()[0]
    return result


@ConnectBaseReturnTypeList
def CountIssuedBookToday(cursor: MySQLCursor = None) -> int:
    """
    Данная функция подсчитывает количество выданных книг за сегодня
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
    sql = ("SELECT "
           "    COUNT(ID) "
           "FROM "
           "    take_book "
           "WHERE date_take < DATE_SUB(CURRENT_DATE(), INTERVAL how_many_days_give DAY) AND date_return IS NULL;")
    cursor.execute(sql)
    result = cursor.fetchone()[0]

    return result


@ConnectBaseReturnTypeList
def WhichBookTakeUser(user_id, cursor: MySQLCursor = None) -> tuple:
    """
    Выводит все книги, которые брал пользователь (которые вернул)
    """
    sql = f"SELECT * FROM take_book WHERE user_id = %s AND date_return IS NOT NULL;"
    cursor.execute(sql, (user_id,))
    result = cursor.fetchall()

    return result


@ConnectBaseReturnTypeList
def WhichNowBookAtUser(user_id, cursor: MySQLCursor = None) -> tuple:
    """
    Выводит все книги которые сейчас у пользователя
    """
    sql = f"SELECT * FROM take_book WHERE user_id = %s AND date_return IS NOT NULL;"
    cursor.execute(sql, (user_id,))
    result = cursor.fetchall()

    return result


@ConnectBaseReturnTypeList
def GetQuantityBookThatUserHaveById(book_id: int, cursor: MySQLCursor = None) -> int:
    """
    Получает количество экземпляров книг которые находиться у пользователей по айди книги
    """
    sql = f"SELECT COUNT(id) FROM take_book WHERE book_id = %s AND date_return IS NULL;"
    cursor.execute(sql, (book_id,))
    result = cursor.fetchone()[0]

    return result


@ConnectBaseReturnTypeList
def GetInfoHistoryBooksTakenUserById(user_id: int, cursor: MySQLCursor = None) -> tuple[tuple, ...]:
    """
    Получает информацию(историю) о взятых книгах и об их датах получения и возращения пользователем по введенному его id
    """
    sql = f"""
    SELECT 
        books.name_book,
        books.author,
        books.ISBN,
        books.year_publication,
        take_book.date_take,
        take_book.date_return
    FROM 
        take_book
    INNER JOIN 
        books ON take_book.book_id = books.id
    WHERE 
        take_book.user_id = %s AND take_book.date_return IS NOT NULL;
    """
    cursor.execute(sql, (user_id,))
    result = cursor.fetchall()

    return tuple(result)


@ConnectBaseReturnTypeList
def GetInfoBooksTakenUserById(user_id: int, cursor: MySQLCursor = None) -> tuple[tuple, ...]:
    """
    Получает информацию о книгах которые находится у пользователя сейчас
    """
    sql = """
    SELECT 
        books.id,
        books.name_book,
        books.author,
        books.ISBN,
        books.year_publication,
        take_book.date_take
    FROM 
        take_book
    INNER JOIN 
        books ON take_book.book_id = books.id
    WHERE 
        take_book.user_id = %s AND take_book.date_return IS NULL;
    """
    cursor.execute(sql, (user_id,))
    result = cursor.fetchall()

    return tuple(result)


@ConnectBaseReturnTypeList
def UpdateReturnBook(user_id: int, book_id, cursor: MySQLCursor = None) -> bool:
    """
    Обновляет информацию, что пользователь вернул книгу
    """
    sql = """
    UPDATE 
        take_book 
    SET 
        date_return = CURRENT_DATE() 
    WHERE 
        user_id = %s AND book_id = %s AND date_return IS NULL;
    """

    cursor.execute(sql, (user_id, book_id))
    cursor.fetchone()

    return True

@ConnectBaseReturnTypeList
def HistoryUsersTakeBookById(id_book: int, cursor: MySQLCursor = None) -> tuple:
    sql = """
    SELECT 
        users.id,
        users.FIO,
        users.number_group,
        users.student_id_number,
        take_book.date_take,
        take_book.how_many_days_give,
        take_book.date_return
    FROM 
        take_book
    INNER JOIN
        users ON take_book.user_id = users.id
    WHERE 
        take_book.id = %s
    AND
        take_book.date_return IS NOT NULL;
    """
    cursor.execute(sql, (id_book, ))
    result = cursor.fetchall()

    return tuple(result)


slq = """
SELECT
	books.*,
	books.name_book,
    books.author,
    books.ISBN,
    books.year_publication,
    take_book.how_many_days_give,
    take_book.date_take,
    take_book.date_return,
    (SELECT FIO FROM users WHERE id = take_book.user_id)
FROM
	take_book
INNER JOIN
	books ON take_book.book_id = books.id
WHERE 
	date_return IS NOT NULL;
"""