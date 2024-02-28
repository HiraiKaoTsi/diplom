from mysql.connector import connect, Error
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor

from .config import *


def _createConnectionAndCursorDataBase(type_cursor):
    """
    Данная функция создает экземпляр класса
    :return: connect & cursor если подключиться к базе не удалось возращает None & None
    """
    connection, cursor = None, None
    try:
        connection = connect(host=HOST, port=PORT, user=USER, password=PASSWORD, db=NAME_DATABASE, charset=CHARSET)
        if type_cursor is list:
            cursor = connection.cursor()
        elif type_cursor is dict:
            cursor = connection.cursor(dictionary=True)
    except Error as base_error:
        print(base_error)
    return connection, cursor


def _breakConnectionDataBase(connection: MySQLConnection, cursor: MySQLCursor) -> None:
    """
    Данная функция закрывает поключение к базе данных с курсором
    :param connect: MySQLConnection
    :param cursor: MySQLCursor
    """
    if connect:
        cursor.close()
        connection.close()


def ConnectBaseReturnTypeList(input_funct):
    """
    Декоратор для открытия и закрытия подключения к базе данных с курсором 
    Cursor - 
    """
    def output_func(*args):
        connection, cursor = _createConnectionAndCursorDataBase(list)
        if cursor is not None:
            try:
                result = input_funct(*args, cursor=cursor)
                connection.commit()
                return result
            except Error as base_error:
                print(base_error)
            finally:
                _breakConnectionDataBase(connection, cursor)
    return output_func



def ConnectBaseReturnTypeDict(input_funct):
    """
    Декоратор для открытия и закрытия подключения к базе данных с курсором 
    Cursor - 
    """
    def output_func(*args):
        connection, cursor = _createConnectionAndCursorDataBase(dict)
        if cursor is not None:
            try:
                result = input_funct(*args, cursor=cursor)
                connection.commit()
                return result
            except Error as base_error:
                print(base_error)
            finally:
                _breakConnectionDataBase(connection, cursor)
    return output_func

