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
    Функция возращает информацию о пользователе по его id
    """
    sql = "SELECT * FROM users WHERE id = %s;"
    cursor.execute(sql, (id_user, ))
    result = cursor.fetchone()
    return result


@ConnectBaseReturnTypeList
def GetUsersBookDebtors(cursor: MySQLCursor = None) -> tuple[tuple, ...]:
    """
    Функция возращает информацию о задолжниках
    """
    sql = """
    SELECT 
        users.*
    FROM 
        take_book 
    INNER JOIN 
        users ON user_id = users.id
    WHERE 
        date_return IS NULL;
    """
    cursor.execute(sql)
    result = cursor.fetchall()
    return result