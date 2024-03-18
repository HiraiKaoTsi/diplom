from .connect import *

@ConnectBaseReturnTypeList
def CountBook(cursor: MySQLCursor = None) -> int:
    """
    Данная функция подсчитывает количество книг в базе данных
    :param cursor: водиться автоматический
    :return: возращает количество 
    """
    sql = "SELECT COUNT(id) FROM books;"
    cursor.execute(sql)
    result = cursor.fetchone()[0]
    return result

@ConnectBaseReturnTypeDict
def GetInfoBookById(id_book: int, cursor: MySQLCursor = None) -> dict:
    sql = "SELECT * FROM books WHERE id = %s"
    cursor.execute(sql, (id_book, ))
    result = cursor.fetchone()
    return result


@ConnectBaseReturnTypeList
def TakeInfoAboutBook(info: str, cursor: MySQLCursor = None):
    info = f"%{info}%"
    sql = f"SELECT * FROM books WHERE LOWER(name_book) || LOWER(author) || ISBN || year_publication LIKE %s;"
    cursor.execute(sql, (info, ))
    result = cursor.fetchall()
    return result


@ConnectBaseReturnTypeList
def InsertNewBooks(param: tuple, cursor: MySQLCursor = None) -> bool:
    sql = f"""
    INSERT INTO 
    books(name_book, author, ISBN, year_publication, quantity) 
    VALUES(%s, %s, %s, %s, %s);
    """

    cursor.execute(sql, param)
    cursor.fetchone()
    return True


@ConnectBaseReturnTypeList
def GetAllBooks(cursor: MySQLCursor = None) -> tuple:
    sql = "SELECT *, CountQuantityTakeBook(books.id) AS quantity_take FROM books;"
    cursor.execute(sql)
    result = cursor.fetchall()
    return tuple(result)

@ConnectBaseReturnTypeList
def GetBookWhichAllMissing(cursor: MySQLCursor = None) -> tuple:
    """
    Книги у которых отсуствуют все экземпляры
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
def GetBookNotAllMinning(cursor: MySQLCursor = None) -> tuple:
    """
    Книги которые имеються не во всех экзмемплярах
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
def GetInfoByInputDataBook(input_data: str, cursor: MySQLCursor = None) -> tuple[tuple, ...] | tuple:
    """
    Функция по полученной информации
    """
    input_data = f"%{input_data}%"
    sql = """
    SELECT 
        *,
        CountQuantityTakeBook(books.id)
    FROM 
        books
    WHERE 
        CONCAT_WS(name_book, author, ISBN, year_publication) LIKE %s;
    """
    cursor.execute(sql, (input_data, ))
    result = cursor.fetchall()
    return tuple(result)

@ConnectBaseReturnTypeList
def UpdateDataBook(id_book: int, param: dict, cursor: MySQLCursor = None) -> bool:
    """
    Изменяет информацию книги по id
    """

    param_edit_for_sql = ""
    for key, value in zip(param.keys(), param.values()):
        param_edit_for_sql+=f"""{key} = {'NULL' if value == "" else f'"{value}"'}, """
    param_edit_for_sql = param_edit_for_sql[:-2]

    sql = f"""
    UPDATE books
    SET {param_edit_for_sql}
    WHERE id = %s;
    """
    cursor.execute(sql, (id_book, ))
    cursor.fetchone()
    return True

@ConnectBaseReturnTypeList
def DeleteBookById(id_book: int, cursor: MySQLCursor = None) -> bool:
    """
    Удаляет книгу по введенному id
    """
    sql = "DELETE FROM books WHERE id = %s;"
    cursor.execute(sql, (id_book, ))
    cursor.fetchone()
    return True