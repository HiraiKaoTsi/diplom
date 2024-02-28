from .connect import *


@ConnectBaseReturnTypeList
def GetAllUser(cursor: MySQLCursor = None) -> tuple[list]:
    """
    Функция выводит инфоормацию о всех студентах
    """
    sql = "SELECT * FROM users;"
    cursor.execute(sql)
    result = cursor.fetchall()
    return tuple(result)



@ConnectBaseReturnTypeDict
def GetAboutUser(id_user: int, cursor: MySQLCursor = None) -> dict:
    """
    Получает информацию о пользователе по его id
    """
    sql = "SELECT * FROM users WHERE id = %s;"
    cursor.execute(sql, (id_user, ))
    result = cursor.fetchone()
    return result
