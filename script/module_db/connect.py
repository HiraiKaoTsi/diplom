from mysql.connector import connect, Error


from .config import *


def _createConnectionAndCursorDataBase(type_cursor):
    """
    Данная функция создает экземпляр класса MySQLConnection и MySQLCursor и возвращает их
    если подключиться к базе не удалось возвращать None
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


def _breakConnectionDataBase(connection, cursor) -> None:
    """
    Данная функция закрывает подключение к базе данных с курсором
    :param connection: MySQLConnection
    :param cursor: MySQLCursor
    """
    if connection.is_connected():
        cursor.close()
        connection.close()


def ConnectBaseReturnTypeList(input_funct):
    """
    Декоратор для подключения к базе данных
    тип возвращаемой информации курсора - list
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
    Декоратор для подключения к базе данных
    тип возвращаемой информации курсора - dict
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
