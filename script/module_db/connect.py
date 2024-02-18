import sqlite3
from .config import *


def _createConnectionAndCursorDataBase():
    """
    Данная функция создает экземпляр класса
    :return: connect & cursor если подключиться к базе не удалось возращает None & None
    """
    connect, cursor = None, None
    try:
        connect = sqlite3.connect(f"{WAY_TO_BASE}")
        cursor = connect.cursor()
    except sqlite3.Error as error_connect:
        a = type(error_connect)
        print(str(a))
        # print(error_connect)
    return connect, cursor


def _breakConnectionDataBase(connect: sqlite3.Connection, cursor: sqlite3.Cursor) -> None:
    """
    Данная функция закрывает поключение к базе данных с курсором
    :param connect: sqlite3.Connection
    :param cursor: sqlite3.Cursor
    """
    if connect:
        cursor.close()
        connect.close()


def ConnectBase(input_funct):
    """
    Декоратор для открытия и закрытия подключения к базе данных с курсором
    """
    def output_func(*args):
        connect, cursor = _createConnectionAndCursorDataBase()
        
        if cursor is not None:
            try:
                result = input_funct(*args, cursor=cursor)
                connect.commit()
                return result
            except sqlite3.ProgrammingError as data_error:
                print(data_error)
            except sqlite3.OperationalError as request_error:
                print(request_error)
            finally:
                _breakConnectionDataBase(connect, cursor)
            
    return output_func
