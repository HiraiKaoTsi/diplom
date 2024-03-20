from .connect import *


@ConnectBaseReturnTypeList
def InsertTakeBook(user_id: int, book_id: int, how_many_days: int, cursor: MySQLCursor = None) -> bool:
    """
    Осуществляет добовление информации, что пользователь взял книгу
    :param user_id: id пользователя
    :param book_id: id книги
    :param how_many_days: на сколько дней будет выданна данная книга
    :param cursor: (не требует ввода) предназначен для обращения к нему запросов
    """

    sql = "INSERT INTO take_book(user_id, book_id, how_many_days_give, date_take) VALUES(%s, %s, %s, CURRENT_DATE());"
    cursor.execute(sql, (user_id, book_id, how_many_days))
    cursor.fetchone()
    return True


@ConnectBaseReturnTypeList
def UpdateReturnBook(user_id: int, book_id: int, cursor: MySQLCursor = None) -> bool:
    """
    Осуществляет изменение информации, что пользователь вернул книгу
    :param user_id: id пользователя
    :param book_id: id книги
    :param cursor: (не требует ввода) предназначен для обращения к нему запросов
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
def GetCountIssuedBookAll(cursor: MySQLCursor = None) -> int:
    """
    Осуществляет подсчет количество всех выданных книг
    :param cursor: (не требует ввода) предназначен для обращения к нему запросов
    """
    sql = "SELECT COUNT(id) FROM take_book WHERE date_return is NULL;"
    cursor.execute(sql)
    result = cursor.fetchone()[0]
    return result


@ConnectBaseReturnTypeList
def GetCountIssuedBookToday(cursor: MySQLCursor = None) -> int:
    """
    Осуществляет подсчет количество выданных книг за сегодня
    :param cursor: (не требует ввода) предназначен для обращения к нему запросов
    """

    sql = "SELECT COUNT(id) FROM take_book WHERE date_return IS NULL AND date_take = CURRENT_DATE();"
    cursor.execute(sql)
    result = cursor.fetchone()[0]
    return result


@ConnectBaseReturnTypeList
def GetCountReturnBookToday(cursor: MySQLCursor = None) -> int:
    """
    Осуществляет подсчет количество вернутых книг за сегодня
    :param cursor: (не требует ввода) предназначен для обращения к нему запросов
    """

    sql = "SELECT COUNT(id) FROM take_book WHERE date_return = CURRENT_DATE();"
    cursor.execute(sql)
    result = cursor.fetchone()[0]
    return result


@ConnectBaseReturnTypeList
def GetCountQuantityDebtors(cursor: MySQLCursor = None) -> int:
    """
    Осуществляет подсчет количество задолжников книг
    :param cursor: (не требует ввода) предназначен для обращения к нему запросов
    """

    sql = """
    SELECT
        COUNT(ID) 
    FROM
        take_book 
    WHERE
        date_take < DATE_SUB(CURRENT_DATE(), INTERVAL how_many_days_give DAY) 
    AND
        date_return IS NULL;
    """
    cursor.execute(sql)
    result = cursor.fetchone()[0]
    return result


@ConnectBaseReturnTypeList
def GetQuantityBookThatUserHaveById(book_id: int, cursor: MySQLCursor = None) -> int:
    """
    Осуществляет подсчет количество экземпляров книг которые находиться у пользователй по id книги
    :param book_id: id книги
    :param cursor: (не требует ввода) предназначен для обращения к нему запросов
    """

    sql = "SELECT COUNT(id) FROM take_book WHERE book_id = %s AND date_return IS NULL;"
    cursor.execute(sql, (book_id, ))
    result = cursor.fetchone()[0]
    return result


@ConnectBaseReturnTypeList
def GetInfoHistoryBooksTakenUserById(user_id: int, cursor: MySQLCursor = None) -> tuple[tuple, ...]:
    """
    Осуществляет поиск информации о взятых книгах по введенному id пользователя
    :param user_id: id пользователя
    :param cursor: (не требует ввода) предназначен для обращения к нему запросов
    """

    sql = """
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
    cursor.execute(sql, (user_id, ))
    result = cursor.fetchall()
    return tuple(result)


@ConnectBaseReturnTypeList
def GetInfoBooksTakenUserById(user_id: int, cursor: MySQLCursor = None) -> tuple[tuple, ...]:
    """
    Осуществляет поиск информации о книгах которые находится у пользователя
    :param user_id: id пользователя
    :param cursor: (не требует ввода) предназначен для обращения к нему запросов
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
    cursor.execute(sql, (user_id, ))
    result = cursor.fetchall()
    return tuple(result)


@ConnectBaseReturnTypeList
def GetHistoryUsersTakeBookById(id_book: int, cursor: MySQLCursor = None) -> tuple:
    """
    Осуществляет поиск пользователей и информации (когда выдана, на сколько, когда вернуто) книга
    по введенном id книги
    :param id_book: id книги
    :param cursor: (не требует ввода) предназначен для обращения к нему запросов
    """

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
