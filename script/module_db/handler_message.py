from .connect import *


@ConnectBaseReturnTypeList
def GetAllHistoryMessageUsers(id_user: int, cursor: MySQLCursor = None) -> tuple:
    sql = "SELECT date_emit, main_text, social_network FROM history_message WHERE user_id = %s;"
    cursor.execute(sql, (id_user, ))
    result = cursor.fetchall()
    return result


@ConnectBaseReturnTypeList
def CreateNewMessage(id_user: int, text_message: str, social_network: str, cursor: MySQLCursor = None) -> bool:
    sql = "INSERT INTO history_message VALUES(%s, CURRENT_DATE(), %s, %s);"
    cursor.execute(sql, (id_user, text_message, social_network))
    cursor.fetchone()
    return True
