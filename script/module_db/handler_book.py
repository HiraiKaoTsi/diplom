from .connect import *
from datetime import datetime


@ConnectBaseReturnTypeList
def InsertNewBooks(value: tuple[str, str, str, datetime.year, int], cursor: MySQLCursor = None) -> bool:
    """
    Осуществляет добавление новой книги
    :param value: [название_книги, автор, isbn, год_публикации, количество]
    :param cursor: (не требует ввода) предназначен для обращения к нему запросов ы
    :return: True если успешна добавлена запись
    """

    sql = """
    INSERT INTO 
    books(name_book, author, ISBN, year_publication, quantity) 
    VALUES(%s, %s, %s, %s, %s);
    """
    cursor.execute(sql, value)
    cursor.fetchone()
    return True


@ConnectBaseReturnTypeList
def DeleteBookById(id_book: int, cursor: MySQLCursor = None) -> bool:
    """
    Осуществляет удаление книги по введенному id номеру
    :param id_book: id книги
    :param cursor: (не требует ввода) предназначен для обращения к нему запросов
    :return: True если успешна удаление
    """

    sql = "DELETE FROM books WHERE id = %s;"
    cursor.execute(sql, (id_book, ))
    cursor.fetchone()
    return True


# МБ ПЕРЕЙТИ НА БОРЕЕ СТАТИЧНОЕ ПЕРЕДАЧА ИФНОРАМЦММ БЕЗ ЦИКЛА ВНУТРИ
@ConnectBaseReturnTypeList
def UpdateDataBook(id_book: int, param: dict, cursor: MySQLCursor = None) -> bool:
    """
    Осуществляет изменение информации книги по его id номеру
    :param id_book: id книги
    :param param: значение которые требуется изменить где key - это столбец, а value это значение
    :param cursor: (не требует ввода) предназначен для обращения к нему запросов
    :return: True если успешна добавлена запись
    """

    # Делает из веденного param часть для sql запроса
    param_edit_for_sql = ""
    for key, value in zip(param.keys(), param.values()):
        param_edit_for_sql += f"""{key} = {'NULL' if value == "" else f'"{value}"'}, """
    param_edit_for_sql = param_edit_for_sql[:-2]

    sql = f"""
    UPDATE books
    SET {param_edit_for_sql}
    WHERE id = %s;
    """
    cursor.execute(sql, (id_book, ))
    cursor.fetchone()
    return True


# ВЕРНУТЬ ОБРАТНО
@ConnectBaseReturnTypeList
def GetAllBooks(cursor: MySQLCursor = None) -> tuple:
    """
    Осуществляет получение информации о всех книгах
    :param cursor: (не требует ввода) предназначен для обращения к нему запросов
    """

    sql = "SELECT *, 4 AS quantity_take FROM books;"
    # sql = "SELECT *, CountQuantityTakeBook(books.id) AS quantity_take FROM books;"
    cursor.execute(sql)
    result = cursor.fetchall()
    return tuple(result)


@ConnectBaseReturnTypeDict
def GetAboutBookById(id_book: int, cursor: MySQLCursor = None) -> dict:
    """
    Осуществляет поиск информацию о книге по его id номеру
    :param id_book: id книги, которую требуется найти
    :param cursor: (не требует ввода) предназначен для обращения к нему запросов
    """

    sql = "SELECT * FROM books WHERE id = %s"
    cursor.execute(sql, (id_book, ))
    result = cursor.fetchone()
    return result


@ConnectBaseReturnTypeList
def GetCountBook(cursor: MySQLCursor = None) -> int:
    """
    Осуществляет подсчитывание книг в базе данных
    :param cursor: (не требует ввода) предназначен для обращения к нему запросов
    """

    sql = "SELECT COUNT(id) FROM books;"
    cursor.execute(sql)
    result = cursor.fetchone()[0]
    return result


@ConnectBaseReturnTypeList
def GetBookWhichAllMissing(cursor: MySQLCursor = None) -> tuple:
    """
    Осуществляет получение книги у которых отсутствуют все экземпляры
    :param cursor: (не требует ввода) предназначен для обращения к нему запросов ы
    """

    sql = """
    SELECT DISTINCT
        books.*,
        COUNT(take_book.id) AS count_take_book
    FROM 
        take_book
    INNER JOIN
        books ON take_book.book_id = books.id
    WHERE 
        take_book.date_return IS NULL 
    GROUP BY
        books.id
    HAVING
        (books.quantity - COUNT(take_book.id)) = 0;
    """
    cursor.execute(sql)
    result = cursor.fetchall()
    return tuple(result)


@ConnectBaseReturnTypeList
def GetBookNotAllMissing(cursor: MySQLCursor = None) -> tuple:
    """
    Осуществляет получение книги которые имеются не во всех экземплярах
    :param cursor: (не требует ввода) предназначен для обращения к нему запросов
    """

    sql = """
    SELECT DISTINCT
        books.*,
        COUNT(take_book.id) AS count_take_book
    FROM 
        take_book
    INNER JOIN
        books ON take_book.book_id = books.id
    WHERE 
        take_book.date_return IS NULL 
    GROUP BY
        books.id
    HAVING
        (books.quantity - COUNT(take_book.id)) > 1;
    """
    cursor.execute(sql)
    result = cursor.fetchall()
    return tuple(result)


@ConnectBaseReturnTypeList
def GetInfoByInputDataBook(input_data: str, cursor: MySQLCursor = None) -> tuple[tuple, ...]:
    """
    Осуществляет поиск книги по введенной информации из всей таблицы books
    :param input_data: любая текстовая информация
    :param cursor: (не требует ввода) предназначен для обращения к нему запросов
    """

    input_data = f"%{input_data}%"
    sql = """
    SELECT 
        *,
        4
    FROM 
        books
    WHERE 
        CONCAT_WS(name_book, author, ISBN, year_publication) LIKE %s;
    """
    # ql = """
    #     SELECT
    #         *,
    #         CountQuantityTakeBook(books.id)
    #     FROM
    #         books
    #     WHERE
    #         CONCAT_WS(name_book, author, ISBN, year_publication) LIKE %s;
    #     """
    cursor.execute(sql, (input_data, ))
    result = cursor.fetchall()
    return tuple(result)
