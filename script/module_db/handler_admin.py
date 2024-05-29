from .connect import *


@ConnectBaseReturnTypeList
def CheckInfoAdmin(login: str, password: str, cursor = None) -> bool:
    """
    Осуществляет проверку данных админа
    :param cursor: (не требует ввода) предназначен для обращения к нему запросов
    """
    sql = "SELECT * FROM library_database.admin WHERE login = %s AND password = %s;"
    cursor.execute(sql, (login, password))
    result = cursor.fetchone()
    if result is not None:
        return True
    else:
        False
