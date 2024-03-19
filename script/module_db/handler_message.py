from .connect import *


@ConnectBaseReturnTypeList
def InsertNewMessage(id_user: int, text_message: str, social_network: str, cursor: MySQLCursor = None) -> bool:
    """
    Осуществляет добавление нового сообщение
    :param id_user: id пользователя
    :param text_message: текст сообщения
    :param social_network: в какую социальную сеть было отправлено сообщение
    :param cursor: (не требует ввода) предназначен для обращения к нему запросов ы
    :return: True если успешна добавлена запись
    """
    
    sql = "INSERT INTO history_message VALUES(%s, CURRENT_DATE(), %s, %s);"
    cursor.execute(sql, (id_user, text_message, social_network))
    cursor.fetchone()
    return True


@ConnectBaseReturnTypeList
def GetAllHistoryMessageUsers(id_user: int, cursor: MySQLCursor = None) -> tuple:
    """
    Осуществляет получение истории сообщений которые отправлены пользователю
    :param id_user: id пользователя
    :param cursor: (не требует ввода) предназначен для обращения к нему запросов ы
    """

    sql = "SELECT date_emit, main_text, social_network FROM history_message WHERE user_id = %s;"
    cursor.execute(sql, (id_user, ))
    result = cursor.fetchall()
    return tuple(result)
