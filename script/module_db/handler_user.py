from .connect import *


@ConnectBaseReturnTypeList
def GetAllUser(cursor: MySQLCursor = None) -> tuple[tuple, ...]:
    """
    Функция выводит информацию о всех студентах
    """
    sql = "SELECT * FROM users;"
    cursor.execute(sql)
    result = cursor.fetchall()
    return tuple(result)


@ConnectBaseReturnTypeDict
def GetAboutUser(id_user: int, cursor: MySQLCursor = None) -> dict:
    """
    Функция возвращает информацию о пользователе по его id
    """
    sql = "SELECT * FROM users WHERE id = %s;"
    cursor.execute(sql, (id_user, ))
    result = cursor.fetchone()
    return result


@ConnectBaseReturnTypeList
def GetUsersTakesBook(cursor: MySQLCursor = None):
    """
    Функция возвращает информацию о взявших книг пользователя
    """
    sql = """
    SELECT 
        users.*
    FROM 
        take_book 
    INNER JOIN 
        users ON user_id = users.id
    WHERE 
        date_return IS NULL
    """
    cursor.execute(sql)
    result = cursor.fetchall()
    return tuple(result)



@ConnectBaseReturnTypeList
def GetUsersBookDebtors(cursor: MySQLCursor = None) -> tuple[tuple, ...] | tuple:
    """
    Функция возвращает информацию о задолжниках
    """
    sql = """
    SELECT 
        users.*
    FROM 
        take_book 
    INNER JOIN 
        users ON user_id = users.id
    WHERE 
        date_return IS NULL
    AND 
        DATE_ADD(date_take, INTERVAL how_many_days_give DAY) <= CURDATE();
    """
    cursor.execute(sql)
    result = cursor.fetchall()
    return tuple(result)


@ConnectBaseReturnTypeList
def GetInfoTheyFitDelivery(cursor: MySQLCursor = None) -> tuple[tuple, ...] | tuple:
    """
    Пользователи которые вскоре должны стать сдать книгу/книги (в течение 2 дней)
    :param cursor: MySQLCursor - (не требует ввода) предназначен для обращения к нему запросов
    :return: tuple[tuple, ...] - если нашел информацию
    tuple - если информация отсутствует или не найдена
    """
    sql = """
    SELECT 
        users.*
    FROM 
        take_book
    INNER JOIN
        users ON take_book.user_id = users.id
    WHERE
        take_book.date_return IS NULL 
    AND
        DATEDIFF((DATE_ADD(take_book.date_take, INTERVAL take_book.how_many_days_give DAY)), CURRENT_DATE()) <= 3 
    AND
        DATEDIFF((DATE_ADD(take_book.date_take, INTERVAL take_book.how_many_days_give DAY)), CURRENT_DATE()) > 0;
    """
    cursor.execute(sql)
    result = cursor.fetchall()
    return tuple(result)


@ConnectBaseReturnTypeList
def GetInfoByInputData(input_data: str, cursor: MySQLCursor = None) -> tuple[tuple, ...] | tuple:
    input_data = f"%{input_data}%"
    """
    Функция по полученной информации
    """
    sql = """
    SELECT 
        * 
    FROM 
        users
    WHERE 
        CONCAT_WS(FIO, number_group, student_id_number, number_phone, email, vk, telegram) LIKE %s;
    """
    cursor.execute(sql, (input_data, ))
    result = cursor.fetchall()
    return tuple(result)


@ConnectBaseReturnTypeList
def DeleteUserById(id_user: int, cursor: MySQLCursor = None) -> bool:
    """
    Удаляет пользователя по введенному id
    """
    sql = "DELETE FROM users WHERE id = %s;"
    cursor.execute(sql, (id_user, ))
    cursor.fetchone()
    return True

@ConnectBaseReturnTypeList
def EditDataUser(id_user: int, param: dict, cursor: MySQLCursor = None) -> bool:
    """
    Изменяет информацию пользователя по id
    """

    param_edit_for_sql = ""
    for key, value in zip(param.keys(), param.values()):
        param_edit_for_sql+=f"""{key} = {'NULL' if value == "" else f'"{value}"'}, """
    param_edit_for_sql = param_edit_for_sql[:-2]

    sql = f"""
    UPDATE users
    SET {param_edit_for_sql}
    WHERE id = %s;
    """
    
    cursor.execute(sql, (id_user, ))
    cursor.fetchone()
    return True

@ConnectBaseReturnTypeList
def InsertNewUser(param: tuple, cursor: MySQLCursor = None) -> bool:
    sql = f"""
    INSERT INTO 
    users(FIO, number_group, student_id_number, number_phone, email, telegram, vk) 
    VALUES(%s, %s, %s, %s, %s, %s, %s);
    """

    cursor.execute(sql, param)
    cursor.fetchone()
    return True