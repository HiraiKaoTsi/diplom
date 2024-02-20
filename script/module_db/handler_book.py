from .connect import *



@ConnectBase
def CountBook(cursor: sqlite3.Cursor) -> int:
    """
    Данная функция подсчитывает количество книг в базе данных
    :param cursor: водиться автоматический
    :return: возращает количество 
    """
    sql = "SELECT COUNT(id) FROM books;"
    cursor.execute(sql)
    result = cursor.fetchone()[0]
    return result


@ConnectBase
def AddNewBook(name_book, author, isbn, year_publication, quantity, cursor: sqlite3.Cursor = None) -> bool:
    
    """
    Данная функция добовляет новую книгу в базу данных
    :return: True если успешно добавленна запись, None - при ошибки
    """
    sql = f"INSERT INTO books(name_book, author, ISBN, year_publication, quantity) VALUES(?, ?, ?, ?, ?);"
    cursor.execute(sql, (name_book, author, isbn, year_publication, quantity))
    return True



# mb edit name function
@ConnectBase
def TakeQuantityBook(id_book: int, cursor: sqlite3.Cursor = None) -> int:
    """
    Данная функция возращает колиство данной книги
    """
    sql = f"SELECT quantity FROM books WHERE id = ?;"
    cursor.execute(sql, (id_book, ))
    result = cursor.fetchone()[0]
    return result

@ConnectBase
def TakeInfoAboutBook(info: str, cursor: sqlite3.Cursor):
    info = f"%{info}%"
    sql = f"SELECT * FROM books WHERE LOWER(name_book) || LOWER(author) || ISBN || year_publication LIKE ?;"
    cursor.execute(sql, (info, ))
    result = cursor.fetchall()
    return result
